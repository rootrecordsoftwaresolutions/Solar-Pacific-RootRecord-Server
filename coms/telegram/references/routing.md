# Routing (MUST)

| Incoming | Behavior |
|----------|----------|
| @one bot / one name | **Single voice** — that bot token posts |
| DM (private) | Single voice (currently poll bot = Ava until multi-poll designed) |
| Pipeline trigger phrase | **A→B→C→A** serial; each hop `sendMessage` with **that** voice token |
| Bare group chat, no @ | `DEFAULT_SINGLE_VOICE` (ava) — **not** full pipeline |

Triggers live in `relay.conf` → `PIPELINE_TRIGGERS`.

Bot registry: `config/bots.conf` · voices: `config/voices.conf` · council chat: `COUNCIL_CHAT_ID=-1004367256267` (old council).
