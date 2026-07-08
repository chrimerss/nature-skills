# experiment-log

A standardized experiment logging tool. Ingests raw materials such as images, audio recordings, and text notes, and automatically generates structured logs with YAML frontmatter.

## What is this?

This is not just a generic "note-taking helper" — it is a standardized logging pipeline: ingest raw records → extract structured information → generate unique IDs → write standard formatted logs → archive raw files.

It is applicable to any research field requiring rigorous, traceable experimental records.

## Installation

```bash
git clone https://github.com/Jiahao8595/research-pipeline.git
cp -r research-pipeline/experiment-log ~/.hermes/skills/
```

After installation, run `/reload-skills`.

**Prerequisites:**

```bash
hermes skills install feishu-cli-integration   # For messaging app integration (Path B)
hermes skills install obsidian                 # For vault file management
```

## Usage

**Path A — Direct CLI Submission:**
```text
"Record an experiment: Performed 316L chloride salt corrosion at 500°C for 300h under Ar atmosphere, weight loss 0.0032g"
```
Attach images or transcripts, and the agent will analyze them to extract structured data and generate a standard log.

**Path B — Messaging Group Submission:**
Send experimental photos and voice notes to your configured research chat group; the agent will automatically scan and process them.

## File Structure

```text
experiment-log/
├── SKILL.md                    ← Skill entry point
├── README.md                   ← This file
└── references/
    └── example-log.md          ← Complete log example
```

## Core Design

- **Unified ID System** — System Code + Equipment Code + Date + Sequence Number, enabling cross-experiment tracking.
- **Sample Batch Tracking** — Consistent sample batch IDs across multiple experiments, queryable via Dataview.
- **YAML Frontmatter** — Combines structured data with free text for both human readability and machine querying.
- **Messaging CLI Integration** — Take photos on your phone and send to a group chat → automatically archived into your vault.
- **Anomaly Tracking** — Automatically detects experimental anomalies and appends them to the anomaly log.

## Customization

Equipment codes, system codes, and experiment type directories can all be customized for your laboratory setup. See the "Customization Guide" in `SKILL.md` for details.

## Author

Community contribution (JL Lab)
