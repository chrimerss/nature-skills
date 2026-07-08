# nature-ref-verifier

## Purpose

Verify academic reference metadata accuracy entry-by-entry. Ideal for pre-submission checks, responding to reviewer citation queries, and regular Zotero library maintenance.

## Workflow Overview

1. **Parse Input** — Accepts reference lists from entire manuscripts, single citations, BibTeX files, or Zotero item keys.
2. **Multi-Source Parallel Query** — Queries Crossref / IEEE Xplore / Web Search / Zotero concurrently based on available tools.
3. **Field-Level Comparison** — Compares fields individually, categorizing discrepancies by severity into 🔴 Critical (must fix) / 🟡 Warning (suggest checking) / 🟢 Info (for reference).
4. **Confidence Evaluation** — Outputs ✅ Verified / ⚠️ Check suggested / ❌ Needs fix / ❓ Unverifiable.
5. **Output Report** — Generates Markdown summaries / BibTeX patches / Zotero update instructions.

## Design Background

This skill originated from real-world reference verification issues encountered in academic writing:

| Issue Type | Example | Detection Method |
|---|---|---|
| Fabricated Author | Smogavec P → Leckebusch J | CrossRef DOI lookup |
| Reversed Author Order | Vainikainen → Mikhnev | Official journal/IEEE website |
| Volume Year vs. DOI Year | Dadrass Vol. 2025 / Online 2024 | Multi-source comparison |
| Incorrect Page Numbers | Noon: 1444-1449 → 1309-1319 | IEEE Xplore |
| Author Name Misspelling | Zhao Y. → Zhao T. | Publisher database |
| DOI Pointing to Wrong Paper | Abidi: Incorrect DOI | CrossRef |

A single search engine (Google Scholar / Bing / Crossref) is insufficient to cover all issue types; multi-source cross-verification is required.

## Environment and Dependencies

Optional tools (enabled if present):

- `zotero-cli` / `zotero-mcp` — Read Zotero libraries and update entries
- `academic-search` — Academic database search
- `WebSearch` / `FetchURL` — General web search fallback

## Usage

Simply instruct the agent:

```
Please verify the references in this paper
```

```
Verify this citation: Farquharson G, Langman A. ... 1999
```

```
Check my bib file and output the corrected version
```
