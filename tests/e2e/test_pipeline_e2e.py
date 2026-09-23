"""
Level 1 E2E: Deterministic pipeline integration test.

Runs the full analyze → recommend → choose → implement pipeline end-to-end
using subprocess calls (same as a real user session), then asserts the generated
DESIGN_CONTRACT.md is structurally valid.

No LLM calls. No API keys required. Safe to run in CI.
"""
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Mirror the pattern from test_director.py — add paths at module scope
ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-director"))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-audit"))

from director_engine import (
    create_design_spec,
    extract_design_brief,
    generate_implementation_contract,
    recommend_styles,
)

GALLERY_DIR = str(ROOT_DIR / "skills" / "design-director" / "gallery")


# ── Unseen PRDs (not used in any unit-test fixture) ────────────────────────
UNSEEN_PRDS = {
    "edtech": """
    Build an adaptive learning platform for K-12 students.
    The platform delivers personalized lesson sequences, tracks mastery by curriculum standard,
    and provides real-time progress dashboards for teachers and parents.
    Features: adaptive quiz engine, spaced repetition flashcards, parent weekly digest email,
    teacher classroom overview, student achievement badges.
    """,

    "logistics": """
    Fleet management dashboard for a regional freight logistics operator.
    Dispatchers track 300+ trucks across 12 depots in real time.
    Operators need to see delivery status, driver ETA, route deviations,
    fuel consumption by vehicle, and compliance alerts (HOS violations).
    Dense tabular data. Mission-critical uptime.
    """,

    "boutique_store": """
    Online boutique for an independent artisanal ceramics studio.
    Each piece is hand-thrown in small batches. The storefront should feel like
    entering a quiet gallery: warm light, generous whitespace, featured product
    photography, and a minimal checkout flow.
    Audience: design-conscious buyers, gift shoppers, interior decorators.
    """,
}

STYLE_CHOICES = {
    "edtech": "space-age-optimism",
    "logistics": "swiss-editorial",
    "boutique_store": "quiet-luxury",
}


class TestLevel1Pipeline(unittest.TestCase):
    """Runs the full director pipeline on unseen PRDs and validates contract output."""

    def _run_pipeline(self, prd_text: str, style_id: str):
        """Executes the full pipeline programmatically and returns the contract string."""
        brief = extract_design_brief(prd_text)
        self.assertIn("product_type", brief)
        self.assertIn("personality_traits", brief)
        self.assertIsInstance(brief["personality_traits"], list)

        recs = recommend_styles(brief)
        self.assertGreaterEqual(len(recs), 2, "Expected at least 2 style recommendations")
        self.assertLessEqual(len(recs), 4, "Expected at most 4 style recommendations")
        for rec in recs:
            self.assertIn("style_id", rec)
            self.assertIn("fit_rating", rec)
            self.assertIn("tradeoffs", rec)
            self.assertIsInstance(rec["tradeoffs"], list)

        spec = create_design_spec(style_id)
        self.assertEqual(spec["chosen_primary_style"], style_id)
        self.assertIn("layers", spec)
        for layer in ["layout", "typography", "surfaces", "color", "motion", "imagery", "components"]:
            self.assertIn(layer, spec["layers"], f"Missing layer: {layer}")

        contract = generate_implementation_contract(spec, prd_text)
        self.assertIn("HARD IMPLEMENTATION DESIGN CONTRACT", contract)
        self.assertIn("Hard Anti-Patterns", contract)
        self.assertIn("NEVER", contract)
        self.assertIn("Product Specification", contract)
        self.assertGreater(len(contract), 500, "Contract suspiciously short")
        return contract

    def test_edtech_pipeline_space_age(self):
        """EdTech PRD → Space Age Optimism → valid contract."""
        contract = self._run_pipeline(UNSEEN_PRDS["edtech"], STYLE_CHOICES["edtech"])
        self.assertIn("space-age-optimism".upper(), contract.upper())

    def test_logistics_pipeline_swiss(self):
        """Logistics PRD → Swiss Editorial → valid contract."""
        contract = self._run_pipeline(UNSEEN_PRDS["logistics"], STYLE_CHOICES["logistics"])
        self.assertIn("swiss-editorial".upper(), contract.upper())

    def test_boutique_pipeline_quiet_luxury(self):
        """Artisanal boutique PRD → Quiet Luxury → valid contract."""
        contract = self._run_pipeline(UNSEEN_PRDS["boutique_store"], STYLE_CHOICES["boutique_store"])
        self.assertIn("quiet-luxury".upper(), contract.upper())

    def test_extract_brief_edtech_domain(self):
        """EdTech PRD should bucket to EdTech / Learning Platform, not generic Web App."""
        brief = extract_design_brief(UNSEEN_PRDS["edtech"])
        self.assertIn("edtech", brief["product_type"].lower(),
                      f"Expected EdTech product type, got: {brief['product_type']}")

    def test_extract_brief_logistics_domain(self):
        """Logistics PRD should bucket to Enterprise Operations Platform."""
        brief = extract_design_brief(UNSEEN_PRDS["logistics"])
        product_type = brief["product_type"].lower()
        self.assertTrue(
            "logistics" in product_type or "operations" in product_type or "enterprise" in product_type,
            f"Expected logistics/operations type, got: {brief['product_type']}"
        )
        self.assertEqual(brief["ux_requirements"]["density"], "high")

    def test_extract_brief_boutique_domain(self):
        """Artisanal boutique PRD should produce spacious density and premium positioning."""
        brief = extract_design_brief(UNSEEN_PRDS["boutique_store"])
        self.assertIn(brief["ux_requirements"]["density"], ["spacious", "balanced"])
        prem = brief["brand_positioning_axes"]["premium_vs_accessible"]
        self.assertIn(prem, ["Ultra Premium", "Refined Professional"])


