#!/usr/bin/env bash
# One check-stage-commit-push cycle. Safe to run by hand or from the loop.
set -uo pipefail

REPO_DIR="/home/rootrecord/.ollama/skills"
LOG_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/poll-and-push.log"
MAX_FILE_MB=90

log() {
  echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] $*" | tee -a "$LOG_FILE"
}

cd "$REPO_DIR" || { log "ERROR: cannot cd to $REPO_DIR"; exit 1; }

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  log "ERROR: $REPO_DIR is not a git repository"
  exit 1
fi

CHANGED="$(git status --porcelain)"
if [[ -z "$CHANGED" ]]; then
  log "no changes"
  exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# --- size guard: never stage anything over MAX_FILE_MB ---
SKIPPED=()
STAGE_PATHS=()
while IFS= read -r line; do
  # porcelain format: XY path  (path may be quoted if it has spaces)
  path="${line:3}"
  path="${path%\"}"
  path="${path#\"}"
  [[ -z "$path" ]] && continue
  [[ ! -e "$path" ]] && continue   # deleted files: nothing to size-check
  size_bytes=$(stat -c%s -- "$path" 2>/dev/null || echo 0)
  size_mb=$(( size_bytes / 1024 / 1024 ))
  if (( size_mb > MAX_FILE_MB )); then
    SKIPPED+=("$path (${size_mb}MB)")
  else
    STAGE_PATHS+=("$path")
  fi
done <<< "$CHANGED"

if (( ${#SKIPPED[@]} > 0 )); then
  log "SKIPPED (over ${MAX_FILE_MB}MB, not staged):"
  for s in "${SKIPPED[@]}"; do
    log "  - $s"
  done
fi

if (( ${#STAGE_PATHS[@]} == 0 )); then
  log "everything changed was oversized; nothing to commit this cycle"
  exit 0
fi

git add -A -- "${STAGE_PATHS[@]}" 2>>"$LOG_FILE"

if git diff --cached --quiet; then
  log "nothing actually staged after size guard; skipping commit"
  exit 0
fi

COMMIT_MSG="Auto-sync: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
git commit -m "$COMMIT_MSG" >>"$LOG_FILE" 2>&1

if git push backup "HEAD:$BRANCH" >>"$LOG_FILE" 2>&1; then
  log "pushed $BRANCH ($(( ${#STAGE_PATHS[@]} )) file(s) changed)"
else
  log "ERROR: push to backup/$BRANCH failed — see log above"
  exit 1
fi
