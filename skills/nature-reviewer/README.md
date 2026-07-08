# `nature-reviewer` Skill

`nature-reviewer` simulates a `Nature`-style pre-submission review package from the reviewer's perspective, rather than drafting responses from an author rebuttal perspective.

This skill is built specifically upon the review-related guidelines in the official `Nature` editorial criteria and processes:

```text
https://www-nature-com/nature/for-authors/editorial-criteria-and-processes
```

Its core motivation is clear:

- Extract reviewer-related rules from official `Nature` guidelines.
- Ensure simulated peer review adheres strictly within these rule boundaries.
- Avoid drifting into generic peer-review habits or fictional reviewer personas.
- Provide a reusable `nature-reviewer` skill conforming to standard repository skill formats.

Therefore, this skill remains deliberately conservative. Grounded in the local source copy at `references/editorial criteria and processes.md`, it enforces a stable output convention: `3 reviewer reports + 1 cross-review synthesis`. The three reports differ only in analytical emphasis, as the source guidelines support review functions and report structure, but do not endorse fabricating specific reviewer identities or fictional professional personas.

## Features

- Reads manuscript drafts, abstracts, selected sections, figures, or author notes as a review input package.
- Evaluates work across source-defined `Nature` dimensions: `originality`, `scientific importance`, `interdisciplinary readership`, `technical soundness`, and `readability for nonspecialists`.
- When a manuscript belongs to a distinct technical domain, invokes domain evidence-chain gates on demand, covering chemistry, engineering, materials, atmospheric/climate ecology, hydrology, and remote sensing.
- Generates `3` reviewer reports; differences reflect varying emphasis without fabricating identities or background personas.
- Explains which readers will be interested in the results and why.
- Identifies technical failings that must be resolved before author claims can be accepted.
- Synthesizes consensus and divergent emphases across all three reports.
- Flags unsupported claims and aspects that cannot be assessed from provided evidence.

## Applicable Scenarios

- Simulating `Nature` reviewer feedback prior to submission.
- Stress-testing whether a manuscript possesses a credible broad-interest narrative.
- Evaluating novelty, significance, or technical soundness from a reviewer perspective.
- Generating pre-submission peer-review style critiques.
- Assessing whether a manuscript is readable by non-specialists.
- Obtaining a bounded peer-review style critique rather than an author rebuttal letter.

If you need to draft point-by-point rebuttals or revision letters, use `nature-response`.

## Default Output

Unless another format is requested, the skill returns:

1. `Review setup`
2. `Reviewer 1`
3. `Reviewer 2`
4. `Reviewer 3`
5. `Cross-review synthesis`
6. `Risk / unsupported claims`

## Core Rules

- Evaluations must be grounded exclusively in local reviewer source guidelines and user-provided manuscript facts.
- The three reviewers use the identical factual basis, varying only in factual weighting and emphasis.
- Never fabricate reviewer identities, sub-discipline roles, institutions, or hidden domain knowledge.
- Domain gates may only be used to strengthen technical evidence-chain evaluation; they must not rewrite reports into fictionalized personas (e.g., "the chemistry reviewer", "the statistical reviewer").
- Must explicitly answer `who will be interested in the new results and why`.
- Must explicitly identify `technical failings` impeding the validity of author claims.
- Distinguish between technical validity and broad-interest fit; source guidelines treat them as related but distinct.
- Use `AUTHOR_INPUT_NEEDED`, `Not assessable from provided material`, or similar uncertainty tags when evidence is lacking; never fabricate details.

## Source Hierarchy

- `references/editorial criteria and processes.md` is the primary authoritative local source.
- User-provided manuscript facts and evidence.
- Conservative local implementation rules summarized in `references/source-basis.md`.

This skill must not silently expand into generic reviewer roles, fictional personas, or speculative journal policies.

## File Structure

```text
nature-reviewer/
├── README.md
├── SKILL.md
└── references/
    ├── editorial criteria and processes.md
    ├── source-basis.md
    ├── reviewer-workflow.md
    ├── review-axes.md
    ├── domain-specific-review-gates.md
    ├── report-structure.md
    ├── role-boundaries.md
    └── qa-checklist.md
```

## Status

Draft. The initial version is defined by source guidelines and structured as a grounded review simulation, but has not yet been validated against a benchmark corpus of real anonymous manuscript-review examples.
