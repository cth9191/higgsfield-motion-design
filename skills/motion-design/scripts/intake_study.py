"""Register a source immediately, before timings or native files are known."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from library_core import ROOT, load_library, valid_id


def register(study_id, title, source_url, creator='Unverified', root=ROOT):
    root = Path(root)
    catalog, _ = load_library(root)
    if not valid_id(study_id) or not study_id.startswith('STUDY-'):
        raise ValueError('Use a stable STUDY-NAME identifier')
    if not title.strip() or urlparse(source_url).scheme != 'https' or not urlparse(source_url).netloc:
        raise ValueError('A title and HTTPS source URL are required')
    if any(s['id'] == study_id for s in catalog['studies']):
        raise ValueError('Study already exists; update that record instead')
    slug = study_id.lower()
    document = root / f'library/studies/{slug}.md'
    asset_id = slug + '-reference'
    if document.exists() or asset_id in catalog['assets']:
        raise ValueError('Document or asset already exists; choose the existing record or a distinct ID')
    study = dict(id=study_id, title=title.strip(), creator=creator, source_url=source_url,
                 source_asset=asset_id, document=f'library/studies/{slug}.md',
                 source_project=None, original_prompt=None,
                 status='In progress: source registered; media inspection and breakdown pending.')
    document.write_text(f'# {title.strip()}\n\n[Original source]({source_url})\n\n'
                        'Status: in progress. Source media, frame rate, duration, shot inventory, '
                        'original tools and construction remain unverified.\n\n'
                        'Update this stable study during inspection. Add shot records when media timing '
                        'is known; keep unknown settings unknown. Record actual inspection, dependencies, '
                        'renders and review outcomes as they become available.\n', encoding='utf-8')
    catalog['assets'][asset_id] = {'label': title.strip() + ' — source media', 'kind': 'video'}
    catalog['studies'].append(study)
    (root / 'library/catalog.json').write_text(json.dumps(catalog, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    load_library(root)
    return study


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--source-url', required=True)
    parser.add_argument('--creator', default='Unverified')
    args = parser.parse_args()
    study = register(args.id, args.title, args.source_url, args.creator)
    print('Registered ' + study['id'] + '. Inspect the source, update the record, then run build_library.py.')


if __name__ == '__main__':
    main()
