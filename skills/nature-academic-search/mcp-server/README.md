# Unified Academic Search MCP Server

This is the unified academic search MCP server, integrating CrossRef, PubMed, arXiv, Scopus, and ScienceDirect data sources.

## Tools

| Tool | Function |
|------|----------|
| `search_papers` | Unified search supporting concurrent queries across multiple sources |
| `get_paper_by_id` | Fetch details by DOI, PMID, or arXiv ID |
| `get_citation` | Formatted citation string supporting APA, Nature, IEEE, etc. |
| `lookup_mesh` | MeSH vocabulary query |
| `search_scopus` | Scopus advanced search |
| `get_scopus_abstract` | Scopus abstract and detailed metadata |
| `get_scopus_citation_overview` | Scopus citation overview |
| `search_scopus_authors` / `get_scopus_author` | Author search and details |
| `search_scopus_affiliations` / `get_scopus_affiliation` | Affiliation search and details |
| `search_scopus_serial_titles` / `get_scopus_serial_title` | Journal and serial title search and details |
| `get_scopus_plumx_metrics` | PlumX metrics |
| `search_sciencedirect` | ScienceDirect search |
| `get_sciencedirect_article_metadata` | ScienceDirect article metadata |

## Configuration

Environment variables:

- `PUBMED_EMAIL`: Required by NCBI.
- `NCBI_API_KEY`: Optional, used to increase rate limits.
- Elsevier / Scopus / ScienceDirect: Reuses `pybliometrics` configuration files, located by default at `~/.config/pybliometrics.cfg`.

`search_papers` queries CrossRef, PubMed, and arXiv by default. Scopus / ScienceDirect are optional providers: the Elsevier API is only accessed when `scopus` / `sciencedirect` is explicitly passed in `sources` or when dedicated Scopus / ScienceDirect tools are invoked.

This prevents default searches from unintentionally consuming Elsevier API quotas; if local `pybliometrics` configuration is missing, an error for that specific data source will be returned in the JSON `errors` field.

Configuration file: `config.toml`

## Usage

The plugin launches an isolated execution environment via:

```bash
uv run --no-project --directory <mcp-server> --with ... python academic_search_server.py
```

These tools are invoked by the `academic-search` skill.
