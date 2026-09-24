# energy — EcoFlow desk power (BLE-primary)

Thin skill: **one executable script per EcoFlow action**. Shared helpers live in `lib/`.
Measured samples → `/home/rootrecord/Database/ENERGY/` only (not Network).

## INFO — MUST HAVE

- DESK_LIVE honesty: never invent watts/SOC. Unavailable → `WAITING` / `No data`, exit non-zero.
- Devices: Delta 2 (unrestricted for testing), River 2 Pro (AC feeds Starlink as of 2026-09-23; laptop AC + car DC).
- One BLE owner: user unit `ava-ecoflow-ble.service`. Do not dual-start pollers.
- Poll buckets (1/5/15/30/60/daily): **stubs only** under `scripts/poll/` — enable after atomic actions prove out.
- Secrets stay in env files; never paste into chat or SKILL.
- `AVA_ECOFLOW_USER_ID` must be supplied by operator in `/home/rootrecord/master/master-key.env` (placeholder only if missing — never invent).

## HOW TO ADD AN ACTION (no AI required)

1. Copy an existing script under `scripts/actions/` (e.g. `delta2-usb-on.sh`).
2. Rename clearly: `<device>-<port>-<on|off>.sh` or `<device>-read.sh`.
3. Keep thin: call `"$ROOT/lib/py" "$ROOT/lib/action_runner.py"` with `ACTION` args (`--device` / `--method` / `--want`).
4. `chmod +x` the new script.
5. Document one line in `scripts/actions/README.md`.
6. Test dry: run script; expect honest failure if BLE/eflib/USER_ID down — never fake OK watts.

## Deps (light)

| What | Where |
|------|--------|
| Python (owner) | `lib/py` → `.venv/bin/python` (override: `ENERGY_PYTHON`) |
| venv | `~/.ollama/skills/energy/.venv` — bleak + light eflib runtime (ecdsa, bleak-retry-connector, pycryptodome, protobuf, aiohttp) |
| eflib vendor | `lib/vendor/eflib` (PYTHONPATH via `lib/py` / `ENERGY_EFLIB_PATH`) |
| Env secrets | `/home/rootrecord/master/master-key.env` (mode 600) — operator fills `AVA_ECOFLOW_USER_ID` |

## Paths

| What | Where |
|------|--------|
| Skill | `~/.ollama/skills/energy/` |
| Actions | `scripts/actions/` |
| BLE | `scripts/ble/` |
| Boot notes | `scripts/boot/` |
| Config | `config/devices.conf` |
| Samples | `/home/rootrecord/Database/ENERGY/` |
| BLE log | `~/.ollama/skills/logs/store/ava-ecoflow-ble.log` |
| Inventory | `/home/rootrecord/Database/DAILY AI DEV HANDOFF/ENERGY-ECOFLOW-ACTION-INVENTORY-2026-09-23.md` |

## BLE boot

```bash
systemctl --user daemon-reload
systemctl --user enable --now ava-ecoflow-ble.service
~/.ollama/skills/energy/scripts/ble/ble-status.sh
# optional 1s log watch (foreground):
~/.ollama/skills/energy/scripts/ble/ble-log-watch.sh
```

## Real vs stub

- **Real structure:** action scripts + shared runner + BLE owner/log-watch + systemd unit wiring.
- **Live BLE control:** requires `eflib` + `bleak` (via `lib/py` / `.venv`) and `AVA_ECOFLOW_USER_ID`. Without them scripts exit non-zero with a clear reason — never fake success.
- **Do not** enable aggressive polling or dual-start BLE owners while the unit is already running.
