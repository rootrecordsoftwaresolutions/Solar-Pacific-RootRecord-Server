#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-xboost-on.sh - River2Pro X-Boost ON
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_xboost" --want "on" --label "River2Pro X-Boost ON"
