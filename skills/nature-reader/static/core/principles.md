# Core principles (reader)

Use this skill to turn a research paper into a complete Markdown reading artifact. The default output should read like a structured paper companion, not a summary dump:

- keep the extractable prose, paragraph structure, and section flow
- show text blocks clearly at block level with precise source anchors
- extract figures and tables as assets and place them at the first substantive mention or interpretation point
- keep captions attached to figures/tables with clear English caption text
- preserve stable page and block anchors for traceability
- write a complete `paper.md` by default, plus `source_map.json`, `processing_notes.md`, and `assets/`

This skill is for papers, preprints, and conference proceedings across disciplines. It is not limited to Nature-family journals. If the user only wants a summary, use a summarization skill instead. If the user only wants citation search, use a citation skill instead.

## Non-negotiable defaults

When the user asks for paper reading, `nature-reader`, or full paper analysis, produce a structured paragraph-level reader by default.

Do not replace the reader with:

- a summary-only dump
- a paper review without exact source block alignment
- figure captions without figure/table crops
- a list of key points detached from source locations
- only the abstract, introduction, or selected highlights

If constraints prevent full processing, still create a draft reader and clearly label missing pages, missing figures/tables, unprocessed blocks, or low-confidence OCR/crops in `processing_notes.md`.

## Core principle

Analyze for meaning and structure. Preserve the paper's structure, evidence, hedging, terminology, equations, units, and citation markers. Keep the output in prose paragraphs unless the source itself is tabular or list-like. Do not collapse the paper into keyword bullets or slide-style notes.

The reading file should help a reader move between:

- text content
- source location
- figure or table evidence

Each substantive source block should have a stable anchor:

```markdown
<a id="S001"></a>
**Source:** p.1 S001

[source paragraph]
```

## Copyright caution

For copyrighted publisher PDFs, keep chat responses short and point to the local artifact. In local `paper.md`, include the reader only for the user-provided source file or clearly lawful open-access content; avoid reproducing large copyrighted text directly in chat.

## Quality bar

Good output feels like a paper companion, not a crude extraction dump. It should let a reader:

- read the paper cleanly and efficiently
- see where a claim came from
- inspect the nearby figure or table
- move through a complete Markdown file without losing source traceability
