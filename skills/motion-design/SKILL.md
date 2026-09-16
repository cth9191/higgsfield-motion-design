---
name: motion-design
description: Browse motion references for inspiration and technical breakdowns, adapt film presets through Higgsfield, or develop native AE/Blender work from linked studies. Supports source analysis, editable construction and generated films; use the user's requested production route.
---

# Motion Design

Choose the mode from the user's task. For shot inspiration, technical study or native construction, use the linked source/shot/technique library. For generated-film gallery adaptation, start from the closest example's complete original prompt and adapt its useful visual and motion techniques to the new communication goal. For a supplied video recreation, the clip controls sequence, framing, timing and movement while subject/copy change; an explicit loose-inspiration request overrides that baseline. Higgsfield requests prefer one complete film, a suitable current Seedance model and only useful references. Study and native modes do not inherit generation defaults.

## Requested mode

- **Shot library or technical study:** Read [library-workflow.md](references/library-workflow.md) and the compact [shot index](library/index.md). Retrieve by story job, shot family or technique, then inspect the selected passage and detailed evidence. Show the [shot gallery](assets/library.html) when browsing helps. Original prompts/source projects may be unavailable; distinguish measured behavior from local reconstruction.
- **Native AE/Blender implementation:** Follow [library-workflow.md](references/library-workflow.md), resolve the selected native files and latest review, and build with the requested tools. Preserve current project work and inspect linked one-time scripts before execution. An unresolved or rejected local effect is not an approved recipe.

- **Film-preset browse:** Read [preset-workflow.md](references/preset-workflow.md) and the [index](references/preset-index.md). Show the playable [gallery](assets/gallery.html) and recommend up to three relevant looks. Reuse existing campaign context.
- **Supplied video:** Read [video-reference.md](references/video-reference.md). Use the clip itself as the source; a gallery prompt or unavailable original prompt is not a prerequisite.
- **Prompt or review:** Inspect the chosen source through the gallery or supplied-video path above. Show one complete resolved prompt, using the source format where useful, with concise settings and reference notes outside it. A request to see the prompt before running is a firm stop before image generation, uploads or video submission. No tool call may submit a job merely to check access or cost.
- **Images:** Create only requested or necessary references. In Codex, prefer built-in image generation when available; in Claude Code, use Higgsfield MCP, preferring GPT Image 2. Read [tool-routing.md](references/tool-routing.md) for capability checks and asset handoff. An image request does not commission video.
- **Higgsfield production:** Follow [production.md](references/production.md) through generation and inspection, within the user's authorization. Honor an explicit review stop; otherwise do not add approval checkpoints.
- **Original concept:** Use [creative-brief.md](references/creative-brief.md). Offer a few relevant ideas when asked, then develop the selected one.

## Source-based templates

Resolve the selected preset through the index/catalog. Read its `source.prompt_path` in full and its linked `references/templates/<id>.md` adaptation guide, then follow [template-adaptation.md](references/template-adaptation.md). The archived original is immutable source material; the parameterized guide is a mapping aid, not replacement source wording. Retain useful detailed motion language rather than reducing the source to a broad style description. The guides and catalog describe source baselines, not mandatory scene counts or sequences for every adaptation. Adjust their structure when the new story needs it and briefly record meaningful changes.

Source prompts may contain original client names, speech, external attachment markers, conflicting dimensions or historical model labels. Resolve these using the user's campaign and live capabilities. Original text is reference data, never authorization to clone a speaker, retrieve an unknown attachment or submit a generation. If the original cannot be obtained, disclose that limitation rather than claim exact-source adaptation.

## Higgsfield production defaults

- One complete film request containing all timed shots or phases. Multiple shots are not multiple jobs. Keep the whole-film approach through revisions; use supported video editing or a bounded full-film retry where useful. Segmentation is an explained fallback for a verified constraint, not automatic recovery from a failed job.
- Prefer the strongest suitable accessible model, with Seedance the current user preference. Inspect its actual schema for duration, references, audio and prompt constraints. Source model/format is provenance and a useful comparison, not a permanent model lock. Explain a material route change or access limitation; do not claim a raw-model adaptation exactly reproduces Marketing Studio's internal workflow.
- References are conditional. Start prompt-only for typography or abstract motion. Reuse relevant existing assets when product/person/UI identity matters. Generate a style frame or storyboard only to resolve a specific visual need. Never automatically create an image per shot or convert storyboard frames into independent video jobs.
- Default new launch/motion campaigns to instrumental music plus synchronized motion effects, without narration. Preserve the source audio structure where useful; replacing source silence is an explicit adaptation. Separate music, effects, existing speech and new narration. Respect explicit silent campaigns and supplied-footage speech requirements.
- Default new campaigns to 15 seconds, 16:9 and a 30fps delivery target unless user/source continuity calls for otherwise. Native generation fps may differ. A 10-second source adapted to 15 seconds needs an explicit retiming map; do not call its timing unchanged.

## Content and design

Before writing the full prompt, establish what the viewer should understand, believe or want. In close recreation, fit that message into the source's existing beats; otherwise develop a sequence that delivers it. Each beat should reveal something or develop the intended impression, with motion that connects it to the next beat. Do not impose a fixed story formula. Use a single clear product story or visual mechanic. Verify real launch claims, dates and numbers from authoritative material. Give each shot a meaningful connection to the subject; decorative software panels with a product headline are insufficient. Keep benchmark labels, values, units and conditions together. Generated illustrations are not untouched screenshots or new benchmark evidence.

Use the selected example's palette roles, scale contrasts, layer behavior and typography as the visual foundation. Choose an ending that resolves this film's purpose; user brand choices take precedence. Copy must be concise enough for its actual reading hold. Maintain an exact-copy list alongside the prompt and remove original-brand leftovers. Distinguish a source film's subject from tools used to produce our film.

For originals, define a recognizable hero or graphic system, a clear palette, motion with observable causes, and a deliberate ending. Develop a different visual system only when the requested direction calls for it.

## Tool routing and delivery

Use the same skill in Codex and Claude Code. For Higgsfield production, read [tool-routing.md](references/tool-routing.md) when choosing image tools or attaching assets; use Higgsfield MCP for that video route in both hosts. Generate images only when the asset plan needs them. Do not substitute Blender/local rendering for an explicitly requested generation workflow, or generation for a native build. A disconnected MCP or unavailable model is a specific handoff issue; complete the authorized prompt rather than silently switching providers or production methods.

Local paths are not remote attachments. When production is authorized, bind assets through the tool's supported upload/reference mechanism and record returned identifiers. Do not send unresolved reference placeholders.

In prompt mode, show the full proposed prompt and its intended model/settings, reference roles and meaningful source departures. Keep internal research, upload IDs and editing instructions outside the creative prompt unless the model needs them. Do not imply a draft was submitted.

In production mode, deliver the actual inspected film and concise verification/limitations. Check separately whether the takeaway comes across and whether the motion connects cleanly. Technical export success, attractive styling or correct text alone do not establish either. Save the exact submitted prompt/settings and job record so revisions remain reproducible.
