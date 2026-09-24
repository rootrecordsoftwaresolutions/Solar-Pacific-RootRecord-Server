#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/delta2-read.sh - live read forwarder
# -----------------------------------------------------------------------------
# WHAT: Forward to scripts/read/delta2-read.sh -> SQLite + JSON.
# =============================================================================
set -euo pipefail
exec "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh"
