# Structured Draft Schema

## Purpose

Populate a UTF-8 JSON file with this structure before rendering a DOCX. Empty optional arrays are allowed. Preserve `[TO CONFIRM: ...]` markers where facts remain unresolved.

```json
{
  "schema_version": "2.0",
  "title": "A method, apparatus and medium for ...",
  "metadata": {
    "source": "paper.pdf",
    "target": "Invention Patent",
    "draft_status": "For inventor and patent attorney review"
  },
  "source_analysis": {
    "contains_core_formulas": true,
    "formula_count_in_source": 18,
    "contains_methodology_figures": true
  },
  "source_map": [
    {
      "id": "P001",
      "type": "paper-text",
      "locator": "Page 3, Section 2.2, Para 1",
      "summary": "Discloses core feature extraction process",
      "confidence": "high"
    },
    {
      "id": "E001",
      "type": "equation",
      "locator": "Page 4, Equation (1)",
      "summary": "Class prototype calculation",
      "confidence": "high"
    }
  ],
  "terminology_ledger": [
    {
      "concept": "Class prototype",
      "canonical_term": "Class prototype",
      "source_terms": ["class prototype", "prototype"],
      "forbidden_aliases": ["class center"]
    }
  ],
  "formula_inventory": [
    {
      "source_id": "E001",
      "source_number": "(1)",
      "technical_role": "Calculate class prototype based on support set features",
      "disposition": "specification-equation-1"
    }
  ],
  "figure_inventory": [
    {
      "source_id": "F001",
      "source_number": "Fig. 2",
      "type": "methodology",
      "disposition": "redraw-as-figure-2"
    }
  ],
  "abstract_figure_number": 1,
  "assumptions": [
    "Target jurisdiction is United States / International / General Patent"
  ],
  "invention_concept": {
    "technical_problem": "...",
    "technical_means": "...",
    "technical_effect": "..."
  },
  "evidence_ledger": [
    {
      "id": "F1",
      "feature": "...",
      "source_ids": ["P001", "E001"],
      "source_location": "Page 3, Section 2.2",
      "technical_role": "...",
      "effect": "...",
      "support_status": "explicit"
    }
  ],
  "claims": [
    {
      "number": 1,
      "text": "A method of ..., comprising: ..."
    },
    {
      "number": 2,
      "text": "The method of claim 1, wherein ..."
    }
  ],
  "claim_feature_map": [
    {
      "claim_number": 1,
      "feature": "Calculate class prototype based on support set features",
      "evidence_ids": ["F1"],
      "specification_locations": ["Detailed Description, Embodiment 1"]
    }
  ],
  "figures": [
    {
      "number": 1,
      "title": "Method Flowchart",
      "type": "flowchart",
      "orientation": "vertical",
      "claim_number": 1,
      "complete_claim_flow": true,
      "source_ids": ["P001"],
      "nodes": [
        {
          "id": "S1",
          "label": "S1: Acquire and preprocess target data",
          "claim_step": "S1"
        },
        {
          "id": "S2",
          "label": "S2: Extract multiscale features",
          "claim_step": "S2"
        }
      ],
      "edges": [
        {
          "from": "S1",
          "to": "S2",
          "label": ""
        }
      ]
    },
    {
      "number": 2,
      "title": "Core Methodology Schematic",
      "type": "methodology",
      "orientation": "horizontal",
      "source_ids": ["F001", "P001"],
      "nodes": [
        {
          "id": "input",
          "label": "Input feature"
        },
        {
          "id": "module",
          "label": "Core processing module"
        },
        {
          "id": "output",
          "label": "Output feature"
        }
      ],
      "edges": [
        {
          "from": "input",
          "to": "module",
          "label": ""
        },
        {
          "from": "module",
          "to": "output",
          "label": ""
        }
      ]
    }
  ],
  "specification": {
    "technical_field": [
      "The present invention relates to ..."
    ],
    "background": [
      "..."
    ],
    "invention_content": {
      "problem": [
        "..."
      ],
      "solution": [
        "..."
      ],
      "beneficial_effects": [
        "..."
      ]
    },
    "figure_descriptions": [
      "Fig. 1 is a method flowchart of the present invention."
    ],
    "equations": [
      {
        "number": 1,
        "source_location": "Paper page 4, Equation (1)",
        "source_ids": ["E001"],
        "expression": "O_u = (1/|S_u|) Σ_(x_i,y_i∈S_u) h_γ(x_i)",
        "latex": "O_u = \\frac{1}{|S_u|}\\sum_{(x_i,y_i)\\in S_u} h_\\gamma(x_i)",
        "symbols": [
          {"symbol": "O_u", "meaning": "Class prototype of class u"},
          {"symbol": "S_u", "meaning": "Support set of class u"},
          {"symbol": "h_\\gamma", "meaning": "Supervised feature extractor"}
        ],
        "technical_role": "Average supervised features of samples in the same class to obtain class prototype",
        "description": "Wherein O_u represents the class prototype of class u, S_u represents the support set of class u, and h_γ represents the supervised feature extractor. This equation calculates the class prototype by averaging supervised features across samples in the same class."
      }
    ],
    "embodiments": [
      {
        "heading": "Embodiment 1",
        "paragraphs": [
          "..."
        ]
      }
    ]
  },
  "abstract": "The present invention relates to ...",
  "audit": {
    "support_findings": [
      "..."
    ],
    "consistency_findings": [
      "..."
    ]
  },
  "quality_assessment": {
    "status": "review-draft",
    "scores": {
      "evidence_support": {"score": 4, "evidence": "Every claim feature maps to the evidence ledger."},
      "claim_architecture": {"score": 4, "evidence": "Independent claim forms a closed technical chain with layered fallback positions."},
      "terminology_consistency": {"score": 4, "evidence": "Claims, specification, and figures use consistent terminology."},
      "enablement_detail": {"score": 3, "evidence": "Main data flow, equations, and implementation steps are described."},
      "technical_effect_reasoning": {"score": 3, "evidence": "Main effects are causally linked to corresponding technical means."},
      "formula_coverage": {"score": 4, "evidence": "Core equations are included with defined symbols."},
      "figure_alignment": {"score": 4, "evidence": "Main flowchart aligns with steps in claim 1."}
    }
  },
  "inventor_questions": [
    "[TO CONFIRM: ...]"
  ]
}
```

