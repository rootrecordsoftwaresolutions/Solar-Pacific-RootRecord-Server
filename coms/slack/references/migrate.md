# Migrate `slack`

Status: moved from `ns/apps/core/services/slack.py` into `coms/slack`.

Token loading updated twice now:
1. First pass: relative `from .. import config` → skill-local `config/slack.env`
2. This pass: skill-local env → single `/home/rootrecord/master/master-key.env`,
   matching `coms/telegram` and `coms/discord`. Also corrected the token var
   name to `AVA_SLACK_BOT_TOKEN` (found in the real `config.py` while porting
   discord/telegram) — the first pass had used a made-up `SLACK_BOT_TOKEN`.

`config/slack.env.example` removed — no longer applicable, secrets are
centralized now.
