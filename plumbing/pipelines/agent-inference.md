# Pipeline: agent inference (staged)

```
request
  → plumbing/scripts/single-flight.sh run
      → ONLY ONE of:
          ollama (CPU today): run-ollama.sh <model>
          npu-vision (future): pipelines/vision-npu.md
  → release lock
  → optional coms relay (skills/coms) — never holds inference lock during network wait if avoidable
```

## Rules
1. **One model or agent run at a time** — hard. Exit 75 if busy.
2. Queue optional later (`state/queue.json`); v0 = fail-fast busy.
3. Council AVA→Bruce→Carly→AVA = **serial** steps, each acquiring the lock in turn (never overlapping).
4. Do not `ollama run` from cron/poller without `run-ollama.sh`.

## Models
| Lane | Model |
|------|-------|
| Ava core/public/architect/telegram | `ava` / `ava-public` / `ava-architect` / `ava-telegram` |
| Bruce | `bruce` / `bruce-ops` / `bruce-philosophy` / `bruce-telegram` |
| Carly | `carly` / `carly-appsec` / `carly-energy` / `carly-telegram` |
| Vision (staged) | `vision-reader` |
