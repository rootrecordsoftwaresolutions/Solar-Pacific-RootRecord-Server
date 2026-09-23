# energy lib/vendor

## eflib
Copied from github-history ecoflow-ble-poller `store/vendor/eflib` (no secrets, no `__pycache__`).
Import via `lib/vendor` on PYTHONPATH (`lib/py` sets it; or `ENERGY_EFLIB_PATH`).

## Deps (light venv)
Owner python: `~/.ollama/skills/energy/.venv` via `lib/py` (override `ENERGY_PYTHON`).
Packages: bleak + thin eflib runtime (ecdsa, bleak-retry-connector, pycryptodome, protobuf, aiohttp).
No heavy stacks (no Home Assistant / numpy / etc).
