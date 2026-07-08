# Common Reference Verification Issues and Patterns

This document records common metadata error patterns in academic references as a reference during verification.

## 1. Volume Year vs. DOI Year Discrepancies

**Root Cause:** The year in a DOI number is typically the submission year or manuscript assignment year, whereas the citation should be based on the official journal volume year.

| Pattern | Description | Example |
|---|---|---|
| DOI year < Volume year | Manuscript assigned prior to official publication | DOI contains 2024, Vol is 2025 → Cite **2025** |
| DOI year > Volume year | Cross-year processing | DOI contains 2025, published in 2026 → Cite **2026** |
| Online year ≠ Volume year | Online at year-end, assigned to next year's volume | Online 2024-12-31, Vol is 2025 → Cite **2025** |

**Rule:** Prioritize the official journal volume year; if no volume number exists, use the online publication year.

## 2. Author Name Issues

### 2.1 First Author Completely Fabricated

The most common "hallucination" in AI-generated citations—the author is completely different from the actual DOI author. This is a critical error.

**Detection Method:** Query CrossRef / IEEE via DOI and compare the first author's surname.

### 2.2 Reversed Author Order

When exporting from databases or manually compiling, non-first authors may mistakenly be placed first.

**Detection Method:** Verify against the author order on the official journal publication page.

### 2.3 Author Name Typo / Character Confusion

- Visually similar letters or characters may be miswritten during manual data entry
- Verify against the publisher's official record

### 2.4 Spanish / Portuguese Dual Surnames

Dual surnames (paternal + maternal) have multiple acceptable abbreviation styles, **all of which are valid**:
- `Álvarez López Y` = `López Y Á` = `Alvarez Lopez Y`

### 2.5 "et al." vs. Full Author List

Using "et al." in citations is acceptable where formatting guidelines permit. If listing all authors (recommended for 3–5 authors), ensure the order matches the original publication exactly.

## 3. Page Number Errors

Commonly occurs in the following scenarios:
- Preprint page numbers vs. official publication page numbers
- Early conference paper versions vs. final proceedings versions
- Same paper appearing in both journal special issues and conference proceedings with different pagination
- Data entry slips (e.g., copying pagination from an adjacent row)

**Detection Method:** Rely on official journal/conference websites rather than raw database exports.

## 4. DOI Issues

### 4.1 DOI Pointing to a Different Paper

The DOI format is valid but points to a completely different paper—typically due to a single-digit typo (e.g., 482157 → 482187).

**Detection Method:** Look up the DOI on CrossRef and check whether the returned title matches.

### 4.2 Older IEEE DOIs Returning 404

For IEEE papers published before 2000, CrossRef queries often return 404, but they are searchable on IEEE Xplore. **Do not mark these as errors**.

### 4.3 Regional DOIs Missing in CrossRef

Certain regional journals register DOIs in local or national systems rather than CrossRef, so CrossRef API queries return empty. Verify via the journal's official database or web search.

### 4.4 Multiple DOIs for the Same Paper

Preprint, official publication, and OA versions may have different DOIs. Prioritize the official publication DOI.

## 5. Conference Paper Years

- The same paper may have different years and pagination in conference proceedings versus journal special issues
- Conferences may have multiple acronyms or aliases; use the official IEEE/publisher name
- Use the actual conference year, not the proceedings publication year

## 6. Theses and Dissertations

- Many theses published before the 2000s are not digitized
- Standard thesis citation format: `Author. Title [D]. Institution, Year.`
- Page numbers may be omitted
- Specialized thesis databases often provide better coverage than general search engines

## 7. Product Manuals / Technical Reports

- Marked with `[Z]` (other documents) in standard citation schemas
- Verification method: Confirm the product/organization exists and the official webpage or document is accessible
- Use the release year of the referenced version

## 8. Historical Publisher Name Changes

For example, IEE (Institution of Electrical Engineers) merged to form IET (Institution of Engineering and Technology) in 2006. Books or papers published before 2006 should be cited as **IEE**, not IET. Both names refer to the same lineage, but citations should respect historical accuracy.
