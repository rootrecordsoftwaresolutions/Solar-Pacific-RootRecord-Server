#!/usr/bin/env python3
"""Explicit RootRecord condensation runner (writes to the layer's own db file)."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect, connect_layer, initialize_schema, DEFAULT_DB_PATH
from energy.db.aggregate import aggregate_at, LAYERS


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--layer", choices=LAYERS, required=True)
    p.add_argument("--at", help="UTC ISO timestamp; defaults to now")
    p.add_argument("--db", type=Path, help="raw telemetry db (default: canonical rootrecord.db)")
    args = p.parse_args()
    at = datetime.fromisoformat(args.at.replace("Z", "+00:00")) if args.at else datetime.now(timezone.utc)
    raw_path = args.db or DEFAULT_DB_PATH

    raw_conn = connect(raw_path)
    initialize_schema(raw_conn)
    raw_conn.close()

    conn = connect_layer(args.layer, raw_path)
    try:
        n = aggregate_at(conn, args.layer, at)
    finally:
        conn.close()
    print(f"AGGREGATED layer={args.layer} rows={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
