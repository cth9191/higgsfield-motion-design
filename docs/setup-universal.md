# Universal Setup — Any Agent

Works on **any agent** that can read a `SKILL.md` file. Gallery + prompt drafting work with no account. Video needs Higgsfield MCP.

## 1. Install the skill (any agent)

Copy the complete folder `skills/motion-design` into your agent's skills directory:

| Agent | Target path | Invoke |
|---|---|---|
| **Codex** | `~/.codex/skills/motion-design` or via `$skill-installer` | `$motion-design` |
| **Claude Code** | `~/.claude/skills/motion-design` | `/motion-design` |
| **Cursor** | `.cursor/skills/motion-design` or `~/.cursor/skills/motion-design` | `motion-design` |
| **Pi** | `~/.pi/agent/skills/motion-design` | `motion-design` |
| **Windsurf** | `~/.windsurf/skills/motion-design` | `motion-design` |
| **Generic / Other** | `./skills/motion-design` or `~/.agent/skills/motion-design` | `motion-design` |

**Universal installer (copy-paste):**
```sh
git clone https://github.com/cth9191/motion-design.git /tmp/motion-design
# Pick ONE of these:
mkdir -p ~/.claude/skills && cp -r /tmp/motion-design/skills/motion-design ~/.claude/skills/motion-design  # Claude
mkdir -p ~/.pi/agent/skills && cp -r /tmp/motion-design/skills/motion-design ~/.pi/agent/skills/motion-design  # Pi
mkdir -p .cursor/skills && cp -r /tmp/motion-design/skills/motion-design .cursor/skills/motion-design  # Cursor
```

Verify entrypoint exists: `skills/motion-design/SKILL.md` must be present in the destination.

## 2. Connect Higgsfield (only for image/video generation)

Official MCP endpoint: `https://mcp.higgsfield.ai/mcp` (HTTP + OAuth)

| Host | Command / UI |
|---|---|
| Claude Code | `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp` then `/mcp` |
| Codex | Add Higgsfield connector in Codex UI, or manual remote MCP `https://mcp.higgsfield.ai/mcp` |
| Cursor | Settings → MCP → Add Server → `https://mcp.higgsfield.ai/mcp` |
| Windsurf | MCP Settings → Add HTTP Server → same URL |
| Pi | `pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp` |
| Generic | Add HTTP MCP server named `higgsfield` at `https://mcp.higgsfield.ai/mcp` |

No MCP? You can still browse and export the full prompt, then paste it into https://higgsfield.ai Marketing Studio.

**Check without generating:**
```
Check the connected Higgsfield tools and use read-only model discovery to find
a suitable Seedance video model and GPT Image 2 for reference images.
Report the available routes. Do not generate or upload anything.
```

## 3. Try a prompt (no generation)

In your agent, run `motion-design` (or `$motion-design` / `/motion-design` per host) then:

```
Use the kinetic typography preset for a 15-second announcement:
"Build your first AI workflow."
Use music and synchronized effects, without narration.
Show me the complete adapted prompt before generating anything.
```

Should return a full adapted prompt without calling any generation tool.

## 4. Browse the gallery (offline-capable)

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory skills/motion-design
# open http://127.0.0.1:8765/assets/gallery.html
```

Or open `skills/motion-design/assets/gallery.html` directly. Gallery does not send data anywhere; it copies a request for you to paste into your agent.

## Host capability detection

Skill auto-detects at runtime (see `references/tool-routing.md`):
- **Prompt/gallery** → always works
- **Images** → host-native if available, else Higgsfield `gpt_image_2`
- **Video** → Higgsfield MCP Seedance (any host with MCP). Without MCP, delivers prompt for web use.

See `references/tool-routing.md` for the full matrix.
