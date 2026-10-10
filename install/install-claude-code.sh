#!/usr/bin/env bash
# Installs all SEO skills for Claude Code (macOS / Linux).
# Usage: open a terminal in this folder and run:  bash install-claude-code.sh
# Project-only install instead:                  bash install-claude-code.sh /path/to/your/project
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../3-coding-agents/skills"
[ -d "$SRC" ] || SRC="$HERE/../skills"
if [ -n "$1" ]; then DEST="$1/.claude/skills"; else DEST="$HOME/.claude/skills"; fi
mkdir -p "$DEST"
count=0
for d in "$SRC"/*/; do
  name="$(basename "$d")"
  rm -rf "$DEST/$name"
  cp -R "$d" "$DEST/$name"
  echo "  ✔ $name"
  count=$((count+1))
done
echo ""
echo "Done: $count skills installed in $DEST"
echo "সম্পন্ন: $count টি skill ইনস্টল হয়েছে → $DEST"
echo "Restart Claude Code, then try:  I just started a website. How do I get it on Google?"
