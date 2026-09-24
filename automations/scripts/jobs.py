# ==============================================================================
# # INFO — MUST HAVE (future agents / operators)
# ------------------------------------------------------------------------------
# Ctrl-C in the poller window / `rootserver-poller stop` MUST kill the whole stack
# (poller + cloudflared + systemd unit). Never "window only".
# Data intake → /home/rootrecord/Database/intake/
# Baks/logs  → /home/rootrecord/Database/GITHUB/
# GitHub trio: skills + website + mainland (skills/us-mainland-server).
# Pacific .gitignore excludes us-mainland-server/ (own repo). No rclone / aws-sync.
# Inference: prefer FLM llama3.2:3b on NPU (:52625); Ollama dolphin lanes = CPU fallback.
# Telegram council-relay via coms/telegram (one getUpdates). Plumbing single-flight.
#
# Deploy format (standing, all future builds):
#   push to GitHub → github_sync_all merge → schedule-stack-reload full stop/start.
#   Do not suggest parallel pollers or default manual restart after ordinary pushes.
# ==============================================================================
#
# HOW TO ADD A JOB (no AI required)
#   1) Copy the blank TEMPLATE block from the matching section below.
#   2) Paste it inside that section's list (keep the commas).
#   3) Set enabled=True, fill labeled fields.
#   4) Keep the same key order and quoting style as the examples.
#   5) Code apply is automatic after GitHub pull; manual restart only if hung/operator asks.
#
# ACTION TYPES
#   builtin  — engine built-in (see labels on each live job)
#   command  — shell string run with bash -lc
#
# BOOT ORDER
#   ON_BOOT runs first, sorted by priority (0 = highest / first).
#   Then ONCE_AT_START (if any).
#   Then recurring: EVERY_SECONDS / EVERY_MINUTE / EVERY_HOUR / ON_AT.
# ON_AT = exact local wall-clock HH:MM (desk TZ = HST). Example: at_times=["13:00"]
# ====================================================

DEFAULTS = {
    "enabled": False,
    "timeout_sec": 120,
    "cwd": "",
    "env": {},
}

# Shared EcoFlow dual-read: succeed if either device saved data (exit 0).
# Individual WAITING still prints; overall FAIL only when both fail.
ECOFLOW_DUAL_READ = (
    "flock -w 90 /tmp/ecoflow-ble.lock bash -c '"
    "ok=0; "
    "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh && ok=1 || true; "
    "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh && ok=1 || true; "
    "exit $((1-ok))'"
)

ON_BOOT = [
    {
        "id": "self_terminal",
        "enabled": True,
        "priority": 0,
        "description": "This desk process + status terminal (self registry).",
        "builtin": "self_process",
        "command": "",
        "process": "/home/rootrecord/.ollama/skills/automations/scripts/rootserver_poller.py",
        "terminal": "RootRecord poller — rootserver",
        "watch": "/home/rootrecord/.ollama/skills/automations/scripts/poller-watch.py",
        "timeout_sec": 5,
        "cwd": "",
        "env": {},
    },
    {
        "id": "cloudflare_tunnel",
        "enabled": True,
        "priority": 1,
        "description": "Start Cloudflare tunnel for rootserver.rootrecord.cloud.",
        "builtin": "tunnel_start",
        "command": "",
        "public_host": "rootserver.rootrecord.cloud",
        "token_file": "/home/rootrecord/.cloudflared/rootserver.token",
        "cloudflared_bin": "/home/rootrecord/.ollama/skills/automations/bin/cloudflared",
        "local_service": "http://127.0.0.1:8799",
        "timeout_sec": 45,
        "cwd": "",
        "env": {},
    },
    {
        "id": "github_setup_remotes",
        "enabled": True,
        "priority": 2,
        "description": "Ensure remotes for skills + website + mainland (repos.conf).",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/github/scripts/setup-all-remotes.sh",
        "timeout_sec": 180,
        "cwd": "/home/rootrecord/.ollama/skills/github",
        "env": {},
    },
    {
        "id": "ollama_warmup",
        "enabled": True,
        "priority": 3,
        "description": "Ensure ollama serve is up (CPU fallback lanes).",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/plumbing/scripts/ollama-warmup.sh",
        "timeout_sec": 120,
        "cwd": "/home/rootrecord",
        "env": {},
    },
    {
        "id": "flm_npu_warmup",
        "enabled": True,
        "priority": 4,
        "description": "Start FastFlowLM llama3.2:3b on XDNA NPU :52625 if binary present.",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/plumbing/scripts/flm-warmup.sh",
        "timeout_sec": 240,
        "cwd": "/home/rootrecord",
        "env": {},
    },
    {
        "id": "council_relay",
        "enabled": True,
        "priority": 5,
        "description": "Start council-relay.py if not already running (single getUpdates).",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/coms/telegram/scripts/ensure-relay.sh",
        "timeout_sec": 30,
        "cwd": "/home/rootrecord/.ollama/skills/coms/telegram",
        "env": {},
    },
]

ONCE_AT_START = [
    {
        "id": "ecoflow_read_boot",
        "enabled": True,
        "description": "One BLE read of Delta 2 + River 2 Pro after boot; saves SQLite then JSON.",
        "builtin": "",
        "command": ECOFLOW_DUAL_READ,
        "timeout_sec": 180,
        "cwd": "/home/rootrecord/.ollama/skills/energy",
        "env": {},
    },
]

