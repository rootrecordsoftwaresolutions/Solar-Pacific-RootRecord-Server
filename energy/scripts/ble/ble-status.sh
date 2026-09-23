#!/usr/bin/env bash
set -euo pipefail
LOG=/home/rootrecord/.ollama/skills/logs/store/ava-ecoflow-ble.log
echo "=== systemctl --user ava-ecoflow-ble.service ==="
systemctl --user is-enabled ava-ecoflow-ble.service 2>&1 || true
systemctl --user is-active ava-ecoflow-ble.service 2>&1 || true
systemctl --user --no-pager --full status ava-ecoflow-ble.service 2>&1 | head -25 || true
echo "=== last log lines ($LOG) ==="
if [[ -f "$LOG" ]]; then tail -n 15 "$LOG"; else echo "WAITING — no BLE log yet"; fi
