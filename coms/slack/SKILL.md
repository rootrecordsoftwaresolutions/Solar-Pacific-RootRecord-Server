---
name: slack
description: >-
  Slack Web API: post_message, history, auth_test. Replies only — never
  delete history. Token AVA_SLACK_BOT_TOKEN in master-key.env.
---

# slack

`scripts/slack.py`

- `auth_test()` · `post_message(channel, text)` (3500-cap) · `history(channel, limit=12)`

**Rule:** read/post only — never delete history.
