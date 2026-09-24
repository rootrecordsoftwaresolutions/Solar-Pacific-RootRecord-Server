# Current State

This file records durable cross-project state that is intentionally maintained at the master-prompt level.

## 2026-09-24 baseline

- RootRecord uses multiple repositories, including US Mainland Server, Solar Pacific RootRecord Server, and RootRecord Website.
- A separate RootRecord Master Prompt repository is intended to reduce repeated handoff uploads.
- The master prompt should remain an index/operating contract rather than a duplicate of the implementation repositories.
- A local `dev-prompts` skill is intended at `/home/rootrecord/.ollama/skills/dev-prompts`.
- EcoFlow temporary work should use `/tmp/`; permanent EcoFlow action scripts remain in the established energy skill structure.
- Historical handoff material identified documentation drift around Delta 2 AC behavior; current implementation and live behavior must be verified before changing policy.
