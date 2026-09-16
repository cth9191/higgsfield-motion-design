#!/usr/bin/env python3
"""Validate the preset catalog and refresh the offline-capable gallery and index."""
import hashlib
import json
import math
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- PRESET_DATA_START -->'
END = '<!-- PRESET_DATA_END -->'


def build():
    catalog = json.loads((ROOT / 'assets/presets.json').read_text(encoding='utf-8'))
    presets = catalog['presets']
    if not presets:
        raise ValueError('The catalog must contain at least one preset.')
    ids = set()
    for preset in presets:
        preset_id = preset['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', preset_id) or preset_id in ids:
            raise ValueError(f'Invalid or duplicate preset ID: {preset_id}')
        ids.add(preset_id)
        for field in ('title', 'category', 'description', 'best_for', 'required', 'preserve', 'defaults', 'ending', 'strategy', 'template', 'template_version', 'structure', 'timeline'):
            if not preset.get(field):
                raise ValueError(f'{preset_id}: missing {field}')
        recipe = (ROOT / preset['recipe']).resolve()
        if not recipe.is_relative_to(ROOT) or not recipe.is_file():
            raise ValueError(f'{preset_id}: recipe is missing or outside the package')
        if f'`{preset_id}`' not in recipe.read_text(encoding='utf-8'):
            raise ValueError(f'{preset_id}: recipe ID does not match catalog')
        template = (ROOT / preset['template']).resolve()
        if not template.is_relative_to(ROOT) or not template.is_file():
            raise ValueError(f'{preset_id}: template is missing or outside the package')
        template_text = template.read_text(encoding='utf-8')
        if f'`{preset_id}`' not in template_text:
            raise ValueError(f'{preset_id}: template ID does not match catalog')
        cursor = 0
        for beat in preset['timeline']:
            start, end = beat['start_s'], beat['end_s']
            if not all(isinstance(t, (int, float)) and not isinstance(t, bool) and math.isfinite(t) for t in (start, end)):
                raise ValueError(f'{preset_id}: invalid timeline value')
            if abs(start - cursor) > 1e-6 or end <= start:
                raise ValueError(f'{preset_id}: timeline gap, overlap or reversed interval')
            cursor = end
        if abs(cursor - preset['defaults']['duration_s']) > 1e-6:
            raise ValueError(f'{preset_id}: timeline does not cover the default duration')
        written_times = re.findall(r'^\[(\d+(?:\.\d+)?)–(\d+(?:\.\d+)?)s\]', template_text, re.MULTILINE)
        written_times = [(float(a), float(b)) for a, b in written_times]
        catalog_times = [(b['start_s'], b['end_s']) for b in preset['timeline']]
        if written_times != catalog_times:
            raise ValueError(f'{preset_id}: template timing differs from the catalog')
        # Embed the actual reference text, so the viewer works without fetching .md files.
        preset['template_text'] = template_text
        source_path = (ROOT / preset['source']['prompt_path']).resolve()
        if not source_path.is_relative_to(ROOT) or not source_path.is_file():
            raise ValueError(f'{preset_id}: original prompt missing or outside package')
        source_bytes = source_path.read_bytes()
        if hashlib.sha256(source_bytes).hexdigest() != preset['source']['prompt_sha256']:
            raise ValueError(f'{preset_id}: archived original prompt hash mismatch')
        preset['source_prompt_text'] = source_bytes.decode('utf-8')

        for field in ('url', 'preview_url'):
            url = urlparse(preset['source'][field])
            if url.scheme != 'https' or not url.netloc:
                raise ValueError(f'{preset_id}: invalid source {field}')

    gallery = ROOT / 'assets/gallery.html'
    html = gallery.read_text(encoding='utf-8')
    if html.count(START) != 1 or html.count(END) != 1:
        raise ValueError('Gallery must contain exactly one pair of catalog markers.')
    compact = json.dumps(catalog, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    before, rest = html.split(START, 1)
    _, after = rest.split(END, 1)
    gallery.write_text(before + START + '\n<script type="application/json" id="preset-data">' + compact + '</script>\n' + END + after, encoding='utf-8', newline='\n')

    index = [
        '# Preset index', '',
        'Use this compact index to select a preset, then read its archived original prompt and linked adaptation guide. Do not generate from the short description or load every template for browsing.', '',
        '[Open the playable gallery](../assets/gallery.html). The gallery opens locally; previews stream from their public source and require internet. It copies a request into chat and does not launch generation itself.', '',
        '| Preset | Full template | Best for | Essential input |', '|---|---|---|---|',
    ]
    for p in presets:
        index.append(f"| [{p['title']}](presets/{p['id']}.md) | [Source + guide](templates/{p['id']}.md) | {p['best_for']} | {' '.join(p['required'])} |")
    index += ['', '## Names and aliases', '']
    for p in presets:
        index.append(f"- **{p['title']}** (`{p['id']}`): {', '.join(p['aliases'])}.")
    index += ['', '## Defaults and source differences', '',
        'New motion/launch adaptations default to music plus synchronized effects, no narration, and 15 seconds / 30fps unless explicit campaign choices or source-footage continuity require otherwise. Use one full-film request; references are optional. Retiming and replacing source silence are labeled adaptations. Most use 16:9; Exploded product starts at 9:16. Explicit campaign choices take precedence. The source baselines include distinct endings: Kinetic typography holds its final line; Glass UI freezes the complete final frame; Blueprint to building ends by un-plotting. Retain those endings where they serve the new film; adapt them deliberately rather than adding a generic house fade or assuming a seamless loop.', '',
        'Source examples may contain audio, branded claims, external reference requirements, or different native durations. These are not inherited permissions or guarantees. The footage section contains two preview clips without a verified input/output relationship. The architectural example has a misleading image-model Recreate parameter, and the watch preview is portrait despite landscape language in its linked prompt. Discover actual tool capabilities at execution time.', '',
        f"[Source article]({catalog['source_url']}). Source mapping observed 2026-09-03. Version 4 archives the exact original prompts with verified hashes and keeps separate adaptation guides. Start from the original text and its effective visual and motion techniques, adapting the sequence and timing to the viewer takeaway. Prefer a suitable current Seedance model; record a different source route as provenance. See [template-adaptation.md](template-adaptation.md).", '',
        'To extend the library, follow [preset-workflow.md](preset-workflow.md), update the catalog, preset and full template, and rerun `scripts/build_gallery.py`.', '',
    ]
    (ROOT / 'references/preset-index.md').write_text('\n'.join(index), encoding='utf-8', newline='\n')
    print(f'Validated {len(presets)} presets; refreshed gallery and index.')


if __name__ == '__main__':
    build()
