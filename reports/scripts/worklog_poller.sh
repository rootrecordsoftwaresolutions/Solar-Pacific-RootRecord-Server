#!/usr/bin/env bash
# Runs until killed. Logging is active only while this process lives.
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=/dev/null
source "$DIR/worklog_lib.sh"
ensure_dirs
if [[ -f "$PID_FILE" ]]; then
  old=$(cat "$PID_FILE" || true)
  if [[ -n "${old:-}" ]] && kill -0 "$old" 2>/dev/null; then
    echo "Already running pid=$old" >&2
    exit 1
  fi
fi
echo $$ > "$PID_FILE"
trap 'rm -f "$PID_FILE"; exit 0' INT TERM EXIT
echo "worklog poller start pid=$$ (scan every 60s)"
while true; do
  scan_once || true
  sleep 60
done
