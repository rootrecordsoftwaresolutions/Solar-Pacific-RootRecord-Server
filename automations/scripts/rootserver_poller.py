#!/usr/bin/env python3
"""RootRecord automations poller — tunnel when online, local jobs always.

Internet gate: TCP check to 1.1.1.1/8.8.8.8 before tunnel/GitHub/Telegram.
If offline at boot, tunnel is deferred; ensure_tunnel_online retries every minute.
BLE / Ollama / HTTP local continue regardless.
"""
from __future__ import annotations

import os
import signal
import socket
import subprocess
import sys
import threading
import time
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
SKILLS_ROOT = SCRIPTS.parent.parent
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SKILLS_ROOT))
import jobs as jobmod  # noqa: E402

INTERVAL_FALLBACK = float(os.environ.get("POLLER_INTERVAL_SEC", "5"))
HOST = os.environ.get("POLLER_BIND", "127.0.0.1")
PORT = int(os.environ.get("POLLER_PORT", "8799"))
SYSTEM_STATUS_JSON = Path("/home/rootrecord/Database/SYSTEM/status/system-status.json")
ENERGY_ROOT = Path(os.environ.get("ENERGY_ROOT", "/home/rootrecord/Database/ENERGY"))
HOSTNAME = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
TOKEN_FILE = Path(os.environ.get("CLOUDFLARED_TOKEN_FILE", str(Path.home() / ".cloudflared" / "rootserver.token")))
CLOUDFLARED_BIN = os.environ.get("CLOUDFLARED_BIN", str(SCRIPTS.parent / "bin" / "cloudflared"))
ENABLE_TUNNEL = os.environ.get("POLLER_ENABLE_TUNNEL", "1") != "0"
TUNNEL_READY_TIMEOUT_SEC = float(os.environ.get("POLLER_TUNNEL_READY_TIMEOUT_SEC", "45"))

_latest = "starting"
_lock = threading.Lock()
_stop = threading.Event()
_tunnel_ready = threading.Event()
_tunnel_proc: subprocess.Popen | None = None
_internet_ok = False
_internet_last_log = 0.0
_tunnel_start_attempts = 0


def full_timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def log(msg: str) -> None:
    print(msg, flush=True)


def heartbeat_line() -> str:
    try:
        return f"{full_timestamp()}{_energy_log_line()}"
    except Exception:
        return f"{full_timestamp()}Poller is online."


def internet_ok(force: bool = False) -> bool:
    global _internet_ok
    for host, port in (("1.1.1.1", 443), ("8.8.8.8", 53), ("1.0.0.1", 443)):
        try:
            with socket.create_connection((host, port), timeout=2.5):
                _internet_ok = True
                return True
        except OSError:
            continue
    _internet_ok = False
    return False


def tunnel_alive() -> bool:
    return _tunnel_proc is not None and _tunnel_proc.poll() is None


def ensure_tunnel_online() -> None:
    global _tunnel_start_attempts, _internet_last_log
    if not ENABLE_TUNNEL:
        return
    if internet_ok(force=True):
        if tunnel_alive():
            return
        _tunnel_start_attempts += 1
        log(f"{full_timestamp()}internet OK — starting Cloudflare tunnel (attempt {_tunnel_start_attempts})")
        _tunnel_ready.clear()
        if start_tunnel():
            wait_for_tunnel_ready()
        return
    now = time.time()
    if now - _internet_last_log >= 55:
        log(f"{full_timestamp()}internet DOWN — net services waiting (retry ~60s)")
        _internet_last_log = now


