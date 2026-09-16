# Use references for inspiration and implementation

Use this workflow when the user wants shot ideas, deep reference studies, technical breakdowns or a native reconstruction. The existing Higgsfield preset workflow remains available for generated-film requests.

## Retrieve the relevant evidence

Start with [the compact index](../library/index.md), the [gallery](../assets/library.html), or a metadata query from the skill directory:

```sh
python scripts/build_library.py search "persistent hero" --video-type product-launch
python scripts/build_library.py search "blur bounds" --tool "After Effects"
python scripts/build_library.py show DETAIL-INF-DEFOCUS
```

Search by the story job, shot family, visual behavior and chosen tool. Open the selected detail JSON and its source study; do not load every entry to answer one shot question. For inspiration, inspect the actual passage and explain which action or relationship helps the new story. For technical work, read the controls, hierarchy, effect order, files and latest review before adapting them.

Keep four things separate: visible reference behavior; original source settings when available; our implementation; and untested proposals. A reference clip needs no original prompt. An attractive source does not make a rejected reconstruction a validated recipe. Use the recorded inspection scope; frame sheets cannot establish continuous motion or sound quality.

## Choose the production route from the task

- **Study or inspiration:** inspect and explain; create measurements or a deeper record when requested. No generation is required.
- **Native AE/Blender build:** use the selected local implementation and the user's chosen tools. Resolve linked files and dependencies first. Inspect one-time authoring scripts and their source-project guards rather than executing them wholesale. Keep native projects editable, preserve current work, and compare the uncertain passage including both joins.
- **Higgsfield generation:** use the chosen preset or supplied-video workflow, with the existing production/tool-routing guidance. Do not silently replace an explicitly requested native build with generation, or a generation request with local rendering.

A native entry is an evidence-backed starting point, not a universal ready-to-run template. Refit typography, geometry, scene scale and timing for the current story. Retain useful relationships such as longer settles than onset gaps and independently timed focus/opacity. Inspect the actual render and save the version and keep/reject reason before changing the entry's review state.

## Open the local gallery

From the repository root:

```sh
python skills/motion-design/scripts/build_library.py
python skills/motion-design/scripts/serve_library.py
```

Open `http://127.0.0.1:8766/assets/library.html`. Both gallery sections and all packaged breakdowns work without a media connection. Source links remain available; unbound local previews and native files are labeled as disconnected.

To connect an existing Shot Studio workspace, copy `skills/motion-design/library/asset-map.example.json` to ignored `work/library-assets.local.json`, change its `study-workspace` root, then run:

```sh
python skills/motion-design/scripts/serve_library.py --assets-file work/library-assets.local.json
```

For an installed skill, run the same scripts from that skill folder and store the private manifest outside the package. The server binds only to loopback. It exposes explicit asset IDs, supports video byte ranges for seeking, and never opens AE/Blender or sends assets to a provider. Stop it with Ctrl+C when no longer needed.

## Add a study or result

Follow [the data contract](../library/schema.md). Add a source study, select a passage with its incoming/outgoing context, then link shot and technique entries. Record overlapping event tracks rather than forcing independent actions into consecutive narrative phases. Keep units, source/preview clocks, exact provenance, dependencies and source-usage terms.

Keep shareable descriptions and independently authored reusable code in the package. Keep original videos, restricted projects and private production files in the workspace; bind their stable IDs locally. Use one canonical entry for a technique and link it from several video types. Run the library builder and focused tests after changing the data contract. Source-study depth and creative approval are independent: unknown fields stay unknown.
