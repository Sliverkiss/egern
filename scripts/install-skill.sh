#!/usr/bin/env bash
# Install the egern-docs skill into a Claude Code skills directory.
# Links (not copies) so the skill always reads the current snapshot.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="${1:-$HOME/.claude/skills}"
TARGET="$SKILLS_DIR/egern-docs"

mkdir -p "$SKILLS_DIR"

if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
  echo "error: $TARGET exists and is not a symlink; move it away first" >&2
  exit 1
fi

ln -sfn "$REPO/.agents/skills/egern-docs" "$TARGET"
ln -sfn "$REPO/docs" "$TARGET/docs"

echo "installed: $TARGET"
echo "  -> $REPO/.agents/skills/egern-docs"
echo "  -> $REPO/docs"
