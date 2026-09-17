# Shot library validation

Recorded September 16, 2026. Current scope: five complete source timelines, 44 entries (41 shot records and three supporting technique/lighting records), alongside the existing ten film presets. Infinex has 15 records, Cero 12, Jaw/vedu_boi 12, Ordinary Folk 1, and Bhumimov/Blender 4. Records can overlap and montage records can contain several edits; these numbers are not asserted source cut counts.

## Package and delivery

- Both builders pass. Original ten preset/source-prompt data remains unchanged. Generated library output is deterministic.
- 25 standard-library tests pass: retrieval, preserved rejection state, full-source coverage without gaps, fractional FPS, intake without invented timing, duplicate-intake protection, overlapping events, technical provenance, portable paths, explicit assets, range delivery, native download names and missing media.
- Skill frontmatter and JavaScript syntax checks pass.
- The 44 records contain 278 technical sections, 110 tables and 63 formula/hierarchy blocks. Exact original controls are available for Radial Delay; exact local controls for the existing Infinex and Blender builds are distinct from proposed reconstructions.
- CI is configured to repeat both builders, tests and generated-file checks. Local success does not claim hosted CI has passed; the upstream draft PR can require maintainer approval before workflows run.

## Viewer and media

An isolated headless Chromium session verified all 44 detail routes and their excerpt metadata, all five source filters, lazy card video loading, search/reset/empty state, section navigation, keyboard tabs, native evidence, retained rejected blur, missing-media browsing and the existing ten-preset request/copy flow. Playback and source-frame seeking were checked on the fractional-rate Jaw excerpt. No page-script errors occurred.

All 44 local previews have the expected decoded frame counts and pass complete ffmpeg decoding. Preview dimensions preserve source aspect ratios: landscape references, 600×600 Radial Delay, and the wide UI source are not forced into one crop. Poster frames are documented inside each excerpt and do not change playback start. 177 explicitly bound local files exist, including dense evidence and source presentation-timestamp tables. These original/native/media payloads are not part of the public package.

Desktop and 390px mobile screenshots were inspected, including the expanded filters and representative Infinex, Cero, Jaw, Ordinary Folk and camera-study technical pages. There is no horizontal page overflow; large tables and code scroll inside their own regions.

## Inspection and creative limits

Full timeline coverage means every supplied interval has an analytical record. It does not mean every boundary is frame-exact, every original technique has been recovered, or every proposed build has been rendered. The records state sampling scope: existing dense Infinex/Cero evidence, full-film 0.5s samples for Cero/Jaw, an additional every-three-frame Jaw typography check, original Radial Delay property inspection, and existing local Blender comparison evidence.

No new AE/Blender production render, uninterrupted real-time aesthetic review, soundtrack audit or user approval was performed by this library expansion. Infinex V05 blur remains rejected and V06 remains pending. Cero/Jaw native builds are proposed. Radial Delay's independent scheduler is numerically tested, not production-approved. The existing Blender camera A/B is technically verified with creative preference pending.

## Standing capture workflow

The skill now registers every requested study/recreation immediately and updates stable records during inspection, construction and review. `intake_study.py` creates an in-progress source with unknown timing and an unbound media ID, refuses duplicates, and does not submit generation jobs. The user's preferred native tool takes precedence over the preset-generation route.