class TestLevel1Refinement(unittest.TestCase):
    """Tests that refine_spec now uses reference library entries, not just hardcoded keywords."""

    def setUp(self):
        from director_engine import create_design_spec
        self.base_spec = create_design_spec("swiss-editorial")

    def test_refine_more_like_vercel(self):
        """'More like Vercel' should trigger dark canvas from the reference library."""
        from director_engine import refine_spec
        result = refine_spec(self.base_spec, "Make it feel more like Vercel")
        diff = result["diff_report"]
        self.assertEqual(diff["matched_reference"], "Vercel",
                         "Expected Vercel to be matched from reference library")
        self.assertGreater(diff["layers_changed_count"], 0,
                           "Expected at least one layer to change")

    def test_refine_more_like_spotify(self):
        """'More like Spotify' should trigger dark/obsidian canvas layers."""
        from director_engine import refine_spec
        result = refine_spec(self.base_spec, "Make it feel more like Spotify")
        diff = result["diff_report"]
        self.assertEqual(diff["matched_reference"], "Spotify")
        changed_layers = [c["layer"] for c in diff["changes"]]
        self.assertIn("color", changed_layers)

    def test_refine_more_like_aesop(self):
        """'More like Aesop' should trigger warm earth palette."""
        from director_engine import refine_spec
        result = refine_spec(self.base_spec, "More like Aesop")
        diff = result["diff_report"]
        self.assertEqual(diff["matched_reference"], "Aesop")

    def test_stable_layers_preserved(self):
        """Refinement should only change targeted layers; all others must remain stable."""
        from director_engine import refine_spec
        result = refine_spec(self.base_spec, "More like Spotify")
        diff = result["diff_report"]
        changed = {c["layer"] for c in diff["changes"]}
        all_layers = set(result["updated_spec"]["layers"].keys())
        stable = all_layers - changed
        self.assertGreater(len(stable), 0, "At least one layer should remain stable")
        for layer in stable:
            self.assertEqual(
                result["updated_spec"]["layers"][layer],
                self.base_spec["layers"][layer],
                f"Layer '{layer}' reported as stable but its value changed"
            )


