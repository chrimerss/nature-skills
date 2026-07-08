# Manual Review Compilation Workflow

End-to-end review writing workflow from zero inventory to submission, applicable for literature integration after determining the topic direction. Complementary to the daily automated pipeline — the pipeline handles daily discovery, while this file manages intensive review drafting.

## Phase 1: Inventory Assessment

### 1.1 Extract from Vault
- Use `gbrain_query` to search topic keywords
- Use `gbrain_search` to search the broadest keywords (e.g., `corrosion`) to catch missed items
- Deeply read core pages (e.g., review chapter drafts) and extract citation lists

### 1.2 Extract from Zotero
- `zotero_search_items` for topic keywords, `qmode=everything`
- Deduplicate (cross-check with vault contents)
- Grade by relevance (A = directly relevant / B = partially relevant / C = background)

### 1.3 Summary Assessment
- Estimate literature quantity and determine if supplementary searches are needed
- Compare against the review framework to identify weak sub-directions

## Phase 2: Gap Filling

### 2.1 Identify Gaps
Common gap types:
- Insufficient literature on specific systems (e.g., impurity effects)
- Scarcity of data on specific mechanistic angles (e.g., quantitative spalling criteria)
- Systemic gaps at specific time scales (>10000h) — mark as domain gaps rather than continuing search
- Omission of work from specific research groups

### 2.2 Targeted Search
- `web_search` across different keyword combinations
- Trace citation chains of key papers (who cited foundational domain papers?)
- Search domain-specific databases or regional journals for incremental insights

### 2.3 Extraction and Screening
- `web_extract` to pull full text/abstracts of key papers
- Record gap-to-literature mappings
- Re-evaluate whether total literature volume meets targets (review target journals typically require 80-150 citations)

## Phase 3: Audience Filtering

For collaborator review versions, apply audience-relevant filtering principles:

| Principle | Action |
|-----------|--------|
| Audience's domain | Remove papers the audience already knows well |
| Unfamiliar domains | Retain quantitative data papers in that direction as incremental information |
| Far from main thread | Trim pure methodology or tangential papers |
| Low incremental value | Trim papers with redundant findings or regional papers without global scope |
| Retain collaborator work | Retain relevant papers from the same institution or collaborator team |

Typical trim ratio: 90 → 50 papers.

## Phase 4: Architecture Design

### 4.1 Overall Narrative
- A causal chain running through: environmental chemistry → structure formation → failure modes → engineering controls
- Avoid catalog-style listing of material A → B → C
- Core chapters (failure modes) should account for ~30% of total length

### 4.2 Typical 7-Section Structure
```
§1 Introduction         (~8% length, low citation density)
§2 Chemical Environment (~13%, medium)
§3 Formation/Structure  (~17%, medium-high)
§4 Failure Modes ★Core  (~27%, high)
§5 Control Factors      (~13%, medium-high)
§6 Methodology          (~10%, medium)
§7 Engineering Outlook  (~10%, low)
```

Citation distribution: Core chapters account for about 16 out of 50 citations.

## Phase 5: Figure Planning

### 5.1 Category A Figures (Self-drawn)
Do not require raw data; draw using concept diagram tools:
- Structural schematics (e.g., oxide bilayer)
- Causal flowcharts (e.g., material chemistry → failure chain)
- Mechanism comparison diagrams (e.g., four failure modes)
- Conceptual phase diagrams (e.g., stability zones)
- Methodology comparison tables

Typical quantity: 8-10 figures.

### 5.2 Category B Figures (Cited)
Require cropping from published papers, annotated with "adapted from":
- SEM cross-sections (empirical images)
- Quantitative relationship curves (e.g., corrosion rates)
- Comparative bar charts (e.g., isothermal vs. thermal cycling)

Prioritize selecting from benchmark domain papers: foundational series, representative reviews, latest breakthroughs.

## Phase 6: BibTeX Export

- Create `.bib` file under `outputs/literature/`
- Each entry includes: title, author, journal, volume, pages, year, doi, abstract (brief annotation)
- Use `%` comments to group by section
- Enable drag-and-drop import into reference managers like Zotero

## Appendix: Example Review Parameters

This section illustrates parameters from a sample review for reference:

- Topic: material oxidation and failure in high-temperature environments
- Total literature: 90 → 50 papers (streamlined for target audience)
- Category A figures: 8 figures (fig1-fig8, see `outputs/figures/`)
- Category B figure requirements: 3-4 figures (SEM cross-sections / quantitative curves)
- Length: ~15,000 words → ~36-40 typeset pages
- Target journal candidates: Domain-specific corrosion and materials science journals
