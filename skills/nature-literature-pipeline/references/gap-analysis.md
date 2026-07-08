# Literature Gap Analysis Methodology

## When to use

When the user asks to confirm whether a specific research topic has been explored:
- "Check if anyone has studied the XX system"
- "Confirm whether this research direction is a gap"
- "See if there is any literature on this quaternary system"

## Workflow (4 steps)

### Step 1: Multi-source search

Search the exact topic string across at least 3 sources:
- Web search with exact phrase match (e.g., `"MgCl2-KCl-NaCl-ZnCl2"`)
- Broader search with key components (e.g., `material A material B compound`)
- Adjacent/related terms (e.g., `compound A thermal storage application`)

→ Record hit counts per query.

### Step 2: Decompose and classify

If direct hits = 0, decompose the system into sub-systems:

| Sub-system | Search | Status |
|------------|--------|--------|
| MgCl₂-KCl-NaCl (ternary) | keyword | studied / not studied |
| NaCl-KCl-ZnCl₂ (ternary) | keyword | studied / not studied |
| MgCl₂-KCl-ZnCl₂ (ternary) | keyword | studied / not studied |
| MgCl₂-NaCl-ZnCl₂ (ternary) | keyword | studied / not studied |

Classify hits into three tiers:
- **Directly relevant**: exact quaternary system → if 0, confirmed gap
- **Partially relevant**: contains 2-3 of 4 components → extract key data (method, salt composition, findings)
- **Irrelevant**: only 1 component → skip

### Step 3: Extract edge papers

For each partially relevant paper, extract:
- Full citation (authors, journal, year, DOI if available)
- Salt composition used
- Method (CV, DSC, XRD, simulation, etc.)
- Key finding relevant to the gap topic
- What can be borrowed for the user's work

### Step 4: Output gap report

Write to `outputs/literature/<topic>_gap_report.md` with these sections:

1. **Core Conclusion** — one sentence: confirmed gap or partial overlap
2. **Sub-system Literature Overview** — table per sub-system with representative works
3. **Partially Relevant Literature** — extracted details from edge papers
4. **Gap Analysis** — why nobody did it + why it's worth doing
5. **Draft Gap Statement** — English paragraph ready for introduction
6. **Recommended Next Steps** — concrete experimental/computational next steps
7. **Search Methodology Log** — all search terms and hit counts (for reproducibility)

### Cost control

- Search: ≤4 parallel web_search calls per decomposition level
- Extract: only edge papers (≤5), not every hit
- No browser: use web_extract, skip paywalled pages silently
- Aim for ≤6 tool calls total
