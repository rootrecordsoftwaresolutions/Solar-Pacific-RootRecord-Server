"""RootRecord telemetry condensation engine.

Builds persisted aggregate measurements from the canonical observation layer.
It is restart-safe and never treats missing samples as zero.
"""
from __future__ import annotations
import math
import sqlite3
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

LAYERS=("1sec","1min","5min","15min","1hour","day","7days","month","year")
SECONDS={"1sec":1,"1min":60,"5min":300,"15min":900,"1hour":3600,"day":86400,"7days":604800}
LOCAL=ZoneInfo("Pacific/Honolulu")

def _dt(s): return datetime.fromisoformat(s.replace("Z","+00:00"))
def _iso(d): return d.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")

def period_bounds(layer, at):
    d=at.astimezone(LOCAL)
    if layer=="1sec": start=d.replace(microsecond=0)
    elif layer=="1min": start=d.replace(second=0,microsecond=0)
    elif layer=="5min": start=d.replace(minute=(d.minute//5)*5,second=0,microsecond=0)
    elif layer=="15min": start=d.replace(minute=(d.minute//15)*15,second=0,microsecond=0)
    elif layer=="1hour": start=d.replace(minute=0,second=0,microsecond=0)
    elif layer=="day": start=d.replace(hour=0,minute=0,second=0,microsecond=0)
    elif layer=="7days":
        day=d.date()-timedelta(days=d.weekday())
        start=datetime.combine(day,datetime.min.time(),LOCAL)
    elif layer=="month": start=d.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    elif layer=="year": start=d.replace(month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
    else: raise ValueError(layer)
    if layer=="1sec": end=start+timedelta(seconds=1)
    elif layer in SECONDS: end=start+timedelta(seconds=SECONDS[layer])
    elif layer=="month":
        y=start.year+(start.month==12); m=1 if start.month==12 else start.month+1
        end=start.replace(year=y,month=m)
    elif layer=="year": end=start.replace(year=start.year+1)
    return start,end

def _stats(rows, power=False):
    vals=[r[0] for r in rows if r[0] is not None]
    if not vals: return dict(sample_count=len(rows),valid_sample_count=0,coverage_pct=0,
                             value_avg=None,value_min=None,value_max=None,value_sum=None,
                             value_delta=None,energy_wh=None,state="missing")
    avg=sum(vals)/len(vals)
    energy=None
    if power:
        energy=0.0
        for (v,t),(nv,nt) in zip(rows,rows[1:]):
            if v is not None and nv is not None:
                dt=max(0,(_dt(nt)-_dt(t)).total_seconds())
                energy += ((v+nv)/2)*dt/3600
    return dict(sample_count=len(rows),valid_sample_count=len(vals),coverage_pct=None,
                value_avg=avg,value_min=min(vals),value_max=max(vals),value_sum=sum(vals),
                value_delta=vals[-1]-vals[0],energy_wh=energy,state="measured")

def _coverage(rows,start,end):
    if not rows: return 0.0
    span=(end-start).total_seconds()
    if span<=0:return 0.0
    if len(rows)==1:return min(100.0,100.0/span)
    intervals=[]
    for a,b in zip(rows,rows[1:]):
        if a[0] is not None and b[0] is not None:
            intervals.append(max(0,(_dt(b[1])-_dt(a[1])).total_seconds()))
    return min(100.0,100*sum(intervals)/span)

def aggregate_period(conn, layer, start, end, source_layer=None):
    if layer not in LAYERS: raise ValueError(layer)
    now=_iso(datetime.now(timezone.utc))
    cur=conn.execute("""INSERT INTO aggregation_run(layer,period_start,period_end,source_layer,status,started_at)
                        VALUES(?,?,?,?, 'running',?) ON CONFLICT(layer,period_start,period_end)
                        DO UPDATE SET status='running',started_at=excluded.started_at,source_layer=excluded.source_layer""",
                     (layer,_iso(start),_iso(end),source_layer,now))
    run=conn.execute("SELECT aggregation_run_id FROM aggregation_run WHERE layer=? AND period_start=? AND period_end=?",(layer,_iso(start),_iso(end))).fetchone()[0]
    conn.execute("DELETE FROM aggregate_measurement WHERE aggregation_run_id=?",(run,))
    rows=conn.execute("""SELECT dm.metric_key, dm.value_num, o.observed_at, dm.state, dm.unit
                         FROM device_measurement dm JOIN observation o ON o.observation_id=dm.observation_id
                         WHERE o.observed_at>=? AND o.observed_at<?
                         ORDER BY dm.metric_key,o.observed_at""",(_iso(start),_iso(end))).fetchall()
    grouped={}
    for r in rows:
        grouped.setdefault(("device",r[0],r[0]),[]).append((r[1],r[2]))

    brows=conn.execute("""SELECT b.battery_id,bm.metric_key,bm.value_num,o.observed_at
                          FROM battery_measurement bm JOIN battery b ON b.battery_id=bm.battery_id
                          JOIN observation o ON o.observation_id=bm.observation_id
                          WHERE o.observed_at>=? AND o.observed_at<? AND bm.state IN ('measured','defaulted')
                          ORDER BY b.battery_id,bm.metric_key,o.observed_at""",(_iso(start),_iso(end))).fetchall()
    for r in brows: grouped.setdefault(("battery",r[0],r[1]),[]).append((r[2],r[3]))
    erows=conn.execute("""SELECT em.channel,em.metric_key,em.value_num,o.observed_at
                          FROM electrical_measurement em JOIN observation o ON o.observation_id=em.observation_id
                          WHERE o.observed_at>=? AND o.observed_at<? AND em.state IN ('measured','defaulted')
                          ORDER BY em.channel,em.metric_key,o.observed_at""",(_iso(start),_iso(end))).fetchall()
    # electrical subjects are device-scoped; channel is part of metric identity
    for r in erows: grouped.setdefault(("device",0,f"electrical:{r[0]}:{r[1]}"),[]).append((r[2],r[3]))
    count=0
    for (stype,sid,metric), vals in grouped.items():
        power=metric.endswith(":power_w") or metric in ("input_power","output_power")
        s=_stats(vals,power)
        s["coverage_pct"]=_coverage(vals,start,end)
        conn.execute("""INSERT INTO aggregate_measurement(
          aggregation_run_id,subject_type,subject_id,metric_key,unit,sample_count,valid_sample_count,
          coverage_pct,value_avg,value_min,value_max,value_sum,value_delta,energy_wh,state)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
          (run,stype,sid,metric,None,s["sample_count"],s["valid_sample_count"],s["coverage_pct"],
           s["value_avg"],s["value_min"],s["value_max"],s["value_sum"],s["value_delta"],s["energy_wh"],s["state"]))
        count+=1
    conn.execute("""UPDATE aggregation_run SET status='complete',completed_at=?,row_count=? WHERE aggregation_run_id=?""",(now,count,run))
    conn.commit()
    return count

def aggregate_at(conn, layer, at, source_layer=None):
    start,end=period_bounds(layer,at)
    return aggregate_period(conn,layer,start,end,source_layer)
