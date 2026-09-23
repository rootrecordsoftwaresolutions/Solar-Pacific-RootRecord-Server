#!/usr/bin/env python3
"""Read live snapshot; WAITING/No data when BLE unavailable. Never invent watts."""
from __future__ import annotations
import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from paths import SAMPLES, SOC, WATTS, ensure_dirs, BLE_LOG  # noqa: E402
from ble_client import connect, BleUnavailable, eflib_ready  # noqa: E402

HST = ZoneInfo("Pacific/Honolulu")


def _fields(device) -> dict:
    def g(name, default=None):
        return getattr(device, name, default)

    solar = g("xt60_input_power")
    if solar is None:
        solar = g("solar_input_power")
    return {
        "ac_ports": g("ac_ports"),
        "usb_ports": g("usb_ports"),
        "dc_12v_port": g("dc_12v_port"),
        "ac_output_power": g("ac_output_power"),
        "ac_input_power": g("ac_input_power"),
        "usbc_output_power": g("usbc_output_power"),
        "usba_output_power": g("usba_output_power"),
        "solar_input_power": solar,
        "soc": g("battery_level", g("soc")),
    }


async def _read(alias: str) -> dict:
    device = await connect(alias)
    try:
        await asyncio.sleep(2.0)
        return {"alias": alias, "fields": _fields(device)}
    finally:
        try:
            await device.disconnect()
        except Exception:
            pass


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--device", required=True)
    args = p.parse_args()
    ensure_dirs()
    ok, reason = eflib_ready()
    if not ok:
        print("WAITING")
        print(f"No data — {reason}")
        return 2
    try:
        snap = asyncio.run(_read(args.device))
    except BleUnavailable as e:
        print("WAITING")
        print(f"No data — {e}")
        return 2
    except Exception as e:
        print("WAITING")
        print(f"No data — {type(e).__name__}: {e}")
        return 1
    snap["at"] = datetime.now(HST).isoformat(timespec="seconds")
    snap["source"] = "ble"
    # Only persist when we actually got a connection; still may have None fields
    path = SAMPLES / f"read-{args.device}-{datetime.now(HST).strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps(snap, indent=2), encoding="utf-8")
    fields = snap["fields"]
    if fields.get("soc") is not None:
        (SOC / f"{args.device}-last.json").write_text(json.dumps({"soc": fields["soc"], "at": snap["at"]}, indent=2))
    watts = {k: fields[k] for k in ("ac_output_power", "ac_input_power", "usbc_output_power", "solar_input_power") if fields.get(k) is not None}
    if watts:
        (WATTS / f"{args.device}-last.json").write_text(json.dumps({**watts, "at": snap["at"]}, indent=2))
    else:
        # connected but no watt fields yet — still honest
        print("WAITING")
        print("No data — connected but watt fields empty/None (not inventing)")
    print(json.dumps(snap, indent=2))
    # exit 0 if any port or soc present; else 2
    if any(v is not None for v in fields.values()):
        print("STATUS=OK")
        return 0
    print("STATUS=WAITING")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
