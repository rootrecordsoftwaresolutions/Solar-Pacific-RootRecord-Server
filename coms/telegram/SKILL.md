---
name: telegram
description: Telegram Bot API functions — send_message, get_me, get_updates. Token from /home/rootrecord/master/master-key.env (AVA_TELEGRAM_BOT_TOKEN). Separate from the still-running AWS chat_poll.py trigger poller (rr-chat) — see references/aws-chat-poll.md.
---

`scripts/telegram.py` — ported from `communications/telegram/scripts/telegram.py`.
Simple REST functions only (matches `coms/slack`, `coms/discord` in shape) —
not the AWS-side trigger/wake-word poller.

## Functions

- `send_message(chat_id, text)`
- `get_me()`
- `get_updates(offset=None, timeout=20)`

## Not ported (out of scope — functions only, not persona logic)

- `telegram_rooms.py` — per-group Ava persona voice locking, deep
  `apps.core` dependency. Not a messaging function.

## References

- `references/aws-chat-poll.md` — the separate, still-running AWS
  `chat_poll.py` trigger poller (rr-chat). Different system, not replaced
  by this skill.
