# `nature-polishing` Skill

`nature-polishing` is designed to polish, restructure, or translate academic prose into concise English that aligns closely with Nature-family style.

## Source Hierarchy
- `Main strategy`: Writing course notes from `Chapter1-Week1-7 full version.pdf`.
- `Published article patterns`: Curated writing patterns from Nature and Nature Communications articles.

## Key Architecture
- The main `SKILL.md` is structured around core writing strategies: paper types, reader workflows, hourglass structure, writing order, section responsibilities, intellectual debt, and AI/ethics boundaries.
- Full-manuscript polishing leverages published article patterns, covering abstracts, introductions, results, discussion, conclusion, and titles.
- `references/` serves targeted roles: phrase families, move templates, and style guardrails.
- The skill distinguishes between `research papers` and `methods papers`.
- `Core argument ownership` is treated as a fundamental rule rather than an incidental reminder.

## File Structure
```
nature-polishing/
├── SKILL.md
├── README.md
├── manifest.yaml
├── static/
│   ├── core/
│   ├── fragments/
│   │   ├── journal/
│   │   ├── language/
│   │   ├── paper_type/
│   │   └── section/
└── references/
    ├── latex-layout.md
    ├── nat-comms-2025-diction.md
    ├── phrasebank-playbook.md
    ├── published-article-patterns.md
    ├── section-moves.md
    ├── style-guardrails.md
    └── writing-strategy.md
```

## Applicable Scenarios
- Polishing abstracts, introductions, results, discussion, conclusions, or titles.
- Polishing methods sections, or handling methods papers that emphasize fair comparison logic.
- Translating or refining academic drafts into publication-ready English.
- Tightening section logic prior to submission.
- Mitigating overclaiming and adjusting phrasing where evidence strength does not match claims.
- Making text sound more like top-tier journal English without fabricating content.
- Fixing LaTeX typesetting and layout issues: loose or sparse pages, stranded headings, figures that do not fill the page or split across pages, `Float too large` warnings, multi-panel figure arrangements, sparse Supplementary Information pages, etc.

## Design Intent
This skill aims to:
- Preserve facts, citation intent, and author responsibility.
- Use core writing strategies as the primary guiding principles.
- Improve rhetorical order at the paragraph level.
- Keep sentences concise, clear, and readable.
- Use reference files strictly as a phrase and style support layer.
- Avoid generic AI phrasing and unsupported claims.

## Reference Files
- `section-moves.md`: Section sequence and move patterns.
- `published-article-patterns.md`: Curated writing patterns from Nature and Nature Communications.
- `phrasebank-playbook.md`: Hedging, transition, evidence, limitation, and future work expressions.
- `style-guardrails.md`: British English style, articles, abbreviations, units, register, and overclaim control.
- `writing-strategy.md`: Paragraph and section level argumentation logic.
- `latex-layout.md`: LaTeX float and page layout guidelines, including top-alignment, `\clearpage` + `[H]` title-figure units, `placeins` caveats, redrawing wide/short figures at the source, multi-panel stacking, and diagnostic contact sheets.

## Important Notes
- This skill is intended for polishing and structural refactoring, not for inventing scientific content.
- Primary strategic rules reside in `SKILL.md`; reference files should never override these core rules.
- Reference files are intentionally selective, designed to assist judgment rather than encourage boilerplate repetition.
