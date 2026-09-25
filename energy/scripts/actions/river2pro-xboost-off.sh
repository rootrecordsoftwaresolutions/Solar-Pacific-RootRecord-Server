#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-xboost-off.sh - River2Pro X-Boost OFF
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_xboost" --want "off" --label "River2Pro X-Boost OFF"
