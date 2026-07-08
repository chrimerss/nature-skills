---
name: nature-ref-verifier
description: >-
  Performs multi-source cross-verification on academic references entry by entry. Compares authors, titles, years, volumes, issues, and pages field by field, flagging conflicts such as volume-year/DOI-year discrepancies, author sequence anomalies, and page number errors, and outputs a structured verification report.
  Can process reference lists from full manuscripts or research proposals in batch, or verify single entries, supporting synchronized corrections with Zotero.
---

# nature-ref-verifier — Multi-Source Academic Reference Verification Skill

## Triggers

`verify references`, `check references`, `reference verification`, `ref check`

## Applicable Scenarios

- Final verification of all references before submitting a proposal or manuscript
- Pinpointing issues when editorial or reviewer feedback highlights citation errors
- Batch validating effectiveness when migrating references from older projects to new papers
- Regular health checks for Zotero libraries

## Workflow

### Step 1: Parse Input

Supports three input formats:

**A. Full Manuscript / Proposal**
- Extracts reference lists formatted with `[N]` numbering
- Automatically identifies DOIs for each entry (if present)

**B. Single Reference Entry**
- User directly pastes a single citation string
- Or passes a Zotero item key

**C. BibTeX File**
- Directly parses `.bib` files and verifies entry by entry

### Step 2: Multi-Source Parallel Query

For each reference, queries the following sources concurrently (availability depends on environment configuration):

| Source | Applicable References | Typical Coverage |
|---|---|---|
| **Crossref** | English journal papers with DOIs | ~70% (older IEEE papers or local journals often missing) |
| **IEEE Xplore** | IEEE journals / conferences | Fallback when IEEE DOIs return 404 |
| **WebSearch (Bing/Google)** | References without DOIs or missing from sources | Fallback solution |
| **Academic Databases** | Regional or institutional theses/journals | Essential for specialized regional literature |
| **Zotero Local Library** | Existing library entries | Fast comparison against local data |

**Query Strategy:** Prioritize DOI lookup via Crossref; on failure, downgrade to web search using title + authors.

### Step 3: Field-Level Comparison

Executes the following comparison matrix for each entry, categorized into three severity levels:

#### 🔴 Critical (Must Fix)

| Check Item | Description | Typical Case |
|---|---|---|
| Author **Name/Order** Mismatch | Different first author, reversed order, completely fabricated | Smogavec→Leckebusch, Vainikainen→Mikhnev |
| **Page** Discrepancy ≥5 | Page numbers completely mismatched | Noon: 1309-1319→1444-1449 |
| **Title Core Word** Mismatch | Non-case/punctuation differences | Iwasaki T→Wu K H, Zhang W→Zhu M H |
| DOI Pointing to Different Paper | DOI exists but title/author does not correspond | Abidi 1995: 10.1109/4.482157→10.1109/4.482187 |

#### 🟡 Warning (Suggest Checking)

| Check Item | Description | Typical Case |
|---|---|---|
| **Volume Year** ≠ DOI Year | Volume attribution year differs from DOI registration year | Dadrass Vol 2025/Online 2024, Ni Vol 2022/DOI 2020 |
| Author **Middle Name Missing/Extra** | "Rabiner L" vs "Rabiner L R" | Generally does not affect retrieval |
| **Issue Number** Missing | Volume present without issue | Smogavec 2025: 17→17(10) |
| Page Discrepancy ≤4 | Minor differences | Leckebusch 15-24→15-25 |
| Publisher Name Variation | "IET" vs "IEE" | Historical name changes |

#### 🟢 Info (For Reference Only)

| Check Item | Description |
|---|---|
| Title Case Differences | Title Case vs Sentence case |
| Journal Abbreviation vs Full Name | "IEEE Trans. AES" vs "IEEE Transactions on Aerospace and Electronic Systems" |
| Punctuation/Conjunction Differences | "and" vs "&", etc. |

### Step 4: Confidence Evaluation

Assigns an overall confidence rating to each reference entry:

| Level | Meaning |
|---|---|
| ✅ **Verified** | Consistent across multiple sources, no changes needed |
| ⚠️ **Check suggested** | Contains 🟡 level discrepancies, requires manual judgment |
| ❌ **Needs fix** | Contains 🔴 level discrepancies, must be corrected |
| ❓ **Unverifiable** | Cannot be found across any sources (e.g., internal reports, older theses) |

### Step 5: Output Report

Supports the following output formats:

**Markdown Summary Report:**
```markdown
## Verification Results: 56 References

- ✅ Verified: 42
- ⚠️ Check suggested: 8
- ❌ Needs fix: 4
- ❓ Unverifiable: 2

### ❌ Must Fix
| # | Issue | Current Value | Correct Value | Source |
|---|---|---|---|---|
| [6] | Author Error | Smogavec P | Leckebusch J | Wiley |
| [42] | Reversed Author Order | Vainikainen P… | Mikhnev V A… | IEEE |

### ⚠️ Suggest Checking
| # | Issue | Details |
|---|---|---|
| [18] | Volume Year / DOI Year Discrepancy | Volume year 2025, DOI year 2024 |
```

**BibTeX Patch:** Directly generates corrected `.bib` file contents.

**Zotero Update Instructions:** Generates executable commands for updating entries in batch.

## Multi-Source Cross-Verification Strategy

```text
                   ┌─────────────┐
                   │ User Input  │
                   │ DOI / Title │
                   └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
                   │ Field Split │
                   │ author/title│
                   │ year/vol/pg │
                   └──────┬──────┘
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ CrossRef │   │  IEEE    │   │ WebSearch│
    │  (DOI)   │   │ Xplore   │   │ (Bing/GG)│
    └────┬─────┘   └────┬─────┘   └────┬─────┘
         │              │              │
         ▼              ▼              ▼
    ┌──────────────────────────────────────┐
    │  Field-Level Comparison + Rating     │
    │ author / title / year / vol / issue  │
    │       pages / DOI / journal          │
    └────────────────┬─────────────────────┘
                     │
                     ▼
            ┌────────────────┐
            │   Confidence   │
            │ ✅ ⚠️ ❌ ❓    │
            └────────────────┘
```

## Known Limitations and Mitigations

| Limitation | Mitigation |
|---|---|
| **Regional DOIs missing in Crossref** | Downgrade to academic search or general web search |
| **Older IEEE DOIs return 404** | Search directly via IEEE Xplore (DOIs not registered in Crossref) |
| **Theses lacking DOIs** | Verify title + author + year via specialized thesis databases |
| **Product Manuals / Patents** | Skip metadata verification, confirm only accessibility of source |
| **Google Scholar missing certain papers** | Switch search engines (Bing, Semantic Scholar) |

## Environment Dependencies

The following tools are optional; enable if present, downgrade if unavailable:

- `zotero-cli` / `zotero-mcp`: Zotero library read/write
- `academic-search`: Academic database search
- General WebSearch / FetchURL: General fallback
