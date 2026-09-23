#!/usr/bin/env bash
# Wire + enable single BLE owner on boot (thin). Safe to re-run.
set -euo pipefail
systemctl --user daemon-reload
systemctl --user enable ava-ecoflow-ble.service
systemctl --user restart ava-ecoflow-ble.service
systemctl --user --no-pager --full status ava-ecoflow-ble.service | head -25
echo "log: /home/rootrecord/.ollama/skills/logs/store/ava-ecoflow-ble.log"
