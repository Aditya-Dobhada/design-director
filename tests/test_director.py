"""
Comprehensive Test Suite for Design Director
Validates all acceptance criteria from the PRD:
- Criterion 6.1: Design Brief Extraction
- Criterion 6.2: Style Recommendations with Qualitative Ratings & Tradeoffs
- Criterion 6.3: Reference Library Property Mapping (10+ terms)
- Criterion 6.4: Layered Design Spec Resolution (No Blends)
- Criterion 6.5: Iterative Refinement (Layer-Scoped Diffs)
- Criterion 6.6: Style Packs Completeness & Negative Constraints
- Criterion 6.7: Implementation Contract Generation
- Criterion 6.8: Post-Implementation Design Audit Precision & Recall
"""

import sys
import os
import unittest
from pathlib import Path

# Add project root and director to sys.path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "design-skills" / "director"))
sys.path.insert(0, str(ROOT_DIR / "design-skills" / "audit" / "scripts"))

from director_engine import (
    extract_design_brief,
    recommend_styles,
    create_design_spec,
    refine_spec,
    generate_implementation_contract,
    load_reference_library,
    find_reference,
    SUPPORTED_STYLES
)
from audit_code import DesignAuditor

class TestDesignDirector(unittest.TestCase):

    def test_design_brief_extraction(self):
        """Criterion 6.1: Director extracts structured Design Brief from PRDs."""
        prds_dir = ROOT_DIR / "tests" / "fixtures" / "prds"
        
        # Test Fintech PRD
        with open(prds_dir / "fintech-wealth.md", "r", encoding="utf-8") as f:
            brief = extract_design_brief(f.read())
            
        self.assertIn("FinTech", brief["product_type"])
        self.assertIn("wealth", brief["target_audience"].lower())
        self.assertIn("authoritative", brief["personality_traits"])
        self.assertEqual(brief["ux_requirements"]["density"], "spacious")
        self.assertEqual(brief["brand_positioning_axes"]["premium_vs_accessible"], "Ultra Premium")
        self.assertIn("WCAG AAA", brief["visual_constraints"]["accessibility_needs"])

        # Test Telemetry PRD
        with open(prds_dir / "dev-telemetry-cli.md", "r", encoding="utf-8") as f:
            dev_brief = extract_design_brief(f.read())
            
        self.assertIn("Developer", dev_brief["product_type"])
        self.assertEqual(dev_brief["ux_requirements"]["density"], "high")
        self.assertIn("tactical", dev_brief["personality_traits"])

    def test_style_recommendations(self):
        """Criterion 6.2: Recommends 2-4 candidate directions with honest tradeoffs and qualitative ratings only."""
        with open(ROOT_DIR / "tests" / "fixtures" / "prds" / "fintech-wealth.md", "r", encoding="utf-8") as f:
            brief = extract_design_brief(f.read())
            
        recs = recommend_styles(brief)
        
        # Must recommend 2 to 4 directions
        self.assertTrue(2 <= len(recs) <= 4, f"Expected 2-4 recommendations, got {len(recs)}")
        
        valid_ratings = {"Strong fit", "Good fit", "Possible", "Poor fit"}
        for r in recs:
            # Check qualitative rating
            self.assertIn(r["fit_rating"], valid_ratings)
            # Ensure NO numeric scores or percentages are present
            self.assertNotIn("%", str(r.values()))
            self.assertNotIn("0.", str(r.values()))
            # Must include honest tradeoffs / risks
            self.assertTrue(len(r["tradeoffs"]) >= 1, f"Missing tradeoffs for {r['name']}")
            # Must have justification reasoning
            self.assertTrue(len(r["reasoning"]) > 20)

    def test_reference_library(self):
        """Criterion 6.3: Reference library maps at least 10 test reference terms to concrete properties."""
        test_terms = [
            "linear", "traditional-bank", "stripe", "apple", "vercel",
            "notion", "pitch", "bloomberg-terminal", "teenage-engineering",
            "gumroad", "craigslist", "raycast", "aesop", "balenciaga"
        ]
        
        # Verify at least 10 entries exist and match
        matched_count = 0
        for term in test_terms:
            ref = find_reference(term)
            self.assertIsNotNone(ref, f"Failed to find reference mapping for '{term}'")
            # Verify decomposed properties
            self.assertIn("mode", ref)
            self.assertIn("density", ref)
            self.assertIn("spacing", ref)
            self.assertIn("borders", ref)
            self.assertIn("shadows", ref)
            self.assertIn("typography", ref)
            self.assertIn("color", ref)
            self.assertIn("motion", ref)
            self.assertIn("personality", ref)
            self.assertIn("mapped_style_layers", ref)
            matched_count += 1
            
        self.assertTrue(matched_count >= 10, f"Expected >= 10 references, found {matched_count}")

    def test_layered_design_spec(self):
        """Criterion 6.4: Resolves direction into independent layers with single source of truth (no percentage blends)."""
        for style in SUPPORTED_STYLES:
            spec = create_design_spec(style)
            self.assertEqual(spec["chosen_primary_style"], style)
            layers = spec["layers"]
            
            # Check all required layers
            required_layers = ["layout", "typography", "surfaces", "color", "motion", "imagery"]
            for layer in required_layers:
                self.assertIn(layer, layers)
                self.assertTrue(isinstance(layers[layer], str))
                # Ensure no ambiguous percentage blend syntax like "50% A, 50% B"
                self.assertNotIn("%", layers[layer])
                self.assertNotIn("blend", layers[layer].lower())
                
            self.assertTrue(spec["constraints"]["single_source_of_truth_per_layer"])
            self.assertTrue(spec["constraints"]["no_percentage_blends"])

    def test_iterative_refinement(self):
        """Criterion 6.5: Refinement changes only targeted layers; unrelated layers remain stable."""
        initial_spec = create_design_spec("swiss-editorial")
        initial_layout = initial_spec["layers"]["layout"]
        initial_typography = initial_spec["layers"]["typography"]
        initial_imagery = initial_spec["layers"]["imagery"]

        # Critique: "More like Linear"
        refinement = refine_spec(initial_spec, "make it more like Linear")
        updated_spec = refinement["updated_spec"]
        diff = refinement["diff_report"]

        # Surfaces and color should update
        self.assertNotEqual(initial_spec["layers"]["surfaces"], updated_spec["layers"]["surfaces"])
        self.assertNotEqual(initial_spec["layers"]["color"], updated_spec["layers"]["color"])

        # Layout, typography, and imagery should remain completely stable
        self.assertEqual(updated_spec["layers"]["layout"], initial_layout)
        self.assertEqual(updated_spec["layers"]["imagery"], initial_imagery)
        self.assertIn("layout", diff["stable_layers"])
        self.assertIn("imagery", diff["stable_layers"])
        self.assertTrue(diff["layers_changed_count"] >= 1)

    def test_style_packs_completeness_and_anti_patterns(self):
        """Criterion 6.6: All 5 style packs contain required files, testable tokens, and negative constraints."""
        styles_dir = ROOT_DIR / "design-skills" / "styles"
        required_files = [
            "SKILL.md", "tokens.md", "typography.md",
            "layout.md", "components.md", "motion.md"
        ]

        for style in SUPPORTED_STYLES:
            style_path = styles_dir / style
            self.assertTrue(style_path.exists(), f"Style directory missing: {style}")

            for rf in required_files:
                target_file = style_path / rf
                self.assertTrue(target_file.exists(), f"Missing required file {rf} in {style}")
                content = target_file.read_text(encoding="utf-8")
                self.assertTrue(len(content) > 100, f"{rf} in {style} is unexpectedly short")

            # Check explicit negative constraints in SKILL.md
            skill_content = (style_path / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Anti-Patterns", skill_content, f"Missing Anti-Patterns section in {style}/SKILL.md")
            self.assertIn("NEVER", skill_content, f"Missing explicit negative constraint keyword NEVER in {style}/SKILL.md")

    def test_implementation_contract_generation(self):
        """Criterion 6.7: Generates binding implementation contract with hard anti-patterns."""
        spec = create_design_spec("quiet-luxury")
        contract = generate_implementation_contract(spec, "Build a private wealth portal.")
        
        self.assertIn("HARD IMPLEMENTATION DESIGN CONTRACT", contract)
        self.assertIn("QUIET-LUXURY", contract)
        self.assertIn("Hard Anti-Patterns", contract)
        self.assertIn("NEVER** use rounded corners", contract)
        self.assertIn("Contract Verification Notice", contract)

    def test_design_audit_precision_and_recall(self):
        """Criterion 6.8: Design audit correctly flags seeded deviations and passes clean implementations."""
        fixtures_dir = ROOT_DIR / "tests" / "fixtures" / "seeded_code"

        # 1. Clean Quiet Luxury implementation -> Must pass
        auditor_clean = DesignAuditor("quiet-luxury")
        clean_report = auditor_clean.run_audit(fixtures_dir / "clean_quiet_luxury.html")
        self.assertEqual(clean_report["summary"]["critical"], 0, "Clean implementation incorrectly flagged critical violations")
        self.assertIn("PASSED", clean_report["status"])

        # 2. Deviant Quiet Luxury implementation -> Must detect seeded violations
        auditor_dev = DesignAuditor("quiet-luxury")
        dev_report = auditor_dev.run_audit(fixtures_dir / "deviant_quiet_luxury.html")
        self.assertIn("FAILED", dev_report["status"])
        self.assertTrue(dev_report["summary"]["critical"] >= 3, "Failed to detect seeded critical violations in quiet luxury")
        
        violation_types = [v["type"] for v in dev_report["violations"]]
        self.assertIn("radius_violation", violation_types)
        self.assertIn("shadow_violation", violation_types)
        self.assertIn("color_violation", violation_types)

        # 3. Deviant Neo-Brutalism implementation -> Must detect pill radius, blurry shadow, and timid borders
        auditor_neo = DesignAuditor("neo-brutalism")
        neo_report = auditor_neo.run_audit(fixtures_dir / "deviant_neo_brutalism.html")
        self.assertIn("FAILED", neo_report["status"])
        neo_violation_types = [v["type"] for v in neo_report["violations"]]
        self.assertIn("radius_violation", neo_violation_types)
        self.assertIn("shadow_violation", neo_violation_types)
        self.assertIn("border_violation", neo_violation_types)

        # 4. Deviant Cyberpunk implementation -> Must detect light background
        auditor_cyber = DesignAuditor("cyberpunk")
        cyber_report = auditor_cyber.run_audit(fixtures_dir / "deviant_cyberpunk.html")
        self.assertIn("FAILED", cyber_report["status"])
        cyber_violation_types = [v["type"] for v in cyber_report["violations"]]
        self.assertIn("color_violation", cyber_violation_types)

if __name__ == "__main__":
    unittest.main()
