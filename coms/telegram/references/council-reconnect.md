# Council reconnect

1. `bash scripts/status.sh`
2. Set `COUNCIL_CHAT_ID` in `config/relay.conf`
3. Stop legacy `apps.council` (Alexander approve) — one getUpdates only
4. `python3 scripts/council-relay.py`
5. Smoke: `@bruce status` → No data without DESK_LIVE
6. Grok lane stays manual
