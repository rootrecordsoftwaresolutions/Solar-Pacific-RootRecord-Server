# Architecture

RootRecord consists of multiple repositories with distinct implementation responsibilities.

The master-prompt repository provides cross-project operating rules and references. It must not become a duplicate of the application/server source trees.

Repository-specific architecture belongs in the corresponding implementation repository.
