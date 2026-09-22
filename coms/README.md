# coms/

Parent folder grouping every communications/relay protocol RootRecord uses.
This folder itself is **not** a skill (no metadata entry, nothing to
discover) — it's purely organizational. Each subfolder below it is its own
independently-loadable skill with its own `SKILL.md`, so activating one
never pulls the others' instructions into context. That matters on
NPU-constrained inference: cheap to keep several around (each metadata
entry is ~50-100 tokens), expensive to merge them into one skill that loads
everything at once on activation.

| Skill | Status | Purpose |
|---|---|---|
| `ssh/` | **Live** | Data-pack pull + verify + remote-wipe-confirm between RootRecord and AWS Mainland. Replaced the old Telegram-based `rr-packer` relay. |
| `telegram/` | **Live** (functions) | `send_message`/`get_me`/`get_updates`. Separate from the still-running AWS `chat_poll.py` trigger poller — see `telegram/references/aws-chat-poll.md`. |
| `discord/` | **Live** (functions) | Post/pin/forward/read messages, DMs, guild channels. Persona reply logic (`discord_chat.py`) intentionally not ported. |
| `slack/` | **Live** (functions) | `post_message`/`history`/`auth_test`. Replies only, never deletes history. |

All three protocol skills load their bot token from a single file:
`/home/rootrecord/master/master-key.env` — `AVA_TELEGRAM_BOT_TOKEN`,
`AVA_DISCORD_BOT_TOKEN` (+ fallbacks), `AVA_SLACK_BOT_TOKEN`. `ssh/` doesn't
use this — its credential is the SSH key file itself, referenced directly.

## Adding a new protocol later

Copy the shape of `ssh/` or `telegram/`: a `SKILL.md` describing what it
does and how to invoke it, `scripts/` for anything it runs, `references/`
for anything it needs to look up but shouldn't load by default. Keep each
skill's `SKILL.md` body reasonably lean (rough guideline: under ~5000
tokens) — if a protocol's instructions get big, push the bulk into
`references/` and have `SKILL.md` point at it rather than inlining
everything.
