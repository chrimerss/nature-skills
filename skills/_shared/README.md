# `_shared/` - Shared content for `nature-*` skills

This directory **is not a standalone skill**. It has no `SKILL.md` and is not registered by plugin loaders. Its purpose is to store reference materials shared across multiple `nature-*` skills, avoiding duplicate maintenance of the same content across different skill directories.

Sibling skills reference files here via relative paths in their `manifest.yaml`, for example:

```yaml
always_load:
  - ../_shared/core/reader-workflow.md
```

## Current Contents

| File | Consumers |
|---|---|
| `core/reader-workflow.md` | `nature-polishing`, `nature-writing` |
| `core/paper-type-taxonomy.md` | `nature-polishing`, `nature-writing` |
| `core/ethics.md` | `nature-polishing`, `nature-writing` |
| `core/terminology-ledger.md` | `nature-polishing`, `nature-writing` |
| `journal-formats/nat-comms.md` | `nature-polishing`, `nature-writing` |

## When to put files here

Place files in `_shared/` only when **two or more skills** need to reuse the exact same content. If content serves only one skill, keep it in that skill's own `static/` or `references/` directory.

## When to keep content local to a skill

The shared layer only stores **definitions and reference materials**, such as paper type taxonomies, reader workflows, ethics rules, or terminology ledgers. How a specific skill diagnoses, drafts, revises, or formats results should remain local in its own `static/fragments/`. Multiple skills can reuse the same paper type taxonomy while executing completely different task logic on top of it.
