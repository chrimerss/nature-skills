# researchwrite

A proposal-first scientific writing state machine. This is not a generic "write a paper for me" tool—it enforces argumentation architecture prior to drafting, followed by a four-layer QA pipeline.

## What is it?

Three modes + four quality gates:

```
Your Input                  Mode           What it does
─────────────            ─────          ──────────────────
Title, direction, vague idea →  compose       9 steps: from research canon to .docx export
Existing paragraphs/sections →  revise        9 steps: gap analysis → compare before/after
Existing draft + expansion   →  hybrid        combination of compose + revise
```

Automated QA pipeline after drafting:

```
Gate 2: professor Expert Review (Content Layer)
  ├── Paper → Methodology Expert + Domain Expert
  ├── Proposal → Feasibility Expert + Innovation Expert
  └── Review → Coverage Expert + Critical Depth Expert
      ↓
Gate 1: avoid-ai-writing (Language Layer, English only)
      ↓
Gate 3: Automated Validation (Citations present? Reproducible? Consecutive numbering?)
      ↓
Gate 4: Scoring Threshold (≥7.0 passes, <7.0 targeted rollback ≤3 rounds)
```

## Core Principles

| # | Principle | Description |
|---|------|------|
| 1 | Evidence before prose | Must establish research_canon and evidence_table before drafting |
| 2 | Argument before sections | Must complete argument_map before writing main body text |
| 3 | Contracts before paragraphs | Each section requires defined purpose / allowed claims / forbidden claims |
| 4 | Dynamic experts | Summon domain experts tailored to specific failure modes |
| 5 | Content before language | Diagnose scientific logic before performing language polishing |
| 6 | Stop when appropriate | Plateaus and missing evidence are valid reasons to stop |

## Installation

```bash
# Hermes / Claude Code
git clone https://github.com/Jiahao8595/research-pipeline.git
cp -r research-pipeline/researchwrite ~/.hermes/skills/
```

After installation, run `/reload-skills`.

**Dependencies:**

```bash
hermes skills install brainstorm     # Entry-point follow-up questioning
hermes skills install professor      # Dynamic expert review
hermes skills install avoid-ai-writing  # English anti-AI-slop
hermes skills install docx           # Word document export
```

## Usage Examples

```
# Write a proposal from scratch
"Use researchwrite to draft a research proposal on perovskite stability optimization"

# Review existing text
"Use researchwrite to review this discussion section, paper gear"

# Quick scan
"Quickly scan this abstract" (marks issues only without running full QA)
```

## Four Gears

| Gear | Scenario | Threshold | Description |
|------|------|:---:|------|
| `paper` | Journal submission | 7.0 | Full run |
| `proposal` | Research proposal | 7.0 | Full run |
| `internal` | Internal report | 5.0 | Skip expert review |
| `quick` | Quick scan | — | Mark P0 issues only |

## File Structure

```
researchwrite/
├── SKILL.md                       ← Skill entry point
├── README.md                      ← This file
├── references/
│   ├── evaluation-rubric.md       ← 8 dimensions × 4 anchor scoring system
│   ├── stopping-rules.md          ← Iteration stopping conditions
│   ├── foundation-files.md        ← Establishing foundation files
│   └── validation-checklist.md    ← Automated validation checklist
├── scripts/
│   └── build_proposal_docx.py     ← .md → .docx build script
└── templates/                     ← Empty templates (for new projects)
    ├── 00_scope.md
    ├── 01_research_canon.md
    ├── 02_evidence_table.md
    ├── 03_argument_map.md
    ├── 04_section_contracts.md
    ├── 05_style_guide.md
    ├── qa_report.md
    └── revision_brief.md
```

> **Complete reference files** (detailed explanations of compose/revise/hybrid modes, expert dispatch, export archiving, review frameworks, etc., 12 files total) are not included in the public release. Contact the author via [GitHub issue](https://github.com/Jiahao8595/research-pipeline/issues) or email if needed.

## Author

JL Lab — A writing framework built on doctoral research practice.
