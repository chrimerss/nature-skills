# nature-writing Skill

`nature-writing` drafts, restructures, or plans Nature-style manuscript sections from author-provided claims, results, figures, notes, or rough drafts.

## Features

`nature-writing` helps draft and structure:

- Title
- Abstract
- Introduction
- Results narrative
- Discussion
- Conclusion
- Significance paragraph
- Manuscript outline

This skill focuses on argument construction and section drafting. If you already have an English draft and only need sentence-level polishing, use `nature-polishing` instead.

## Source Basis

This skill is derived from close readings of Nature and Nature Communications research papers across fields such as materials science, energy systems, building decarbonization, and machine learning, combined with established academic writing strategies.

Section-level drafting and adversarial self-review rules also incorporate structured scientific writing principles and community research best practices:

- https://pengsida.notion.site/c1a22465a0fa4b15a12985223916048e
- https://github.com/pengsida/learning_research

## File Structure

```text
nature-writing/
├── README.md
├── SKILL.md
└── references/
    ├── abstract.md
    ├── article-architecture.md
    ├── conclusion.md
    ├── experiments.md
    ├── introduction.md
    ├── method.md
    ├── nature-summary-paragraph.md
    ├── paragraph-flow.md
    ├── paper-review.md
    ├── related-work.md
    └── examples/
```

## Core Rules

| Area | Rule |
|---|---|
| Evidence First | Never fabricate data, mechanisms, statistics, sample sizes, or novelty |
| Abstract | Background, research gap, method, key results, significance, boundaries |
| Introduction | Domain scale, bottlenecks, prior attempts, unresolved gap, present work; use staged summary-paragraph funnel for `Nature` |
| Method | Explain module motivation, design, forward pipeline, and technical advantages |
| Results | Build an evidence ladder rather than writing a chronological lab log |
| Experiments | Every major claim must be supported by comparisons, ablations, metrics, or stress-test evidence |
| Discussion | Explain significance, relationship to existing work, constraints, and future utility |
| Self-Review | Perform adversarial self-review before submission |
| Rough Notes | Convert intent and argument structure; do not mechanically translate note syntax |

## Author Workflow

| Source Type | Core Approach |
|---|---|
| Complete Draft | Restructure and sharpen arguments; do not rewrite sentences that are already clear and precise |
| Rough Notes | Convert intent and argument structure; do not mechanically translate note syntax |
| Bullet Points | Build coherent paragraphs following `1 paragraph = 1 argument` rule |
| Section-by-Section | Maintain consistent terminology and narrative flow across sections |
