---
name: researchwrite
description: |
  Proposal-first scientific writing pipeline. Three modes (compose/revise/hybrid) with four-layer QA pipeline. Enforces evidence-before-prose, argument-before-sections, and contracts-before-paragraphs.
version: 1.0.0
author: JL Lab
license: MIT
metadata:
  hermes:
    tags: [research, writing, proposal, revision, qa, multi-agent]
    related_skills: [brainstorming, professor, avoid-ai-writing, docx]
---

# researchwrite — Proposal-First Scientific Writing Pipeline

A scientific writing state machine inspired by autonovel (state machine + scoring), professor (dynamic expert persona), brainstorming (entry-point follow-up questioning), and anti-AI-writing (language cleanup). **This is NOT a generic "write a paper for me" prompt.**

## Core Principles

1. **Evidence Before Prose** — Must establish or read `research_canon` and `evidence_table` before drafting.
2. **Argument Before Sections** — Must complete `argument_map` before writing main body text.
3. **Contracts Before Paragraphs** — Each section requires defined purpose / allowed claims / forbidden claims / inputs / validation.
4. **Scope Before Completeness** — If writing in stages, lock down stage boundaries first.
5. **Dynamic Experts (No Fixed Pool)** — Use `professor` to summon domain experts tailored to specific failure modes.
6. **Content Before Language** — Diagnose scientific logic before performing anti-slop / language polishing.
7. **No Automatic Fact Upgrades** — Never upgrade "may indicate" to "proves" without supporting evidence.
8. **Deletion Over Explanation** — When a claim is unfeasible, delete it directly. Keep text clean; leave explanations for oral defense.
9. **Stop When Appropriate** — Plateaus, expert conflicts, and missing evidence are reasons to stop, not reasons to polish.

## Mode Dispatch

| Input | Mode |
|---|---|
| Title, research direction, vague ideas | `compose` — Load `references/compose-mode.md` |
| Existing paragraphs/sections/complete proposal | `revise` — Load `references/revise-mode.md` |
| Existing draft + expansion/supplement/refactor | `hybrid` — Load `references/hybrid-mode.md` |

Infer the default mode when ambiguous. Only ask the user when the choice would alter the workflow.

## Project Structure

**Working Directory**: `<outputs>/researchwrite/<project-slug>/`

**Standard Files**:

```
00_scope.md              Writing task boundaries
01_research_canon.md     Hard facts and constraints
02_evidence_table.md      claim → evidence mapping table
03_argument_map.md        Argumentation architecture
04_section_contracts.md   Section purpose / inputs / allowed & forbidden claims
05_style_guide.md         Style, terminology, forbidden expressions
state.json                Project state (mode, round, scores, technical_debts)
sources/                  User materials, literature, data
drafts/                   Drafts and section files
revision_briefs/          Revision briefs
qa_logs/                  Diagnostics, expert review, anti-slop, scoring logs
exports/                  Final output (.md + .docx)
```

When creating a new project, take empty templates from `templates/`. `references/worked-example-quaternary-proposal.md` provides a complete filling example based on materials science.

## Reference File Index

The public release contains four key references:

| Reference | Purpose |
|---|------|
| `references/evaluation-rubric.md` | 8 dimensions × 4 anchor scoring system + scoring workflow |
| `references/stopping-rules.md` | Iteration loop stopping conditions |
| `references/foundation-files.md` | Establishing the five foundation files |
| `references/validation-checklist.md` | Automated validation checklist |

> Complete reference files (detailed explanations of compose/revise/hybrid modes, expert dispatch, export archiving, review frameworks, etc., 12 files total) are not included in the public release. Contact the author via [GitHub issue](https://github.com/Jiahao8595/research-pipeline/issues) or email if needed.

## Execution Delivery

Output at the end of each run:

1. Current file path or revised text
2. Current score/status
3. Remaining risks
4. One recommended next step

## QA Mode — Four-Layer Quality Assurance Pipeline

Enter QA mode when the user asks to "review this section / run QA / check proposal / pass pipeline".

### Context Gears

| Gear | Applicable Scenario | Threshold |
|------|---------|------|
| `paper` | Journal submission | 7.0 |
| `proposal` | Research proposal | 7.0 |
| `internal` | Internal report / weekly report | 5.0 |
| `quick` | Quick scan | None |

### Pipeline Sequence (Content First, Language Second)

```
Gate 2: professor Convener (Content Layer)
  ├── Paper → Methodology Expert + Domain Expert
  ├── Proposal → Feasibility Expert + Innovation Expert
  └── Literature reviews → Coverage Expert + Critical Depth Expert
  │
  ▼
Gate 1: avoid-ai-writing mode detect-only
  └── Applies to English drafts; for L2/non-native drafts, perform manual structural scan
  │
  ▼
Gate 3: auto-validation (Format / Completeness Layer)
  └── Every claim has citation? Method reproducible? Consecutive numbering?
  │
  ▼
Gate 4: Scoring Threshold (Dimension-based scoring)
  ├── Total score ≥ threshold → Pass ✅
  └── Total score < threshold → Targeted rollback based on low-scoring dimensions (max 3 rounds)
```

**Gate 2 precedes Gate 1** — Avoid rewriting sentences only to have them rejected by experts later.

### Usage Examples

```
User: "Review this discussion section using researchwrite, paper gear"
  → Automatically run Gate 2 → Gate 1 → Gate 3 → Gate 4
  → Return review report + targeted revision suggestions

User: "Quickly scan this email"
  → Run quick gear, mark P0 issues only
```

## Configure Your Research Domain

On first use, tell the agent your research background. The agent will invoke `professor` to establish domain expert knowledge. Subsequent expert reviews during writing will be tailored to your domain.
