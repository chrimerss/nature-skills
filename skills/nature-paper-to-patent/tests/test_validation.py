import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_patent_draft", ROOT / "scripts" / "validate_patent_draft.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def valid_draft():
    return {
        "title": "A method for industrial image defect detection",
        "metadata": {"draft_status": "review-draft"},
        "source_analysis": {
            "contains_core_formulas": True,
            "contains_methodology_figures": False,
        },
        "source_map": [
            {"id": "P001", "type": "paper-text", "locator": "Page 3", "summary": "Process"},
            {"id": "E001", "type": "equation", "locator": "Page 4 Eq 1", "summary": "Fusion"},
        ],
        "terminology_ledger": [
            {
                "concept": "Fused feature",
                "canonical_term": "Fused feature",
                "source_terms": ["fused feature"],
                "forbidden_aliases": [],
            }
        ],
        "formula_inventory": [
            {
                "source_id": "E001",
                "source_number": "(1)",
                "technical_role": "Fuse multiscale features",
                "disposition": "specification-equation-1",
            }
        ],
        "figure_inventory": [
            {
                "source_id": "P001",
                "source_number": "Method section",
                "type": "flowchart",
                "disposition": "redraw-as-figure-1",
            }
        ],
        "evidence_ledger": [
            {
                "id": "EV1",
                "feature": "Multiscale feature fusion",
                "source_ids": ["P001", "E001"],
                "support_status": "explicit",
            }
        ],
        "claims": [
            {
                "number": 1,
                "text": "A method for industrial image defect detection, comprising: S1, acquiring an industrial image; S2, performing multiscale feature fusion on the industrial image; S3, outputting a defect detection result based on the fused feature.",
            }
        ],
        "claim_feature_map": [
            {"claim_number": 1, "feature": "Multiscale feature fusion", "evidence_ids": ["EV1"]}
        ],
        "abstract_figure_number": 1,
        "figures": [
            {
                "number": 1,
                "title": "Method Flowchart",
                "type": "flowchart",
                "orientation": "vertical",
                "claim_number": 1,
                "complete_claim_flow": True,
                "source_ids": ["P001"],
                "nodes": [
                    {"id": "S1", "label": "S1: Acquire an industrial image", "claim_step": "S1"},
                    {
                        "id": "S2",
                        "label": "S2: Perform multiscale feature fusion",
                        "claim_step": "S2",
                    },
                    {
                        "id": "S3",
                        "label": "S3: Output defect detection result",
                        "claim_step": "S3",
                    },
                ],
                "edges": [{"from": "S1", "to": "S2"}, {"from": "S2", "to": "S3"}],
            }
        ],
        "specification": {
            "technical_field": ["The present invention relates to the field of industrial visual inspection."],
            "background": ["Existing methods are insufficient for representing small defects."],
            "invention_content": {
                "problem": ["Improve the capability of detecting small defects."],
                "solution": ["Adopt multiscale feature fusion."],
                "beneficial_effects": ["Preserve defect information across different scales."],
            },
            "figure_descriptions": ["Fig. 1 is a flowchart of the method."],
            "equations": [
                {
                    "number": 1,
                    "source_ids": ["E001"],
                    "latex": "F=F_1+F_2",
                    "expression": "F=F1+F2",
                    "symbols": [
                        {"symbol": "F", "meaning": "Fused feature"},
                        {"symbol": "F_1", "meaning": "First scale feature"},
                    ],
                    "technical_role": "Fuse features of different scales",
                    "description": "Wherein F represents the fused feature, and F1 and F2 represent features of different scales.",
                }
            ],
            "embodiments": [{"heading": "Embodiment 1", "paragraphs": ["Execute the above steps."]}],
        },
        "abstract": "The present invention discloses a method for industrial image defect detection, which outputs a defect detection result through multiscale feature fusion.",
        "quality_assessment": {
            "status": "review-draft",
            "scores": {
                "evidence_support": {"score": 4, "evidence": "All features have documented sources."},
                "claim_architecture": {"score": 4, "evidence": "Technical chain is closed."},
                "terminology_consistency": {"score": 4, "evidence": "Terminology is consistent."},
                "enablement_detail": {"score": 3, "evidence": "Main steps are explained."},
                "technical_effect_reasoning": {"score": 3, "evidence": "Effects are linked to technical means."},
                "formula_coverage": {"score": 4, "evidence": "Core formulas are included."},
                "figure_alignment": {"score": 4, "evidence": "Figures align with steps."},
            }
        },
    }


class DraftValidationTests(unittest.TestCase):
    def test_valid_draft_passes(self):
        self.assertEqual([], VALIDATOR.validate(valid_draft()))

    def test_unmapped_claim_fails(self):
        draft = valid_draft()
        draft["claim_feature_map"] = []
        codes = {item.code for item in VALIDATOR.validate(draft)}
        self.assertIn("CLAIM_NOT_MAPPED", codes)

    def test_missing_core_equation_fails(self):
        draft = valid_draft()
        draft["specification"]["equations"] = []
        codes = {item.code for item in VALIDATOR.validate(draft)}
        self.assertIn("MISSING_CORE_EQUATIONS", codes)


if __name__ == "__main__":
    unittest.main()
