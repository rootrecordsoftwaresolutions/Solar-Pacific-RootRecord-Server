#!/usr/bin/env bash
# ==============================================================================
# sync-all.sh  — iterate enabled repos.conf → push-repo-once.sh
# Called by automations jobs.py  github_sync_all  (every 300s)
#
# After a successful pull/merge of skills code from GitHub, schedules a full
# poller stack reload (stop every operated process, then start clean).
# ==============================================================================
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$HERE/common.sh"
ensure_bak_root
mkdir -p "$BAK_ROOT/flags"

RELOAD_SCRIPT="/home/rootrecord/.ollama/skills/automations/scripts/schedule-stack-reload.sh"

while IFS=$'\t' read -r id enabled mode local_path slug remote_name; do
  [[ "$id" =~ ^#.*$ || -z "${id:-}" ]] && continue
  [[ "$enabled" == "1" ]] || continue
  # A remote update can arrive between fetch/merge and push. Retry the entire
  # sync cycle immediately so remote changes are not left waiting for the next
  # five-minute poll.
  success=0
  for attempt in 1 2 3; do
    if bash "$HERE/push-repo-once.sh" "$id"; then
      success=1
      break
    fi
    echo "↻ [$id] sync retry $attempt/3"
    sleep 2
  done
  (( success )) || echo "✗ [$id] sync failed after 3 attempts (continuing)"
done < <(grep -v '^#' "$REPOS_CONF" | grep -v '^[[:space:]]*$')

# If skills code was pulled, arm a deferred full stack reload (does not run in
# parallel with this job — waits until sync-all exits).
if [[ -f "$BAK_ROOT/flags/reload-poller-stack" ]]; then
  if [[ -x "$RELOAD_SCRIPT" ]]; then
    bash "$RELOAD_SCRIPT" || true
  else
    echo "⚠ reload flag set but missing $RELOAD_SCRIPT"
  fi
fi
