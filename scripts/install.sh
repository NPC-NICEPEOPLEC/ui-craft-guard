#!/usr/bin/env bash
set -euo pipefail
CLIENT="${1:-codex}"
PROJECT="${2:-.}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
case "$CLIENT" in
  codex) TARGET="$PROJECT/.agents/skills/ui-craft-guard" ;;
  claude) TARGET="$PROJECT/.claude/skills/ui-craft-guard" ;;
  dsh) TARGET="$PROJECT/.dsh/skills/ui-craft-guard" ;;
  *) echo "Usage: bash scripts/install.sh {codex|claude|dsh} /path/to/project" >&2; exit 2 ;;
esac
if [[ -e "$TARGET" ]]; then
  echo "Refusing to overwrite existing skill: $TARGET" >&2
  exit 1
fi
mkdir -p "$(dirname "$TARGET")"
cp -R "$ROOT/skills/ui-craft-guard" "$TARGET"
echo "Installed to: $TARGET"
