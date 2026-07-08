# `nature-citation` Skill

`nature-citation` turns paper paragraphs, manuscript excerpts, or scientific claims into reviewable Nature / CNS series reference candidates, and exports files directly importable by reference managers.

This skill supports multilingual input. Users can make requests like "segment citation", "Nature series citations", "CNS and sister journals", "add citations", "supporting literature", "export Zotero", etc.; the skill will search using English scientific concepts and return review explanations in English.

## Features

- Splits manuscripts into citable claim units with stable numbering, e.g., `S001`, `S002`, `S003`.
- Generates search queries for structured metadata sources like Crossref for each segment.
- Restricts results to Nature Portfolio, AAAS Science family, Cell Press, or flagship-only scopes.
- Matches candidate references for each segment and suggests insertion points in the text.
- Exports an `ENW`, `RIS`, or Zotero `RDF` reference management file.
- Optionally generates JSON, TSV, Markdown, and HTML review materials for manual screening.
- Supports long-article batch processing, partial checkpoints, failure retries, and local paragraph runs.
- Supports DOI-only export, suitable for scenarios where the user has already confirmed a reference list.

## Source Hierarchy

- Crossref structured metadata and DOI records.
- PubMed / NCBI E-utilities for biomedical cross-checking when relevant.
- Official publisher pages of Nature Portfolio, AAAS Science, and Cell Press.
- Secondary academic indexes are used only as discovery leads and cannot serve as sole supporting evidence.

## File Structure

This skill adopts a router/static-dynamic architecture: `SKILL.md` acts as a short router, while `manifest.yaml` determines persistent content and on-demand reference files. `nature-citation` is a linear workflow without a content axis, thus primarily consisting of persistent core content and on-demand references.

```text
nature-citation/
├── SKILL.md                     # Short router
├── manifest.yaml                # always_load core + on-demand references
├── README.md
├── static/
│   └── core/                    # Always loaded
│       ├── principles.md        # Artifacts, journal scope, source hierarchy, search rules
│       └── workflow.md          # 7-step workflow and report format
├── references/                  # Opened on demand
│   ├── script-usage.md          # nature_citation.py arguments and long-article batching
│   ├── journal-scope.md
│   ├── ris-endnote.md
│   └── search-strategy.md
└── scripts/
    └── nature_citation.py
```

## Applicable Scenarios

- Adding citations to abstracts, introductions, results, discussions, or single paragraphs.
- Splitting long texts into "segment - candidate reference" correspondence tables.
- Restricting searches exclusively to `Nature series`, `CNS`, `CNS and sister journals`, or `Flagship only`.
- Exporting records for EndNote, Zotero, or other reference managers.
- Assessing whether a statement receives direct support, partial support, or background support.
- Generating HTML review pages allowing users to filter by year, select references, and download records.

## Long Text Processing

Short inputs use a standard one-time search workflow. Longer inputs can be processed in batches, writing partial export checkpoints after each batch to prevent progress loss if subsequent batches fail. Temporary Crossref failures are retried automatically.

Rule of thumb:

- 1-10 segments: Standard run.
- 11-25 segments: Prefer batch mode.
- 26+ segments: Prefer running section by section.

## Design Intent

This skill prioritizes defensibility over the quantity of reference candidates. Its goal is to help users discover potential supporting literature within scope, rather than treating metadata as evidence itself. Each exported record preserves authentic metadata without fabricating missing fields, and clearly indicates that manual reading of abstracts or full texts is required to confirm support strength.

For long manuscripts, design goals also emphasize operational stability: smaller batches, fewer interruptions, and clearer checkpoint trails.

## Reference Files

- `search-strategy.md`: Claim decomposition, support grading, and common search failure modes.
- `journal-scope.md`: Nature / Science / Cell family boundaries and flagship journal explanations.
- `ris-endnote.md`: `ENW`, `RIS`, and Zotero `RDF` export instructions.
- `scripts/nature_citation.py`: Local CLI for segmentation, Crossref searching, export, and HTML review page generation.

## Common CLI Arguments

- `--batch-size 2`: Splits long texts into smaller batches for processing.
- `--max-segments 12`: Limits the number of segments processed in a single run.
- `--max-retries 2`: Retries temporary Crossref failures.
- `--sleep 0.3`: Shortens default waiting time between requests.
- `--with-artifacts`: Generates HTML, TSV, JSON, and Markdown review files.

## Notes

- The default artifact is a single reference management file; other review materials must be explicitly enabled.
- `metadata-only candidate` indicates that manual review of the abstract or full text is still required before citing.
- The HTML review page can export user-selected records as `ENW`, `RIS`, or Zotero `RDF`.
- For long texts, `--with-artifacts` is recommended since HTML pages are most convenient for manual screening.
- Batch mode continuously writes `.partial.enw`, `.partial.ris`, or `.partial.rdf` checkpoints before final export.
