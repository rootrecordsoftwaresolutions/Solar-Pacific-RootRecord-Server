# Migrate `discord`

Status: moved from `communications/discord/scripts/discord.py` into
`coms/discord`.

Token loading replaced: old `from .. import config` (package-relative,
scanned multiple `.env` candidates) → single load from
`/home/rootrecord/master/master-key.env`. Env var names unchanged
(`AVA_DISCORD_BOT_TOKEN` with fallbacks `SEXI_DISCORD_BOT_TOKEN`,
`DISCORD_ROOTMC_BOT_TOKEN`, `DISCORD_BOT_TOKEN`).

`discord_chat.py` (persona reply logic) intentionally not ported — separate
concern, deep `apps.core` dependency chain.
