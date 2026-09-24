"""Small runtime hook for completing closed condensation periods."""
from __future__ import annotations
from datetime import datetime,timezone
from energy.db.store import connect,initialize_schema
from energy.db.aggregate import aggregate_period,period_bounds,LAYERS

def condense_closed_periods(db_path=None):
    now=datetime.now(timezone.utc)
    conn=connect(db_path) if db_path else connect()
    initialize_schema(conn)
    total=0
    try:
        for layer in LAYERS:
            start,end=period_bounds(layer,now)
            if end<=now:
                total+=aggregate_period(conn,layer,start,end,"raw")
        return total
    finally:
        conn.close()
