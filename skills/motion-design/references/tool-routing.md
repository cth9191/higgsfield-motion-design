# Universal Tool Routing — Any Agent

One shared skill supports **any agent**. Capability is detected at runtime, not by host name. Check what tools are actually exposed in the current session; tool prefixes differ between clients.

## Capability matrix (detect, don't assume host)

| Task | Preferred route | Fallback | Never do |
|---|---|---|---|
| Browse examples / draft prompt | Local skill files — works everywhere, no generation | — | Don't require MCP for browsing |
| Create needed reference images | **Host-native image generation** if exposed (Codex built-in, Pi image tool, etc.) | **Higgsfield MCP** → `gpt_image_2` (GPT Image 2) | Don't call a non-existent built-in tool; don't hallucinate |
| Generate the complete film | **Higgsfield MCP** → suitable current **Seedance** | Explain missing connection + deliver prompt-ready plan | Don't switch provider silently; don't use Blender/local render |
| Inspect & finish | Host playback + Higgsfield media tools if available | Save job record + explain inspection limit | Don't claim inspection you didn't do |

**Rule:** Explicit user choices override defaults. If the preferred route is unavailable, state the gap and propose the fallback — don't silently change route.

## How to detect at runtime

1. List available tools / MCP servers in this session.
2. If a native `generate_image` / `create_image` tool exists → use it for images, following its own parameter docs.
3. Else if `higgsfield` MCP is connected → use its image + video tools.
4. Else → prompt-only mode: finish the prompt/asset plan and explain how to connect Higgsfield (see below).

Do not install or reconfigure a connection just because the user asked to browse or draft.

## Higgsfield image generation (when using MCP route)

1. Decide whether an image is needed at all. Reuse supplied product photos, screenshots or existing assets when they meet the need. A prompt-only film needs no image job.
2. Discover the image model through read-only `models/search` / `models/get` operations. The catalog observed 2026-09-05 exposes **GPT Image 2** as `gpt_image_2`, with `resolution` choices `1k`, `2k`, `4k` and `quality` choices `low`, `medium`, `high`. These are an observed preference, not a permanent schema: **inspect current availability and parameters before use**. Select quality/resolution for the asset's role and requested budget; do not silently accept a low-quality default for a detail-critical reference.
3. Inspect accepted aspect ratios, reference roles and upload requirements. Confirm cost through read-only estimation when supported. Model presence does not establish account access or free generation. If GPT Image 2 is unavailable, explain the limitation and a suitable alternative; preserve any explicit model restriction.
4. Submit only within image/production authorization. A request to review the film prompt first stops before image generation, uploads and video generation. Follow the live tool's result/wait mechanism, inspect the image, and retain its job record.

## Higgsfield video generation (universal)

- **Same in every host:** Higgsfield MCP, preferring current Seedance family. Inspect its actual schema for duration, aspect ratio, resolution, reference roles/limits, audio support and prompt constraints.
- Use **one complete-film request** by default. See `production.md`.
- Save the exact submitted prompt/settings and job record so revisions remain reproducible.
- A failed probe is not a completed film. Rejoin an existing job after an uncertain response instead of submitting a duplicate.

## Bind images to the film (any host)

Record why each image is used: identity, style, motion, start frame or end frame. Keep content references distinct from style references. A general style image must not silently become a fixed opening composition. Do not use a storyboard contact sheet as the literal first frame.

A local image path is not a remote attachment. Use the client's supported upload operation, transfer bytes if the tool requires it, and confirm only after successful transfer. Reuse a Higgsfield-generated asset directly only when the video tool accepts its returned media identifier or URL. A job ID is not automatically a media ID. Bind actual inputs using the video model's current schema; never invent an ID, reuse an unrelated asset, or pass a local path as a public URL.

Keep exact image prompts, selected models/settings, asset roles and returned identifiers in the private campaign workspace. Do not copy account configuration or private asset URLs into this public skill package.

## Connection help — universal MCP

Installing this skill and authenticating to Higgsfield are separate steps.

**Official Higgsfield MCP endpoint:** `https://mcp.higgsfield.ai/mcp` (HTTP transport, OAuth)

### Per-host quick connect:

| Host | How to connect |
|---|---|
| **Claude Code** | `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp` then `/mcp` → authenticate |
| **Codex** | Add Higgsfield plugin/connector in Codex UI, or manual remote MCP `https://mcp.higgsfield.ai/mcp` |
| **Cursor** | Settings → MCP → Add Server → `https://mcp.higgsfield.ai/mcp` (HTTP) |
| **Windsurf** | MCP settings → Add HTTP server → same URL |
| **Pi** | `pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp` or via `~/.pi/config` |
| **Generic MCP host** | Add HTTP MCP server `higgsfield` at `https://mcp.higgsfield.ai/mcp`, then OAuth |
| **No MCP support** | Prompt-only mode: you can still browse, adapt prompts, and export the full prompt for use in Higgsfield web app |

**Check without generating:**
```
Check the connected Higgsfield tools and use read-only model discovery to find
a suitable Seedance video model and GPT Image 2 for reference images.
Report the available routes. Do not generate or upload anything.
```

GPT Image 2 appeared as `gpt_image_2` in the connected catalog on 2026-09-05. Availability, input roles and settings must still be checked for the current account. A model listing alone does not prove entitlement or free usage.

Also see: https://higgsfield.ai/mcp and https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent

## Host adapters

Adapters in `agents/` provide host-specific install hints but the skill itself is host-agnostic. Any agent that can read `SKILL.md` and expose MCP tools can run production; others run prompt/gallery mode.
