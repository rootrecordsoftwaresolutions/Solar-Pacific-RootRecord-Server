#!/usr/bin/env bash
# ==============================================================================
# sync-all.sh  — iterate enabled repos.conf → push-repo-once.sh
# Called by automations jobs.py  github_sync_all  (every 300s)
# ==============================================================================
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$HERE/common.sh"
ensure_bak_root

while IFS=$'\t' read -r id enabled mode local_path slug remote_name; do
  [[ "$id" =~ ^#.*$ || -z "${id:-}" ]] && continue
  [[ "$enabled" == "1" ]] || continue
  bash "$HERE/push-repo-once.sh" "$id" || echo "✗ [$id] sync failed (continuing)"
done < <(grep -v '^#' "$REPOS_CONF" | grep -v '^[[:space:]]*$')
