#!/usr/bin/env bash
# Read-only NPU presence — never invent utilization %
set -euo pipefail
echo "=== accel ==="
ls -la /dev/accel 2>&1 || echo "No data"
echo "=== xrt packages ==="
dpkg -l 2>/dev/null | grep -iE 'npu|xrt|libze' || echo "No data"
echo "=== single-flight ==="
bash "$(dirname "$0")/single-flight.sh" status
