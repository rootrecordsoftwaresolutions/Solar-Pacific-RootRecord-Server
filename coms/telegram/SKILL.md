---
name: telegram
description: >-
  Telegram Bot API: send_message, get_me, get_updates. Token
  AVA_TELEGRAM_BOT_TOKEN in master-key.env. Not AWS rr-chat poller
  (see references/aws-chat-poll.md).
---

# telegram

`scripts/telegram.py` — REST helpers only (same shape as coms/slack|discord).

- `send_message(chat_id, text)` · `get_me()` · `get_updates(offset=None, timeout=20)`

**Out of scope:** `telegram_rooms.py` (Ava persona). **Not this skill:** AWS `chat_poll.py` / rr-chat — `references/aws-chat-poll.md`.
