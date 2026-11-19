#!/usr/bin/env bash
# Offline, backup-first updater for three user-level skill directories.
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
source_dir="$repo/skills/ui-craft-guard"

for file in VERSION SKILL.md references/design-principles.md references/evidence-protocol.md templates/AUDIT_REPORT.md scripts/validate_report.py; do
  if [ ! -f "$source_dir/$file" ]; then
    echo "ERROR: missing source file $file; no local skill has been touched" >&2
    exit 1
  fi
done

version="$(cat "$source_dir/VERSION")"
if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "ERROR: malformed VERSION ($version); no local skill has been touched" >&2
  exit 1
fi

for root in "$HOME/.dsh/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$root"
  dest="$root/ui-craft-guard"
  stage="$(mktemp -d "$root/.ui-craft-guard.stage.XXXXXX")"

  if command -v ditto >/dev/null 2>&1; then
    ditto "$source_dir" "$stage"
  else
    cp -R "$source_dir/." "$stage/"
  fi

  test -f "$stage/SKILL.md"
  test -f "$stage/scripts/validate_report.py"
  test "$(cat "$stage/VERSION")" = "$version"

  backup=""
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    backup="$dest.backup-$(date +%Y%m%d-%H%M%S)-$$"
    if [ -e "$backup" ]; then
      echo "ERROR: backup path already exists: $backup" >&2
      exit 1
    fi
    mv "$dest" "$backup"
    echo "Backup: $backup"
  fi

  if ! mv "$stage" "$dest"; then
    echo "ERROR: install failed at $dest" >&2
    if [ -n "$backup" ] && [ -e "$backup" ]; then
      mv "$backup" "$dest"
      echo "Restored: $dest" >&2
    fi
    exit 1
  fi
  echo "PASS v$version: $dest"
done

echo "All three user-level Skill directories updated. Restart clients to reload."
