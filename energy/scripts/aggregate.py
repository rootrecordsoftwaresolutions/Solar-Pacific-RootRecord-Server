#!/usr/bin/env python3
"""Explicit RootRecord condensation runner."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect, initialize_schema
from energy.db.aggregate import aggregate_at, LAYERS

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--layer",choices=LAYERS,required=True)
    p.add_argument("--at",help="UTC ISO timestamp; defaults to now")
    args=p.parse_args()
    at=datetime.fromisoformat(args.at.replace("Z","+00:00")) if args.at else datetime.now(timezone.utc)
    conn=connect()
    try:
        initialize_schema(conn)
        n=aggregate_at(conn,args.layer,at)
    finally: conn.close()
    print(f"AGGREGATED layer={args.layer} rows={n}")
    return 0
if __name__=="__main__": raise SystemExit(main())
