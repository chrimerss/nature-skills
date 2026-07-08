# `nature-data` Skill

`nature-data` prepares or audits Data Availability statements, data repository plans, dataset citations, and FAIR metadata checks for Nature / Springer Nature style submissions.

This skill supports author notes in any language. Users can describe situations like "data available upon request", "raw data", "restricted data", or "public repository"; the skill converts these into submission-ready English statements and provides English confirmation checklists when needed.

## Features

- Drafts Data Availability statements ready to paste directly into manuscripts.
- Audits weak or incomplete data availability statements prior to submission.
- Maps each dataset supporting the results to a repository, accession number, DOI, or access route.
- Differentiates between public data, controlled-access data, third-party data, supplementary material data, and not-applicable scenarios.
- Prepares FAIR metadata and DataCite-style dataset citation checks.
- Flags missing repository records, licenses, provenance, embargo details, and access conditions.
- Aligns author intent with Nature-style English data availability wording.

## Source Hierarchy

- Research data policies of Nature Portfolio and Springer Nature.
- Reporting standards for the availability of data, code, materials, and experimental protocols from Nature Portfolio.
- Best practices from Scientific Data regarding repositories, originality, long-term preservation, and data citation.
- FAIR Guiding Principles and DataCite metadata specifications.

## File Structure

This skill adopts a router/static-dynamic architecture: `SKILL.md` acts as a short router, while `manifest.yaml` loads the persistent core and on-demand references. `nature-data` is a linear workflow without a content axis.

```text
nature-data/
├── SKILL.md                     # Short router
├── manifest.yaml                # always_load core + on-demand references
├── README.md
├── agents/
│   └── openai.yaml
├── static/
│   └── core/                    # Always loaded
│       ├── stance.md            # Default stance and source hierarchy
│       └── workflow.md          # 8-step workflow and output format
└── references/
    ├── fair-metadata-checklist.md
    ├── policy-principles.md
    ├── repository-and-identifiers.md
    ├── source-basis.md
    └── statement-patterns.md
```

## Applicable Scenarios

- Preparing Data Availability statements for Nature series or Springer Nature journals.
- Deciding which repository to deposit data into prior to submission.
- Revising vague "available on request" statements.
- Handling controlled-access, human participant, commercial proprietary, or third-party data.
- Citing datasets with DOIs, accession numbers, Handles, ARKs, or repository records.
- Checking whether data archiving meets the FAIR standards required for submission.
- Converting informal data availability notes into accurate English submission text.

## Design Intent

This skill requires every dataset supporting paper conclusions to have an explicit, traceable access route. It never fabricates accession numbers, licenses, restrictions, or repository metadata. When information is missing, it provides a usable draft along with a concise checklist of items the author must confirm. All outputs and explanations are provided exclusively in English.
