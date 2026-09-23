#!/usr/bin/env bash
# Start single BLE owner via user systemd (preferred) or foreground fallback.
set -euo pipefail
UNIT=ava-ecoflow-ble.service
systemctl --user daemon-reload
systemctl --user start "$UNIT"
systemctl --user --no-pager --full status "$UNIT" | head -20
