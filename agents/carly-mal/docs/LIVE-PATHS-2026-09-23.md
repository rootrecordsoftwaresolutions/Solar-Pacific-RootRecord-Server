# Carly Mal — LIVE PATHS (2026-09-23 HST)
# Owner: Carly Mal. Jobs.py-clean. No secrets. No invented watts.

## SECTION: DATA
- Measured energy: `/home/rootrecord/Database/ENERGY/{soc,watts,samples}/`
- Contract files: `soc/{delta2|river2pro}-last.json`, `watts/…-last.json`, `samples/read-…json`
- Empty / missing file = **No data** / **Waiting** (River until seen)
- NETWORK stays off watts — never `Database/NETWORK/metrics/ecoflow`

## SECTION: SCRIPTS / BLE
- Action scripts + BLE: `~/.ollama/skills/energy/` → **Bruce**
- Carly seals honesty; does not toggle ports
- Delta 2 AC on/off: **fail-closed** while Starlink is on AC

## SECTION: VISITOR
- `/home` = core landing (Vercel stage)
- `/home/status` = the one status/energy board (AWS globe iframe bg only)
- No visitor top-level `/energy`
- `/api/energy` reads measured `*-last.json` only — never `master-key.env`
- Desk smoke ≠ public ship until ENERGY reaches hosted runtime + Carly re-seal

## SECTION: SECRETS
- Central only: `/home/rootrecord/master/master-key.env`
- Retired: `RootRecord/Ava-Core/.env` and any Ava-Core folder name for secrets
- Never paste values in room, git, or handoff

## SECTION: PORT-SMOKE HONESTY
- Report: `Database/ENERGY/samples/PORT-SMOKE-2026-09-23.md` (+ handoff twin)
- Reads OK; most toggles FAIL AssertionError at ~3% SOC
- Public copy: do **not** claim ports verified green; say Waiting / measured-only

## SECTION: MEMBERSHIPS (carry)
- Proposal-only until Alexander approves; bak first; never paste Stripe secrets
