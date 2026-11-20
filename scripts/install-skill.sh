#!/usr/bin/env bash
# Install the self-contained egern-docs skill into an agent skills directory.
#
#   ./scripts/install-skill.sh                      # -> ~/.claude/skills
#   ./scripts/install-skill.sh ~/.agents/skills     # any other skills dir
#
# The skill directory carries its own docs snapshot, so one symlink is enough.
# Symlinked (not copied) so it always reads the current snapshot.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$REPO/.agents/skills/skills/egern-docs"
SKILLS_DIR="${1:-$HOME/.claude/skills}"
TARGET="$SKILLS_DIR/egern-docs"

if [ ! -d "$SOURCE" ]; then
  echo "error: skill source not found at $SOURCE" >&2
  exit 1
fi

mkdir -p "$SKILLS_DIR"

if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
  echo "error: $TARGET exists and is not a symlink; move it away first" >&2
  exit 1
fi

ln -sfn "$SOURCE" "$TARGET"

echo "installed: $TARGET -> $SOURCE"
