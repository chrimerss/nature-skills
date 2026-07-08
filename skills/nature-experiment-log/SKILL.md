---
name: nature-experiment-log
description: "Standardized experiment logging — ingests raw materials (images/audio/text) and outputs standardized logs with YAML frontmatter to an Obsidian vault. Works with Feishu/Lark CLI or direct manual input."
version: 1.0.0
author: Community contribution (JL Lab)
license: MIT
metadata:
  hermes:
    tags: [research, experiment, logging, feishu, obsidian, automation]
    related_skills: [nature-literature-pipeline, feishu-cli-integration]
---

# experiment-log — Standardized Experiment Logging

## Trigger Conditions

Automatically loaded when the user submits raw experimental records or notes via:

- **Path A** — Direct CLI submission (images / audio transcripts / text notes)
- **Path B** — Sent to a messaging group (e.g., Feishu/Lark research group) and scanned via `feishu-cli-integration`

## Prerequisites

When used with messaging integrations like `feishu-cli-integration`, ensure:
- The bot is added to the target group
- Bot permissions: `im:message` + `im:resource` + `im:message.group_msg`
- Group ID is configured in the skill context

## Workflow

1. Ingest materials → use vision analysis to read images + extract structured information
2. Generate unique Experiment ID + Sample Batch ID
3. Write standardized log to `wiki/Experiment-Logs/{System}/{Type}/{exp_id}.md`
4. Archive raw materials (images, audio, etc.) to `raw/experiments/YYYY.MM.DD_Description_EXPID/`
5. Append a "Raw Materials" section at the end of the log referencing the raw file paths
6. Check for anomalies → if found, append to `Anomaly-Log.md`
7. Append operation record to the Experiment Index
8. Notify the user of the written file location

If information is ambiguous or missing (e.g., exact temperature forgotten, sample ID unclear), actively ask the user rather than guessing or inventing data.

## Directory Structure

```text
/vault/
├── raw/experiments/                       ← Raw layer (archive)
│   └── YYYY.MM.DD_Description_EXPID/
│       ├── Notes.md
│       ├── Images/
│       └── Audio/
│
wiki/Experiment-Logs/                      ← Standard layer (output)
├── Experiment-Index.md
├── Anomaly-Log.md
├── {SystemA}/
│   ├── ExpType1/
│   ├── ExpType2/
│   └── ...
├── {SystemB}/
│   └── ...
└── Common/
    └── Equipment-Tracking.md
```

## Experiment ID Rules

```text
{SystemCode}-{EquipmentCode}-YYMMDD-{Seq}
  │            │               │       └─ Daily sequence number (starting from 001)
  │            │               └─ Date
  │            └─ Equipment code (M=Muffle furnace, T=Tube furnace, E=Electrochemical, G=Glovebox, F=Controlled-atmosphere furnace, B=General)
  └─ System code (Custom, e.g., CL / NO / OX / HY / etc.)
```

## Sample Batch ID Rules

```text
{SystemCode}-{CandidateID}-B{Seq}
  │            │             └─ Batch sequence number
  │            └─ Candidate formulation/sample ID
  └─ System code
```

When the same sample batch is used across multiple experiments, keep `sample_batch` consistent for Dataview tracking.

## Equipment Codes

| Code | Equipment | Scenarios |
|------|-----------|-----------|
| M | Muffle Furnace | Heat treatment, immersion corrosion |
| T | Tube Furnace | Atmosphere control, dehydration, thermal stability |
| E | Electrochemical Workstation | CV / SWV / EIS |
| G | Glovebox | Salt preparation, weighing, sampling |
| F | Controlled-Atmosphere Furnace | Precision atmosphere control |
| B | General / Benchtop | Drying, cleaning, sample preparation |

Extend codes based on actual laboratory equipment.

## Obsidian Integration

This skill is designed to work with an [Obsidian](https://obsidian.md) vault. Obsidian is a local Markdown-based note-taking system. Combined with the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin, it enables dynamic querying and dashboards for experimental data.

**Why Obsidian:**
- All logs are plain text Markdown: version-controllable and full-text searchable
- YAML frontmatter structure allows Dataview to automatically generate experiment lists, anomaly summaries, and equipment usage logs
- Local storage with zero cloud dependency and high data security

**Required Vault Files:**

| File | Template | Purpose |
|------|----------|---------|
| `Experiment-Logs/Experiment-Index.md` | `templates/experiment-index.md` | Dataview query dashboard |
| `Experiment-Logs/Anomaly-Log.md` | `templates/anomaly-log.md` | Anomaly tracking |
| `Experiment-Logs/Common/Equipment-Tracking.md` | `templates/equipment-tracking.md` | Equipment and reagent tracking |

Copy the template files into your Obsidian vault at the corresponding locations to get started.

## Reference Examples

The `references/` directory contains three complete experiment log examples covering common experimental workflows:

| File | Experiment Type |
|------|-----------------|
| `references/example-log.md` | Materials immersion corrosion experiment |
| `references/example-electrochemical.md` | Electrochemical characterization (CV window test) |
| `references/example-thermal-stability.md` | Thermal stability experiment |

Each example contains complete YAML frontmatter and Markdown body content and can be modified directly as a template.

## CLI & Messaging Integration Notes

For Path B using messaging CLI tools (like Feishu/Lark CLI):

- Fetch messages: `lark-cli im +chat-messages-list --chat-id oc_*** --page-size 30 --sort asc`
- Download resources: `lark-cli im +messages-resources-download --message-id *** --file-key *** --type image --output <relative_path>`
- ⚠️ Note: `--output` typically accepts relative paths; `cd` into the `raw/experiments/` archive directory first.

Group ID and bot permissions should be retrieved from your messaging plugin configuration.

## Customization Guide

- **System Code**: Customize according to your research systems (e.g., CL/NO/OR/PO)
- **Experiment Type**: Create subdirectories under `wiki/Experiment-Logs/{System}/` as needed
- **YAML Fields**: The template provides a recommended structure; add or remove fields as required
- **Equipment Codes**: Extend based on your lab's actual instrument inventory

## Related Files

| File | Purpose |
|------|---------|
| `references/example-log.md` | Complete experiment log example |
| `wiki/Experiment-Logs/Experiment-Index.md` | Dataview dashboard |
| `wiki/Experiment-Logs/Anomaly-Log.md` | Anomaly log format |
| `wiki/Experiment-Logs/Common/Equipment-Tracking.md` | Equipment and reagent tracking |
