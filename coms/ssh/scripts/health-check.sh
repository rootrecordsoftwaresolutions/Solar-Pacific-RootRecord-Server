#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "SSH Globe Relay Health Check"
echo "Directory: $ROOT"

command -v ssh >/dev/null && echo "SSH: OK" || echo "SSH: MISSING"
command -v node >/dev/null && echo "Node: OK" || echo "Node: MISSING"

echo "Health check complete."
