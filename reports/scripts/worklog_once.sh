#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=/dev/null
source "$DIR/worklog_lib.sh"
scan_once
echo "OK wrote/updated $CURRENT"
