"""Runtime condensation of newly closed telemetry periods."""
from __future__ import annotations
from datetime import datetime, timezone
from energy.db.store import connect, initialize_schema
from energy.db.aggregate import aggregate_period, period_bounds, LAYERS, _iso

def condense_closed_periods(db_path=None):
    conn=connect(db_path) if db_path else connect()
    initialize_schema(conn)
    total=0
    try:
        row=conn.execute("SELECT MAX(observed_at) FROM observation").fetchone()
        if not row or not row[0]:
            return 0
        latest=datetime.fromisoformat(row[0].replace("Z","+00:00"))
        for layer in LAYERS:
            start,end=period_bounds(layer,latest)
            if end>latest:
                continue
            key=(_iso(start),_iso(end))
            done=conn.execute(
                "SELECT status FROM aggregation_run WHERE layer=? AND period_start=? AND period_end=?",
                (layer,*key)).fetchone()
            if done and done[0]=="complete":
                continue
            total += aggregate_period(conn,layer,start,end,"raw")
        return total
    finally:
        conn.close()
