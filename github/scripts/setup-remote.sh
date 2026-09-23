#!/usr/bin/env bash
# Compat: skills remote only. Prefer setup-all-remotes.sh.
set -euo pipefail
SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPTS/common.sh"
ensure_bak_root
load_token
ROOT="/home/rootrecord/.ollama/skills"
SLUG="rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server"
URL="https://x-access-token:${GITHUB_TOKEN}@github.com/${SLUG}.git"
cd "$ROOT"
if git remote get-url backup >/dev/null 2>&1; then
  git remote set-url backup "$URL"
  echo "Updated existing 'backup' remote."
else
  git remote add backup "$URL"
  echo "Added new 'backup' remote."
fi
echo "Done. 'origin' remote is untouched."
echo "(backup remote URL hidden from output on purpose — it contains the token)"
