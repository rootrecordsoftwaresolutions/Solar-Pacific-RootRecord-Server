#!/usr/bin/env python3
"""Run completed RootRecord condensation periods automatically (per-layer db files)."""
from __future__ import annotations
import argparse, sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect, connect_layer, initialize_schema, DEFAULT_DB_PATH
from energy.db.aggregate import aggregate_period, period_bounds, LAYERS


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path)
    p.add_argument("--at", help="UTC ISO timestamp; defaults to now")
    p.add_argument("--layers", nargs="+", choices=LAYERS, default=list(LAYERS))
    args = p.parse_args()
    now = datetime.fromisoformat(args.at.replace("Z", "+00:00")) if args.at else datetime.now(timezone.utc)
    raw_path = args.db or DEFAULT_DB_PATH

    raw_conn = connect(raw_path)
    initialize_schema(raw_conn)
    raw_conn.close()

    total = 0
    for layer in args.layers:
        start, end = period_bounds(layer, now)
        if end > now:
            continue
        conn = connect_layer(layer, raw_path)
        try:
            total += aggregate_period(conn, layer, start, end, "raw")
        finally:
            conn.close()
    print(f"CONDENSATION_COMPLETE layers={len(args.layers)} rows={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
