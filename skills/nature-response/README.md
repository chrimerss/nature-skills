# nature-response Skill

`nature-response` drafts, audits, and revises revision correspondence materials, including point-by-point response letters to reviewers, revision cover letters, red-marked manuscript drafts, and editable LaTeX templates. It is tailored for revision scenarios in Nature series and other high-impact journals.

## Features

- Splits reviewer comments into stable IDs, e.g., `R1.1`, `R1.2`, `R2.1`.
- Directly parses pasted editorial revision emails, extracting manuscript numbers, titles, decision types, deadlines, required files, editor instructions, and reviewer reports, automatically initiating the response package workflow.
- Categorizes each comment by type, severity, required action, evidence needs, and risk.
- Generates a response strategy summary prior to formal drafting.
- Routes tasks dynamically to drafting, auditing, revising, triage-only, or appeal-like workflows.
- If the decision letter contains editor requirements, generates `E.1` editor instruction IDs before processing reviewer IDs.
- Drafts clear, editor-friendly point-by-point response letters.
- Drafts revision cover letters summarizing primary modifications and referencing the point-by-point response document.
- Provides `templates/cover-letter.tex`, `templates/response-to-reviewers.tex`, and `templates/revised-manuscript-redline.tex`.
- Enforces that revised manuscripts must be produced from a backed-up copy, highlighting modifications in red.
- When quoting revised manuscript text within response letters, formats quoted excerpts in italics.
- In LaTeX or print-oriented PDF response letters, enforces page breaks when transitioning between different reviewers' responses.
- Maps every response to a manuscript modification action, location, or missing information flag.
- Reframes defensive or vague author notes into professional academic response language.
- Handles difficult scenarios, such as out-of-scope experiments, reviewer factual errors, conflicting reviewer comments, statistical challenges, and compliance issues.
- Flags missing experiments, analyses, line numbers, citations, figure panels, and manuscript changes without fabricating details.

## Applicable Scenarios

- Preparing revisions for Nature, Nature Portfolio, Springer Nature, or similar high-impact journals.
- Feeding pasted editorial email content directly to the agent to extract revision requirements and generate response packages.
- Responding to major or minor revision feedback.
- Translating reviewer comments into an actionable manuscript modification checklist.
- Auditing rebuttal drafts for missing responses, tone issues, or unsupported claims.
- Translating informal author notes into submission-ready English point-by-point responses.
- Translating informal author notes into submission-ready cover letters or LaTeX response packages.
- Determining how to politely rebut reviewer critiques or explain study scope boundaries.
- Generating LaTeX-formatted cover letters, rebuttal letters, response to reviewers, or red-marked revised manuscripts.

## Default Output

Unless another format is requested, the skill returns:

1. Response strategy summary
2. Comment-response tracker
3. Draft point-by-point response letter
4. Draft revision cover letter (if requested)
5. Marked manuscript changes (if requested)
6. LaTeX files or template paths (if requested)
7. Manuscript change checklist
8. Missing information / risk flags

## Core Rules

- Preserve reviewer comments faithfully before drafting responses.
- Every comment must be addressed, cross-referenced, or explicitly marked as unresolved.
- Every response must map to a specific action, such as `ACCEPT_TEXT`, `ACCEPT_ANALYSIS`, `SOFTEN_CLAIM`, `DISAGREE`, or `AUTHOR_INPUT_NEEDED`.
- Never fabricate experiments, analyses, citations, line numbers, figure panels, supplementary items, reviewer identities, editor instructions, or manuscript changes.
- Maintain cooperative, evidence-first, non-defensive language.
- Treat response letters as verification documents for editor review rather than mere polite correspondence.
- Treat cover letters as executive summaries of revisions for editors; they do not replace point-by-point responses.
- When modifying original manuscripts, highlight changes in red on a backed-up copy rather than overwriting clean drafts directly.
- Quoted revised manuscript text pasted in response letters must be italicized.
- Enforce page breaks between reviewer sections; LaTeX templates implement this via `\ReviewerSection{...}`.

## Source Hierarchy

- Target journal instructions and decision letter requirements.
- Nature / Nature Portfolio / Springer Nature revision and peer-review process guidelines.
- Springer Nature editorial guidance on rebuttal letters.
- Local manuscript facts provided by the author.

Source justifications are summarized in `references/source-basis.md`, including URLs, rule summaries, and source type labels.

## File Structure

This skill utilizes a router/static-dynamic architecture: `SKILL.md` acts as the short router, while `manifest.yaml` loads the persistent core and on-demand references. `nature-response` follows a linear workflow without content axes.

```text
nature-response/
├── README.md
├── SKILL.md                     # Short router
├── manifest.yaml                # always_load core + on-demand references
├── static/
│   └── core/                    # Always loaded
│       ├── stance.md            # Purpose, default stance, red lines, source hierarchy
│       └── workflow.md          # Input types, revision workflow, output format
├── references/
│   ├── source-basis.md
│   ├── response-structure.md
│   ├── latex-templates.md
│   ├── comment-taxonomy.md
│   ├── action-mapping.md
│   ├── tone-and-stance.md
│   ├── difficult-cases.md
│   ├── intake-and-routing.md
│   └── qa-checklist.md
├── templates/
│   ├── cover-letter.tex
│   ├── response-to-reviewers.tex
│   └── revised-manuscript-redline.tex
├── tests/
│   ├── conflicting-reviewers.md
│   ├── defensive-draft-audit.md
│   ├── evaluation-summary.md
│   ├── minor-revision.md
│   ├── major-revision-missing-evidence.md
│   ├── impossible-experiment.md
│   └── rubric.md
└── examples/
    ├── conflicting-reviewers.md
    ├── major-revision-with-missing-evidence.md
    └── minor-revision.md
```

## Status

Beta. Current behavior is defined by synthetic Markdown fixtures and examples. It should be promoted to Stable only after validation against real anonymous revision packages with author consent.
