#!/usr/bin/env bash
# 1s log check — thin: only reads log mtime/size + last line. No BLE scans.
set -euo pipefail
LOG=/home/rootrecord/.ollama/skills/logs/store/ava-ecoflow-ble.log
INTERVAL="${1:-1}"
echo "watching $LOG every ${INTERVAL}s (Ctrl-C to stop)"
prev=""
while true; do
  ts=$(date -Iseconds)
  if [[ ! -f "$LOG" ]]; then
    echo "$ts WAITING — log missing (owner not started?)"
  else
    sz=$(stat -c%s "$LOG" 2>/dev/null || echo 0)
    last=$(tail -n 1 "$LOG" 2>/dev/null || true)
    if [[ "$last" != "$prev" ]]; then
      echo "$ts size=$sz NEW: $last"
      prev="$last"
    else
      echo "$ts size=$sz ok (no new line)"
    fi
  fi
  sleep "$INTERVAL"
done
