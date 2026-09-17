# Validation and next steps

The shared workflow is implemented for Codex and Claude Code. This page separates shipped instructions and tooling from creative results that still need recorded trials. It is not a promise that all ten presets reproduce their source examples reliably.

## Implemented

- [x] Ten presets, exact archived source prompts with hash checks, separate adaptation guides and a playable gallery.
- [x] One shared skill with Codex and Claude Code installation instructions and the appropriate invocation in gallery requests.
- [x] Host-aware reference images: Codex built-in image generation when available; Claude Code via Higgsfield MCP, preferring GPT Image 2 after live capability checks.
- [x] Before/after production review using each preset's existing fidelity requirements, with observed timestamps and pass/fail/not-inspected status. See [quality-review.md](skills/motion-design/references/quality-review.md).
- [x] Separate correction guidance for motion, identity, exact text/data, audio and export problems, with bounded retries.
- [x] README source-preview stills and links, setup walkthrough and source attribution.
- [x] One Infinex study with three complete documented shot breakdowns and two supporting technique/lighting records, inspiration and technical views, inline formulas/control tables, overlapping timelines, native evidence bindings and separate creative review states. See [validation](docs/library-validation.md).
- [x] Explicit study/native/generation routing, portable retrieval data, local video seeking and catalog/server checks in CI.

The pilot does not complete the broader four-study set. Next: select and audit the remaining references using the same data contract, validate a reusable native construction, and resolve the Infinex blur defect before approving that recipe. No new native render or creative approval was produced by the library integration.

These items mean the instructions and package exist. They do not establish generation quality, production cost or successful end-to-end execution in both clients.

## Before the public walkthrough

| Trial | Evidence to retain | Done when |
|---|---|---|
| Typography announcement | Original reference, adapted prompt, resulting film, exact copy and timing review | The headline reads correctly and the defining graphic phases and ending are inspected. |
| One real product | Supplied identity asset, its declared role, prompt, resulting film | Appearance remains recognizable and the product-specific action matches the chosen guide. |
| One-idea explainer | Verified concept/claims, copy inventory, resulting film | The animation explains the intended idea without unsupported claims or invented chart data. |
| Claude Code image handoff | GPT Image 2 image request/result, actual video input binding, film and review | A needed image reaches a complete film through the Claude Code MCP route. |

For each trial record host/version, model, exact native settings, source departures, assets and roles, generation time, retries, actual cost if available (estimates labeled separately), and remaining defects. Keep private campaign files outside the public repository. Publish only examples intended for public sharing, labeling source examples and our adaptations separately.

The source previews are usable as style demonstrations now. They are not completion evidence for the trials above. No paid trials were run as part of the documentation/compatibility update.

## Experiments after the baseline

| Question | Useful comparison | Evidence needed before claiming an improvement |
|---|---|---|
| Does a style frame improve fidelity? | Prompt-only versus one composed style reference, holding other settings and product inputs steady | Repeated reviews against the same preset requirements; report variations and costs. |
| Does a video reference preserve motion better? | Same campaign with and without a supported motion-reference input | Verified model support and playback evidence, separate from identity-reference effects. |
| Can fact-heavy films preserve exact graphics? | Generated text/data versus a supported exact overlay or replacement | Delivered frames matching the verified source text, values and geometry. No pixel-exact claim from conditioning alone. |
| Can CLI-only Claude Code use the same workflow? | Verify equivalent discovery, uploads, image/video jobs, waits and inspection through the official CLI | A documented adapter and a complete trial; do not silently substitute CLI commands for MCP calls. |

Exact text/chart finishing is a disclosed conditional fallback today, not a universally tested automatic compositor. Failure-routing instructions exist; their success rate remains unmeasured. A passing catalog validator establishes package consistency, not creative reliability.
