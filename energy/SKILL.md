# energy — EcoFlow desk power (BLE-primary)

Thin skill: **one executable script per EcoFlow action**. Shared helpers live in `lib/`.
Measured samples → `/home/rootrecord/Database/ENERGY/` only (not Network).

## INFO — MUST HAVE

- DESK_LIVE honesty: never invent watts/SOC. Unavailable → `WAITING` / `No data`, exit non-zero.
- Devices: Delta 2 (B2), River 2 Pro (B1); B3 = expansion under B2 (no invented MAC).
- One BLE owner: user unit `ava-ecoflow-ble.service`. Do not dual-start pollers.
- Poll buckets: stubs under `scripts/poll/` — enable after atomic actions prove out.
- Secrets stay in env files; never paste into chat or SKILL.
- SQLite canonical dual-write via `lib/read_runner.py` → `/home/rootrecord/Database/ROOTRECORD/rootrecord.db`.

## HOW TO ADD AN ACTION (no AI required)

1. Copy an existing script under `scripts/actions/` (e.g. `delta2-usb-on.sh`).
2. Rename clearly: `<device>-<port>-<on|off>.sh` or `<device>-read.sh`.
3. Keep thin: call `"$ROOT/lib/py" "$ROOT/lib/action_runner.py"` with `ACTION` args.
4. `chmod +x` the new script.
5. Document one line in `scripts/actions/README.md`.
6. Test dry: honest failure if BLE/eflib/USER_ID down — never fake OK watts.

## HOW TO ADD A DEVICE

1. Edit `config/devices.conf` — copy the **TEMPLATE** under SECTION: BLE DEVICES.
2. Fill model, alias, sn, mac, name, eflib_module (do not invent MAC).
3. Expansion packs: parent section + `[inventory]` only.

## Layout style (standing)

Keep SECTION + TEMPLATE in `config/devices.conf` and operator scripts.
If stripped, restore from git. See `0-master-prompt/prompts/09-file-layout-style.md`.

## Deps (light)

| What | Where |
|------|--------|
| Python (owner) | `lib/py` → `.venv/bin/python` |
| eflib vendor | `lib/vendor/eflib` |
| Env secrets | `/home/rootrecord/master/master-key.env` |
| Config | `config/devices.conf` |
| Samples | `/home/rootrecord/Database/ENERGY/` |
| SQLite | `/home/rootrecord/Database/ROOTRECORD/rootrecord.db` |

## BLE boot

```bash
systemctl --user daemon-reload
systemctl --user enable --now ava-ecoflow-ble.service
~/.ollama/skills/energy/scripts/ble/ble-status.sh
```

## Real vs stub

- **Live BLE:** requires eflib + bleak + account id. Without them scripts exit non-zero with a clear reason.
- **Do not** dual-start BLE owners while the unit is already running.
