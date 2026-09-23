# US-MAINLAND-SERVER — Functions, Improvements, To-Dos

**Agent:** US-MAINLAND-SERVER (AWS Worker)  
**Date:** 2026-09-22 16:45:07 HST  
**Owner lane:** RootRecord US mainland AWS (rr-aws) and how it feeds OmniBook  
**Saved:** `/home/rootrecord/Database/DAILY AI DEV HANDOFF/US-MAINLAND-SERVER-FUNCTIONS-TODOS-2026-09-22.md`

---

## 1. Specific functions (what I own)

1. **Always-on AWS collector** — EC2 `rr-aws` (`ssh.rootrecord.cloud` / Host `rr-aws`): hazard pollers (`rr-weather`, `rr-earthquake`, `rr-radar`, `rr-hurricane`, `rr-noaa`, `rr-kilauea`, `rr-solar-cam`, …), chat/audio recv, drop-ins.
2. **Radio stack** — Icecast + `rr-radio` + `rr-cloudflared` (and related); localhost bind, tunnel for public path.
3. **Network globe** — `network-globe` + `rr-cloudflared-globe` on the same host when present.
4. **Datapacks** — `rr-packer`: zip `work/` → send → wipe. Today: Telegram primary. Target ops: **SSH first** into OmniBook `/home/rootrecord/Database/US-MAINLAND-SERVER/`, Telegram only if SSH fails (every ~5 min).
5. **Admin / deploy** — SSH/SFTP only for code, units, packages; bak dated before every edit; revert to last known-good if debug stalls.
6. **Operator docs / worklog** — Status reports and append-only worklog under `DAILY AI DEV HANDOFF/US-MAINLAND-SERVER/`.
7. **Walls** — Live AWS / datapack / radio facts only. Stripe/tiers → Carly Mal. Council mediate → Bruce Monitor. Public wording → Ava Ivy. Never invent billing or desk EcoFlow watts. Never stack LLM generations (single-flight on OmniBook).

**Not my lane:** EcoFlow BLE, AVA Console inference, Telegram council UX, Stripe/D1 memberships.

---

## 2. Current understanding (post-rebuild, measured)

| Item | Status |
|------|--------|
| SSH | `ssh rr-aws` via Cloudflare Access hostname `ssh.rootrecord.cloud` (stable; raw IP fallback `rr-aws-ip`) |
| Instance | t3.micro, us-east-2; live collector + radio + packer + globe |
| Desk skill `rootrecord-aws` | **Missing** from active `~/.ollama/skills/` (archived under old skills / github-history / aws-sync mirror) |
| Packer wipe | Wipes `work/` + out zips **after successful Telegram send**; last wipe was OK earlier today |
| Voice-played | `radio/voice-played/*Current*.wav` were **not** wiped by packer → disk growth; cleaned 2026-09-22 |
| Disk | After cleanup: ~88% (~825M free); still tight on 6.7G root |
| Desk ingest | `rr-ingest` unit still points at missing `rootrecord-aws` skill path (broken) |
| Telegram extract | Still under `aws-sync/scripts/telegram_extract.py` → `Database/telegram` (not yet `US-MAINLAND-SERVER/DATA PACKETS`) |
| `rootserver.rootrecord.cloud` | Live HTTP poller tunnel (:8799); **SSH not exposed** — AWS cannot scp-push yet |
| Live snap (2026-09-22 16:45:07 HST) | SSH_OK=yes; disk: /dev/root       6.7G  5.8G  833M  88% /; rr-packer: active; last-wipe: {   "at": "2026-09-22T16:40:06.881521-10:00",   "ok": true }  |

---

## 3. Improvements (priority order)

1. **SSH-first datapath** — Pack → SCP/rsync to `Database/US-MAINLAND-SERVER/DATA PACKETS/` first; Telegram fallback only on SSH failure; same cadence (~5 min). Needs either desk pull (works now via `ssh rr-aws`) and/or Cloudflare Access SSH on rootserver.
2. **Wipe completeness** — Extend packer wipe (or radio cleanup) to clear sent/played `Current*` voice clips and app `.log` rotation so disk never climbs back to ENOSPC.
3. **Restore / re-home desk AWS skill** — Replace broken `rr-ingest` with a thin skill or aws-sync path that lands packs in `US-MAINLAND-SERVER/` and does not require the deleted tree.
4. **Disk headroom** — Rotate logs, bound `hawaii.ndjson` / media growth, consider modest EBS bump if collectors stay on t3.micro.
5. **Named radio tunnel** — Move off ephemeral trycloudflare if still in use; keep secrets out of chat.
6. **Worklog discipline** — Keep appending to `US-MAINLAND-SERVER/US-MAINLAND-WORKLOG.md`; use template for new days.
7. **Ops docs** — Keep `How to connect to US-MAINLAND-SERVER.md` and status reports current after every material change.

---

## 4. To-dos (actionable)

- [ ] Confirm with Alexander: desk-pull SSH-first now vs add Access SSH on `rootserver.rootrecord.cloud` (or both).
- [ ] Bak + patch `packer.py`: try SSH send → else Telegram; wipe only after success; also prune `voice-played` Current clips / ensure logrotate.
- [ ] Change pack cadence to every 5 minutes if confirmed (today slots are :10/:25/:40/:55).
- [ ] Desk: install pull/ingest timer writing into `Database/US-MAINLAND-SERVER/DATA PACKETS/`; retire broken `rr-ingest` path or retarget it.
- [ ] Verify Telegram still works as fallback when SSH path fails (token/chat stay on host secrets — never paste).
- [ ] Re-check disk after next two pack cycles; watch journal ENOSPC.
- [ ] Update `rootrecord-aws-ops` Grok skill: datapath SSH-first + Telegram fallback (overrides old “Telegram only” rule once live).
- [ ] Optional: named radio Cloudflare hostname; document in connect/status handoff.

---

## 5. Standing rules (unchanged)

- Dated backup before every AWS/desk-deploy edit.
- Full revert to last known-good if debugging stalls.
- No local→AWS data seed; AWS collects live.
- Soft-park overlapping AVA skills with OFFLOADED — never delete skill trees.
- EcoFlow stays on OmniBook.
- Single-flight: never stack LLM generations with council/desk inference.

---

## 6. Handoff pointers

- Worklog: `DAILY AI DEV HANDOFF/US-MAINLAND-SERVER/US-MAINLAND-WORKLOG.md`
- Template: `…/US-MAINLAND-WORKLOG-TEMPLATE.md`
- Connect: `DAILY AI DEV HANDOFF/How to connect to US-MAINLAND-SERVER.md`
- Incoming SSH target: `/home/rootrecord/Database/US-MAINLAND-SERVER/`
