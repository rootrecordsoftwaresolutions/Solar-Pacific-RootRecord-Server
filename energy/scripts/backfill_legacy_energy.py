#!/usr/bin/env python3
"""Backfill both configured EcoFlow devices from legacy read samples."""
from __future__ import annotations
import argparse,configparser,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.scripts.migrate_json import main as migrate_main

# This wrapper intentionally remains an operator-facing entry point. It does
# not delete legacy files and requires explicit source/device arguments.
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source",type=Path,required=True,help="ENERGY/samples directory")
    p.add_argument("--config",type=Path,default=Path("/home/rootrecord/.ollama/skills/energy/config/devices.conf"))
    p.add_argument("--alias",required=True,choices=("delta2","river2pro"))
    p.add_argument("--db",type=Path)
    args=p.parse_args()
    cfg=configparser.ConfigParser()
    cfg.read(args.config)
    section=cfg[args.alias]
    argv=["migrate_json.py","--source",str(args.source), "--serial",section["sn"],
          "--model",section["model"],"--alias",section["alias"]]
    if args.db: argv += ["--db",str(args.db)]
    # Filter the source tree to the selected device's read samples.
    source=args.source
    if source.is_dir():
        files=sorted(source.glob(f"read-{args.alias}-*.json"))
        if not files:
            print(f"NO_FILES alias={args.alias}")
            return 0
        import tempfile
        with tempfile.TemporaryDirectory(prefix="rootrecord-migrate-") as td:
            staging=Path(td)
            for src in files:
                (staging/src.name).write_bytes(src.read_bytes())
            old=sys.argv
            try:
                sys.argv=argv[:-2]+[str(staging),"--serial",section["sn"],"--model",section["model"],"--alias",section["alias"]]
                if args.db: sys.argv += ["--db",str(args.db)]
                return migrate_main()
            finally: sys.argv=old
    sys.argv=argv
    return migrate_main()
if __name__=="__main__": raise SystemExit(main())
