# Figure & Table Legend Conventions (Nat Commun 2025 CS/AI corpus)

Use this file when **writing or auditing the legend text** of a figure or table.
It complements `nature-2026-observations.md`, which covers visual/layout
archetypes; this file covers the *words* of the caption. Distilled from a 2025
set of 20 open-access *Nature Communications* computer-science / AI papers
(legend conventions were consistent across all research articles). **Do not copy
source wording.**

## Legend structure — the fixed skeleton

1. **`Fig. N | ` + a bold noun-phrase overall title** that names the whole
   figure. Common openers: *Overview of …*, *Comparison of …*, *Performance of
   …*, or a finding phrase. No terminal full stop required on the title.
2. **`a / b / c …` panels, each described in present tense, telegraphic style**,
   often subject-less: *"a Comparison of the four EMS paradigms. b Distributions
   of WSIs and patches in the pre-training dataset."*
3. **Statistics written into the legend**: sample size `n=`, error type, and
   test — *"mean ± 95% CI (n = 1373) … one-way ANOVA with Tukey correction."*
4. **Data-availability boilerplate** at the end: *"Source data are provided as a
   Source Data file."*

## Tense

- Visual facts in **present** tense — *"are shown as cyan sticks"*, *"depicts"*.
- Methods/how-it-was-made in **past** tense — *"was performed"*, *"was adopted
  from"*.

## Self-containment rule

A legend must be readable away from the body text. Put colour/shape mappings,
sample size, and key numeric anchors (PDB id, RMSD, units) into the legend
itself — *"tRNA-Glu of E. coli (PDB: 2DER chain C). 76 nt, RMSD: 2.88 Å."*;
*"Grey boxes designate what is defined by the benchmark, and orange boxes
indicate what is unique to each solution."*

## Advanced: the claim-closing sentence

A legend's final sentence may advance an argument rather than only describe —
*"…indicating that these co-folding models are not predicting poses based on
physics but rather learning patterns in global structures."* Use sparingly, and
only when the panel actually supports the inference.

## Review/Perspective legends

When a figure aggregates others' published systems, each sub-panel gets a
one-line characterisation (often past tense, describing prior work) and the
legend carries an attribution line — *"adapted with permission from refs. 16,17
… by Springer Nature."* Include the permission/attribution string for any
adapted panel.

## Table captions

Same shape: **`Table N | ` + noun phrase**, with detailed specs pointed to
Methods — *"Table 1 | … Detailed specifications are provided in the Methods
section."* Benchmark/framework papers lean on tables (multi-metric results) more
than figures.

## Length & title limits (consistency with style-guardrails)

- Keep a Nature-style legend `<= 300` words.
- Keep the `Fig. N |` title short and nominal; no numbers/results in the figure
  *title* line (numbers live in the panels and stats).

## Key caption rules

- Structural rule: `Fig. N | Bold noun phrase title` → `a/b/c` telegraphic present tense panels → statistics (n, error bar, test) in caption → "Source data are provided as a Source Data file." boilerplate.
- Tense: present tense for visual facts, past tense for experimental methods.
- Self-contained: color/shape mapping, sample sizes, and key values (PDB/RMSD/units) must be in the caption so it can be understood without reading the main text.
- Advanced: the final sentence of the caption may state an inferred conclusion, provided it is directly supported by a panel.
- Review legends: when aggregating systems from others, describe each sub-panel in one sentence and include copyright attribution such as "adapted with permission from refs… by Springer Nature".