class TestLevel1AuditOnP2Fixtures(unittest.TestCase):
    """Runs the auditor over all 12 gallery HTML preview files and asserts zero critical violations."""

    def _audit_file(self, style_id: str, html_filename: str):
        from pathlib import Path

        from audit_code import DesignAuditor
        clean_name = html_filename.replace("p2_", "")
        html_path = os.path.join(GALLERY_DIR, clean_name)
        if not os.path.exists(html_path):
            self.skipTest(f"Gallery fixture not found: {clean_name}")
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(html_path, tmp)
            auditor = DesignAuditor(style_id)
            report = auditor.run_audit(Path(tmp))
        criticals = report["summary"]["critical"]
        self.assertEqual(
            criticals, 0,
            f"{style_id}: Expected 0 critical violations, got {criticals}.\n"
            f"Violations: {[v['message'] for v in report.get('violations', [])]}"
        )

    def test_quiet_luxury_p2(self):
        self._audit_file("quiet-luxury", "p2_quiet_luxury.html")

    def test_swiss_editorial_p2(self):
        self._audit_file("swiss-editorial", "p2_swiss_editorial.html")

    def test_neo_brutalism_p2(self):
        self._audit_file("neo-brutalism", "p2_neo_brutalism.html")

    def test_y2k_p2(self):
        self._audit_file("y2k-frutiger-aero", "p2_y2k_frutiger_aero.html")

    def test_cyberpunk_p2(self):
        self._audit_file("cyberpunk", "p2_cyberpunk.html")

    def test_retro_americana_p2(self):
        self._audit_file("retro-americana", "p2_retro_americana.html")

    def test_memphis_p2(self):
        self._audit_file("memphis-postmodern", "p2_memphis_postmodern.html")

    def test_space_age_p2(self):
        self._audit_file("space-age-optimism", "p2_space_age_optimism.html")

    def test_wabi_sabi_p2(self):
        self._audit_file("japanese-wabi-sabi", "p2_japanese_wabi_sabi.html")

    def test_bauhaus_p2(self):
        self._audit_file("bauhaus", "p2_bauhaus.html")

    def test_organic_natural_p2(self):
        self._audit_file("organic-natural", "p2_organic_natural.html")

    def test_maximalist_dopamine_p2(self):
        self._audit_file("maximalist-dopamine", "p2_maximalist_dopamine.html")

    def test_minimal_modern_p2(self):
        self._audit_file("minimal-modern", "minimal_modern.html")

    def test_dark_minimal_p2(self):
        self._audit_file("dark-minimal", "dark_minimal.html")

    def test_terminal_cli_p2(self):
        self._audit_file("terminal-cli", "terminal_cli.html")

    def test_web_brutalism_p2(self):
        self._audit_file("web-brutalism", "web_brutalism.html")

    def test_art_deco_p2(self):
        self._audit_file("art-deco", "art_deco.html")

    def test_mid_century_modern_p2(self):
        self._audit_file("mid-century-modern", "mid_century_modern.html")

    def test_vaporwave_p2(self):
        self._audit_file("vaporwave", "vaporwave.html")

    def test_high_fashion_editorial_p2(self):
        self._audit_file("high-fashion-editorial", "high_fashion_editorial.html")

    # ── New: Tactile family ────────────────────────────────────────────────────
    def test_glassmorphism_p2(self):
        self._audit_file("glassmorphism", "glassmorphism.html")

    def test_neumorphism_p2(self):
        self._audit_file("neumorphism", "neumorphism.html")

    def test_claymorphism_p2(self):
        self._audit_file("claymorphism", "claymorphism.html")

    # ── New: Additional foundations ────────────────────────────────────────────
    def test_data_native_p2(self):
        self._audit_file("data-native", "data_native.html")

    def test_command_center_p2(self):
        self._audit_file("command-center", "command_center.html")

    def test_aurora_gradient_p2(self):
        self._audit_file("aurora-gradient", "aurora_gradient.html")

    def test_digital_organic_p2(self):
        self._audit_file("digital-organic", "digital_organic.html")


if __name__ == "__main__":
    unittest.main()
