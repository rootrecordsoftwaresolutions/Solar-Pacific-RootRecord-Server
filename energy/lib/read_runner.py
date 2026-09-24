#!/usr/bin/env python3
"""Read live snapshot and persist connected telemetry to SQLite."""
from __future__ import annotations
import argparse, asyncio, json, sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE)); sys.path.insert(0,str(HERE.parent.parent))
from paths import SAMPLES,SOC,WATTS,ensure_dirs
from ble_client import connect,BleUnavailable,eflib_ready
from energy.db.ingest import persist_eflow_device
HST=ZoneInfo("Pacific/Honolulu")
def _fields(device):
    def g(n,d=None): return getattr(device,n,d)
    solar=g("xt60_input_power")
    if solar is None: solar=g("solar_input_power")
    return {"ac_ports":g("ac_ports"),"usb_ports":g("usb_ports"),"dc_12v_port":g("dc_12v_port"),
            "ac_output_power":g("ac_output_power"),"ac_input_power":g("ac_input_power"),
            "usbc_output_power":g("usbc_output_power"),"usba_output_power":g("usba_output_power"),
            "solar_input_power":solar,"soc":g("battery_level",g("soc"))}
async def _read(alias):
    device=await connect(alias)
    await asyncio.sleep(2.0)
    return device,{"alias":alias,"fields":_fields(device)}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--device",required=True); args=p.parse_args(); ensure_dirs()
    ok,reason=eflib_ready()
    if not ok: print("WAITING"); print(f"No data — {reason}"); return 2
    try: device,snap=asyncio.run(_read(args.device))
    except BleUnavailable as e: print("WAITING"); print(f"No data — {e}"); return 2
    except Exception as e: print("WAITING"); print(f"No data — {type(e).__name__}: {e}"); return 1
    observed_at=datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")
    snap["at"]=datetime.now(HST).isoformat(timespec="seconds"); snap["source"]="ble"
    try:
        persist_eflow_device(device,args.device,observed_at)
    except Exception as e:
        print(f"DB_ERROR: {type(e).__name__}: {e}",file=sys.stderr)
        try: asyncio.run(device.disconnect())
        except Exception: pass
        return 1
    finally:
        try: asyncio.run(device.disconnect())
        except Exception: pass
    path=SAMPLES/f"read-{args.device}-{datetime.now(HST).strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps(snap,indent=2),encoding="utf-8")
    fields=snap["fields"]
    if fields.get("soc") is not None: (SOC/f"{args.device}-last.json").write_text(json.dumps({"soc":fields["soc"],"at":snap["at"]},indent=2))
    watts={k:fields[k] for k in ("ac_output_power","ac_input_power","usbc_output_power","solar_input_power") if fields.get(k) is not None}
    if watts: (WATTS/f"{args.device}-last.json").write_text(json.dumps({**watts,"at":snap["at"]},indent=2))
    else: print("WAITING"); print("No data — connected but watt fields empty/None (not inventing)")
    print(json.dumps(snap,indent=2))
    print("STATUS=OK" if any(v is not None for v in fields.values()) else "STATUS=WAITING")
    return 0 if any(v is not None for v in fields.values()) else 2
if __name__=="__main__": raise SystemExit(main())
