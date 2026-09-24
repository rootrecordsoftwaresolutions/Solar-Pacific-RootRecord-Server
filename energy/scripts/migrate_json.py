#!/usr/bin/env python3
"""Additive migration of legacy Energy JSON samples into RootRecord SQLite."""
from __future__ import annotations
import argparse,json,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect,initialize_schema,upsert_device,create_observation,add_device_measurement

TIME_KEYS=("timestamp","ts","time","at")

def iso(value):
    if isinstance(value,(int,float)):
        return datetime.fromtimestamp(value,timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")
    return datetime.fromisoformat(str(value).replace("Z","+00:00")).astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")

def files_for(source):
    return sorted(source.rglob("*.json")) if source.is_dir() else [source]

def unpack(obj):
    if isinstance(obj,list): return [(x,{}) for x in obj if isinstance(x,dict)]
    if not isinstance(obj,dict): return []
    if any(k in obj for k in TIME_KEYS):
        fields=obj.get("fields")
        if isinstance(fields,dict): return [(obj,fields)]
        return [(obj,{k:v for k,v in obj.items() if k not in TIME_KEYS})]
    for key in ("samples","records","data","readings","telemetry"):
        if isinstance(obj.get(key),list):
            return unpack(obj[key])
    return []

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--serial",required=True)
    p.add_argument("--model",required=True)
    p.add_argument("--alias")
    p.add_argument("--db",type=Path)
    args=p.parse_args()
    conn=connect(args.db) if args.db else connect()
    initialize_schema(conn)
    now=datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")
    device=upsert_device(conn,serial_number=args.serial,model=args.model,alias=args.alias,role="primary_power_storage",observed_at=now)
    imported=0; skipped=0
    for path in files_for(args.source):
        source_name=str(path.resolve())
        row=conn.execute("SELECT source_id FROM observation_source WHERE source_type='legacy_json' AND source_name=?",(source_name,)).fetchone()
        if row: source_id=row[0]
        else:
            source_id=conn.execute("""INSERT INTO observation_source(source_type,source_name,parser_name,parser_version,created_at)
                                     VALUES('legacy_json',?,?,?,?)""",(source_name,"legacy_json_importer","2",now)).lastrowid
        try: obj=json.loads(path.read_text(encoding="utf-8"))
        except (OSError,ValueError): skipped+=1; continue
        for envelope,fields in unpack(obj):
            stamp=next((envelope.get(k) for k in TIME_KEYS if envelope.get(k) is not None),None)
            if stamp is None: skipped+=1; continue
            observed=iso(stamp)
            obs=create_observation(conn,device,observed,source_id,quality="legacy")
            for key,value in fields.items():
                if isinstance(value,(dict,list)): continue
                add_device_measurement(conn,observation_id=obs,metric_key=key,value=value,state="missing" if value is None else "measured")
            imported+=1
    conn.commit(); conn.close()
    print(f"IMPORTED={imported} SKIPPED={skipped}")
    return 0
if __name__=="__main__": raise SystemExit(main())
