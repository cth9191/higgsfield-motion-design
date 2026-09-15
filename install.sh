#!/usr/bin/env bash
set -e
# King-design — Universal One-liner Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash
#    or: curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash -s -- --agent pi
REPO="https://github.com/MOT1209/King-design.git"
BRANCH="main"

AGENT=""
TARGET=""
while [ $# -gt 0 ]; do
  case "$1" in
    --agent) AGENT="$2"; shift 2;;
    --target) TARGET="$2"; shift 2;;
    --help|-h) echo "Usage: $0 [--agent claude|codex|cursor|pi|windsurf|generic] [--target DIR]"; exit 0;;
    *) echo "Unknown arg: $1"; exit 1;;
  esac
done

detect_agent() {
  if [ -n "$AGENT" ]; then echo "$AGENT"; return; fi
  if [ -d "$HOME/.claude" ]; then echo "claude"; return; fi
  if command -v pi >/dev/null 2>&1 || [ -d "$HOME/.pi" ]; then echo "pi"; return; fi
  if [ -d ".cursor" ] || [ -d "$HOME/.cursor" ]; then echo "cursor"; return; fi
  if [ -d "$HOME/.codex" ]; then echo "codex"; return; fi
  echo "generic"
}

AGENT=$(detect_agent)
case "$AGENT" in
  claude) TARGET="${TARGET:-$HOME/.claude/skills/motion-design}" ;;
  codex) TARGET="${TARGET:-$HOME/.codex/skills/motion-design}" ;;
  cursor) TARGET="${TARGET:-.cursor/skills/motion-design}" ;;
  pi) TARGET="${TARGET:-$HOME/.pi/agent/skills/motion-design}" ;;
  windsurf) TARGET="${TARGET:-$HOME/.windsurf/skills/motion-design}" ;;
  generic|*) TARGET="${TARGET:-./skills/motion-design}" ;;
esac

echo "┌─────────────────────────────────────┐"
echo "│  Motion Design — Universal Installer │"
echo "└─────────────────────────────────────┘"
echo "Agent : $AGENT"
echo "Target: $TARGET"
echo ""

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo "→ Cloning $REPO ($BRANCH)..."
git clone --depth 1 --branch "$BRANCH" "$REPO" "$TMPDIR/motion-design" 2>&1 | sed 's/^/  /'

SRC="$TMPDIR/motion-design/skills/motion-design"
if [ ! -f "$SRC/SKILL.md" ]; then echo "✗ SKILL.md not found in $SRC"; exit 1; fi

echo "→ Installing to $TARGET..."
mkdir -p "$(dirname "$TARGET")"
rm -rf "$TARGET"
cp -r "$SRC" "$TARGET"

echo ""
echo "✓ Installed to $TARGET"
echo "  Verify: ls $TARGET/SKILL.md"
echo ""
echo "─ Higgsfield MCP (for video generation) ─"
echo "  Endpoint: https://mcp.higgsfield.ai/mcp"
echo "  Claude : claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp"
echo "  Pi     : pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp"
echo "  Cursor : Settings → MCP → Add HTTP server"
echo "  Docs   : https://github.com/MOT1209/King-design/blob/main/docs/setup-universal.md"
echo ""
echo "  Prompt & gallery work without MCP."
echo ""
echo "Try: motion-design  (or \$motion-design / /motion-design per host)"
