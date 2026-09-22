#!/usr/bin/env bash
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "SSH relay status directory:"
ls -la "$ROOT/logs" "$ROOT/data" 2>/dev/null || true
