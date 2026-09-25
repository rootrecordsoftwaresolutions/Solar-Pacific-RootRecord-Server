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
#   push to GitHub → github_sync_all merge → schedule-stack-reload full stop/start + window.
#   Do not suggest parallel pollers or default manual restart after ordinary pushes.
#
# Internet gate:
#   needs_internet=True jobs skip while offline; tunnel deferred; ensure_tunnel_online each minute.
#   Local jobs (BLE, Ollama, FLM, heartbeat, worklog) always run.
#
# File layout (standing): keep SECTION banners + TEMPLATE blocks. See
#   0-master-prompt/prompts/09-file-layout-style.md — restore layout if stripped.
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

# ------------------------------------------------------------------------------
# SHARED DEFAULTS (optional overrides per job still win)
# ------------------------------------------------------------------------------
DEFAULTS = {
    "enabled": False,
    "timeout_sec": 120,
    "cwd": "",
    "env": {},
}

# ------------------------------------------------------------------------------
# SHARED EcoFlow dual-read (Delta 2 + River 2 Pro). Succeed if either device OK.
# ------------------------------------------------------------------------------
ECOFLOW_DUAL_READ = (
    "flock -w 90 /tmp/ecoflow-ble.lock bash -c '"
    "ok=0; "
    "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh && ok=1 || true; "
    "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh && ok=1 || true; "
    "exit $((1-ok))'"
)

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
        "description": "Start Cloudflare tunnel when internet is up (deferred if offline).",
        "builtin": "tunnel_start",
        "command": "",
        "public_host": "rootserver.rootrecord.cloud",
        "token_file": "/home/rootrecord/.cloudflared/rootserver.token",
        "cloudflared_bin": "/home/rootrecord/.ollama/skills/automations/bin/cloudflared",
        "local_service": "http://127.0.0.1:8799",
        "timeout_sec": 45,
        "needs_internet": True,
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
        "needs_internet": True,
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
        "needs_internet": True,
        "cwd": "/home/rootrecord/.ollama/skills/coms/telegram",
        "env": {},
    },
    # --- priority 6: a-eyes cam server -------------------------------------------
    {
        "id": "a_eyes_cam_server",
        "enabled": True,
        "priority": 6,
        "description": "Ensure a-eyes cam server (127.0.0.1:8791) is running.",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/a-eyes/scripts/ensure_cam_server.sh",
        "timeout_sec": 30,
        "cwd": "/home/rootrecord/.ollama/skills/a-eyes",
        "env": {},
    },
    # --- priority 7: a-eyes timelapse boot catch-up ------------------------------
    {
        "id": "a_eyes_timelapse_catchup",
        "enabled": True,
        "priority": 7,
        "description": "Compile any completed hour missing a chunk today + run daily render if the window already closed (covers late boot/downtime).",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/a-eyes/scripts/timelapse_catchup.sh",
        "timeout_sec": 600,
        "cwd": "/home/rootrecord/.ollama/skills/a-eyes",
        "env": {},
    },
    # --- priority 8: weather scheduler daemon -------------------------------------
    {
        "id": "weather_poller",
        "enabled": True,
        "priority": 8,
        "description": "Ensure the weather/ scheduler daemon is running -- fetches everything once immediately on start (all tiers, hurricanes included), then keeps its own internal per-tier cadence forever. See weather/scheduler/run_cycle.py.",
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/automations/scripts/ensure-weather-poller.sh",
        "timeout_sec": 30,
        "needs_internet": False,
        "cwd": "/home/rootrecord/.ollama/skills/weather",
        "env": {},
    },
    # --- TEMPLATE (on boot) — copy from here -------------------------------------
    # {
    #     "id": "example_on_boot_p3",
    #     "enabled": False,
    #     "priority": 3,
    #     "description": "One-line plain description of what this job does.",
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
    # --- first EcoFlow sample after boot (SQLite dual-write + legacy JSON) --------
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
    {
        "id": "heartbeat",
        "enabled": True,
        "description": "ENERGY snapshot once per minute (last sample / 1m).",
        "interval_sec": 60,
        "builtin": "heartbeat",
        "command": "",
        "timeout_sec": 5,
        "cwd": "",
        "env": {},
    },

    {
        "id": "ecoflow_read_cycle",
        "enabled": True,
        "description": "Leap-frog: Delta2 / River2Pro alternate; API fallback when BLE out of range.",
        "interval_sec": 15,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/energy/scripts/read/leapfrog-read.sh",
        "timeout_sec": 180,
        "cwd": "/home/rootrecord/.ollama/skills/energy",
        "env": {},
    },

    {
        "id": "sys_stats_cycle",
        "enabled": True,
        "description": "Host CPU/load/mem → Database/SYSTEM; same 6s cadence optional — keep 15min-aligned via only_at if preferred.",
        "interval_sec": 5,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/system-stats/scripts/sys-sample.sh",
        "timeout_sec": 60,
        "cwd": "/home/rootrecord/.ollama/skills/system-stats",
        "env": {},
    },

    # --- live job: desk heartbeat (do not remove; disable only if intentional) ---

    # --- github autopush: one check-stage-commit-push cycle ---------------------
    {
        "id": "github_sync_all",
        "enabled": True,
        "description": "Push skills + website + mainland; skills merge arms auto stack reload.",
        "interval_sec": 300,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/github/scripts/sync-all.sh",
        "timeout_sec": 300,
        "needs_internet": True,
        "cwd": "/home/rootrecord/.ollama/skills/github",
        "env": {},
    },
    # --- worklog: one scan per cycle (NOT the forever poller — that times out) ---
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
    # --- a-eyes: periodic 4-channel frame grab into Database (1s = PERF TEST) ---
    {
        "id": "a_eyes_frame_grab",
        "enabled": True,
        "description": "Grab ch1-4 stills, save to /home/rootrecord/Database/A-EYES/frames/.",
        "interval_sec": 1,
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/a-eyes/scripts/grab_all.sh",
        "timeout_sec": 120,
        "cwd": "/home/rootrecord/.ollama/skills/a-eyes",
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
    # --- internet gate: start Cloudflare when link is up; wait if offline ---------
    {
        "id": "ensure_tunnel_online",
        "enabled": True,
        "description": "If internet is up and tunnel is down, start Cloudflare; if offline, wait ~60s.",
        "only_at_minutes": [],
        "builtin": "ensure_tunnel_online",
        "command": "",
        "timeout_sec": 90,
        "cwd": "",
        "env": {},
    },
    # --- EcoFlow dual-write read (SQLite canonical + legacy JSON last-files) -----
    # BLE sessions ~20–40s each; serialize with flock. Minutes 0/15/30/45.


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
    # --- a-eyes timelapse: compile the hour that just ended -----------------------
    {
        "id": "a_eyes_timelapse_hourly_compile",
        "enabled": True,
        "description": "Compile the previous hour's ch1 frames into video_chunks/hour_HH.mp4, then archive those frames. No-op outside the 05:00-22:00 capture window.",
        "only_at_hours": [],
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/a-eyes/scripts/timelapse_hourly.sh",
        "timeout_sec": 600,
        "cwd": "/home/rootrecord/.ollama/skills/a-eyes",
        "env": {},
    },
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
# ====================================================
ON_AT = [
    # --- a-eyes timelapse: end-of-day master render + gif -------------------------
    {
        "id": "a_eyes_timelapse_daily_render",
        "enabled": True,
        "description": "Stitch today's hour_HH.mp4 chunks into master_stitched_timelapse.mp4 and export optimized_web_timelapse.gif.",
        "at_times": ["22:01"],
        "builtin": "",
        "command": "bash /home/rootrecord/.ollama/skills/a-eyes/scripts/timelapse_daily.sh",
        "timeout_sec": 900,
        "cwd": "/home/rootrecord/.ollama/skills/a-eyes",
        "env": {},
    },
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
# NOT read by the poller (scheduler only reads ON_BOOT / ONCE_AT_START / EVERY_* / ON_AT).
# To SCHEDULE one: copy into ON_AT (or EVERY_*), set enabled=True + at_times.
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
     "verify": "readback (PD heartbeat = real measurement)", "note": "USB-C often feeds River / OmniBook — check loads before OFF"},
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
     "verify": "readback changes", "note": ""},
    {"id": "delta2_grid_bypass", "device": "delta2", "function": "Grid bypass", "on": "delta2-grid-bypass-on.sh",
     "off": "delta2-grid-bypass-off.sh", "field": "disable_grid_bypass", "protected": False, "status": "UNTESTED post-fix",
     "verify": "readback changes", "note": "confirm on/off meaning in wrapper before scheduling"},
    {"id": "river2pro_ac", "device": "river2pro", "function": "AC outlets", "on": "river2pro-ac-on.sh", "off": "river2pro-ac-off.sh",
     "field": "ac_ports", "protected": False, "status": "UNTESTED post-fix",
     "verify": "ON = inverter packets + ac_ports True; OFF = fresh connection", "note": ""},
    {"id": "river2pro_dc12v", "device": "river2pro", "function": "DC 12V (car)", "on": "river2pro-dc-on.sh", "off": "river2pro-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "UNTESTED post-fix", "verify": "readback changes", "note": ""},
]

READS = [
    {"id": "delta2_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh"},
    {"id": "river2pro_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh"},
]

# ====================================================
# FULL BLANK TEMPLATE (reference — all keys labeled)
# ====================================================
# {
#     "id": "example_job_id",
#     "enabled": False,
#     "priority": 2,                            # ON_BOOT only — lower runs first
#     "description": "One-line plain description.",
#     "interval_sec": 60,                       # EVERY_SECONDS only
#     "only_at_minutes": [],                    # EVERY_MINUTE only — [] = all minutes
#     "only_at_hours": [],                      # EVERY_HOUR only
#     "at_times": ["13:00"],                    # ON_AT only
#     "builtin": "",                            # or heartbeat / tunnel_start / ensure_tunnel_online / self_process
#     "command": "/home/rootrecord/path/to/script.sh",
#     "timeout_sec": 120,
#     "needs_internet": False,                  # True = skip while offline
#     "cwd": "/home/rootrecord",
#     "env": {},
# },
