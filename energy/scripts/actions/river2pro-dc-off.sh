#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-dc-off.sh - River2Pro DC 12V OFF
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_dc_12v_port" --want "off" --label "River2Pro DC 12V OFF"
