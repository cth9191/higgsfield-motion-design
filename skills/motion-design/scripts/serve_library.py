"""Serve the gallery on loopback, optionally connecting explicitly listed local assets."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import re
from urllib.parse import quote, unquote, urlsplit

from library_core import ROOT, inside, load_bindings, load_library


def byte_range(header, size):
    if header is None:
        return 0, size - 1, False
    match = re.fullmatch(r'bytes=(\d*)-(\d*)', header)
    if not match or not any(match.groups()) or size == 0:
        raise ValueError('Invalid byte range')
    first, last = match.groups()
    if not first:
        count = int(last)
        if not count:
            raise ValueError('Invalid suffix range')
        return max(0, size - count), size - 1, True
    first, last = int(first), min(int(last), size - 1) if last else size - 1
    if first >= size or last < first:
        raise ValueError('Unsatisfiable byte range')
    return first, last, True


def make_handler(root=ROOT, bindings=None):
    catalog, _ = load_library(root)
    bindings = bindings or {}

    class Handler(BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.respond(head=True)

        def do_GET(self):
            self.respond()

        def respond(self, head=False):
            host = urlsplit('http://' + self.headers.get('Host', '')).hostname
            if host not in {'127.0.0.1', 'localhost', '::1'}:
                self.send_error(403, 'Loopback host required')
                return
            route = unquote(urlsplit(self.path).path)
            if route == '/api/assets':
                body = json.dumps({key: {'label': value['label'], 'kind': value['kind'],
                    'available': key in bindings and bindings[key].is_file(),
                    'url': '/asset/' + key if key in bindings and bindings[key].is_file() else None}
                    for key, value in catalog['assets'].items()}).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(body)))
                self.send_header('Cache-Control', 'no-store')
                self.end_headers()
                if not head:
                    self.wfile.write(body)
                return
            download = False
            if route.startswith('/asset/'):
                key = route[len('/asset/'):]
                path = bindings.get(key)
                if key not in catalog['assets'] or path is None or not path.is_file():
                    self.send_error(404, 'Local asset not connected')
                    return
                download = catalog['assets'][key]['kind'] in {'native', 'code'}
            else:
                try:
                    path = inside(root, route.lstrip('/') or 'assets/library.html')
                except ValueError:
                    self.send_error(404)
                    return
                if not path.is_file():
                    self.send_error(404)
                    return
            size = path.stat().st_size
            try:
                first, last, partial = byte_range(self.headers.get('Range'), size)
            except ValueError:
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{size}')
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            self.send_response(206 if partial else 200)
            self.send_header('Content-Type', mimetypes.guess_type(path.name)[0] or 'application/octet-stream')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Length', str(max(0, last - first + 1)))
            self.send_header('Cache-Control', 'no-cache')
            if partial:
                self.send_header('Content-Range', f'bytes {first}-{last}/{size}')
            if download:
                # Preserve the native extension without inserting raw filenames into headers.
                self.send_header('Content-Disposition', "attachment; filename*=UTF-8''" + quote(path.name, safe=''))
            self.end_headers()
            if not head and size:
                try:
                    with path.open('rb') as stream:
                        stream.seek(first)
                        remaining = last - first + 1
                        while remaining:
                            data = stream.read(min(65536, remaining))
                            if not data:
                                break
                            self.wfile.write(data)
                            remaining -= len(data)
                except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                    pass  # Browser seeking or leaving a page can cancel a range request.

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--assets-file', help='Local manifest with roots and explicit asset bindings')
    args = parser.parse_args()
    catalog, _ = load_library()
    bindings = load_bindings(args.assets_file, catalog)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(bindings=bindings))
    print(f'Shot library: http://127.0.0.1:{server.server_port}/assets/library.html', flush=True)
    print(f'{sum(path.is_file() for path in bindings.values())} local assets connected. Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
