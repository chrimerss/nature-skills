# nature-paper-to-patent Skill

`nature-paper-to-patent` is an evidence-grounded workflow for converting scientific papers, academic theses, technical reports, source code, figures, and inventor notes into structured invention patent application drafts.

This skill generates formal patent documentation in English while maintaining clear agent-facing analysis and routing instructions that can be transferred across AI agent workflows.

## Features

- Maps manuscript prose, formulas, figures, code, and supplementary evidence to stable source IDs.
- Extracts technical problems, synergistic technical solutions, implementation chains, and specific technical outputs.
- Builds an evidence ledger prior to drafting claims.
- Maps every substantive claim feature back to source evidence.
- Supports full application drafts, claim sets only, technical disclosure analysis, and paper-patent audits.
- Handles selectable PDF text, scanned PDFs, pasted text, and mixed project folders.
- Routes algorithm/software, apparatus/system, process/material, and mixed inventions to specialized drafting rules.
- Preserves source-supported core formulas and renders them as editable Office Math in DOCX.
- Generates black-and-white flowchart SVGs and PNGs aligned with claim steps.
- Reuses the principal claim flowchart as the abstract drawing and specification figure.
- Generates separate DOCX documents: Claims, Specification, Abstract, Abstract Drawings, and a Complete Review Draft.
- Validates claim structure, evidence traceability, formula coverage, figure alignment, terminology consistency, and quality thresholds.

## File Structure

```text
nature-paper-to-patent/
├── README.md
├── SKILL.md
├── manifest.yaml
├── static/
│   └── core/
│       ├── stance.md
│       ├── workflow.md
│       └── output-contract.md
├── references/
│   ├── cn-patent-drafting-guide.md
│   ├── draft-schema.md
│   └── patent-figure-guide.md
├── scripts/
│   ├── audit_claims.py
│   ├── build_patent_package.py
│   ├── init_patent_project.py
│   ├── render_flowchart_svg.py
│   ├── render_patent_docx.py
│   └── validate_patent_draft.py
├── tests/
│   └── test_validation.py
└── evals/
    └── evals.json
```

## Routing Model

The short `SKILL.md` acts as the router. `manifest.yaml` selects only the fragments needed for the current request:

- `source_format`: `pdf-text`, `scanned-pdf`, `pasted-text`, or `mixed-project`
- `task_mode`: `full-draft`, `claim-set`, `disclosure-analysis`, or `paper-patent-audit`
- `invention_type`: `algorithm-software`, `apparatus-system`, `process-material`, or `mixed`

The always-loaded core defines evidence discipline, staged drafting workflows, and output contracts.

## Default Workflow

1. Record inputs, publication status, inventor questions, and ownership notes.
2. Establish a full-text source map.
3. Build terminology, formula, figure, and input-operation-output inventories.
4. Construct the evidence ledger.
5. Formulate the inventive concept and claim strategy.
6. Draft and review the claim set.
7. Align the specification, formulas, drawings, embodiments, and abstract.
8. Validate and generate the complete application package.

Each stage includes explicit quality gates. Unsupported features are excluded from formal claims, and unresolved facts are retained as inventor questions rather than fabricated.

## Installation

Install the entire directory rather than just `SKILL.md`, as the router depends on `manifest.yaml`, `static/`, `references/`, and `scripts/`.

Install dependencies:
```bash
pip install -r requirements.txt
```

Run verification tests:
```bash
pytest tests/
```

## Example Requests

- "Please read and follow the nature-paper-to-patent skill."
- "Analyze paper/paper.pdf and generate an invention patent draft."
- "Create separate DOCX files for Claims, Specification, Abstract, and Abstract Drawings."
- "Preserve core source formulas as editable Office Math."
- "Generate main flowcharts and methodology drawings aligned with the claims."
- "Map every substantive claim feature to source evidence."

## Default Deliverables

```text
outputs/
├── patent-claims.docx
├── patent-specification.docx
├── patent-abstract.docx
├── patent-abstract-drawings.docx
└── patent-complete-review.docx
```
