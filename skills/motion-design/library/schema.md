# Library data contract — version 1

`catalog.json` is the portable registry. `entries/<ID>.json` contains the selected detail; the browser loads that record only when opened. The builder generates the compact gallery index and Markdown retrieval index. The existing whole-film `assets/presets.json` remains a separate, unchanged contract.

## Registry

- `studies`: stable ID, title, attribution, HTTPS source URL, source asset ID and packaged study document. `source_project` and `original_prompt` may be null.
- `assets`: stable asset ID → label and kind (`video`, `image`, `document`, `native`, `code`). No machine-specific location belongs here.
- `entries`: stable ID, study ID, title/summary, kind (`shot`, `technique`, `lighting`), video types, story jobs, tags, implementation tools, review state and detail path. The summary review state must match the detailed record.
  Optional `poster_asset` references a local image, with `poster_source_frame` documenting a representative frame inside the excerpt. Posters do not change playback start or the source/preview time mapping.

## Detail

- `clip`: preview asset ID, explicit source-frame clock, integer FPS and half-open `[first,end)` source interval. Previews start at player time 0; map source events with `(sourceFrame-first)/fps`.
- `inspiration`: viewer purpose, action sequence, useful situations, attention and shot-level meta fields. Analytical system counts must state the grouping and never claim unknown source layer counts.
- `tracks`: named animation tracks and labeled half-open frame intervals. Overlap is permitted both within and across tracks. Events must stay within the excerpt and carry their evidence basis.
- `technical`: evidence statement, construction/reproduction sections, parameters with units and basis, implementations with tool/status/asset IDs. Do not label proposed code as rendered.
  Sections may include `code` blocks (`label`, `text`, `basis`) and `tables` (`caption`, `columns`, rectangular `rows`, `basis`). Use them to publish formulas, hierarchy and complete authored control arrays directly on the shot page. Put units in column headings and distinguish measured coordinates from native property values. These are evidence snippets, not scripts to execute against an open project.
- `review`: independent creative state, scope, date, actual inspection and limitations. State is `pending`, `mixed`, `rejected` or `approved`; approval applies only to the documented version and scope.
- `evidence_assets` and `related_ids`: resolvable links to evidence and other entries.

Evidence basis is `measured-reference`, `original-source`, `local-implementation` or `proposed`. Recording an exact local setting does not recover an original source setting. Measurements carry sampling uncertainty in the record's notes.

## Private asset bindings

Copy `asset-map.example.json` outside the package or into the repository's ignored `work/` directory. Set the named root to the actual local study workspace. Each binding maps one known asset ID to a relative path within that root. Missing files remain visibly disconnected; arbitrary paths, traversal and directory browsing are not supported.

Shared catalogs never need an absolute user path. The loopback server serves only enumerated local asset files, plus packaged static files. It does not upload media or launch native applications. Keep restricted source archives and project assets outside the public package.

Run `python scripts/build_library.py` from the skill folder to validate IDs, relationships, asset references, frame intervals, evidence labels, review consistency and packaged documents. This checks catalog consistency; it does not validate the perceptual quality of a film.
