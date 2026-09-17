# Set up Codex or Claude Code

Install the same complete `skills/motion-design/` folder in either app. It includes film presets, shot studies, technical breakdowns and both galleries. App-specific image routes live in [tool-routing.md](../skills/motion-design/references/tool-routing.md). Higgsfield setup is only needed for generation; skip to section 5 for reference studies and native construction.

## Updating an earlier installation

Earlier versions used the name `higgsfield-motion-design`. Install the updated folder as `motion-design`, then archive the old folder outside your app's skills directory after preserving any customizations. This avoids loading both names. Your commands become `$motion-design` in Codex and `/motion-design` in Claude Code. The repository is now `cth9191/motion-design`; update the Git remote in existing checkouts if needed.

## 1. Install the skill

### Codex

Paste this into Codex:

```text
$skill-installer

Install the skill from:
https://github.com/cth9191/motion-design/tree/main/skills/motion-design
```

For an existing installation, ask to update it and preserve any local customizations. Start a new session if the installed skill is not yet visible.

### Claude Code

Paste this into Claude Code:

```text
Install the motion-design skill from
https://github.com/cth9191/motion-design

Clone the repository into a temporary working folder, then copy the complete
skills/motion-design directory into my personal ~/.claude/skills/
directory. If it already exists, compare it, back up local customizations,
and update that skill. Do not put the entire repository inside the skill folder.
```

The final entrypoint must be `~/.claude/skills/motion-design/SKILL.md`. On Windows, `~` is your user profile. For project-only installation, use `.claude/skills/motion-design/` in that project instead. Invoke it with `/motion-design`. See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills) for discovery and scope.

## 2. Connect Higgsfield

You can browse the gallery and draft prompts without Higgsfield. Image/video generation needs your own authenticated account, model access and credits or an applicable allowance. Installing this skill does not install or authenticate Higgsfield.

### Codex

Add and authenticate the Higgsfield plugin/connector available in your Codex environment. If your client uses manual remote MCP configuration, the official endpoint is `https://mcp.higgsfield.ai/mcp`. Follow the client's connection UI and the [Higgsfield connection page](https://higgsfield.ai/mcp); connection options vary by client.

### Claude Code: direct MCP route

First inspect existing connections:

```sh
claude mcp list
```

If Higgsfield is already connected, reuse it. Otherwise add the remote server for your user:

```sh
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Open Claude Code, run `/mcp`, select Higgsfield and complete its browser authentication. Then check `claude mcp list` again. This direct MCP route was observed connected on the maintainer's Claude Code installation on September 5, 2026. See [Claude Code's MCP documentation](https://code.claude.com/docs/en/mcp) for HTTP servers and OAuth.

Higgsfield also documents a CLI installation path for Claude Code in its [integration guide](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent). This package currently targets MCP. Installing only the CLI does not expose the MCP tools expected by this skill; CLI-only execution is not yet validated here.

### Check access without generating

Ask your assistant:

```text
Check the connected Higgsfield tools and use read-only model discovery to find
a suitable Seedance video model and GPT Image 2 for reference images.
Report the available routes. Do not generate or upload anything.
```

GPT Image 2 appeared as `gpt_image_2` in the connected model catalog on September 5, 2026. Availability, input roles and settings must still be checked for the current account. A model listing alone does not prove entitlement or free usage.

## 3. Try a prompt first

In Codex, start with `$motion-design`; in Claude Code, use `/motion-design`. Then paste:

```text
Use the kinetic typography preset for a 15-second announcement:
"Build your first AI workflow."
Keep the copy short. Use music and synchronized effects, without narration.
Show me the complete adapted prompt before generating anything.
```

The assistant should read the original source prompt, adapt its motion and copy, and show the complete draft. This request stops before creating images, uploading assets or submitting video. When ready, ask it to generate the film; actual production can incur Higgsfield charges.

## 4. Browse the playable gallery

Open `skills/motion-design/assets/gallery.html` from your local repository or installed skill. If your app cannot open local HTML, run this from the repository root:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory skills/motion-design
```

Visit [the local gallery](http://127.0.0.1:8765/assets/gallery.html), choose a look, select Codex or Claude Code, add a brief and copy the request into that app. Close the server with Ctrl+C when finished. Python 3.10+ is needed only for this server or the gallery builder. Previews stream from public source URLs and need internet; the prompt library is local.

## Common fixes

See [section 5](#5-browse-shots-and-technical-breakdowns) for the shot library and local media connection.

| Symptom | Check |
|---|---|
| The skill is missing | Confirm the full folder and `SKILL.md` are at the correct discovery path; start a new session if necessary. |
| Claude tries to use a built-in Codex image tool | Update the entire skill folder, including references and gallery. The shared version routes Claude images to Higgsfield. |
| Higgsfield needs authentication | Reconnect through your client's MCP/plugin UI; installing the skill does not transfer someone else's login. |
| GPT Image 2 or Seedance is unavailable | Inspect current models and account access; report the limitation before changing an explicit model choice. |
| A preview is unavailable | Use its source article link. A failed preview does not remove the archived prompt or prove generation is unavailable. |
| The gallery shows HTML source on GitHub | Open the downloaded file locally or use the loopback server above. |
| Exact type or charts are wrong in the film | Inspect the output and use the supported correction/finishing route; a reference image cannot guarantee exact pixels. |

## 5. Browse shots and technical breakdowns

From a repository checkout, run:

```sh
python skills/motion-design/scripts/serve_library.py
```

Visit [the shot library](http://127.0.0.1:8766/assets/library.html). Search by story purpose, subject or technique, then switch between **Inspiration** and **Technical breakdown**. Event bars use source-frame timing and seek the corresponding excerpt when connected. Native links download evidence files; opening the gallery does not execute construction scripts or change an AE/Blender project.

The packaged records work without local media. To connect existing source clips and native evidence:

1. Copy `skills/motion-design/library/asset-map.example.json` to the ignored `work/library-assets.local.json` file; create `work/` if needed.
2. Change `study-workspace` to your local study workspace and, if connecting the full UI reconstruction, `world-cup-workspace` to that project folder. The example's relative paths describe the original workspaces; adjust or remove bindings when your files differ. Use forward slashes in JSON paths.
3. Start the server with that manifest:

```sh
python skills/motion-design/scripts/serve_library.py --assets-file work/library-assets.local.json
```

Only explicit asset IDs are served. Missing files are labeled disconnected, and the breakdown stays readable. Keep private manifests and media outside the shared skill; do not commit machine-specific paths. In an installed skill, run `python scripts/serve_library.py` from the skill folder and pass an absolute path to your private manifest. Stop the server with Ctrl+C.

To retrieve evidence without a browser, run from the skill folder:

```sh
python scripts/build_library.py search "blur bounds" --tool "After Effects"
python scripts/build_library.py show DETAIL-INF-DEFOCUS
```

The [library workflow](../skills/motion-design/references/library-workflow.md) explains native reuse and adding studies. Code validation and creative approval are separate: inspect the entry's review state before reusing a recipe.
