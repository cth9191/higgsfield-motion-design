#!/usr/bin/env bash
set -e
# Universal installer for motion-design skill — any agent
# Usage: bash scripts/install-universal.sh [--target DIR] [--agent NAME]
REPO="https://github.com/cth9191/motion-design.git"
SKILL_SRC="skills/motion-design"

detect_agent() {
  if [ -d "$HOME/.claude" ]; then echo "claude"; return; fi
  if [ -d "$HOME/.pi" ]; then echo "pi"; return; fi
  if [ -d ".cursor" ] || [ -d "$HOME/.cursor" ]; then echo "cursor"; return; fi
  echo "generic"
}

TARGET=""
AGENT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2;;
    --agent) AGENT="$2"; shift 2;;
    *) echo "Unknown arg $1"; exit 1;;
  esac
done

if [ -z "$AGENT" ]; then AGENT=$(detect_agent); fi

case "$AGENT" in
  claude) TARGET="${TARGET:-$HOME/.claude/skills/motion-design}" ;;
  pi) TARGET="${TARGET:-$HOME/.pi/agent/skills/motion-design}" ;;
  cursor) TARGET="${TARGET:-.cursor/skills/motion-design}" ;;
  codex) TARGET="${TARGET:-$HOME/.codex/skills/motion-design}" ;;
  windsurf) TARGET="${TARGET:-$HOME/.windsurf/skills/motion-design}" ;;
  generic|*) TARGET="${TARGET:-./skills/motion-design}" ;;
esac

echo "Agent: $AGENT"
echo "Target: $TARGET"

if [ -d "$SKILL_SRC" ]; then
  echo "Found local $SKILL_SRC — copying"
  SRC="$SKILL_SRC"
else
  echo "Cloning $REPO to /tmp/motion-design"
  rm -rf /tmp/motion-design
  git clone "$REPO" /tmp/motion-design
  SRC="/tmp/motion-design/$SKILL_SRC"
fi

mkdir -p "$(dirname "$TARGET")"
rm -rf "$TARGET"
cp -r "$SRC" "$TARGET"
echo "✓ Installed to $TARGET"
echo "Verify: ls $TARGET/SKILL.md"

# Higgsfield MCP hint
echo ""
echo "For video generation, connect Higgsfield MCP:"
echo "  https://mcp.higgsfield.ai/mcp"
echo "  Claude: claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp"
echo "  Pi: pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp"
echo "  Cursor/Windsurf: Settings → MCP → Add HTTP server → same URL"
echo "Prompt & gallery work without MCP."
