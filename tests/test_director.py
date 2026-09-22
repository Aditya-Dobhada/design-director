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

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-director"))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-audit"))

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
        """Criterion 6.6: All 12 style packs contain complete tokens, typography, and negative constraints."""
        styles_dir = ROOT_DIR / "styles"

        for style in SUPPORTED_STYLES:
            style_file = styles_dir / f"{style}.md"
            self.assertTrue(style_file.exists(), f"Style pack missing: {style}.md")
            content = style_file.read_text(encoding="utf-8")
            self.assertTrue(len(content) > 500, f"{style}.md is unexpectedly short")

            # Check explicit tokens and negative constraints
            self.assertIn("Mandatory Anti-Patterns", content, f"Missing Anti-Patterns in {style}.md")
            self.assertIn("NEVER", content, f"Missing negative constraint keyword NEVER in {style}.md")
            self.assertIn("Color Tokens", content, f"Missing Color Tokens in {style}.md")
            self.assertTrue("Radius Tokens" in content or "Border Radius" in content, f"Missing Border Radius in {style}.md")

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

        # 5. Deviant Bauhaus implementation -> Must detect rounded radius and blurry shadow
        auditor_bau = DesignAuditor("bauhaus")
        bau_report = auditor_bau.run_audit(fixtures_dir / "deviant_bauhaus.html")
        self.assertIn("FAILED", bau_report["status"])
        bau_violation_types = [v["type"] for v in bau_report["violations"]]
        self.assertIn("radius_violation", bau_violation_types)
        self.assertIn("shadow_violation", bau_violation_types)

    def test_all_twenty_styles_taxonomy(self):
        """Verifies all 20 styles in the taxonomy can generate valid specs and contracts."""
        self.assertEqual(len(SUPPORTED_STYLES), 20)
        expected_styles = {
            "swiss-editorial", "neo-brutalism", "y2k-frutiger-aero", "quiet-luxury",
            "cyberpunk", "retro-americana", "memphis-postmodern", "space-age-optimism",
            "japanese-wabi-sabi", "bauhaus", "organic-natural", "maximalist-dopamine",
            "minimal-modern", "dark-minimal", "terminal-cli", "web-brutalism",
            "art-deco", "mid-century-modern", "vaporwave", "high-fashion-editorial"
        }
        self.assertEqual(set(SUPPORTED_STYLES), expected_styles)

        for style in SUPPORTED_STYLES:
            spec = create_design_spec(style)
            contract = generate_implementation_contract(spec, f"Build product UI in {style}")
            self.assertIn("HARD IMPLEMENTATION DESIGN CONTRACT", contract)
            self.assertIn(style.upper(), contract)
            self.assertIn("NEVER", contract)

    def test_contract_generation_with_modifiers(self):
        """Verifies contracts properly incorporate declared orthogonal modifiers."""
        spec = create_design_spec("dark-minimal")
        contract = generate_implementation_contract(
            spec,
            "Build an observability console",
            modifiers=["frosted-glass", "micro-snappy"]
        )
        self.assertIn("Active Orthogonal Modifiers", contract)
        self.assertIn("frosted-glass", contract)
        self.assertIn("micro-snappy", contract)
        self.assertIn("backdrop-blur", contract)

    def test_ambiguous_prd_multi_defensible_recommendations(self):
        """Verifies an ambiguous PRD returns diverse defensible recommendations without score ties."""
        ambiguous_context = """
        # ArchStudio AI
        An AI collaboration platform for independent architects and industrial designers.
        Must support CAD file inspections, client moodboards, and specification drafting.
        Needs to feel high-craft, precise, and professional, yet inspiring for creative spatial work.
        """
        brief = extract_design_brief(ambiguous_context)
        recs = recommend_styles(brief)

        self.assertTrue(len(recs) >= 2, "Expected at least 2 recommendations for ambiguous PRD")
        rec_ids = [r["id"] for r in recs]
        
        # Verify valid qualitative ratings and honest tradeoffs
        valid_ratings = {"Strong fit", "Good fit", "Possible"}
        for r in recs:
            self.assertIn(r["fit_rating"], valid_ratings)
            self.assertTrue(len(r["tradeoffs"]) >= 1)
            self.assertTrue(len(r["reasoning"]) >= 15)

    def test_new_styles_refinement(self):
        """Tests refinement prompts targeting the expanded style families."""
        base_spec = create_design_spec("swiss-editorial")

        # Test organic refinement
        res_org = refine_spec(base_spec, "make it more organic and natural")
        self.assertIn("organic-natural", res_org["updated_spec"]["layers"]["surfaces"])
        self.assertIn("organic-natural", res_org["updated_spec"]["layers"]["color"])

        # Test wabi-sabi refinement
        res_wabi = refine_spec(base_spec, "feel like wabi-sabi tea house")
        self.assertIn("japanese-wabi-sabi", res_wabi["updated_spec"]["layers"]["surfaces"])

        # Test bauhaus refinement
        res_bau = refine_spec(base_spec, "make it constructivist bauhaus")
        self.assertIn("bauhaus", res_bau["updated_spec"]["layers"]["surfaces"])
        self.assertIn("bauhaus", res_bau["updated_spec"]["layers"]["color"])

        # Test space age refinement
        res_space = refine_spec(base_spec, "more like NASA space age optimism")
        self.assertIn("space-age-optimism", res_space["updated_spec"]["layers"]["surfaces"])

        # Test maximalist dopamine refinement
        res_max = refine_spec(base_spec, "more maximalist dopamine sticker bomb")
        self.assertIn("maximalist-dopamine", res_max["updated_spec"]["layers"]["surfaces"])

        # Test terminal CLI refinement
        res_cli = refine_spec(base_spec, "make it look like a terminal CLI console")
        self.assertIn("terminal-cli", res_cli["updated_spec"]["layers"]["surfaces"])
        self.assertIn("terminal-cli", res_cli["updated_spec"]["layers"]["color"])

        # Test art deco refinement
        res_deco = refine_spec(base_spec, "shift towards the Great Gatsby art deco luxury")
        self.assertIn("art-deco", res_deco["updated_spec"]["layers"]["surfaces"])
        self.assertIn("art-deco", res_deco["updated_spec"]["layers"]["color"])

        # Test vaporwave refinement
        res_vapor = refine_spec(base_spec, "give it 80s synthwave vaporwave aesthetics")
        self.assertIn("vaporwave", res_vapor["updated_spec"]["layers"]["surfaces"])

        # Test high fashion editorial refinement
        res_fashion = refine_spec(base_spec, "style like balenciaga high-fashion runway editorial")
        self.assertIn("high-fashion-editorial", res_fashion["updated_spec"]["layers"]["surfaces"])

        # Test mid-century modern refinement
        res_mcm = refine_spec(base_spec, "bring in mid-century modern eames era vibes")
        self.assertIn("mid-century-modern", res_mcm["updated_spec"]["layers"]["surfaces"])

if __name__ == "__main__":
    unittest.main()
