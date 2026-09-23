#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG=/home/rootrecord/Database/GITHUB/logs/council-relay.log
mkdir -p "$(dirname "$LOG")"
if pgrep -f 'council-relay.py' >/dev/null; then
  echo "[ok] council-relay already running"
  exit 0
fi
if pgrep -f 'apps.council' >/dev/null; then
  echo "[warn] legacy apps.council running — not starting relay (409 risk)"
  exit 0
fi
nohup python3 "$HERE/council-relay.py" >>"$LOG" 2>&1 &
echo "[ok] council-relay started pid=$! → $LOG"
