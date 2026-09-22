# AWS chat_poll.py (rr-chat) — separate system, still running

Not part of this skill's runtime. Documented here for context only.

## Current behavior (chat_poll.py, AWS Mainland)

- Polls Telegram ~1s for `RR_CONTROL_CHAT_ID`, watching wake-words (`ava`,
  `bruce`, `carly`, `/ask`, `@ava`, etc.)
- Logs every message to `work/chatlogs/Current.jsonl` — rides along in the
  SSH data pack (`coms/ssh`)
- Radar-related message → shells out to `radar_post_once.py`, posts GIF back
- Wake-word trigger → writes `work/triggers/Current.json` + posts a quiet
  `RR_TRIGGER ...` notice to the control chat
- No LLM inference here — stays on AVA-CORE (RootRecord's NPU side)
- Two bot tokens (trigger watch vs. retired datapack-recv) to avoid
  Telegram 409 on concurrent `getUpdates`
- `RR_PUBLISH_CHAT_ID` — separate broadcast destination

## Why it stays on Telegram (confirmed design)

Outbound-only `getUpdates`/`sendMessage` solves NAT traversal for the home
box for free. Deliberate, not being replaced.

## If ever migrated

1. Bring in `chat_poll.py` + `radar_post_once.py` + `common.py` source
2. Decide AWS-only vs. RootRecord-side counterpart for reply-now — confirm
   how AVA-CORE currently picks up `RR_TRIGGER` before assuming either way
3. Bring in `OPERATOR.md`'s token/chat-id table
