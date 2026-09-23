#!/usr/bin/env bash
# River2Pro DC 12V ON (car/drives)
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/action_runner.py" \
  --device "river2pro" \
  --method "enable_dc_12v_port" \
  --want "on" \
  --label "River2Pro DC 12V ON (car/drives)"
