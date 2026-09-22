---
name: slack
description: Slack Web API functions — post_message, history, auth_test. Replies only, never deletes history. Token from /home/rootrecord/master/master-key.env (AVA_SLACK_BOT_TOKEN).
---

`scripts/slack.py` — ported from `ns/apps/core/services/slack.py` (the
version already in production use by Desk/ava-ops).

## Functions

- `auth_test()` — verify token
- `post_message(channel, text)` — chat.postMessage, 3500-char cap
- `history(channel, limit=12)` — conversations.history read

## Not carried over from the original location

- `DAILY.md` / `INDEX.md` — hybrid-reports/Desk notebook system (weather +
  EcoFlow telemetry), not this skill's runtime. Left at original path.
- `data/channels/*` — real archived channel metadata (18 channels, ~252KB,
  index/meta only). Left at original location, not duplicated here.

## Rules

- Never delete channel history — read/post only
