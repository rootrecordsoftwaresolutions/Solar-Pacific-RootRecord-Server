# ====================================================
# # INFO — MUST HAVE (future agents / operators)
# ------------------------------------------------------------------------------
# Ctrl-C in the poller window, or running stop-poller-stack.sh / the home
# shortcut "stop", MUST kill EVERY related process:
#   - rootserver_poller.py
#   - cloudflared (tunnel child)
#   - systemd user unit: rr-rootserver-poller.service
#   - poller-watch.py (status terminal)
# Leaving an orphan tunnel or poller is a bug. Do not "fix only" the window.
# Restart shortcut: /home/rootrecord/rootserver-poller
# ====================================================
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
#   Then recurring: EVERY_SECONDS / EVERY_MINUTE / EVERY_HOUR.
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
    # --- priority 2: TEMPLATE (on boot) — copy from here -------------------------
    # {
    #     "id": "example_on_boot_p2",
    #     "enabled": False,
    #     "priority": 2,
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
