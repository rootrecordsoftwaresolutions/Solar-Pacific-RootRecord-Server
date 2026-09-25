#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-read.sh - live read forwarder
# -----------------------------------------------------------------------------
# WHAT: Forward to scripts/read/river2pro-read.sh -> SQLite + JSON.
# =============================================================================
set -euo pipefail
exec "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh"
