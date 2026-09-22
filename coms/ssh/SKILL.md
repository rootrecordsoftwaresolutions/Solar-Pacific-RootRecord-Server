# SSH Globe Relay Skill

## Purpose

SSH-based telemetry collection and relay skill for the RootRecord Network Globe system.

This skill is designed for:
- human operators
- AI-assisted maintenance
- repeatable deployment

## Runtime Flow

    Local collector
        |
        v
    SSH relay transport
        |
        v
    US-Mainland-Server
        |
        v
    Network Globe backend

## Deployment

This skill is loaded from:

    /home/rootrecord/.ollama/skills/coms/ssh

Part of the `coms` group alongside `telegram`, `discord`, and `slack` —
each is its own independently-loadable skill (own SKILL.md, own metadata
entry) so activating one doesn't pull the others into context. `coms/`
itself is just the organizational parent folder, not a skill.

Do not create duplicate copies.

## Active Components

The active runtime directory contains only files intended to execute:
run.sh, scripts/, config/, data/, logs/

## Context Preservation

Historical files are retained as .bak context where they are not part of the
active runtime. See backups/ (retired Python/paramiko implementation) and
context/ (planning and setup docs) for history.

## Operational Rules

- Do not delete historical implementations.
- Do not commit runtime data.
- Keep secrets outside the skill package.
- Verify SSH connectivity before relay startup.

## Start

From the skill directory:

    cd /home/rootrecord/.ollama/skills/coms/ssh
    ./run.sh

## Stop

    Ctrl+C

or:

    pkill -f ssh-relay

## Status

    cd /home/rootrecord/.ollama/skills/coms/ssh
    ./scripts/health-check.sh

## Logs

Location:

    ./logs/

## Troubleshooting

SSH failure:
- verify key
- verify host
- verify permissions

Relay failure:
- check outbox
- check network connectivity
