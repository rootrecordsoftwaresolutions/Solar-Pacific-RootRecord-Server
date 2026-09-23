#!/usr/bin/env bash
# Usage: bak-new.sh <tag> [src...]
# Creates /home/rootrecord/Database/GITHUB/<tag>.bak-YYYYMMDD-HHMMSS and copies srcs in.
set -euo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
TAG="${1:-change}"
shift || true
TS=$(date +%Y%m%d-%H%M%S)
DEST="$BAK_ROOT/${TAG}.bak-${TS}"
mkdir -p "$DEST"
if (($# > 0)); then
  cp -a "$@" "$DEST/"
fi
echo "$DEST"
