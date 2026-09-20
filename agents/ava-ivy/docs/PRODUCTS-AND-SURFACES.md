# Products and surfaces — Ava Ivy

## Products

### Root Record
- Site: https://rootrecord.info/
- Database + data center + ops software
- Apps: Weather Manager, Kīlauea Alerts, Business Manager, Account Hub, token rails
- Ava wiki: https://rootrecord.info/ava/
- Professional volcano / weather briefs stay free of Ava ops internals

### RootMC
- Site: https://rootmc.net/
- Play: play.rootmc.net
- Wiki: https://rootmc.net/wiki/
- API: https://api.rootmc.net/
- Survival network, closed-loop Gold, not pay-to-win
- Homepage Talk to Ava → `POST https://ava.rootmc.net/api/public-chat`

### The Root
- Site: https://merged.rootrecord.info/
- Merged bridge + Ava chat

## Public boards

| Board | URL |
|-------|-----|
| Wiki hub | https://rootrecord.info/ava/ |
| AI context | https://rootrecord.info/ava/context |
| Status / solar | https://rootrecord.info/ava/status |
| Connections | https://rootrecord.info/ava/status/connections |
| Logs | https://rootrecord.info/ava/logs |
| Plugins | https://rootrecord.info/ava/status/plugins |
| Apps | https://rootrecord.info/ava/status/apps |
| Services | https://rootrecord.info/ava/status/services |
| Tunnel | https://ava.rootmc.net/ |

## Public APIs (edge `ava.rootmc.net`)

| Method | Path | Notes |
|--------|------|-------|
| GET | `/api/context` | `ava-core-context/v1` |
| GET | `/api/ava-hours` | Awake/asleep, typical HST hours, bank % |
| POST | `/api/public-chat` | Public Q&A |
| GET | `/api/status` | Ops status JSON |
| GET | `/api/solar` | Solar / bank series |
| GET | `/api/powered-by` | Footer widget metrics |
| GET | `/api/connections` | Gaming / web / apps throughput |

Prefer live `/api/context` over cached snapshots. Do not send secrets in chat payloads.

## Messaging surfaces

| Surface | Role |
|---------|------|
| Slack | Staff digs — professional + lightly flirty with rapport |
| Discord | Community, votes, proposals — snappy |
| Telegram | Ops / council paths (Council Ops worker) |
| Grok Bot | Architecture / PR propose lane with Bruce & Carly |

— Ava Ivy · 2026-09-18
