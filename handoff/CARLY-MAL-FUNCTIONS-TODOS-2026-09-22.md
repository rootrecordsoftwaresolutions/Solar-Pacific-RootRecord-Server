# Carly Mal — Functions, Improvements & To-Dos

**Date:** 2026-09-22 HST  
**Agent:** Carly Mal (RootRecord Gamma / AppSec Seal)  
**Lanes:** AppSec ship-seal + Memberships (Stripe / D1 / tiers) — Memberships Worker dismissed  
**Mode:** Proposal-only for host/cloud edits until Alexander approves; dated bak before OmniBook touch; never paste secrets; **never stack LLM generations** (single-flight)

---

## 1. Functions (current)

### AppSec Seal
- Final security word on the panel (Ava designs/PR → Bruce ops → **Carly seals**).
- Zero-trust / least privilege; treat elegant diagrams and “just this once” as threats until proven.
- Block secret leakage (git, chat, Telegram, public Kīlauea); no tokens/.env in copy.
- Seal persona/prompt parity diffs before Telegram live (bak → Carly seal → Bruce NPU/RAM veto).
- Energy desk honesty: DESK_LIVE measured facts only — else **No data** (never invent SOC/W).
- Non-owner `/approve` → **No**.
- Local Ollama voices: `carly` / `carly-appsec` / `carly-energy` / `carly-telegram` (dolphin-mistral) via plumbing `run-ollama` / `single-flight`.
- Telegram `@carlymal_bot` via `skills/coms/telegram` council relay (**staged**); Advisor room ≠ auto-wake from Telegram.
- Coding in coding lane unless operator says otherwise.

### Memberships (owned 2026-09-22)
- RootRecord / RootMC Stripe, D1 entitlements, tiers.
- Live edge (re-verify before acting): `rootrecord.cloud/billing` → Stripe Payment Link; `rootrecord-api-account` `/api/auth/me`; webhook writes historically on Worker `rootrecord-license` → D1 `root-record` `user_accounts`.
- RootMC separate webhook `api.rootmc.info/v1/stripe/webhook` + vouchers/plugin.
- Tiers: Free; Monthly ~$4.99 → `pro_unlocked` when `active|trialing`; Lifetime ~$150 → `pro_unlocked` + `life_member` (sticky MAX).
- Desk skills archived under `~/.ollama/old skills/` (stripe-poll, account-import, cloudflare-workers, credentials.env) — **not** in active tree post-rebuild.
- Prior doc (pre-rebuild): `/workspace/reports/Memberships-Worker-Full-Doc-2026-09-18.md` — treat as foundation; re-verify live before changes.

### Walls
| Lane | Owner |
|------|--------|
| AppSec + Stripe/tier facts | **Carly Mal** |
| Council mediate (one relay, single-flight) | **Bruce Monitor** |
| Final public wording | **Ava Ivy** |
| AWS / rr-aws / datapacks / radio | **US-MAINLAND-SERVER** |

---

## 2. Findings after rebuild

1. Active skills tree is coms/plumbing/website/us-mainland — **membership desk not re-homed**; archive only.
2. Advisor Carly KB lives on box: `/workspace/carly-identity/kb/CARLY-KNOWLEDGEBASE.md` — OmniBook `carly-mal` / `energy-report` live trees still **Waiting** full verify from this lane.
3. Persona parity Telegram vs Advisor room still pending (process locked: bak → seal → Bruce veto → desk sample).
4. `COUNCIL_CHAT_ID` / live poll: staged; confirm before any poll change (Bruce mediates).
5. Hard rule: **one LLM generation at a time** on OmniBook — refuse busy if lock held.

---

## 3. Improvements (priority order)

| # | Improvement | Why |
|---|-------------|-----|
| P0 | Enforce single-flight on every Carly voice entry (`carly*`) — refuse busy, never parallel with council/desk | Operator hard rule; stacking breaks OmniBook |
| P0 | Re-verify live Stripe/D1 edge (billing link, webhook Worker, `/api/auth/me`) before any membership edit | Archive docs are pre-rebuild; inventing tiers is forbidden |
| P1 | Re-home memberships ops into active skills (or explicit proposal for where Worker/desk lives) | Lane owned but desk archived — gap |
| P1 | Persona parity draft for `carly-telegram` vs Advisor Carly — bak → seal → Bruce veto | Local LLM must feel like this room |
| P1 | Wire/confirm `DESK_LIVE` for energy desk stills; No data without measured desk | Honesty gate |
| P2 | Secret hygiene audit of archived `credentials.env` path + CF Workers (names only, no paste) | AppSec + memberships overlap |
| P2 | Sync OmniBook Carly agent packet / KB beside Ava’s rebuild when host paths available | Continuity after wipe |

---

## 4. To-dos

- [ ] Confirm single-flight lock path used by `carly*` scripts (`rootrecord-inference.lock` / `single-flight.sh`) — refuse if busy
- [ ] Live read (proposal-only first): billing Payment Link target, `rootrecord-license` webhook health, D1 tier sample counts — **no invented MRR**
- [ ] Draft proposal: where memberships desk should live in active skills tree post-rebuild
- [ ] Draft `carly-telegram` persona parity diff vs profile/KB; queue bak → seal → Bruce veto
- [ ] Verify energy desk path (DESK_LIVE_FILE / measured EcoFlow facts) with Bruce — else stay No data
- [ ] Keep walls: never invent AWS; pull @US-MAINLAND-SERVER; never invent public copy past Ava without seal
- [ ] Update Carly KB team map (remove retired Council Ops / Memberships Worker agents) — partially done 2026-09-22

---

## 5. Will not do

- Stack LLM generations
- Paste Stripe/CF tokens or `.env` values into chat/git/Telegram
- Call parity “live” without bak + seal + Bruce NPU/RAM veto + honest desk sample
- Invent Stripe tiers, MRR, or AWS datapack/radio facts
- Auto-wake Advisor from Telegram

— Carly Mal
