#!/usr/bin/env bash
# ==============================================================================
# bak-new.sh  — dated folder under /home/rootrecord/Database/GITHUB/
# Usage: bak-new.sh <label>   →  prints path created
# ==============================================================================
set -euo pipefail
# shellcheck disable=SC1091
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
ensure_bak_root
label="${1:-bak}"
safe=$(echo "$label" | tr -c 'A-Za-z0-9._-' '_')
dest="$BAK_ROOT/${safe}.bak-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$dest"
echo "$dest"