EVERY_SECONDS = [
    {
        "id": "heartbeat",
        "enabled": True,
        "description": "Log + HTTP body line: <timestamp>Poller is online.",
        "interval_sec": 5,
        "builtin": "heartbeat",
        "command": "",
        "timeout_sec": 5,
        "cwd": "",
        "env": {},
    },
    {
        "id": "github_sync_all",
        "enabled": True,
        "description": "Push skills + website + mainland; skills merge arms auto stack reload.",
        "interval_sec": 300,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/github/scripts/sync-all.sh",
        "timeout_sec": 300,
        "cwd": "/home/rootrecord/.ollama/skills/github",
        "env": {},
    },
    {
        "id": "worklog_scan",
        "enabled": True,
        "description": "Offline work auto-doc: one full-home file/folder scan into Database/WORKLOG.",
        "interval_sec": 90,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_once.sh",
        "timeout_sec": 180,
        "cwd": "/home/rootrecord/.ollama/skills/reports/scripts",
        "env": {},
    },
]

EVERY_MINUTE = [
    {
        "id": "ecoflow_read_cycle",
        "enabled": True,
        "description": "BLE read Delta 2 + River 2 Pro → SQLite + JSON; poller /energy shows saved data.",
        "only_at_minutes": [0, 15, 30, 45],
        "builtin": "",
        "command": ECOFLOW_DUAL_READ,
        "timeout_sec": 180,
        "cwd": "/home/rootrecord/.ollama/skills/energy",
        "env": {},
    },
]

EVERY_HOUR = []

ON_AT = []

ECOFLOW_ACTIONS = "/home/rootrecord/.ollama/skills/energy/scripts/actions"
ECOFLOW_LOCK = "/tmp/ecoflow-ble.lock"


def ecoflow_command(script: str) -> str:
    """Shell string for a job `command`: serialize BLE with flock, then run one action script."""
    return f"flock -w 60 {ECOFLOW_LOCK} bash {ECOFLOW_ACTIONS}/{script}"


TOGGLES = [
    {"id": "delta2_usb", "device": "delta2", "function": "USB ports", "on": "delta2-usb-on.sh", "off": "delta2-usb-off.sh",
     "field": "usb_ports", "protected": False, "status": "PASS real change 2026-09-23 (chg2)",
     "verify": "readback (PD heartbeat = real measurement)", "note": "USB-C often feeds River / OmniBook - check loads before switching OFF"},
    {"id": "delta2_dc12v", "device": "delta2", "function": "DC 12V (car socket)", "on": "delta2-dc-on.sh", "off": "delta2-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "PASS real change 2026-09-23 (chg1)",
     "verify": "readback (PD heartbeat = real measurement)", "note": ""},
    {"id": "delta2_ac", "device": "delta2", "function": "AC outlets", "on": "delta2-ac-on.sh", "off": "delta2-ac-off.sh",
     "field": "ac_ports", "protected": False,
     "status": "PASS 2026-09-23 (chg3): ON by inverter packets; OFF via safety-net readback",
     "verify": "ON = inverter packets + ac_ports True; OFF = fresh connection, zero inverter packets", "note": ""},
    {"id": "delta2_ac_charging", "device": "delta2", "function": "AC charging", "on": "delta2-ac-charging-on.sh",
     "off": "delta2-ac-charging-off.sh", "field": "ac_charging", "protected": False,
     "status": "PASS 2026-09-23 (chg4)", "verify": "readback changes to the wanted value", "note": ""},
    {"id": "delta2_energy_backup", "device": "delta2", "function": "Energy backup", "on": "delta2-energy-backup-on.sh",
     "off": "delta2-energy-backup-off.sh", "field": "energy_backup", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": ""},
    {"id": "delta2_grid_bypass", "device": "delta2", "function": "Grid bypass", "on": "delta2-grid-bypass-on.sh",
     "off": "delta2-grid-bypass-off.sh", "field": "disable_grid_bypass", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": ""},
    {"id": "river2pro_ac", "device": "river2pro", "function": "AC outlets", "on": "river2pro-ac-on.sh", "off": "river2pro-ac-off.sh",
     "field": "ac_ports", "protected": False, "status": "UNTESTED post-fix",
     "verify": "ON = inverter packets + ac_ports True; OFF = fresh connection, zero inverter packets", "note": ""},
    {"id": "river2pro_ac_always_on", "device": "river2pro", "function": "AC always-on", "on": "river2pro-ac-always-on-on.sh",
     "off": "river2pro-ac-always-on-off.sh", "field": "", "protected": False, "status": "UNTESTED post-fix",
     "verify": "unknown", "note": ""},
    {"id": "river2pro_xboost", "device": "river2pro", "function": "AC X-Boost", "on": "river2pro-xboost-on.sh",
     "off": "river2pro-xboost-off.sh", "field": "", "protected": False, "status": "UNTESTED post-fix",
     "verify": "unknown", "note": ""},
    {"id": "river2pro_dc12v", "device": "river2pro", "function": "DC 12V (car)", "on": "river2pro-dc-on.sh", "off": "river2pro-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "UNTESTED post-fix", "verify": "readback changes", "note": ""},
    {"id": "river2pro_energy_backup", "device": "river2pro", "function": "Energy backup", "on": "river2pro-energy-backup-on.sh",
     "off": "river2pro-energy-backup-off.sh", "field": "energy_backup", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes", "note": ""},
]

READS = [
    {"id": "delta2_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh"},
    {"id": "river2pro_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh"},
]
