# Article Anatomy — a reading aid (CS/AI corpus)

Use this file as a **reading aid** while building the structured reader, to label
the *argumentative function* of each block so the reader can locate the gap, the
contribution, the decisive result, and the self-contained figure legends. It is
distilled from a set of open-access computer science / AI papers across genres.

> This is an aid for **locating structure**, not a license to summarise. The
> `core/principles.md` contract still holds: process every block for meaning,
> keep the structured text blocks, and never degrade to a summary-only output.
> Use the function labels to help a reader navigate, e.g. in a short orientation
> note, not to replace the full text.

## Where each function lives

- **Abstract = a funnel.** Read it as five moves: field value → gap (almost
  always after **However**) → hinge `Here we show/present X` → one quantified
  result → significance. The hinge sentence is the fastest way to state what the
  paper actually contributes.
- **Introduction = hook → gap → contribution.** Gap signal words to spot:
  **However / remains / Unfortunately / underexplored / the scarcity of … /
  Without X, Y cannot be …**. The contribution is the explicit `Here we… / In
  this work, we…` sentence, often with a `(Fig. 1)` pointer.
- **Results = conclusion-first.** Each paragraph opens with the judgement; the
  figure call (`Fig. Xa`, or `Figure X shows…`) and the numbers follow.
  Subheadings are often conclusions or method names, so the subheading list
  alone sketches the evidence ladder.
- **Figure/Table legends are self-contained.** `Fig. N | bold noun title`, then
  `a/b/c` panels, with `n=`, error type, and test written in. A legend's last
  sentence sometimes advances a claim (*"…indicating that the models are not
  predicting poses based on physics…"*) — flag it; it is interpretation, not
  description.
- **Discussion = restate contribution → why credible → wider meaning → limits
  (`Another limitation…` / `remains to be tested`) → future work.** The limits
  sentence is where the paper bounds its own claim.

## Genre tells (so the reader frames the paper correctly)

- **Research article**: own data, IMRaD, `we` + passive.
- **Review**: chapters by topic/modality synthesising others' citations, little
  own data, closes with `Conclusions and outlook`.
- **Perspective**: history/era hook, numbered argument, normative `X should…`,
  roadmap close.
- **Comment**: first-person `I`, rhetorical-question opening, analogy/history,
  no IMRaD, no figures.
- **Benchmark/framework**: the gap is "the field lacks an agreed standard";
  tables dominate; stresses community / reproducibility / versioning.

## Critical Reading Tips

- Labeling the argumentative function of each paragraph (background/gap/contribution/result/limits) helps readers quickly grasp the argumentation skeleton, but **must not** replace or omit paragraph-level structured processing.
- Words like "However", "remains challenging", "scarcely studied", "lacks", "without X, Y cannot be..." signal research gaps; sentences starting with "Here we..." or "In this work..." state the author's contribution.
- Figure captions are usually self-contained (including sample size n, error bars, and statistical tests); if the last sentence of a caption presents an inferred conclusion, label it as "Interpretation" rather than "Description".
- First determine the genre (research article/review/perspective/comment/benchmark), then understand its organizational structure and tone accordingly.
