"""Validate the study library, generate its small gallery index, or retrieve an entry."""
import argparse
import json
from library_core import ROOT, load_library, search


def build():
    catalog, entries = load_library()
    index = {key: catalog[key] for key in ('schema_version', 'title', 'studies', 'assets', 'entries')}
    payload = json.dumps(index, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c')
    (ROOT / 'assets/library-index.js').write_text('window.MOTION_LIBRARY = ' + payload + ';\n', encoding='utf-8', newline='\n')
    lines = ['# Shot and technique index', '',
             'Read this compact index first, then open only the selected detail JSON and study. Source observations, local settings and review states are independent.', '',
             '| Entry | Use | Tools | Local review |', '|---|---|---|---|']
    for item in catalog['entries']:
        lines.append(f"| [{item['title']}](../{item['detail']}) (`{item['id']}`) | {item['summary']} | {', '.join(item['tools'])} | {item['review_state']} |")
    lines.extend(['', 'Use `python scripts/build_library.py search "persistent hero"` or `show SHOT-INF-PHONE-CARDS` from the skill folder. Search is metadata retrieval; inspect the selected evidence before applying it.', ''])
    (ROOT / 'library/index.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print(f'Validated {len(entries)} entries and {len(catalog["studies"])} study; generated library index.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command')
    lookup = sub.add_parser('search')
    lookup.add_argument('query', nargs='?', default='')
    lookup.add_argument('--video-type')
    lookup.add_argument('--tool')
    lookup.add_argument('--review-state', choices=['pending', 'mixed', 'rejected', 'approved'])
    show = sub.add_parser('show')
    show.add_argument('id')
    args = parser.parse_args()
    if not args.command:
        build()
        return
    catalog, entries = load_library()
    if args.command == 'search':
        result = search(catalog, args.query, args.video_type, args.tool, args.review_state)
    else:
        if args.id not in entries:
            parser.error('Unknown entry ID: ' + args.id)
        result = entries[args.id]
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
