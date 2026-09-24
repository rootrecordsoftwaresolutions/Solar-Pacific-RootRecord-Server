#!/usr/bin/env python3
"""Import legacy RootRecord JSON telemetry into the canonical SQLite store."""
from __future__ import annotations
import argparse,json,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from energy.db.store import connect,initialize_schema,upsert_device,create_observation,add_device_measurement

def iso(value):
    if isinstance(value,(int,float)):
        return datetime.fromtimestamp(value,timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")
    return datetime.fromisoformat(str(value).replace("Z","+00:00")).astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")

def records(obj):
    if isinstance(obj,list): return obj
    if isinstance(obj,dict):
        for k in ("samples","records","data","readings","telemetry"):
            if isinstance(obj.get(k),list): return obj[k]
        if "timestamp" in obj or "ts" in obj or "time" in obj: return [obj]
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
    device=upsert_device(conn,args.serial,args.model,args.alias,now)
    source=conn.execute("SELECT source_id FROM observation_source WHERE source_type='legacy_json' AND source_name=?",(str(args.source),)).fetchone()
    if source: source_id=source[0]
    else:
        source_id=conn.execute("""INSERT INTO observation_source(source_type,source_name,parser_name,parser_version,created_at)
                                  VALUES('legacy_json',?,?,?,?)""",(str(args.source),"legacy_json_importer","1",now)).lastrowid
    data=json.loads(args.source.read_text())
    imported=0
    for r in records(data):
        if not isinstance(r,dict): continue
        stamp=r.get("timestamp",r.get("ts",r.get("time")))
        if stamp is None: continue
        observed=iso(stamp)
        obs=create_observation(conn,device,observed,source_id,quality="legacy")
        for key,value in r.items():
            if key in ("timestamp","ts","time") or isinstance(value,(dict,list)): continue
            if isinstance(value,bool): add_device_measurement(conn,obs,key,value_bool=int(value),state="measured")
            elif isinstance(value,(int,float)): add_device_measurement(conn,obs,key,value_num=float(value),state="measured")
            elif value is None: add_device_measurement(conn,obs,key,state="missing")
            else: add_device_measurement(conn,obs,key,value_text=str(value),state="measured")
        imported+=1
    conn.commit(); conn.close()
    print(f"IMPORTED={imported}")
    return 0
if __name__=="__main__": raise SystemExit(main())
