---
name: plumbing
description: >-
  Inference pipelines for RootRecord: NPU-first when the runtime can use
  /dev/accel, hard single-flight (one model/agent run at a time), staged
  vision. Not a coms skill — wires how brains run.
---

# plumbing

| Piece | Path | Role |
|-------|------|------|
| Single-flight lock | `scripts/single-flight.sh` | `flock` — **one** inference/agent job worldwide on this host |
| Ollama run wrapper | `scripts/run-ollama.sh` | Always takes the lock; never parallel `ollama run` |
| NPU policy | `references/NPU-FIRST.md` | Prefer NPU for anything that binds XDNA/XRT; honesty on Ollama |
| Pipelines | `pipelines/*.md` | Staged runbooks (not live yet) |
| Vision agent | `~/.ollama/agents/vision/` | Staged image-reader Modelfile |

**MUST:** never start a second model/agent run while one holds `/run/user/$UID/rootrecord-inference.lock` (or `$XDG_RUNTIME_DIR`).

State dir: `/home/rootrecord/.ollama/skills/plumbing/state/` (queue, last-run).
