# `nature-paper2ppt` Skill

`nature-paper2ppt` converts scientific papers into concise PowerPoint presentations for journal clubs, group meetings, lab meetings, or paper sharing, structured with a Nature-style evidence narrative.

The skill accepts paper PDFs, preprints, article texts, abstracts plus figure legends, or structured reading notes. It classifies the paper type, extracts the scientific argument, selects key figures/tables that support the argument, writes slide content and speaker notes, generates a real `.pptx`, and runs lightweight QA on the presentation package.

## Features

- Converts scientific papers into a 10-16 slide presentation.
- Uses the paper's scientific argument as the presentation spine rather than blindly copying manuscript section order.
- Determines paper type first, then selects the narrative logic.
- Treats key figures, tables, or panels as evidence rather than decoration.
- Crops or splits dense multi-panel figures when full figures are difficult to read at presentation scale.
- Writes slide titles, concise bullet points, captions, takeaways, and speaker notes.
- Generates an editable `.pptx` as the primary deliverable.
- Records an asset manifest when extracting figures and tables.
- Runs lightweight QA on slide count, embedded media, speaker notes, figure crops, layout alignment, AI template phrasing, and PPTX package structure.

## Origins and Design Hierarchy

- Nature-style scientific narrative: problem, gap, claim, evidence, validation, reusability value, limitations, and discussion.
- Academic journal club practice: short slides tailored for live presentation, rather than dense reading notes.
- Evidence-first slide design: result slides focus on a main figure or table as the centerpiece.
- Lean production overhead: time-consuming OCR, image extraction, and rendering are performed only when they materially improve the final presentation.

## File Structure

This skill uses a router/static-dynamic structure: a short `SKILL.md` router combined with `manifest.yaml` loads only the fragments needed for the current task.

```text
nature-paper2ppt/
├── SKILL.md                     # Short router: identifies paper_type, loads fragments
├── manifest.yaml                # always_load core + paper_type axis + on-demand references
├── README.md
├── scripts/
│   └── audit_pptx_quality.py     # PPTX XML quality audit: bounds, cropping, alignment, boilerplate
├── static/
│   ├── core/                    # Always loaded
│   │   ├── principles.md        # Purpose, core principles, lean mode, inputs, language
│   │   ├── toolchain.md         # Cross-platform Python stack and default fast path
│   │   ├── workflow.md          # 9-step workflow spine
│   │   └── output-and-quality.md# Output package, citation, quality, fallback rules
│   └── fragments/
│       └── paper_type/          # One reporting arc per paper category
│           ├── discovery.md     # question-to-evidence
│           ├── methods.md       # problem-to-solution
│           ├── resource.md      # workflow-to-validation
│           ├── clinical.md      # design-to-inference
│           ├── materials.md     # property-to-mechanism / design-to-performance
│           └── review.md        # evidence-map
└── references/                  # Loaded on demand
    ├── design-and-layout.md     # Composition, layout, typography, anti-template, archetypes
    ├── figure-assets.md         # Figure selection, extraction, crop self-check
    └── self-review.md           # Self-review loop, severity grading, programmatic checks, verification
```

The shared terminology ledger `../_shared/core/terminology-ledger.md` is loaded on every run to ensure technical terms remain consistent across slides.

## Use Cases

- Creating PPT or PPTX presentations from research paper PDFs.
- Preparing for journal clubs, group meetings, lab seminars, paper sharing, or thesis defenses.
- Summarizing Nature-family papers into structured presentation decks.
- Converting article text, figure legends, or reading notes into presentations.
- Requiring figure-integrated decks rather than just outlines or summaries.
- Requiring speaker notes, source labels, and QA reports.

## Default Output Package

The default output is a small workspace directory:

```text
output/
├── final_presentation.pptx
├── qa_report.md
├── asset_manifest.md          # Generated when source figures are extracted
└── assets/
    └── figures/
```

Outlines or script files can be optionally generated if helpful for review or debugging, but `.pptx` is always the primary deliverable.

## Reporting Logic

The default narrative arc helps the audience answer:

1. Why does this problem matter?
2. What gap or bottleneck does the paper address?
3. What did the authors do?
4. What is the key evidence?
5. Why should we trust the result?
6. What is new, reusable, or broadly meaningful?
7. Where are the boundaries and open questions?

The skill adjusts this arc based on paper type. Discovery papers use question-to-evidence logic; methods, AI, and tool papers use problem-to-solution; resource and atlas papers use workflow-to-validation; reviews use an evidence-map structure.

## Design Intent

This skill creates decks ready for oral academic reporting. It is concise, figure-led, evidence-sensitive, and does not fabricate values, methods, mechanisms, datasets, or image interpretations unsupported by the source paper.

Dense result figures are cropped, split, or placed on individual slides, rather than squeezed into unreadable symmetrical two-column layouts. On-slide text is short, with detailed explanations placed in speaker notes.

## Notes

- Default language is English. Technical terms, abbreviations, gene names, model names, equations, and statistical terms are preserved accurately.
- Applicable across multiple scientific disciplines, not limited to biomedical papers.
- If a reliable headless renderer is unavailable, the skill performs structural QA and records why rendered preview QA was skipped.
- Run `scripts/audit_pptx_quality.py` after generating the PPTX; high-severity issues must be fixed before delivery.
