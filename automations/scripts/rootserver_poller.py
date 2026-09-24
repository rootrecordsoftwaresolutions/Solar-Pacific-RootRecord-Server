#!/usr/bin/env python3
"""RootRecord automations poller — tunnel first, then scheduled jobs.

# INFO — MUST HAVE (future agents):
# Ctrl-C / stop-poller-stack.sh must terminate this process, cloudflared, and
# rr-rootserver-poller.service. See scripts/jobs.py header and stop-poller-stack.sh.
#
# Job definitions live in jobs.py — ON_BOOT priorities (0=self, 1=cloudflare, 2+=templates),
# then recurring sections (EVERY_* + ON_AT exact HH:MM). Keep section formatting identical.
#
# Energy: /energy prefers SQLite (canonical) then falls back to legacy JSON last-files.
# EcoFlow reads are scheduled in jobs.py (ONCE_AT_START + EVERY_MINUTE 0/15/30/45).
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import threading
import time
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
SKILLS_ROOT = SCRIPTS.parent.parent  # ~/.ollama/skills
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SKILLS_ROOT))
import jobs as jobmod  # noqa: E402

INTERVAL_FALLBACK = float(os.environ.get("POLLER_INTERVAL_SEC", "5"))
HOST = os.environ.get("POLLER_BIND", "127.0.0.1")
PORT = int(os.environ.get("POLLER_PORT", "8799"))
ENERGY_ROOT = Path(os.environ.get("ENERGY_ROOT", "/home/rootrecord/Database/ENERGY"))
HOSTNAME = os.environ.get("POLLER_PUBLIC_HOST", "rootserver.rootrecord.cloud")
TOKEN_FILE = Path(
    os.environ.get(
        "CLOUDFLARED_TOKEN_FILE",
        str(Path.home() / ".cloudflared" / "rootserver.token"),
    )
)
CLOUDFLARED_BIN = os.environ.get(
    "CLOUDFLARED_BIN",
    str(SCRIPTS.parent / "bin" / "cloudflared"),
)
ENABLE_TUNNEL = os.environ.get("POLLER_ENABLE_TUNNEL", "1") != "0"
TUNNEL_READY_TIMEOUT_SEC = float(os.environ.get("POLLER_TUNNEL_READY_TIMEOUT_SEC", "45"))

_latest = "starting"
_lock = threading.Lock()
_stop = threading.Event()
_tunnel_ready = threading.Event()
_tunnel_proc: subprocess.Popen | None = None


def full_timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def log(msg: str) -> None:
    print(msg, flush=True)


def heartbeat_line() -> str:
    return f"{full_timestamp()}Poller is online."


def _read_energy_json(rel: str):
    """Measured ENERGY last-file or None. Never invent."""
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
    """Latest measured board from canonical SQLite, or None."""
    try:
        from energy.db.latest import board_snapshot

        return board_snapshot()
    except Exception:
        return None


def build_energy_snapshot() -> dict:
    """Hawaii ENERGY board for /energy — SQLite first, then legacy JSON."""
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

    # Expansion B3 summary when present on Delta 2
    b3 = None
    if isinstance(delta_sql, dict):
        for exp in delta_sql.get("expansions") or []:
            if exp.get("soc") is not None or exp.get("sn"):
                b3 = {
                    "sn": exp.get("sn"),
                    "slot": exp.get("slot"),
                    "soc": _fmt_soc(exp.get("soc")) if exp.get("soc") is not None else "No data",
                }
                break

    return {
        "status": "live" if live else "Waiting",
        "solarInW": _fmt_w(solar) if live else "No data",
        "deltaSoc": _fmt_soc(d_soc) if d_soc is not None else ("No data" if not has_delta else "Waiting"),
        "riverSoc": _fmt_soc(r_soc) if r_soc is not None else ("Waiting" if not has_river else "No data"),
        "acOut": _fmt_w(ac) if ac is not None else ("Waiting" if live else "No data"),
        "usbC": _fmt_w(usbc) if usbc is not None else ("No data" if live else "No data"),
        "b3": b3,
        "buckets": "Waiting",
        "ports": {
            "ac": _fmt_w(ac) if ac is not None else "Waiting",
            "usbc": _fmt_w(usbc) if usbc is not None else "No data",
        },
        "source": source,
        "files": {
            "present": {
                "delta2Soc": d_soc is not None or bool(delta_soc),
                "river2proSoc": r_soc is not None or bool(river_soc),
                "delta2Watts": bool(delta_w) or (isinstance(delta_sql, dict) and delta_sql.get("ac_output_power") is not None),
                "river2proWatts": bool(river_w) or (isinstance(river_sql, dict) and river_sql.get("ac_output_power") is not None),
                "sqlite": bool(delta_sql or river_sql),
            }
        },
        "updated": updated,
        "note": "Measured samples. SQLite is canonical; JSON last-files are compatibility. Missing = No data / Waiting.",
    }


def _energy_log_line() -> str:
    """One clean line for poller console after EcoFlow reads."""
    snap = build_energy_snapshot()
    parts = [
        f"status={snap.get('status')}",
        f"B2={snap.get('deltaSoc')}",
        f"B1={snap.get('riverSoc')}",
        f"solar={snap.get('solarInW')}",
        f"ac={snap.get('acOut')}",
        f"usbc={snap.get('usbC')}",
        f"src={snap.get('source')}",
    ]
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

    def do_GET(self) -> None:  # noqa: N802
        with _lock:
            line = _latest
        if self.path in ("/", "/health", "/poller"):
            self._send(200, line + "\n")
            return
        if self.path == "/json":
            self._send(
                200,
                json.dumps({"ok": True, "host": HOSTNAME, "line": line}) + "\n",
                "application/json; charset=utf-8",
            )
            return
        if self.path in ("/energy", "/energy/", "/api/energy"):
            body = build_energy_snapshot()
            self._send(
                200,
                json.dumps(body) + "\n",
                "application/json; charset=utf-8",
            )
            return
        self._send(404, "not found\n")


def _cloudflared_interesting(text: str) -> str | None:
    t = text.strip()
    if not t:
        return None
    drop_sub = (
        "CONNECTIVITY PRE-CHECKS",
        "-----------",
        "COMPONENT         TARGET",
        "precheck component=",
        "precheck complete",
        "SUMMARY:",
        "DNS Resolution",
        "UDP Connectivity",
        "TCP Connectivity",
        "Cloudflare API",
        "Tunnel connection curve preferences",
        "ICMP proxy will use",
        "Generated Connector ID",
        "Initial protocol",
        "Starting metrics server",
        "Version ",
        "GOOS:",
        "Settings: map[",
        "Environmental variables map[",
        "Autoupdate frequency",
        "Metrics server",
    )
    if any(s in t for s in drop_sub):
        return None
    if t.startswith("|") or t.startswith("+--"):
        return None
    low = t.lower()
    if " err " in f" {low} " or t.startswith("ERR") or "error=" in low:
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        if "terminated" in low:
            return "tunnel connection terminated"
        return f"cloudflared ERR: {t[:160]}"
    if t.startswith("WRN") or " WRN " in f" {t} ":
        if "timeout" in low:
            return "tunnel timeout — reconnecting"
        return f"cloudflared WRN: {t[:160]}"
    if "Registered tunnel connection" in t:
        idx = loc = ""
        for part in t.split():
            if part.startswith("connIndex="):
                idx = part.split("=", 1)[1]
            if part.startswith("location="):
                loc = part.split("=", 1)[1]
        return f"tunnel connected  conn={idx or '?'}  edge={loc or '?'}"
    if "Starting tunnel" in t:
        tid = ""
        for part in t.split():
            if part.startswith("tunnelID="):
                tid = part.split("=", 1)[1]
        return f"tunnel starting  id={tid or '?'}"
    if "Updated to new configuration" in t:
        if "rootserver.rootrecord.cloud" in t:
            return "tunnel ingress  rootserver.rootrecord.cloud → 127.0.0.1:8799"
        return "tunnel ingress  updated"
    if "Connected to Cloudflare" in t:
        return "tunnel connected to Cloudflare"
    return None


def start_tunnel() -> bool:
    global _tunnel_proc
    if not ENABLE_TUNNEL:
        log(f"{full_timestamp()}Tunnel disabled (POLLER_ENABLE_TUNNEL=0).")
        _tunnel_ready.set()
        return False
    if not Path(CLOUDFLARED_BIN).is_file():
        log(f"{full_timestamp()}Tunnel DOWN — cloudflared missing at {CLOUDFLARED_BIN}")
        return False
    if not TOKEN_FILE.is_file():
        log(f"{full_timestamp()}Tunnel DOWN — token file missing: {TOKEN_FILE}")
        return False
    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not token:
        log(f"{full_timestamp()}Tunnel DOWN — empty token file")
        return False

    mode = os.environ.get("POLLER_TUNNEL_MODE", "token").lower()
    if mode == "quick":
        cmd = [CLOUDFLARED_BIN, "tunnel", "--no-autoupdate", "--url", f"http://{HOST}:{PORT}"]
        popen_kwargs: dict = {}
    else:
        cmd = [CLOUDFLARED_BIN, "tunnel", "--no-autoupdate", "run"]
        env = os.environ.copy()
        env["TUNNEL_TOKEN"] = token
        popen_kwargs = {"env": env}

    log(f"{full_timestamp()}Starting cloudflared mode={mode} public_host={HOSTNAME}")
    _tunnel_proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        **popen_kwargs,
    )

    def pump() -> None:
        assert _tunnel_proc is not None and _tunnel_proc.stdout is not None
        for line in _tunnel_proc.stdout:
            text = line.rstrip()
            interesting = _cloudflared_interesting(text)
            if interesting:
                log(f"{full_timestamp()}{interesting}")
            if "Registered tunnel connection" in text or "Connected to Cloudflare" in text:
                if not _tunnel_ready.is_set():
                    log(f"{full_timestamp()}Tunnel READY — first connection registered.")
                    _tunnel_ready.set()
            if _stop.is_set():
                break
        if _tunnel_proc.poll() is not None and not _tunnel_ready.is_set():
            log(
                f"{full_timestamp()}Tunnel DOWN — cloudflared exited before ready "
                f"(code={_tunnel_proc.returncode})."
            )

    threading.Thread(target=pump, name="cloudflared-log", daemon=True).start()
    return True


def wait_for_tunnel_ready() -> None:
    if not ENABLE_TUNNEL or _tunnel_ready.is_set():
        return
    log(
        f"{full_timestamp()}Waiting for tunnel register "
        f"(timeout={TUNNEL_READY_TIMEOUT_SEC:.0f}s) before jobs…"
    )
    if not _tunnel_ready.wait(timeout=TUNNEL_READY_TIMEOUT_SEC):
        log(
            f"{full_timestamp()}Tunnel WAITING — no register within "
            f"{TUNNEL_READY_TIMEOUT_SEC:.0f}s; starting jobs anyway."
        )


def _is_ecoflow_job(jid: str) -> bool:
    return jid.startswith("ecoflow_") or jid in ("delta2_read", "river2pro_read")


def run_command_job(job: dict) -> None:
    jid = job.get("id", "?")
    cmd = (job.get("command") or "").strip()
    if not cmd:
        log(f"{full_timestamp()}job:{jid} SKIP — empty command")
        return
    timeout = float(job.get("timeout_sec") or 120)
    cwd = (job.get("cwd") or "").strip() or None
    env = os.environ.copy()
    extra = job.get("env") or {}
    if isinstance(extra, dict):
        env.update({str(k): str(v) for k, v in extra.items()})
    quiet = jid in ("github_sync_all", "github_setup_remotes", "github_autopush")
    eco = _is_ecoflow_job(jid)
    if not quiet:
        if eco:
            log(f"{full_timestamp()}job:{jid} RUN  EcoFlow BLE read…")
        else:
            log(f"{full_timestamp()}job:{jid} RUN  {cmd}")
    try:
        r = subprocess.run(
            ["bash", "-lc", cmd],
            cwd=cwd,
            env=env,
            timeout=timeout,
            capture_output=True,
            text=True,
        )
        out = (r.stdout or "").strip()
        err = (r.stderr or "").strip()
        if r.returncode == 0:
            if eco:
                # Prefer SUMMARY= lines from read_runner; else one board line from DB/JSON.
                summaries = [
                    ln.strip()
                    for ln in out.splitlines()
                    if ln.strip().startswith("SUMMARY=") or ln.strip().startswith("STATUS=")
                ]
                if summaries:
                    for ln in summaries[-6:]:
                        log(f"{full_timestamp()}job:{jid} | {ln}")
                log(f"{full_timestamp()}{_energy_log_line()}")
            elif out:
                for line in out.splitlines()[:40]:
                    line = line.strip()
                    if not line:
                        continue
                    if quiet and any(
                        line.startswith(p)
                        for p in ("[ok]", "[skip]", "[clone]", "Updated", "Added", "Done.")
                    ):
                        continue
                    log(f"{full_timestamp()}job:{jid} | {line}")
            elif not quiet:
                log(f"{full_timestamp()}job:{jid} OK")
        else:
            log(f"{full_timestamp()}job:{jid} FAIL code={r.returncode}")
            for line in (err or out).splitlines()[:20]:
                log(f"{full_timestamp()}job:{jid} ! {line}")
            if eco:
                log(f"{full_timestamp()}{_energy_log_line()}")
    except subprocess.TimeoutExpired:
        log(f"{full_timestamp()}job:{jid} TIMEOUT after {timeout:.0f}s")
    except Exception as e:
        log(f"{full_timestamp()}job:{jid} ERROR {e}")


def run_builtin(job: dict) -> None:
    global _latest
    jid = job.get("id", "?")
    name = (job.get("builtin") or "").strip()
    if name == "heartbeat":
        line = heartbeat_line()
        with _lock:
            _latest = line
        log(line)
        return
    if name == "self_process":
        proc = job.get("process") or str(Path(__file__).resolve())
        term = job.get("terminal") or "RootRecord poller — rootserver"
        watch = job.get("watch") or str(SCRIPTS / "poller-watch.py")
        log(f"{full_timestamp()}boot:p0 self_process")
        log(f"{full_timestamp()}boot:p0 process  = {proc}")
        log(f"{full_timestamp()}boot:p0 terminal = {term}")
        log(f"{full_timestamp()}boot:p0 watch    = {watch}")
        log(f"{full_timestamp()}boot:p0 pid      = {os.getpid()}")
        return
    if name == "tunnel_start":
        global HOSTNAME, TOKEN_FILE, CLOUDFLARED_BIN, TUNNEL_READY_TIMEOUT_SEC
        if job.get("public_host"):
            HOSTNAME = str(job["public_host"])
        if job.get("token_file"):
            TOKEN_FILE = Path(str(job["token_file"]))
        if job.get("cloudflared_bin"):
            CLOUDFLARED_BIN = str(job["cloudflared_bin"])
        if job.get("timeout_sec"):
            TUNNEL_READY_TIMEOUT_SEC = float(job["timeout_sec"])
        log(f"{full_timestamp()}boot:p1 cloudflare_tunnel host={HOSTNAME}")
        started = start_tunnel()
        if started:
            wait_for_tunnel_ready()
        elif ENABLE_TUNNEL:
            log(f"{full_timestamp()}Tunnel DOWN — continuing with local jobs only.")
        return
    if name == "http_ping":
        url = (job.get("command") or f"http://{HOST}:{PORT}/").strip()
        try:
            import urllib.request

            with urllib.request.urlopen(url, timeout=5) as resp:
                log(f"{full_timestamp()}job:{jid} http_ping {resp.status} {url}")
        except Exception as e:
            log(f"{full_timestamp()}job:{jid} http_ping FAIL {e}")
        return
    log(f"{full_timestamp()}job:{jid} UNKNOWN builtin={name!r}")


def run_job(job: dict) -> None:
    if not job.get("enabled"):
        return
    builtin = (job.get("builtin") or "").strip()
    if builtin:
        run_builtin(job)
        return
    run_command_job(job)


def enabled_jobs(section: list) -> list:
    return [j for j in section if isinstance(j, dict) and j.get("enabled")]


def _normalize_hhmm(raw: object) -> str | None:
    if not isinstance(raw, str):
        return None
    s = raw.strip()
    if ":" not in s:
        return None
    try:
        hh_s, mm_s = s.split(":", 1)
        hh, mm = int(hh_s), int(mm_s)
    except ValueError:
        return None
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        return None
    return f"{hh:02d}:{mm:02d}"


def scheduler_loop() -> None:
    sec_jobs = enabled_jobs(getattr(jobmod, "EVERY_SECONDS", []))
    min_jobs = enabled_jobs(getattr(jobmod, "EVERY_MINUTE", []))
    hour_jobs = enabled_jobs(getattr(jobmod, "EVERY_HOUR", []))
    at_jobs = enabled_jobs(getattr(jobmod, "ON_AT", []))

    next_due: dict[str, float] = {}
    now = time.monotonic()
    for j in sec_jobs:
        interval = float(j.get("interval_sec") or INTERVAL_FALLBACK)
        if interval <= 0:
            interval = INTERVAL_FALLBACK
        next_due[j["id"]] = now

    last_minute: int | None = None
    last_hour: int | None = None
    fired_at: set[str] = set()

    log(
        f"{full_timestamp()}scheduler  "
        f"every_seconds={len(sec_jobs)}  every_minute={len(min_jobs)}  "
        f"every_hour={len(hour_jobs)}  on_at={len(at_jobs)}"
    )

    while not _stop.is_set():
        wall = datetime.now().astimezone()
        mono = time.monotonic()

        for j in sec_jobs:
            jid = j["id"]
            if mono >= next_due.get(jid, 0):
                run_job(j)
                interval = float(j.get("interval_sec") or INTERVAL_FALLBACK)
                next_due[jid] = mono + max(0.2, interval)

        minute = wall.minute
        hour = wall.hour
        hm = f"{hour:02d}:{minute:02d}"
        day = wall.date().isoformat()

        if last_minute is None:
            last_minute = minute
            last_hour = hour
        else:
            if minute != last_minute:
                for j in min_jobs:
                    only = j.get("only_at_minutes") or []
                    if only and minute not in only:
                        continue
                    run_job(j)

                for j in at_jobs:
                    times = {
                        t
                        for raw in (j.get("at_times") or [])
                        if (t := _normalize_hhmm(raw)) is not None
                    }
                    if hm not in times:
                        continue
                    key = f"{j['id']}|{day}|{hm}"
                    if key in fired_at:
                        continue
                    run_job(j)
                    fired_at.add(key)

                last_minute = minute
            if hour != last_hour and minute == 0:
                for j in hour_jobs:
                    only = j.get("only_at_hours") or []
                    if only and hour not in only:
                        continue
                    run_job(j)
                last_hour = hour
            elif hour != last_hour:
                last_hour = hour

            if fired_at:
                fired_at = {k for k in fired_at if f"|{day}|" in k}

        _stop.wait(0.25)


def shutdown(*_args) -> None:
    _stop.set()
    _tunnel_ready.set()
    global _tunnel_proc
    if _tunnel_proc and _tunnel_proc.poll() is None:
        _tunnel_proc.terminate()
        try:
            _tunnel_proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            _tunnel_proc.kill()


def run_on_boot() -> None:
    boot = [j for j in enabled_jobs(getattr(jobmod, "ON_BOOT", [])) if isinstance(j, dict)]
    boot.sort(key=lambda j: int(j.get("priority", 100)))
    log(f"{full_timestamp()}boot:start  jobs={len(boot)}")
    for j in boot:
        prio = j.get("priority", "?")
        jid = j.get("id", "?")
        log(f"{full_timestamp()}boot:run  priority={prio}  id={jid}")
        run_job(j)
    log(f"{full_timestamp()}boot:done")


def main() -> int:
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    server = ThreadingHTTPServer((HOST, PORT), Handler)
    threading.Thread(target=server.serve_forever, name="http", daemon=True).start()
    log(f"{full_timestamp()}HTTP listening on http://{HOST}:{PORT} (open access on bind)")

    run_on_boot()

    for j in enabled_jobs(getattr(jobmod, "ONCE_AT_START", [])):
        run_job(j)

    scheduler_loop()

    server.shutdown()
    shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
