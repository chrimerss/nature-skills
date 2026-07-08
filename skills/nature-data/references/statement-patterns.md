# Statement Patterns

Use these patterns as starting points. Replace bracketed fields with verified information. Delete
any sentence that does not apply.

Treat the Note under each pattern as author-facing guidance, not as
submission text. Submit the English statement unless the journal explicitly asks otherwise.

## Public repository, single dataset

```text
The [raw/processed/source] data supporting the findings of this study are available in
[Repository] under accession [ACCESSION] / at [DOI or persistent URL]. The deposited record
contains [brief contents: e.g. raw measurements, processed tables, figure source data, metadata
and analysis inputs].
```

Note: State clearly that raw/processed/source data are stored in a formal repository with accession number, DOI, or permanent link.

## Public repository, multiple datasets

```text
The datasets generated in this study are available as follows: [dataset family 1] in
[Repository] under [DOI/accession]; [dataset family 2] in [Repository] under [DOI/accession];
and figure source data in [Repository/Supplementary Data file] under [identifier or file name].
```

Note: When different dataset types are stored in different repositories or files, describe each separately rather than stating "data available in supplements".

## Data in paper and supplementary files only

Use only when the supporting dataset is genuinely small and fully represented in the article,
source data, or supplementary files.

```text
All data supporting the findings of this study are included in the paper, its Supplementary
Information, and Source Data files. [Name exact Supplementary Tables/Data files when possible.]
```

Note: Use this only when all data supporting conclusions are genuinely present in the paper, supplements, and Source Data files.

## Reused public data

```text
This study used publicly available [dataset name/type] from [Repository or source], available under
[DOI/accession/stable URL]. We used [version/release/date accessed, if relevant]. No new primary
[data type] data were generated for this part of the analysis.
```

Note: When using public databases, specify the database name, version/release/access date, and accession number, and cite the dataset.

## Mixed generated and reused data

```text
Data generated in this study are available in [Repository] under [DOI/accession]. Public datasets
reused in the analysis were obtained from [source 1, identifier/version] and [source 2,
identifier/version]. Source data for [figures/tables] are provided in [location].
```

Note: Separate newly generated data from reused public data to avoid implying all data were generated in this study.

## Controlled-access human or sensitive data

```text
The [data type] data supporting this study are not publicly available because [privacy, consent,
legal, ethical or security reason]. A metadata record is available at [repository/accession, if
available]. Qualified researchers may request access from [data access committee/institutional
office/repository procedure] at [contact or URL]. Access requires [ethics approval/data-use
agreement/other conditions] and will be reviewed according to [policy or committee name].
```

Note: For human participants or privacy/ethical restrictions, do not simply state "unavailable due to privacy"; specify the request pathway and access conditions.

## Third-party or licensed data

```text
The [data type/name] data used in this study were obtained from [third-party provider] under
licence and are not publicly redistributable by the authors. Requests for access should be directed
to [provider/contact/URL]. Derived data that can be shared are available in [repository] under
[DOI/accession], subject to [licence or restriction].
```

Note: For third-party licensed data that cannot be redistributed, identify the data owner and where readers should apply.

## Commercially restricted data

```text
The [data type] data are subject to commercial restrictions and cannot be made publicly available.
Requests for access may be directed to [company/data owner/contact or URL] and are subject to
[approval/licence/payment/confidentiality terms]. The authors provide [summary statistics,
metadata, synthetic data, or source data] in [location] to support interpretation of the results.
```

Note: For proprietary or commercial data, specify the commercial restrictions, the contact for requests, and whether aggregated data or metadata are public.

## Embargoed data

Use only when the repository supports embargo and the journal permits it.

```text
The [data type] data have been deposited in [Repository] under [DOI/accession] and are under
embargo until [date/event]. Reviewers can access the data using [private reviewer link or
repository access route]. The data will become publicly available at [DOI/accession] when the
embargo ends.
```

Note: If data are temporarily restricted under embargo, provide an existing repository record, peer-review access mechanism, and explicit release date/conditions.

## Request-based access with justified restriction

```text
The [data type] data are not publicly available because [specific reason]. Requests for access may
be sent to [institutional group/contact route], and will be considered for [eligible purpose/users]
subject to [approval, agreement, or legal condition]. [Public metadata/aggregate data/source data]
are available at [location].
```

Note: "Available upon reasonable request" is acceptable only when accompanied by the specific reason, receiving institution, review criteria, and available metadata.

## No datasets generated or analysed

Use sparingly.

```text
No datasets were generated or analysed during the current study.
```

Note: Use only when no datasets were generated or analyzed during the study; typically not applicable to empirical research.

For theory papers, be more specific:

```text
This work is theoretical and does not generate or analyse empirical datasets.
```

## Anti-patterns to revise

| Weak wording | Why it fails | Stronger move |
|---|---|---|
| Data are available upon request. | No reason, route, eligibility, or durability. | Add restriction reason, responsible access body, conditions, and metadata. |
| Data are available from the corresponding author on reasonable request. | Often too vague and informal; not durable or specific enough. | Use an institutional/repository access route and define review conditions. |
| Data will be uploaded after acceptance. | No current repository or durable identifier. | Deposit before submission or provide a private reviewer link. |
| All data are in the manuscript. | Often false for figures/statistics. | Name exact source data, supplementary files, and omitted raw data. |
| Data are proprietary. | Does not say who controls access. | Name owner/provider and access route. |
| N/A. | Nature-style instructions usually require an explanation. | State why no datasets were generated or analysed. |

## Audit questions

- Which result would fail if this dataset were unavailable?
- Is the route durable beyond the corresponding author's current email address?
- Can a reader tell what each identifier contains?
- Are restrictions specific enough for an editor to judge them?
- Are reused datasets cited, not merely mentioned?
