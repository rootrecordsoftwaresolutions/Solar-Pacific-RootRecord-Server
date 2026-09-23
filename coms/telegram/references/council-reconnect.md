# Council Telegram reconnect (prep)

Bots: `@ava_ivy_bot` · `@brucemonitor_bot` · `@carlymal_bot`
Tokens: `~/.config/ava-council/secrets.env` and/or `master-key.env` — never print.

## Lane → Ollama model
| Voice | Model |
|---|---|
| ava | `ava-telegram` (fallback `ava`) |
| bruce | `bruce-telegram` (fallback `bruce`) |
| carly | `carly-telegram` (fallback `carly`) |

## Relay home
All outbound protocol helpers: `~/.ollama/skills/coms/`
Council long-poll / UX historically: `council-telegram` + `ava-council.service` (may be archived — rewire here, do not fork tokens into skills git).

## Rules
- Exactly one getUpdates poller.
- Relays speak as the named voice only.
- Grok Bot bridge stays manual.
