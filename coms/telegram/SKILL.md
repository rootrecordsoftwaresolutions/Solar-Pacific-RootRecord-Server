---
name: telegram
description: >-
  Telegram helpers + council relay to Ollama ava/bruce/carly. Single-flight
  plumbing. Tokens in secrets — never print.
---

# telegram

| | |
|--|--|
| Config | `config/voices.conf` · `config/relay.conf` |
| Ask | `scripts/ask-voice.sh <voice> '…'` |
| Post | `scripts/post-voice.sh <voice> '…'` |
| Poll | `scripts/council-relay.py` (one process) |
| Status | `scripts/status.sh` |

Set `COUNCIL_CHAT_ID` before live poll. Stop legacy `apps.council` first.
