# Literature Note Template (v2 — 2026-06-03)

> Standardized template for literature notes. Use for all new vault literature notes.
> Replaces the v1 template (date/suggested_class/worth_full_read format).

## Standardized Frontmatter

```yaml
---
title: "Original English Title"
authors: "Last1, F.; Last2, F."
year: 2024
journal: "Full Journal Name"
doi: "10.xxxx/..."
classification: "A_Core_Thread"
tags: [keyword1, keyword2, keyword3]
date_read: 2026-06-03
---
```

### Field Rules

| Field | Format | Example |
|-------|--------|---------|
| `title` | Original English, double-quoted | `"Corrosion of Alloys and Metals by Molten Nitrates"` |
| `authors` | `Last, F.; Last, F.` — comma+semicolon separated, >3 use `et al.` | `"Smith, J.A.; Jones, R.B."` |
| `year` | 4-digit integer, no quotes | `2004` |
| `journal` | Full name or report ID, double-quoted | `"Journal of Materials Engineering and Performance"` |
| `doi` | Full DOI string starting with `10.` | `"10.1016/j.solmat.2019.02.012"` |
| `classification` | **Must be full classification name** — one of: `A_Core_Thread`, `B_Chapter_Support`, `C_Engineering_Context`, `D_Method_Reference`, `E_Low_Priority` | `"A_Core_Thread"` |
| `tags` | YAML list, 3-5 specific keywords | `[nitrate, corrosion, oxide_ion, review]` |
| `date_read` | ISO date of first detailed reading | `2026-06-03` |

**Anti-patterns (do NOT use)**: `date` (use `year`), `suggested_class` (use `classification`), `worth_full_read` (covered by classification), `source_urls` (extraneous), `note_date` (use `date_read`).

## Body Structure (6 sections)

```markdown
## Core Claim
[1-3 sentences. Mark evidence strength: established consensus / emerging / controversial / speculative]

## Methods
[Key methods, advantages, limitations]

## Key Findings
[Bullet points of key data/findings/quantitative results]

## Critique
[Strengths, weaknesses, relevance gaps, evidence reliability]

## Connection to Research
[How this connects to the user's thesis: NO2-/NO3- ratio, CV fingerprint, atmosphere control, Hitec purification, material selection, experimental design]

## Next Steps
[Actionable: cite in which chapter, follow up which reference, design which experiment, what to verify]
```

**Note**: No `# Heading` title line before the sections — the frontmatter `title` field serves that role. Avoid duplicate H1 headers.

## File Naming Convention

Format: `{FirstAuthorLast}{Year}_{Keywords}.md`

- **First author**: last name only, title-cased. For hyphenated names preserve the hyphen (e.g., `Encinas-Sánchez`).
- **Year**: 4 digits, no space after author name.
- **Keywords**: 2-4 words connected by underscores, derived from the paper's core contribution (not generic like `paper`).

### Examples

| Good | Bad |
|------|-----|
| `Goods2004_commercial_nitrates_304_316_corrosion.md` | `goodscorrosionofstainlesssteelscarbon2004.md` |
| `Author2018_topic_method.md` | `authortopicmethodology2018.md` |
| `Kruizenga2011_316SS_failure_analysis.md` | `kruizengastainlesssteelcorrosion2011.md` |
| `Author2025_topic_application.md` | `author2025topicengineeringapplication.md` |

## Directory Discipline

Subagents frequently create short directory names (`A/notes/`, `B/notes/`). Always verify and correct to full names:

- `A_Core_Thread/notes/`
- `B_Chapter_Support/notes/`
- `C_Engineering_Context/notes/`
- `D_Method_Reference/notes/`
- `E_Low_Priority/notes/`

## Bulk Standardization

When standardizing a batch of existing notes, the Python script pattern is:

1. Inventory all `.md` files across A-E directories
2. Parse existing frontmatter → extract known fields
3. Infer missing fields from body content (year regex, author regex, title from H1)
4. Generate standardized frontmatter + remove body H1 duplicates
5. Generate new filename from `AuthorYear + keywords`
6. Write to same directory, rename + collision-check
7. Save rename mapping CSV for rollback

Key extraction patterns:
- Year: `(19|20)\d{2}` in filename or frontmatter
- Authors: `\*\*([^*]+?)\s*\((\d{4})\)\*\*` in body for old-format notes
- Title: frontmatter `title` field or body `# Heading`
- Classification: normalize `A`/`B`/`C`/`D` → full classification names, default to directory name
- Tags: keyword pattern matching on title + body[:1000] against a domain tech-term map