def _read_energy_json(rel: str):
    try:
        return json.loads((ENERGY_ROOT / rel).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return None


def _fmt_w(n) -> str:
    if not isinstance(n, (int, float)):
        return "No data"
    if float(n) == int(n):
        return f"{int(n)} W"
    return f"{n:.1f} W"


def _fmt_soc(n) -> str:
    if not isinstance(n, (int, float)):
        return "No data"
    if float(n) == int(n):
        return f"{int(n)}%"
    return f"{n:.1f}%"


def _sqlite_board() -> dict | None:
    try:
        from energy.db.latest import board_snapshot
        return board_snapshot()
    except Exception:
        return None


def build_energy_snapshot() -> dict:
    sqlite = _sqlite_board()
    delta_sql = (sqlite or {}).get("delta2") if isinstance(sqlite, dict) else None
    river_sql = (sqlite or {}).get("river2pro") if isinstance(sqlite, dict) else None
    delta_soc = _read_energy_json("soc/delta2-last.json")
    river_soc = _read_energy_json("soc/river2pro-last.json")
    delta_w = _read_energy_json("watts/delta2-last.json")
    river_w = _read_energy_json("watts/river2pro-last.json")

    def soc_of(sql_row, json_blob):
        if isinstance(sql_row, dict) and sql_row.get("soc") is not None:
            return sql_row["soc"]
        if isinstance(json_blob, dict) and json_blob.get("soc") is not None:
            return json_blob["soc"]
        return None

    def watt_of(sql_row, key, json_blob):
        if isinstance(sql_row, dict) and sql_row.get(key) is not None:
            return sql_row[key]
        if isinstance(json_blob, dict) and json_blob.get(key) is not None:
            return json_blob[key]
        return None

    d_soc = soc_of(delta_sql, delta_soc)
    r_soc = soc_of(river_sql, river_soc)
    solar = watt_of(delta_sql, "solar_input_power", delta_w)
    if solar is None:
        solar = watt_of(river_sql, "solar_input_power", river_w)
    ac = watt_of(delta_sql, "ac_output_power", delta_w)
    if ac is None:
        ac = watt_of(river_sql, "ac_output_power", river_w)
    usbc = watt_of(delta_sql, "usbc_output_power", delta_w)
    if usbc is None:
        usbc = watt_of(river_sql, "usbc_output_power", river_w)
    has_delta = d_soc is not None or isinstance(delta_sql, dict) or bool(delta_soc or delta_w)
    has_river = r_soc is not None or isinstance(river_sql, dict) or bool(river_soc or river_w)
    live = has_delta or has_river
    ats = []
    for row in (delta_sql, river_sql):
        if isinstance(row, dict) and row.get("observed_at"):
            ats.append(row["observed_at"])
    for blob in (delta_soc, river_soc, delta_w, river_w):
        if isinstance(blob, dict) and blob.get("at"):
            ats.append(blob["at"])
    updated = sorted(ats)[-1] if ats else None
    source = "sqlite" if (delta_sql or river_sql) else str(ENERGY_ROOT)
    b3 = None
    if isinstance(delta_sql, dict):
        for exp in delta_sql.get("expansions") or []:
            if exp.get("soc") is not None or exp.get("sn"):
                b3 = {"sn": exp.get("sn"), "slot": exp.get("slot"),
                      "soc": _fmt_soc(exp.get("soc")) if exp.get("soc") is not None else "No data"}
                break
    return {
        "status": "live" if live else "Waiting",
        "solarInW": _fmt_w(solar) if live else "No data",
        "deltaSoc": _fmt_soc(d_soc) if d_soc is not None else ("No data" if not has_delta else "Waiting"),
        "riverSoc": _fmt_soc(r_soc) if r_soc is not None else ("Waiting" if not has_river else "No data"),
        "acOut": _fmt_w(ac) if ac is not None else ("Waiting" if live else "No data"),
        "usbC": _fmt_w(usbc) if usbc is not None else ("No data" if live else "No data"),
        "b3": b3, "buckets": "Waiting",
        "ports": {"ac": _fmt_w(ac) if ac is not None else "Waiting", "usbc": _fmt_w(usbc) if usbc is not None else "No data"},
        "source": source,
        "files": {"present": {
            "delta2Soc": d_soc is not None or bool(delta_soc),
            "river2proSoc": r_soc is not None or bool(river_soc),
            "delta2Watts": bool(delta_w) or (isinstance(delta_sql, dict) and delta_sql.get("ac_output_power") is not None),
            "river2proWatts": bool(river_w) or (isinstance(river_sql, dict) and river_sql.get("ac_output_power") is not None),
            "sqlite": bool(delta_sql or river_sql),
        }},
        "updated": updated,
        "note": "Measured samples. SQLite canonical; JSON compatibility.",
    }


def _energy_log_line() -> str:
    snap = build_energy_snapshot()
    parts = [f"status={snap.get('status')}", f"B2={snap.get('deltaSoc')}", f"B1={snap.get('riverSoc')}",
             f"solar={snap.get('solarInW')}", f"ac={snap.get('acOut')}", f"usbc={snap.get('usbC')}", f"src={snap.get('source')}"]
    b3 = snap.get("b3")
    if isinstance(b3, dict):
        parts.insert(3, f"B3={b3.get('soc')}")
    return "ENERGY  " + "  ".join(parts)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send(self, code: int, body: str, ctype: str = "text/plain; charset=utf-8") -> None:
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _proxy_aeyes(self) -> None:
        """Reverse-proxy /aeyes* to local a-eyes cam server (127.0.0.1:8791)."""
        import urllib.error
        import urllib.request
        target = f"http://127.0.0.1:8791{self.path}"
        headers = {}
        if self.headers.get("Cookie"):
            headers["Cookie"] = self.headers.get("Cookie")
        if self.headers.get("Content-Type"):
            headers["Content-Type"] = self.headers.get("Content-Type")
        body = None
        if self.command == "POST":
            length = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(length) if length > 0 else b""
        req = urllib.request.Request(target, data=body, headers=headers, method=self.command)
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = resp.read()
                self.send_response(resp.status)
                for key in ("Content-Type", "Set-Cookie", "Location", "Cache-Control"):
                    val = resp.headers.get(key)
                    if val:
                        self.send_header(key, val)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            ctype = e.headers.get("Content-Type") if e.headers else None
            if ctype:
                self.send_header("Content-Type", ctype)
            for key in ("Set-Cookie", "Location"):
                val = e.headers.get(key) if e.headers else None
                if val:
                    self.send_header(key, val)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self._send(502, f"a-eyes proxy error: {type(e).__name__}\n")

    def do_GET(self) -> None:
        if self.path.startswith("/aeyes"):
            self._proxy_aeyes()
            return
        with _lock:
            line = _latest
        if self.path in ("/", "/health", "/poller"):
            self._send(200, line + "\n"); return
        if self.path == "/json":
            self._send(200, json.dumps({"ok": True, "host": HOSTNAME, "line": line}) + "\n", "application/json; charset=utf-8"); return
        if self.path in ("/energy", "/energy/", "/api/energy"):
            self._send(200, json.dumps(build_energy_snapshot()) + "\n", "application/json; charset=utf-8"); return
        if self.path in ("/system-status.json", "/system-status", "/api/system-status"):
            try:
                body = SYSTEM_STATUS_JSON.read_text(encoding="utf-8")
                self._send(200, body if body.endswith("\n") else body + "\n", "application/json; charset=utf-8")
            except FileNotFoundError:
                self._send(503, json.dumps({"ok": False, "error": "system-status not ready"}) + "\n", "application/json; charset=utf-8")
            except Exception as e:
                self._send(500, json.dumps({"ok": False, "error": type(e).__name__}) + "\n", "application/json; charset=utf-8")
            return
        self._send(404, "not found\n")

    def do_POST(self) -> None:
        if self.path.startswith("/aeyes"):
            self._proxy_aeyes()
            return
        self._send(404, "not found\n")


def _cloudflared_interesting(text: str) -> str | None:
    t = text.strip()
    if not t:
        return None
    drop_sub = ("CONNECTIVITY PRE-CHECKS", "precheck ", "SUMMARY:", "DNS Resolution", "UDP Connectivity",
                "TCP Connectivity", "Cloudflare API", "curve preferences", "ICMP proxy", "Generated Connector",
                "Initial protocol", "Starting metrics", "Version ", "GOOS:", "Settings: map", "Environmental variables",
                "Autoupdate frequency", "Metrics server")
    if any(s in t for s in drop_sub) or t.startswith("|") or t.startswith("+--"):
        return None
    low = t.lower()
    if " err " in f" {low} " or t.startswith("ERR") or "error=" in low:
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        if "terminated" in low:
            return "tunnel connection terminated"
        if "lookup" in low or "dns" in low or "srv" in low or "argotunnel" in low:
            return "tunnel DNS/edge discovery failed — check internet + resolver (try 1.1.1.1)"
        return f"cloudflared ERR: {t[:120]}"
    if t.startswith("WRN") or " WRN " in f" {t} ":
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        return f"cloudflared WRN: {t[:120]}"
    if "Registered tunnel connection" in t:
        idx = loc = ""
        for part in t.split():
            if part.startswith("connIndex="):
                idx = part.split("=", 1)[1]
            if part.startswith("location="):
                loc = part.split("=", 1)[1]
        return f"tunnel connected  conn={idx or '?'}  edge={loc or '?'}"
    if "Starting tunnel" in t:
        return "tunnel starting"
    if "Updated to new configuration" in t:
        if "rootserver.rootrecord.cloud" in t:
            return "tunnel ingress  rootserver.rootrecord.cloud → 127.0.0.1:8799"
        return "tunnel ingress  updated"
    if "Connected to Cloudflare" in t:
        return "tunnel connected to Cloudflare"
    return None
