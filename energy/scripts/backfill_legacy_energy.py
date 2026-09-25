#!/usr/bin/env python3
"""Backfill configured EcoFlow devices from legacy read samples."""
from __future__ import annotations
import argparse,configparser,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.scripts.migrate_json import migrate

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--config",type=Path,default=Path("/home/rootrecord/.ollama/skills/energy/config/devices.conf"))
    p.add_argument("--alias",required=True,choices=("delta2","river2pro"))
    p.add_argument("--db",type=Path)
    args=p.parse_args()
    cfg=configparser.ConfigParser(); cfg.read(args.config)
    section=cfg[args.alias]
    files=sorted(args.source.glob(f"read-{args.alias}-*.json")) if args.source.is_dir() else [args.source]
    if not files:
        print(f"NO_FILES alias={args.alias}"); return 0
    total=0
    for path in files:
        total += migrate(path,section["sn"],section["model"],section["alias"],args.db)
    print(f"BACKFILL_COMPLETE alias={args.alias} files={len(files)} observations={total}")
    return 0

if __name__=="__main__": raise SystemExit(main())
