#!/usr/bin/env bash
# River2Pro AC always-on OFF
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/action_runner.py" \
  --device "river2pro" \
  --method "enable_ac_always_on" \
  --want "off" \
  --label "River2Pro AC always-on OFF"
