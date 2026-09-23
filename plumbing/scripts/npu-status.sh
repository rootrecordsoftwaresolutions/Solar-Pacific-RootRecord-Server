#!/usr/bin/env bash
set -euo pipefail
echo "=== accel ==="
ls -la /dev/accel 2>&1 || echo "No data"
echo "=== xrt/npu packages ==="
dpkg -l 2>/dev/null | grep -iE '^ii\s+(libxrt|libze1|linux-firmware-amd-misc|python3-xrt)' || echo "No data"
echo "=== single-flight ==="
bash "$(dirname "$0")/single-flight.sh" status
