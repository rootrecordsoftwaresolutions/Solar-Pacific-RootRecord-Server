# ==============================================================================
# # INFO — MUST HAVE (future agents / operators)
# ------------------------------------------------------------------------------
# Ctrl-C in the poller window, or running stop-poller-stack.sh / the home
# shortcut "stop", MUST kill EVERY related process:
#   - rootserver_poller.py
#   - cloudflared (tunnel child)
#   - systemd user unit: rr-rootserver-poller.service
# Leaving an orphan tunnel or poller is a bug. Do not "fix only" the window.
# Restart shortcut: /home/rootrecord/rootserver-poller
# ==============================================================================
#
# HOW TO ADD A JOB (no AI required)
#   1) Copy the blank TEMPLATE block from the matching section below.
#   2) Paste it inside that section's list (keep the commas).
#   3) Set enabled=True, fill id / description / schedule fields / command.
#   4) Keep the same key order and quoting style as the examples.
#   5) Restart: /home/rootrecord/rootserver-poller restart
#
# ACTION TYPES
#   command  — shell string run with bash -lc (recommended for one-shot scripts)
#   builtin  — engine built-in: "heartbeat" | "http_ping"
#   (leave command="" and builtin="" only while drafting a disabled template)
#
# SCHEDULE SECTIONS
#   EVERY_SECONDS  — fires every interval_sec (float/int seconds)
#   EVERY_MINUTE   — fires once per wall-clock minute (when the minute changes)
#   EVERY_HOUR     — fires once per wall-clock hour (when the hour changes)
#   ONCE_AT_START  — fires one time after tunnel READY (startup scripts)
# ==============================================================================

# ------------------------------------------------------------------------------
# SHARED DEFAULTS (optional overrides per job still win)
# ------------------------------------------------------------------------------
DEFAULTS = {
    "enabled": False,
    "timeout_sec": 120,
    "cwd": "",
    "env": {},
}

# ==============================================================================
# SECTION: EVERY_SECONDS
# Fires on a repeating interval. interval_sec is required.
# ==============================================================================
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
    # --- TEMPLATE (every X seconds) — copy from here -------------------------------
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
    # --- end TEMPLATE --------------------------------------------------------------
]

# ==============================================================================
# SECTION: EVERY_MINUTE
# Fires once when the wall-clock minute changes (second ~0).
# Optional: only_at_minutes = [0, 15, 30, 45]  (empty list = every minute)
# ==============================================================================
EVERY_MINUTE = [
    # --- TEMPLATE (every minute / selected minutes) — copy from here --------------
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
    # --- end TEMPLATE --------------------------------------------------------------
]

# ==============================================================================
# SECTION: EVERY_HOUR
# Fires once when the wall-clock hour changes (minute 0).
# Optional: only_at_hours = [0, 6, 12, 18]  (empty list = every hour, 0–23)
# ==============================================================================
EVERY_HOUR = [
    # --- TEMPLATE (every hour / selected hours) — copy from here ------------------
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
    # --- end TEMPLATE --------------------------------------------------------------
]

# ==============================================================================
# SECTION: ONCE_AT_START
# One-time scripts after tunnel READY (and before / with first heartbeat cycle).
# Use for boot hooks you want to paste in and leave enabled.
# ==============================================================================
ONCE_AT_START = [
    # --- TEMPLATE (run once at start) — copy from here ----------------------------
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
    # --- end TEMPLATE --------------------------------------------------------------
]

# ==============================================================================
# FULL BLANK TEMPLATE (reference — all keys labeled)
# Copy into the correct section list above; delete keys that section does not use.
# ------------------------------------------------------------------------------
# {
#     "id": "unique_snake_case_name",          # required — unique across all sections
#     "enabled": False,                         # required — True to run
#     "description": "Plain words: what / why.",# required — human label
#     "interval_sec": 60,                       # EVERY_SECONDS only
#     "only_at_minutes": [],                    # EVERY_MINUTE only — [] = all minutes
#     "only_at_hours": [],                      # EVERY_HOUR only — [] = all hours 0-23
#     "builtin": "",                            # "" or "heartbeat" | "http_ping"
#     "command": "/home/rootrecord/script.sh",  # shell via bash -lc; "" if builtin set
#     "timeout_sec": 120,                       # kill command after N seconds
#     "cwd": "/home/rootrecord",                # working directory; "" = poller cwd
#     "env": {"EXAMPLE": "value"},              # extra env vars for command only
# },
# ==============================================================================
