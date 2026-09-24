#!/usr/bin/env bash
# ============================================================================
# reports/scripts/worklog_once.sh — one worklog scan cycle
# ----------------------------------------------------------------------------
# WHAT: Full-home file/folder scan into Database/WORKLOG (offline-friendly).
# HOW:  sources worklog_lib.sh then scan_once
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=/dev/null
source "$DIR/worklog_lib.sh"
scan_once
echo "OK wrote/updated $CURRENT"
