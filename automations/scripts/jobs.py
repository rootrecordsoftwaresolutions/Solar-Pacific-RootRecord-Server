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
# ==============================================================================
#
# HOW TO ADD A JOB (no AI required)
#   1) Copy the blank TEMPLATE block from the matching section below.
#   2) Paste it inside that section's list (keep the commas).
#   3) Set enabled=True, fill labeled fields.
#   4) Keep the same key order and quoting style as the examples.
#   5) Restart: /home/rootrecord/rootserver-poller restart
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

# ------------------------------------------------------------------------------
# SHARED DEFAULTS (optional overrides per job still win)
# ------------------------------------------------------------------------------
DEFAULTS = {
    "enabled": False,
    "timeout_sec": 120,
    "cwd": "",
    "env": {},
}

# ====================================================
# SECTION: ON_BOOT  (priority list — lower number runs first)
# Cloudflare lives here at priority 1. Priority 0 is this desk itself.
# ====================================================
ON_BOOT = [
    # --- priority 0: self / status terminal (redundant registry — keep) -----------
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
    # --- priority 1: Cloudflare tunnel -------------------------------------------
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
    # --- priority 2: ensure GitHub backup remote (token from master-key.env) ------
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

    # --- priority 3: Ollama serve warm ------------------------------------------
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
    # --- priority 4: FastFlowLM NPU (llama3.2:3b) ------------------------------
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
    # --- priority 5: Telegram council relay (one process) ----------------------
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

    # --- priority 3: TEMPLATE (on boot) — copy from here -------------------------
    # {
    #     "id": "example_on_boot_p3",
    #     "enabled": False,
    #     "priority": 3,
    #     "description": "One-line plain description of what this boot job does.",
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/boot-script.sh",
    #     "timeout_sec": 120,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]

# ====================================================
# SECTION: ONCE_AT_START
# One-time scripts after ON_BOOT finishes (tunnel already handled above).
# ====================================================
ONCE_AT_START = [
    # --- TEMPLATE (run once after boot priorities) — copy from here --------------
    # {
    #     "id": "example_once_at_start",
    #     "enabled": False,
    #     "description": "One-line plain description of what this job does.",
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/oneshot.sh",
    #     "timeout_sec": 300,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]

# ====================================================
# SECTION: EVERY_SECONDS
# Fires on a repeating interval. interval_sec is required.
# ====================================================
EVERY_SECONDS = [
    # --- live job: desk heartbeat (do not remove; disable only if intentional) ---
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
    # --- github autopush: one check-stage-commit-push cycle (was manual loop) ----
    {
        "id": "github_sync_all",
        "enabled": True,
        "description": "Push skills + website + mainland (repos.conf; 90MB guard). Baks → Database/GITHUB.",
        "interval_sec": 300,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/github/scripts/sync-all.sh",
        "timeout_sec": 300,
        "cwd": "/home/rootrecord/.ollama/skills/github",
        "env": {},
    },
# --- worklog: one scan per cycle (NOT the forever poller — that times out) -----
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
    # --- TEMPLATE (every X seconds) — copy from here -----------------------------
    # {
    #     "id": "example_every_seconds",
    #     "enabled": False,
    #     "description": "One-line plain description of what this job does.",
    #     "interval_sec": 30,
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/script.sh",
    #     "timeout_sec": 120,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]

# ====================================================
# SECTION: EVERY_MINUTE
# Fires once when the wall-clock minute changes (second ~0).
# Optional: only_at_minutes = [0, 15, 30, 45]  (empty list = every minute)
# ====================================================
EVERY_MINUTE = [
    # --- TEMPLATE (every minute / selected minutes) — copy from here ------------
    # {
    #     "id": "example_every_minute",
    #     "enabled": False,
    #     "description": "One-line plain description of what this job does.",
    #     "only_at_minutes": [],
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/script.sh",
    #     "timeout_sec": 120,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]

# ====================================================
# SECTION: EVERY_HOUR
# Fires once when the wall-clock hour changes (minute 0).
# Optional: only_at_hours = [0, 6, 12, 18]  (empty list = every hour, 0–23)
# ====================================================
EVERY_HOUR = [
    # --- TEMPLATE (every hour / selected hours) — copy from here ----------------
    # {
    #     "id": "example_every_hour",
    #     "enabled": False,
    #     "description": "One-line plain description of what this job does.",
    #     "only_at_hours": [],
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/script.sh",
    #     "timeout_sec": 300,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]


# ====================================================
# SECTION: ON_AT
# Exact local wall-clock times (desk TZ — Pacific/Honolulu / HST).
# Fires once when HH:MM matches; repeats next days at the same times.
# at_times = ["13:00"] or ["07:30", "13:00", "21:15"]  (24h HH:MM)
# Already covered for top-of-hour only: EVERY_HOUR + only_at_hours=[13]
# Use ON_AT when you need a specific minute (or several exact times).
# ====================================================
ON_AT = [
    # --- TEMPLATE (exact HH:MM local) — copy from here --------------------------
    # {
    #     "id": "example_on_at_1300",
    #     "enabled": False,
    #     "description": "Runs once at 13:00 HST (local desk clock).",
    #     "at_times": ["13:00"],
    #     "builtin": "",
    #     "command": "/home/rootrecord/path/to/script.sh",
    #     "timeout_sec": 300,
    #     "cwd": "/home/rootrecord",
    #     "env": {},
    # },
    # --- end TEMPLATE ------------------------------------------------------------
]

# ====================================================
# ECOFLOW TOGGLES — per function / access / toggle catalog (added 2026-09-23)
# NOT read by the poller (the scheduler only reads ON_BOOT / ONCE_AT_START / EVERY_* / ON_AT); jobs.py is loaded once at start.
# This is the one place that names every EcoFlow function: its on/off scripts, readback field, how success is verified, status.
# To SCHEDULE one: copy the template below into ON_AT (or EVERY_*), set enabled=True + at_times, then
#   /home/rootrecord/rootserver-poller restart
# CAVEATS (from reading rootserver_poller.py, 2026-09-23):
#  - The scheduler is single-threaded and run_job() blocks. One toggle takes ~25 s wall clock (10 s scan + connect + auth + ~2.5 s),
#    so the 5 s heartbeat stalls meanwhile, and an ON_AT job whose minute passes while the loop is blocked is MISSED (no catch-up).
#    Avoid minutes that collide with long jobs (github_sync_all up to 300 s, worklog_scan up to 180 s).
#  - No on-demand trigger exists: the HTTP handler is GET-only (/, /health, /poller, /json, /energy, /api/energy) and is exposed
#    publicly through the tunnel - do NOT add an unauthenticated state-changing route.
#  - BLE sessions must be serialized: commands are wrapped with flock (the poller is serial, manual runs are not).
#  - AC fields (ac_ports, ac_output_power, ...) are library DEFAULTS when the inverter is silent: verify AC by inverter packets.
# ====================================================
ECOFLOW_ACTIONS = "/home/rootrecord/.ollama/skills/energy/scripts/actions"
ECOFLOW_LOCK = "/tmp/ecoflow-ble.lock"


def ecoflow_command(script: str) -> str:
    """Shell string for a job `command`: serialize BLE with flock, then run one action script."""
    return f"flock -w 60 {ECOFLOW_LOCK} bash {ECOFLOW_ACTIONS}/{script}"


# EXAMPLE scheduled toggle (copy into ON_AT; keep enabled False until times are chosen):
# {
#     "id": "delta2_usb_on_0700",
#     "enabled": False,
#     "description": "Delta 2 USB ON at 07:00 HST",
#     "at_times": ["07:00"],
#     "builtin": "",
#     "command": ecoflow_command("delta2-usb-on.sh"),
#     "timeout_sec": 150,
#     "cwd": "/home/rootrecord/.ollama/skills/energy",
#     "env": {},
# },

TOGGLES = [
    {"id": "delta2_usb", "device": "delta2", "function": "USB ports", "on": "delta2-usb-on.sh", "off": "delta2-usb-off.sh",
     "field": "usb_ports", "protected": False, "status": "PASS real change 2026-09-23 (chg2)",
     "verify": "readback (PD heartbeat = real measurement)", "note": "USB-C often feeds River / OmniBook - check loads before switching OFF"},
    {"id": "delta2_dc12v", "device": "delta2", "function": "DC 12V (car socket)", "on": "delta2-dc-on.sh", "off": "delta2-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "PASS real change 2026-09-23 (chg1)",
     "verify": "readback (PD heartbeat = real measurement)", "note": ""},
    {"id": "delta2_ac", "device": "delta2", "function": "AC outlets", "on": "delta2-ac-on.sh", "off": "delta2-ac-off.sh",
     "field": "ac_ports", "protected": False,
     "status": "PASS 2026-09-23 (chg3): ON by inverter packets; OFF via safety-net readback (probe crashed before its own fresh-connection check)",
     "verify": "ON = inverter packets (src 4) arrive AND ac_ports True; OFF = fresh connection >=12 s after auth with zero inverter packets",
     "note": "same-connection OFF readback may be stale True; AC readbacks are library defaults when the inverter is silent; fresh-connection OFF check still worth re-running once to close the gap formally"},
    {"id": "delta2_ac_charging", "device": "delta2", "function": "AC charging", "on": "delta2-ac-charging-on.sh",
     "off": "delta2-ac-charging-off.sh", "field": "ac_charging", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": "pre-fix: FAIL AssertionError"},
    {"id": "delta2_energy_backup", "device": "delta2", "function": "Energy backup", "on": "delta2-energy-backup-on.sh",
     "off": "delta2-energy-backup-off.sh", "field": "energy_backup", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": "pre-fix OK runs were probably no-ops (charge limits None, H2 unproven)"},
    {"id": "delta2_grid_bypass", "device": "delta2", "function": "Grid bypass", "on": "delta2-grid-bypass-on.sh",
     "off": "delta2-grid-bypass-off.sh", "field": "disable_grid_bypass", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": "method is enable_disable_grid_bypass(disabled): confirm what on/off mean in the wrapper before scheduling"},
    {"id": "river2pro_ac", "device": "river2pro", "function": "AC outlets", "on": "river2pro-ac-on.sh", "off": "river2pro-ac-off.sh",
     "field": "ac_ports", "protected": True, "status": "UNTESTED post-fix",
     "verify": "ON = inverter packets + ac_ports True; OFF = fresh connection, zero inverter packets", "note": "AC feeds Starlink since 2026-09-23 - ask the operator before any use"},
    {"id": "river2pro_ac_always_on", "device": "river2pro", "function": "AC always-on", "on": "river2pro-ac-always-on-on.sh",
     "off": "river2pro-ac-always-on-off.sh", "field": "", "protected": True, "status": "UNTESTED post-fix",
     "verify": "unknown (readback field name unverified)", "note": "AC behavior; Starlink rides this AC - ask first"},
    {"id": "river2pro_xboost", "device": "river2pro", "function": "AC X-Boost", "on": "river2pro-xboost-on.sh",
     "off": "river2pro-xboost-off.sh", "field": "", "protected": True, "status": "UNTESTED post-fix",
     "verify": "unknown (readback field name unverified)", "note": "AC behavior; Starlink rides this AC - ask first"},
    {"id": "river2pro_dc12v", "device": "river2pro", "function": "DC 12V (car)", "on": "river2pro-dc-on.sh", "off": "river2pro-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "UNTESTED post-fix", "verify": "readback changes to the wanted value", "note": ""},
    {"id": "river2pro_energy_backup", "device": "river2pro", "function": "Energy backup", "on": "river2pro-energy-backup-on.sh",
     "off": "river2pro-energy-backup-off.sh", "field": "energy_backup", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes to the wanted value", "note": "pre-fix: FAIL AssertionError"},
]

# Reads (no state change). AC fields may be null/default in the 2 s read window - treat null as "unmeasured".
READS = [
    {"id": "delta2_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh"},
    {"id": "river2pro_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh"},
]

# ====================================================
# FULL BLANK TEMPLATE (reference — all keys labeled)
# Copy into the correct section list above; delete keys that section does not use.
# ------------------------------------------------------------------------------
# {
#     "id": "unique_snake_case_name",          # required — unique across all sections
#     "enabled": False,                         # required — True to run
#     "priority": 2,                            # ON_BOOT only — lower runs first
#     "description": "Plain words: what / why.",# required — human label
#     "interval_sec": 60,                       # EVERY_SECONDS only
#     "only_at_minutes": [],                    # EVERY_MINUTE only — [] = all minutes
#     "only_at_hours": [],                      # EVERY_HOUR only — [] = all hours 0-23
#     "at_times": ["13:00"],                    # ON_AT only — local HH:MM list (HST)
#     "builtin": "",                            # "" or self_process|tunnel_start|heartbeat|http_ping
#     "command": "/home/rootrecord/script.sh",  # shell via bash -lc; "" if builtin set
#     "process": "",                            # ON_BOOT self_process — main process path
#     "terminal": "",                           # ON_BOOT self_process — window title
#     "watch": "",                              # ON_BOOT self_process — watch script path
#     "public_host": "",                        # ON_BOOT tunnel_start
#     "token_file": "",                         # ON_BOOT tunnel_start
#     "cloudflared_bin": "",                    # ON_BOOT tunnel_start
#     "local_service": "",                      # ON_BOOT tunnel_start — origin URL
#     "timeout_sec": 120,                       # kill command / tunnel wait seconds
#     "cwd": "/home/rootrecord",                # working directory; "" = poller cwd
#     "env": {"EXAMPLE": "value"},              # extra env vars for command only
# },
# ====================================================
# {
#     "id": "unique_snake_case_name",          # required — unique across all sections
#     "enabled": False,                         # required — True to run
#     "priority": 2,                            # ON_BOOT only — lower runs first
#     "description": "Plain words: what / why.",# required — human label
#     "interval_sec": 60,                       # EVERY_SECONDS only
#     "only_at_minutes": [],                    # EVERY_MINUTE only — [] = all minutes
#     "only_at_hours": [],                      # EVERY_HOUR only — [] = all hours 0-23
#     "at_times": ["13:00"],                    # ON_AT only — local HH:MM list (HST)
#     "builtin": "",                            # "" or self_process|tunnel_start|heartbeat|http_ping
#     "command": "/home/rootrecord/script.sh",  # shell via bash -lc; "" if builtin set
#     "process": "",                            # ON_BOOT self_process — main process path
#     "terminal": "",                           # ON_BOOT self_process — window title
#     "watch": "",                              # ON_BOOT self_process — watch script path
#     "public_host": "",                        # ON_BOOT tunnel_start
#     "token_file": "",                         # ON_BOOT tunnel_start
#     "cloudflared_bin": "",                    # ON_BOOT tunnel_start
#     "local_service": "",                      # ON_BOOT tunnel_start — origin URL
#     "timeout_sec": 120,                       # kill command / tunnel wait seconds
#     "cwd": "/home/rootrecord",                # working directory; "" = poller cwd
#     "env": {"EXAMPLE": "value"},              # extra env vars for command only
# },

