#!/usr/bin/env bash
# Delta2 AC OFF
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_ac_ports" \
  --want "off" \
  --label "Delta2 AC OFF"
