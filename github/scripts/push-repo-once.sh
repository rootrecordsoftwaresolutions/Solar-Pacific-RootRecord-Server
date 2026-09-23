#!/usr/bin/env bash
# One sync cycle for a single repo id from repos.conf
set -uo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
ID="${1:-}"
[[ -n "$ID" ]] || { echo "Usage: $0 <repo-id>"; exit 2; }

LOG="$BAK_ROOT/logs/${ID}-push.log"
log() { echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] [$ID] $*" | tee -a "$LOG"; }

line="$(grep -v '^#' "$REPOS_CONF" | awk -F'\t' -v id="$ID" '$1==id {print; exit}')"
[[ -n "$line" ]] || { log "ERROR: unknown id $ID"; exit 1; }
IFS=$'\t' read -r id enabled mode local_path slug remote_name <<<"$line"
[[ "$enabled" == "1" ]] || { log "disabled — skip"; exit 0; }

if [[ "$mode" == "inplace" ]]; then
  REPO_DIR="$local_path"
else
  REPO_DIR="$BAK_ROOT/worktrees/$id"
  if [[ ! -d "$REPO_DIR/.git" ]]; then
    log "ERROR: worktree missing — run setup-all-remotes.sh first"
    exit 1
  fi
  if [[ ! -d "$local_path" ]]; then
    log "ERROR: local source missing: $local_path"
    exit 1
  fi
  # Mirror desk → worktree (no node_modules / .next / .git)
  rsync -a --delete \
    --exclude '.git/' \
    --exclude 'node_modules/' \
    --exclude '.next/' \
    --exclude '*.log' \
    "$local_path"/ "$REPO_DIR"/
fi

cd "$REPO_DIR" || { log "ERROR: cd $REPO_DIR"; exit 1; }
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  log "ERROR: not a git repo"
  exit 1
fi

CHANGED="$(git status --porcelain)"
if [[ -z "$CHANGED" ]]; then
  log "— no changes"
  exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
SKIPPED=()
STAGE_PATHS=()
while IFS= read -r row; do
  path="${row:3}"
  path="${path%\"}"; path="${path#\"}"
  [[ -z "$path" ]] && continue
  [[ ! -e "$path" ]] && continue
  size_bytes=$(stat -c%s -- "$path" 2>/dev/null || echo 0)
  size_mb=$(( size_bytes / 1024 / 1024 ))
  if (( size_mb > MAX_FILE_MB )); then
    SKIPPED+=("$path (${size_mb}MB)")
  else
    STAGE_PATHS+=("$path")
  fi
done <<< "$CHANGED"

if (( ${#SKIPPED[@]} > 0 )); then
  log "SKIPPED over ${MAX_FILE_MB}MB:"
  for s in "${SKIPPED[@]}"; do log "  - $s"; done
fi
if (( ${#STAGE_PATHS[@]} == 0 )); then
  log "nothing to commit after size guard"
  exit 0
fi

git add -A -- "${STAGE_PATHS[@]}" 2>>"$LOG" || true
if git diff --cached --quiet; then
  log "nothing staged"
  exit 0
fi

MSG="Auto-sync: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
if ! git -c user.email='bruce@rootrecord.local' -c user.name='Bruce Monitor' commit -m "$MSG" >>"$LOG" 2>&1; then
  # maybe identity already set
  git commit -m "$MSG" >>"$LOG" 2>&1 || { log "ERROR: commit failed"; exit 1; }
fi

if git push "$remote_name" "HEAD:$BRANCH" >>"$LOG" 2>&1; then
  log "↑ ${#STAGE_PATHS[@]} files"
  exit 0
fi
log "✗ push failed"
exit 1
