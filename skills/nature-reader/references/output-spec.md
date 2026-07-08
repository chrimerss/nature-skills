# Output Spec

## Standard bundle

Produce these files when possible:

- `paper.md`
- `source_map.json`
- `processing_notes.md`
- `assets/` for extracted images, crops, or figure snippets
- `reader.html` only when the user explicitly asks for a browser preview

## Full-text mode

When the source is a full paper, include all pages or all extractable sections in the reader. Do not limit the bundle to selected pages, a teaser excerpt, or the abstract unless the user explicitly requests a preview.

`paper.md` is the primary deliverable. It must expose structured paragraph-level alignment:

```markdown
<a id="S001"></a>
**Source:** p.1 S001

[source paragraph]
```

For source material that cannot be extracted or processed confidently, keep the source anchor and write a visible uncertainty note instead of dropping the block.

## `source_map.json`

Keep a stable source map so follow-up questions can cite the same anchors.

```json
{
  "paper": {
    "title": "",
    "venue": "",
    "source_type": "pdf|html|doi|arxiv|text",
    "language": "en",
    "source_path": ""
  },
  "blocks": [
    {
      "id": "S001",
      "page": 1,
      "type": "heading|paragraph|caption|table|table_row|note",
      "order": 1,
      "content": "",
      "bbox": [0, 0, 0, 0],
      "confidence": "high|medium|low",
      "refs": ["F001", "T001"],
      "insert_after": "S001"
    }
  ],
  "pages": [
    {
      "page": 1,
      "block_ids": ["S001", "S002", "S003", "C001"]
    }
  ],
  "figures": [
    {
      "id": "F001",
      "page": 3,
      "caption_id": "C001",
      "image_path": "",
      "bbox": [0, 0, 0, 0],
      "placement_hint": "near_first_mention",
      "placed_after": "S012",
      "alt_text": ""
    }
  ],
  "glossary": [
    {
      "term": "",
      "definition": "",
      "note": ""
    }
  ]
}
```

## `paper.md`

The Markdown reader should support:

- stable headings in paper order
- structured paragraph blocks
- source IDs on every substantive block
- figure/table cards near the relevant prose
- clear captions
- page navigation for full papers
- terminology notes and uncertainty notes

## `reader.html`

The page should support:

- clean desktop reading layout
- mobile stacked layout
- clickable source IDs on every block
- figure cards near the relevant text
- section navigation
- page navigation for full papers

Do not add a question area unless explicitly requested.

## Layout rules

- Keep paragraph alignment stable.
- Keep captions attached to their figures.
- Show tables where they are explained, not only where they appear in the PDF.
- Prefer semantic proximity over exact visual reconstruction.
- If a figure is referenced across multiple sections, anchor it at the first substantive discussion and link later mentions back to it.
- Crop figures and tables with the tightest valid bounding box.
- Do not use a full-page screenshot when the actual content occupies a smaller region.
- If the exact crop box cannot be verified, label the crop as approximate.
- For full papers, preserve page order and include a page index.

## Figure/table card format

```markdown
<a id="F001"></a>
### Fig. 1. [short title]

**Placed near:** p.3 S012
**Source:** p.4 C001

![Fig. 1](assets/fig1.png)

**Caption:** ...

**Reading note:** ...
```

Every image/table asset must have a corresponding card in `paper.md`. Every card must identify the source caption and placement block.

## Citation format in the page

Use short, stable source pointers:

- `p.7 S021`
- `p.8 C003`
- `Fig. 2`
- `Table 1`

For follow-up answers, combine page and block ID when available.
