# `nature-reader` Skill

`nature-reader` is a Markdown-centric full-paper reading and processing workflow.

## Features

`nature-reader` converts PDFs, DOIs, arXiv links, publisher HTML pages, or pasted manuscript text into complete Markdown reading materials, including:

- Paragraph-level source-grounded text presented in a clean prose format.
- Extracted figures and tables placed near their first substantive discussion in the text.
- Original captions and structured annotations.
- Stable page and text block anchors for traceability.
- Tight image cropping and a comprehensive document source map.

## Main Artifacts

- `paper.md`
- `source_map.json`
- `processing_notes.md`
- `assets/`

`reader.html` can be generated as a secondary preview, but this skill is Markdown-centric by default and does not generate an interactive QA panel by default.

## Trigger Phrases

Use this skill when the user requests:

- Full paper reading
- Paper analysis
- Figure/table extraction
- Literature reading
- Full-text Markdown conversion
- paper md
- source-grounded reading notes

## Notes

Do not use this skill for abstract-only summaries, keyword lists, or simple citation searches. When triggered, the default output must be a structured `paper.md` with visible block anchors and figure/table cards, never just an abstract summary.
