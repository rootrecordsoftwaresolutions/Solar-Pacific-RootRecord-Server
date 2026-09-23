#!/usr/bin/env bash
set -euo pipefail
systemctl --user stop ava-ecoflow-ble.service || true
# clear stale pid if any
PIDF=/home/rootrecord/.ollama/skills/state/store/ava-ecoflow-ble.pid
if [[ -f "$PIDF" ]]; then
  pid=$(cat "$PIDF" || true)
  if [[ -n "${pid:-}" ]] && ! kill -0 "$pid" 2>/dev/null; then rm -f "$PIDF"; fi
fi
echo "stopped (or was inactive)"
