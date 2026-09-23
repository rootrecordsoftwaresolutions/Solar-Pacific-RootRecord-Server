#!/usr/bin/env bash
# Delta2 DC 12V OFF
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_dc_12v_port" \
  --want "off" \
  --label "Delta2 DC 12V OFF"
