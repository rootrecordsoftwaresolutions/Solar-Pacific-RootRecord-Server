# ==============================================================================
# Deploy format (standing): push → github_sync_all merge → auto full stack reload.
# Internet gate: tunnel + GitHub + Telegram need net; BLE/Ollama/local continue offline.
# ==============================================================================

DEFAULTS = {
    "enabled": False,
    "timeout_sec": 120,
    "cwd": "",
    "env": {},
}

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
        "needs_internet": True,
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
        "needs_internet": True,
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
    return f"flock -w 60 {ECOFLOW_LOCK} bash {ECOFLOW_ACTIONS}/{script}"


TOGGLES = [
    {"id": "delta2_usb", "device": "delta2", "function": "USB ports", "on": "delta2-usb-on.sh", "off": "delta2-usb-off.sh",
     "field": "usb_ports", "protected": False, "status": "PASS 2026-09-23", "verify": "readback", "note": ""},
    {"id": "delta2_dc12v", "device": "delta2", "function": "DC 12V", "on": "delta2-dc-on.sh", "off": "delta2-dc-off.sh",
     "field": "dc_12v_port", "protected": False, "status": "PASS 2026-09-23", "verify": "readback", "note": ""},
    {"id": "delta2_ac", "device": "delta2", "function": "AC outlets", "on": "delta2-ac-on.sh", "off": "delta2-ac-off.sh",
     "field": "ac_ports", "protected": False, "status": "PASS 2026-09-23", "verify": "inverter packets", "note": ""},
]

READS = [
    {"id": "delta2_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/delta2-read.sh"},
    {"id": "river2pro_read", "script": "/home/rootrecord/.ollama/skills/energy/scripts/read/river2pro-read.sh"},
]
