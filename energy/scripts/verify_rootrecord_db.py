#!/usr/bin/env python3
"""Verify RootRecord SQLite integrity and aggregation readiness."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect,initialize_schema

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--db",type=Path)
    args=p.parse_args()
    c=connect(args.db) if args.db else connect()
    initialize_schema(c)
    checks=[]
    for table in ("device","battery","device_port","observation","device_measurement","battery_measurement","electrical_measurement","port_measurement","aggregation_run","aggregate_measurement"):
        n=c.execute("SELECT COUNT(*) FROM "+table).fetchone()[0]
        checks.append((table,n))
    fk=c.execute("PRAGMA foreign_key_check").fetchall()
    dup=c.execute("""SELECT device_id,observed_at,source_id,source_sequence,COUNT(*) n
                     FROM observation GROUP BY 1,2,3,4 HAVING n>1""").fetchall()
    bad=c.execute("""SELECT COUNT(*) FROM device_measurement
                     WHERE (state IN ('missing','not_applicable') AND (value_num IS NOT NULL OR value_text IS NOT NULL OR value_bool IS NOT NULL))
                        OR (state IN ('measured','defaulted') AND
                            ((value_num IS NOT NULL)+(value_text IS NOT NULL)+(value_bool IS NOT NULL))<>1)""").fetchone()[0]
    c.close()
    print("ROOTRECORD_DB_VERIFY")
    for t,n in checks: print(f"{t}={n}")
    print(f"foreign_key_errors={len(fk)}")
    print(f"duplicate_observations={len(dup)}")
    print(f"invalid_device_measurements={bad}")
    ok=not fk and not dup and bad==0
    print("STATUS="+("OK" if ok else "FAILED"))
    return 0 if ok else 1
if __name__=="__main__": raise SystemExit(main())
