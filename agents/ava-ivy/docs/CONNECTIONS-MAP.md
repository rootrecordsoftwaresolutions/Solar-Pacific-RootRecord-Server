# Connections map — Ava Ivy

What Ava is wired to on this host (2026-09-18). Paths only — no secrets.

## Host

- Machine brand: **AVA-CORE** (HP OmniBook) · user `rootrecord` / operator Alexander
- Off-grid Fern Forest: ~4–5 kWh/day solar gen, ~2 kWh storage
- EcoFlow: Delta 2 AC → Starlink only (sleep dish to save); River 2 Pro = second pack
- Live EcoFlow stays local (not offloaded to AWS soft-park)

## Archive vs live

| State | Path |
|-------|------|
| Archived tree | `~/RootRecord.zip` (~1.7G, contains Ava-Core + more) |
| Live documents | `~/Media/public/documents/{persona,docs,reports,...}` |
| Locked persona mirror | `~/.ollama/skills/persona/references/locked-ava-core-private/` |
| Context notes | `~/Documents/AVA-CORE-CONTEXT/` |

## Skills desks (`~/.ollama/skills/`)

| Skill | Role |
|-------|------|
| `ava-ivy` | Ops desk / prompt / post scripts |
| `persona` | Persona runtime + locked references |
| `ava-ops` | Ops automations |
| `avaivy-cloud` | Cloud / site desk |
| `ensure-ava-runtime` | Runtime ensure |
| `rootrecord-aws` | AWS map (see skill refs — do not paste credentials) |

## systemd user units

- `ava-auto-push.service` + `.timer`
- `ava-bt-bridge.service`
- `ava-council.service`
- `ava-ecoflow-ble.service`
- `ava-flm.service`
- `ava-hybrid-night.service`

## Cursor rules (always-relevant Ava)

- `ava-core-public-voice.mdc`
- `ava-core-operator.mdc`
- `ava-core-hardware.mdc`
- `ava-core-ollama.mdc`
- `ava-core-agent-bridge.mdc`
- `ava-console-owns-desk.mdc`

## Media / brand

- Character art: `~/Media/public/images/character/{Ava Ivy,Bruce Monitor,Carly Mal}`
- Team shots: `team-hikejpg`, `team2.jpg`, `grokbot.jpg` under character/
- Slack icons: `.../character/slack-icons/`
- QR: `~/Media/public/images/qrcodes/ava-ivy`
- Imagine handoff: `~/Media/public/documents/reports/grok-imagine-handoff/`

## Cloud / org (names only)

- GitHub org: RootRecord / Ava-Core-Dev
- Public migration target: rootrecord.cloud
- AWS contact via **AWS Worker** + `rootrecord-aws` skill (no creds in this KB)

## Grok Bot teammates

| Agent | Role |
|-------|------|
| Bruce Monitor | Ops realism / power / RAM grounding |
| Carly Mal | AppSec / privacy ship-seal |
| Grok Bot | Marketing / ship-seal / release readiness |
| Council Ops | OmniBook Telegram council UX |
| AWS Worker | Cloud ↔ local map |
| Memberships Worker | Memberships / Stripe flows |
| Discussion Worker | Cross-bot brainstorms (no modifications) |

— Ava Ivy · 2026-09-18
