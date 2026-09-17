"""Portable study catalog validation, retrieval and local asset resolution."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ID = re.compile(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\Z')
KINDS = {'shot', 'technique', 'lighting'}
BASIS = {'measured-reference', 'original-source', 'local-implementation', 'proposed'}
STATES = {'pending', 'mixed', 'rejected', 'approved'}


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def inside(root, relative):
    root = Path(root).resolve()
    raw = str(relative)
    relative = Path(raw)
    if relative.is_absolute() or '..' in relative.parts or '\\' in raw or ':' in raw:
        raise ValueError('Expected a portable path within its root')
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Path escapes its declared root')
    return path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valid_id(value):
    return isinstance(value, str) and ID.fullmatch(value) is not None


def frame_range(value, label):
    require(isinstance(value, list) and len(value) == 2, label + ': expected two frames')
    require(all(type(x) is int and x >= 0 for x in value) and value[1] > value[0],
            label + ': invalid frame interval')


def load_library(root=ROOT):
    root = Path(root)
    catalog = read_json(root / 'library/catalog.json')
    require(catalog['schema_version'] == 1, 'Unsupported library schema')
    assets = catalog['assets']
    require(all(valid_id(a) for a in assets), 'Invalid asset ID')
    for asset in assets.values():
        require(asset['kind'] in {'video', 'image', 'document', 'native', 'code'}, 'Invalid asset kind')
        require(bool(asset['label']), 'Asset label missing')
    studies = {}
    for study in catalog['studies']:
        require(valid_id(study['id']) and study['id'] not in studies, 'Duplicate/invalid study ID')
        require(urlparse(study['source_url']).scheme == 'https', 'Source must be an HTTPS URL')
        require(inside(root, study['document']).is_file(), 'Study document missing')
        require(study['source_asset'] in assets, 'Study source asset missing')
        studies[study['id']] = study
    entries = {}
    for summary in catalog['entries']:
        key = summary['id']
        require(valid_id(key) and key not in entries, 'Duplicate/invalid entry ID')
        require(summary['study_id'] in studies, key + ': unknown study')
        require(summary['kind'] in KINDS, key + ': unknown kind')
        require(summary['review_state'] in STATES, key + ': unknown review state')
        if summary.get('poster_asset'):
            require(summary['poster_asset'] in assets and assets[summary['poster_asset']]['kind']=='image', key + ': poster missing')
        for field in ('title', 'summary', 'video_types', 'story_jobs', 'tags', 'tools'):
            require(bool(summary[field]), key + ': missing ' + field)
        entry = read_json(inside(root, summary['detail']))
        require(entry['id'] == key, key + ': detail ID mismatch')
        require(entry['review']['state'] == summary['review_state'], key + ': stale review index')
        clip = entry['clip']
        frame_range(clip['source_frames'], key)
        if summary.get('poster_asset'):
            require(type(summary.get('poster_source_frame')) is int and clip['source_frames'][0] <= summary['poster_source_frame'] < clip['source_frames'][1], key + ': poster outside excerpt')
        require(type(clip['fps']) is int and clip['fps'] > 0, key + ': invalid FPS')
        require(clip['asset_id'] in assets and assets[clip['asset_id']]['kind'] == 'video', key + ': preview missing')
        require(summary['preview_asset'] == clip['asset_id'], key + ': stale preview index')
        require(clip.get('clock') == 'source-frames', key + ': clock must be explicit')
        require(bool(entry['inspiration']['purpose']) and bool(entry['inspiration']['beats']), key + ': inspiration missing')
        require(bool(entry['technical']['sections']), key + ': technical breakdown missing')
        for section in entry['technical']['sections']:
            require(bool(section['title']) and bool(section['items']), key + ': empty technical section')
            for block in section.get('code', []):
                require(block['basis'] in BASIS and bool(block['label']) and bool(block['text']), key + ': code evidence missing')
            for table in section.get('tables', []):
                require(table['basis'] in BASIS and bool(table['caption']), key + ': table provenance missing')
                require(bool(table['columns']) and bool(table['rows']), key + ': empty technical table')
                require(all(isinstance(row,list) and len(row)==len(table['columns']) for row in table['rows']), key + ': technical table column mismatch')
        for parameter in entry['technical']['parameters']:
            require(parameter['basis'] in BASIS and bool(parameter['unit']), key + ': parameter provenance/units missing')
        track_ids = set()
        for track in entry['tracks']:
            require(valid_id(track['id']) and track['id'] not in track_ids, key + ': duplicate/invalid track')
            track_ids.add(track['id'])
            for event in track['events']:
                frame_range(event['frames'], key + '/' + track['id'])
                require(event['basis'] in BASIS, key + ': event basis missing')
                require(clip['source_frames'][0] <= event['frames'][0] < event['frames'][1] <= clip['source_frames'][1],
                        key + ': event outside source excerpt')
                # Overlap within/across tracks is intentional; these are animation events, not edit cuts.
        for asset_id in entry['evidence_assets']:
            require(asset_id in assets, key + ': unknown evidence asset')
        for implementation in entry['technical']['implementations']:
            require(implementation['status'] in {'proposed', 'rendered', 'tested', 'approved'}, key + ': invalid implementation state')
            require(all(a in assets for a in implementation['asset_ids']), key + ': unknown implementation asset')
        require(bool(entry['review']['scope']) and bool(entry['review']['limitations']), key + ': review scope missing')
        entries[key] = entry
    for entry in entries.values():
        require(all(key in entries for key in entry['related_ids']), entry['id'] + ': dangling relationship')
    require(bool(entries), 'Empty library')
    return catalog, entries


def search(catalog, query='', video_type=None, tool=None, review_state=None):
    terms = re.findall(r'[\w]+', query.lower())
    found = []
    for item in catalog['entries']:
        if video_type and video_type not in item['video_types']:
            continue
        if tool and tool.lower() not in [x.lower() for x in item['tools']]:
            continue
        if review_state and review_state != item['review_state']:
            continue
        haystack = re.sub(r'[-_]', ' ', json.dumps(item).lower())
        if not terms or all(term in haystack for term in terms):
            found.append(item)
    return found


def load_bindings(path, catalog):
    """An explicit local manifest exposes only enumerated files, never whole roots."""
    if path is None:
        return {}
    config = read_json(path)
    require(config['schema_version'] == 1, 'Unsupported asset manifest')
    roots = {name: Path(value).expanduser().resolve() for name, value in config['roots'].items()}
    resolved = {}
    for asset_id, binding in config['bindings'].items():
        require(asset_id in catalog['assets'], 'Unknown bound asset: ' + asset_id)
        require(binding['root'] in roots, 'Unknown asset root')
        resolved[asset_id] = inside(roots[binding['root']], binding['path'])
    return resolved