## Rules

- Use integer claim numbers in ascending order.
- Use stable source IDs: `P` for paper text, `E` for equations, `F` for
  source figures, and `C` for code or supplementary evidence.
- Give every `explicit` or `inherent` evidence-ledger item one or more
  `source_ids`.
- Add at least one `claim_feature_map` entry for every formal claim. Map each
  material limitation to evidence-ledger IDs, not merely to a general page.
- Store claim text without repeating the number at its beginning.
- Use arrays for paragraphs to preserve paragraph boundaries.
- Use only `explicit`, `inherent`, `needs-confirmation`, or `unsupported` as evidence status.
- Exclude unsupported features from formal claims.
- Keep internal audit material in the appendix, not in the formal application sections.
- Number figures consecutively from 1.
- Set `abstract_figure_number` to the main figure used as the abstract figure.
- Reuse that exact figure in the specification; do not create a conflicting duplicate.
- The abstract figure should normally be an overall method or system flow that represents the principal independent claim.
- Use `flowchart` as the figure type and `vertical` or `horizontal` as the orientation.
- Use `methodology` for an intermediate architecture, module, feature-flow, or loss-relationship figure.
- A methodology figure does not require `claim_number`, `claim_step`, or `complete_claim_flow`.
- Prefer a paper figure when suitable; otherwise redraw it as a concise black-and-white patent figure.
- Give every node a unique ASCII identifier.
- Keep `claim_step` equal to the corresponding identifier in the method claim, such as `S1`.
- Set `claim_number` to the method claim represented by the figure.
- Set `complete_claim_flow` to `true` for an overall flowchart that must cover every numbered step in that claim.
- Reference every figure in `specification.figure_descriptions`.
- Use concise node labels; put implementation detail in the specification.
- If the paper contains formulas that define core technical operations, populate `specification.equations`.
- Set `source_analysis.contains_core_formulas` after reviewing the paper.
- Number equations consecutively from 1.
- Add a valid `latex` field to every equation; the renderer converts it to editable Office Math.
- Add `source_ids`, structured `symbols`, and `technical_role` to every
  equation.
- Treat `expression` as a readable audit copy, not as the DOCX rendering source.
- Record the paper page and original formula number in `source_location`.
- Define every symbol in `description` and state the technical operation performed by the formula.
- Include formulas in the standalone specification DOCX; do not place them only in an internal appendix.
- Record a disposition for every core source formula and methodology figure.
- Populate `quality_assessment.scores` with a 1-5 score and evidence sentence
  for each dimension required by `static/core/output-contract.md`.
