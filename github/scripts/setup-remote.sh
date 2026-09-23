#!/usr/bin/env bash
# Compat: skills remote only. Prefer setup-all-remotes.sh.
set -euo pipefail
SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPTS/common.sh"
ensure_bak_root
ROOT="/home/rootrecord/.ollama/skills"
SLUG="rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server"
URL="git@github.com:${SLUG}.git"
cd "$ROOT"
if git remote get-url backup >/dev/null 2>&1; then
  git remote set-url backup "$URL"
  echo "Updated existing 'backup' remote → SSH."
else
  git remote add backup "$URL"
  echo "Added new 'backup' remote → SSH."
fi
# Also scrub origin if it still embeds a token
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$URL"
  echo "Origin scrubbed → SSH."
fi
echo "Done. No PAT in remote URLs."
