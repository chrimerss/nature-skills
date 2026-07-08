# `nature-academic-search` Skill

`nature-academic-search` is an academic retrieval skill package for agentic coding workflows, integrating CrossRef, PubMed, arXiv, Scopus, and ScienceDirect literature data sources.

## Features

- **Multi-source concurrent search**: Queries CrossRef, PubMed, and arXiv by default, merging the results.
- **Fetch details by ID**: Supports automatic identification and retrieval by DOI, PMID, or arXiv ID.
- **Formatted citations**: Supports APA, Nature, IEEE, Vancouver, and other citation styles.
- **MeSH vocabulary lookup**: Helps construct precise PubMed search strategies.
- **Literature management scripts**: Supports format conversion across `.nbib`, `.ris`, `.bib`, and `.enw`.
- **Scopus / ScienceDirect**: Supports searches for papers, authors, affiliations, journals, citation overviews, PlumX metrics, and ScienceDirect article metadata.
- **Strict independent citation & high-profile citer audits**: Evaluates whether citing papers are strict independent citations by excluding self-citations, team citations, and obvious collaborative network citations; compiles tables containing article title, publication date, authors, affiliations, citation count, strict independent citation count, and DOI; further identifies influential citers (e.g., academy members, institutional leaders, talent awardees, fellows, highly cited researchers) and extracts how they cite the target paper in the full text.

## MCP Execution

The plugin starts an isolated execution environment using `uv` by default:

```bash
uv run --no-project --directory <mcp-server> --with "mcp>=1.0.0,<2.0.0" --with "requests>=2.28.0,<3.0.0" --with "toml>=0.10.2,<2.0.0" --with "lxml>=4.9.0,<6.0.0" --with "pybliometrics>=4.4.1,<5.0.0" python academic_search_server.py
```

PubMed requires configuring an email address in the `PUBMED_EMAIL` environment variable or in `mcp-server/config.toml`. Scopus / ScienceDirect are optional providers that reuse local `pybliometrics` configuration, reading from `~/.config/pybliometrics.cfg` by default; do not store Elsevier API keys directly in plugin files.

`search_papers` invokes the Elsevier-backed provider only when `sources` explicitly includes `scopus` / `sciencedirect` to avoid unintentionally consuming Elsevier API quotas.

## MCP Tools

| Tool | Description |
|------|-------------|
| `search_papers` | Default concurrent search across three sources; can explicitly add Scopus / ScienceDirect |
| `get_paper_by_id` | Fetch details by DOI, PMID, or arXiv ID |
| `get_citation` | Generate formatted citation string |
| `lookup_mesh` | Query MeSH vocabulary |
| `search_scopus` | Scopus advanced search |
| `get_scopus_abstract` | Scopus abstract and detailed metadata |
| `get_scopus_citation_overview` | Scopus citation overview |
| `search_scopus_authors` / `get_scopus_author` | Author search and details |
| `search_scopus_affiliations` / `get_scopus_affiliation` | Affiliation search and details |
| `search_scopus_serial_titles` / `get_scopus_serial_title` | Journal and serial title search and details |
| `get_scopus_plumx_metrics` | PlumX metrics |
| `search_sciencedirect` | ScienceDirect search |
| `get_sciencedirect_article_metadata` | ScienceDirect article metadata |

## Strict Independent Citations & Citer Profiling

When the user asks about strict independent citations, self-citation exclusion, who cited an article, influential citers, article citation tables, or citation tabulation, this skill loads `references/workflows/wf6-strict-other-citation-impact-audit.md`.

The default standard for this workflow is stricter than general "non-self-citation":

1. First confirm the target paper's DOI, authors, affiliations, and available author IDs.
2. Compile citing papers from Scopus, Web of Science, Semantic Scholar, OpenAlex, CrossRef, or publisher cited-by pages, noting coverage limits.
3. Exclude direct self-citations, same-team/same-group citations, obvious collaborative network citations, and cases with insufficient metadata.
4. If a table is requested, output: `Title / Publication Date / Authors / Affiliations / Total Citations / Strict Independent Citations / DOI / Evidence Notes`.
5. For strict independent or potential external citers, verify status signals such as academy member, university president/dean, national talent awardee, Fellow, or highly cited researcher.
6. Extract citation context from accessible full texts to classify whether the target paper is cited as background, method, comparison, extension, reproduction, critique, or review.

All status labels must be accompanied by evidence sources; cases where identity cannot be confirmed must be marked as `unverified`.
