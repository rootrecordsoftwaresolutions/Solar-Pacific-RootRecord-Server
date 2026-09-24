#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-ac-on.sh - River2Pro AC ON
# -----------------------------------------------------------------------------
# WHAT: Atomic BLE toggle on river2pro: method=enable_ac_ports want=on.
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_ac_ports" --want "on" --label "River2Pro AC ON"
