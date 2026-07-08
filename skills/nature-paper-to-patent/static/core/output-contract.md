# Output Contract

## Full package

A full-draft job must produce:

- `claims.docx`;
- `specification.docx`;
- `abstract.docx`;
- `abstract-drawings.docx`;
- `complete-review.docx`;
- `structured-draft.json`;
- `claim-audit.txt`;
- `validation-report.txt`;
- SVG and PNG files for every generated patent figure.

The structured draft is the source of truth. DOCX files are rendered outputs.

## Required traceability

- Every material claim feature maps to at least one source ID.
- Every source-supported core equation has a recorded disposition.
- Every formal term uses the terminology ledger's canonical form.
- Every numbered claim step maps to one main-flowchart node and one embodiment
  explanation.
- Every methodology figure is source-supported or explicitly identified as a
  redrawing of supported operations.

## Formal-document rules

- Use English for claims, specification, abstract, and figure labels.
- Do not place source IDs, support labels, drafting notes, or quality scores in
  formal claims.
- Render formal equations as editable Office Math.
- Use a concrete final method output; do not use vague phrases like "technical result", "processing result", or "final output".
- Keep the abstract concise and free of promotional or unsupported promises.

## Quality thresholds

Score each dimension from 1 to 5 and record one sentence of evidence:

- evidence support: at least 4;
- claim architecture: at least 4;
- terminology and dependency consistency: at least 4;
- enablement detail: at least 3;
- technical-effect reasoning: at least 3;
- formula coverage: at least 4 when core formulas exist;
- figure alignment: at least 4 when figures are required.

Any validation `ERROR`, an unmapped material claim feature, or a missing core
formula forces the status `incomplete draft`.

## Delivery note

State that the package requires inventor confirmation and qualified
patent-professional review. Do not describe it as filing-ready merely because
the automated checks pass.
