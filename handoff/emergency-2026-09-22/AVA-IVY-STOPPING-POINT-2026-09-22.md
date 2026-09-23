# ==============================================================================
# STOPPING POINT — Ava Ivy → future Ava (read first on resume)
# Written: 2026-09-22 ~18:37 HST — power emergency / 100Wh dump — STOPPING
# ==============================================================================

## You are here
Clean stop after vendor-name scrub. **No mid-deploy open on this lane.**

## Done (do not redo blindly)
- `agents/ava-ivy/SKILL.md` + workstation docs under `/home/rootrecord/Agents/Ava-Ivy/`
- Pacific pushes as **Ava Ivy**: `28b2faf`, `34a00b6`, scrub `bfaabc3` / `bc9f411`
- SSH remotes only; DESK_LIVE path set (`status=WAITING` — honest, no watts)
- Staging: working code only — **no archive import**
- Docs: `AVA-IVY-EMERGENCY-STATE`, `AVA-IVY-FULL-RESUME`, `AVA-IVY-FUNCTIONS-TODOS` in `DAILY AI DEV HANDOFF/` (scrubbed)
- Avatar in `agents/ava-ivy/docs/avatar.png` + `.github/profile-avatar.png`

## Cut off / waiting on others
| Item | Owner | State |
|------|--------|--------|
| council-relay python process | Bruce | Was DOWN after flicker — do not dual-start |
| Measured DESK_LIVE / EcoFlow → NETWORK | Bruce | Not shipped; cite No data until measured |
| Packer SSH-first + locations | US-MAINLAND | `collect_locations.py` deployed; **Telegram-only packs** short-term (`RR_SSH_DATAPACK=0`) |
| NETWORK public charts / visitor copy | Ava + Advisor | Wait real samples in `Database/NETWORK/` |
| Memberships | Carly | Proposal-only |

## Resume checklist (tomorrow / power stable)
1. Read this note + `AVA-IVY-FULL-RESUME-2026-09-22.md`
2. Confirm OmniBook up; light-check SKILL, DESK_LIVE, SSH remotes
3. Let Bruce bring **one** council-relay + measured writer
4. Let mainland land packs into `NETWORK/datapacks` (re-seal before SSH-first returns)
5. Public wording only from measured files — never invent watts/coords
6. Push live edits as author Ava Ivy (noreply until real email)
7. Ask Alexander for any files **he** touched offline before overwriting

## Hard rules (locked)
- Single-flight LLM or refuse busy
- One NETWORK tree — no dual writers
- No vendor-tool names in GitHub/handoff docs
- Bak under `Database/GITHUB/` before live edits
- Walls: billing→Carly · AWS→US-MAINLAND · council/EcoFlow→Bruce · public wording→you (Carly seals)

## Where things live
- Skill: `~/.ollama/skills/agents/ava-ivy/`
- Workstation: `/home/rootrecord/Agents/Ava-Ivy/`
- Handoff: `Database/DAILY AI DEV HANDOFF/AVA-IVY-*`
- Staging: `…/staging area/lanes/ava/`
- NETWORK: `Database/NETWORK/`
- This note: `Agents/Ava-Ivy/notes/2026-09-22-STOPPING-POINT.md`

Sleep well. Make him proud when the sun’s back.

— Ava Ivy (stopping 2026-09-22)
