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
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-director"))
sys.path.insert(0, str(ROOT_DIR / "skills" / "design-audit"))

from audit_code import DesignAuditor
from director_engine import (
    SUPPORTED_STYLES,
    create_design_spec,
    extract_design_brief,
    find_reference,
    generate_implementation_contract,
    recommend_styles,
    refine_spec,
)


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
        """Criterion 6.6: All 27 style packs contain complete tokens, typography, and negative constraints."""
        styles_dir = ROOT_DIR / "skills" / "design-director" / "styles"

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

    def test_all_27_styles_taxonomy(self):
        """Verifies all 27 styles in the expanded taxonomy can generate valid specs and contracts."""
        self.assertEqual(len(SUPPORTED_STYLES), 27)
        expected_styles = {
            # Original 20
            "swiss-editorial", "neo-brutalism", "y2k-frutiger-aero", "quiet-luxury",
            "cyberpunk", "retro-americana", "memphis-postmodern", "space-age-optimism",
            "japanese-wabi-sabi", "bauhaus", "organic-natural", "maximalist-dopamine",
            "minimal-modern", "dark-minimal", "terminal-cli", "web-brutalism",
            "art-deco", "mid-century-modern", "vaporwave", "high-fashion-editorial",
            # 3 new Tactile foundations
            "glassmorphism", "neumorphism", "claymorphism",
            # 4 new additional foundations
            "data-native", "command-center", "aurora-gradient", "digital-organic",
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

    def test_density_modifiers_in_yaml(self):
        """Verifies all 5 density modifier levels are present in modifiers.yaml."""
        from director_engine import load_modifiers
        mods = load_modifiers()
        self.assertIn("density", mods, "density dimension missing from modifiers.yaml")
        density_ids = [d["id"] for d in mods["density"]]
        for expected in ["ultra-dense", "dense", "balanced", "spacious", "ultra-spacious"]:
            self.assertIn(expected, density_ids, f"Density level '{expected}' missing from modifiers.yaml")
        # Verify each has required tokens
        for d in mods["density"]:
            self.assertIn("tokens", d, f"density/{d['id']} missing tokens block")
            self.assertIn("--density-row-height", d["tokens"]["css"],
                          f"density/{d['id']} missing --density-row-height token")

    def test_bento_grid_modifier_in_yaml(self):
        """Verifies bento-grid is present in the layout modifier dimension."""
        from director_engine import load_modifiers
        mods = load_modifiers()
        self.assertIn("layout", mods, "layout dimension missing from modifiers.yaml")
        layout_ids = [m["id"] for m in mods["layout"]]
        self.assertIn("bento-grid", layout_ids, "bento-grid modifier missing from modifiers.yaml")
        # Verify it has guidelines but NOT radius/color/shadow tokens (composition only)
        bento = next(m for m in mods["layout"] if m["id"] == "bento-grid")
        self.assertIn("guidelines", bento, "bento-grid missing guidelines block")
        self.assertNotIn("tokens", bento, "bento-grid should NOT define design tokens (composition-only)")

    def test_new_7_styles_packs_completeness(self):
        """Criterion 6.6 extended: All 7 new style packs contain complete tokens and NEVER constraints."""
        styles_dir = ROOT_DIR / "skills" / "design-director" / "styles"
        new_styles = [
            "glassmorphism", "neumorphism", "claymorphism",
            "data-native", "command-center", "aurora-gradient", "digital-organic",
        ]
        for style in new_styles:
            style_file = styles_dir / f"{style}.md"
            self.assertTrue(style_file.exists(), f"New style pack missing: {style}.md")
            content = style_file.read_text(encoding="utf-8")
            self.assertTrue(len(content) > 500, f"{style}.md is unexpectedly short")
            self.assertIn("Mandatory Anti-Patterns", content, f"Missing Anti-Patterns in {style}.md")
            self.assertIn("NEVER", content, f"Missing NEVER constraint in {style}.md")
            self.assertIn("Color Tokens", content, f"Missing Color Tokens in {style}.md")
            self.assertTrue(
                "Radius Tokens" in content or "Border Radius" in content,
                f"Missing Border Radius tokens in {style}.md"
            )

    def test_new_7_styles_gallery_previews(self):
        """Verifies all 7 new gallery HTML files exist and have a DESIGN CONTRACT comment."""
        gallery_dir = ROOT_DIR / "skills" / "design-director" / "gallery"
        expected_gallery_files = [
            "glassmorphism.html",
            "neumorphism.html",
            "claymorphism.html",
            "data_native.html",
            "command_center.html",
            "aurora_gradient.html",
            "digital_organic.html",
        ]
        for filename in expected_gallery_files:
            html_path = gallery_dir / filename
            self.assertTrue(html_path.exists(), f"Gallery preview missing: {filename}")
            content = html_path.read_text(encoding="utf-8")
            self.assertIn("DESIGN CONTRACT", content, f"Missing DESIGN CONTRACT comment in {filename}")
            self.assertGreater(len(content), 1000, f"Gallery file suspiciously short: {filename}")

    def test_new_styles_refinement_extended(self):
        """Tests refinement prompts for the 7 new styles."""
        base_spec = create_design_spec("swiss-editorial")

        # Tactile family
        res_glass = refine_spec(base_spec, "make it glassmorphism frosted panel style")
        self.assertIn("glassmorphism", res_glass["updated_spec"]["layers"]["surfaces"])

        res_neu = refine_spec(base_spec, "go neumorphic with soft extruded shadows")
        self.assertIn("neumorphism", res_neu["updated_spec"]["layers"]["surfaces"])

        res_clay = refine_spec(base_spec, "claymorphism pastel 3d clay style")
        self.assertIn("claymorphism", res_clay["updated_spec"]["layers"]["surfaces"])

        # Utility additions
        res_data = refine_spec(base_spec, "data-native dense data analytics style")
        self.assertIn("data-native", res_data["updated_spec"]["layers"]["surfaces"])

        res_cmd = refine_spec(base_spec, "command center multi panel devops layout")
        self.assertIn("command-center", res_cmd["updated_spec"]["layers"]["surfaces"])

        # Futuristic addition
        res_aurora = refine_spec(base_spec, "aurora gradient atmospheric AI style")
        self.assertIn("aurora-gradient", res_aurora["updated_spec"]["layers"]["surfaces"])

        # Organic addition
        res_dorg = refine_spec(base_spec, "digital organic biomorphic blob style")
        self.assertIn("digital-organic", res_dorg["updated_spec"]["layers"]["surfaces"])

    def test_domain_style_defaults_yaml(self):
        """Verifies domain-style-defaults.yaml exists and maps key domains to valid style IDs."""
        import yaml
        domain_defaults_path = ROOT_DIR / "skills" / "design-director" / "styles" / "domain-style-defaults.yaml"
        self.assertTrue(domain_defaults_path.exists(), "domain-style-defaults.yaml missing")
        with open(domain_defaults_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.assertIn("domain_style_defaults", data)
        domains = data["domain_style_defaults"]
        # Must cover key domains
        for key in ["fintech", "healthcare", "legal", "government", "edtech", "devops", "analytics"]:
            self.assertIn(key, domains, f"Domain '{key}' missing from domain-style-defaults.yaml")
        # All referenced style_ids must be in SUPPORTED_STYLES
        for domain_key, domain_data in domains.items():
            for entry in domain_data.get("recommended_styles", []):
                sid = entry["style_id"]
                self.assertIn(sid, SUPPORTED_STYLES,
                              f"domain-style-defaults.yaml references unknown style_id '{sid}' in domain '{domain_key}'")

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

        # Test cyberpunk refinement
        res_cyber = refine_spec(base_spec, "make it more cyberpunk, neon HUD vibes")
        self.assertIn("cyberpunk", res_cyber["updated_spec"]["layers"]["surfaces"])
        self.assertIn("cyberpunk", res_cyber["updated_spec"]["layers"]["color"])
        self.assertGreater(res_cyber["diff_report"]["layers_changed_count"], 0)

        # Test expanded data-native refinement
        res_tabular = refine_spec(base_spec, "more like a data analytics dashboard, dense tabular")
        self.assertIn("data-native", res_tabular["updated_spec"]["layers"]["surfaces"])
        self.assertGreater(res_tabular["diff_report"]["layers_changed_count"], 0)

    def test_domain_style_defaults_wired_recommendations(self):
        """Verifies domain-style-defaults.yaml wires directly into recommend_styles()."""
        # AI Product query
        brief_ai = extract_design_brief("LLM interface for developers")
        recs_ai = recommend_styles(brief_ai)
        ai_style_ids = [r["style_id"] for r in recs_ai]
        self.assertEqual(ai_style_ids, ["aurora-gradient", "dark-minimal", "digital-organic"])

        # DevOps query
        brief_ops = extract_design_brief("DevOps infrastructure monitoring platform")
        recs_ops = recommend_styles(brief_ops)
        ops_style_ids = [r["style_id"] for r in recs_ops]
        self.assertIn("command-center", ops_style_ids)
        self.assertEqual(ops_style_ids, ["command-center", "dark-minimal", "terminal-cli"])

    def test_corporate_memphis_style_exemptions(self):
        """Verifies claymorphism and neumorphism exemptions from Corporate Memphis false positives."""
        import tempfile
        from pathlib import Path
        import sys
        sys.path.insert(0, str(ROOT_DIR / "skills" / "design-audit"))
        from audit_code import DesignAuditor

        # 1. Claymorphism with bubbly container and purple accent -> bubbly container exempt -> WARNING, NOT CRITICAL
        clay_html = '''<div class="card rounded-3xl bg-indigo-500 shadow-xl p-6">Clay card</div>'''
        # 2. Neumorphism with ambient shadow and purple accent -> ambient shadow exempt -> WARNING, NOT CRITICAL
        neu_html = '''<div class="card shadow-lg bg-[#E0E5EC]"><span class="text-purple-600">Neu</span></div>'''
        # 3. Minimal Modern with all 3 signals -> CRITICAL
        memphis_html = '''<div class="card rounded-2xl shadow-lg"><span class="text-purple-600">Memphis</span></div>'''

        with tempfile.TemporaryDirectory() as tmpdir:
            p_clay = Path(tmpdir) / "clay.html"
            p_clay.write_text(clay_html)
            p_neu = Path(tmpdir) / "neu.html"
            p_neu.write_text(neu_html)
            p_mem = Path(tmpdir) / "memphis.html"
            p_mem.write_text(memphis_html)

            rep_clay = DesignAuditor("claymorphism").run_audit(p_clay)
            rep_neu = DesignAuditor("neumorphism").run_audit(p_neu)
            rep_mem = DesignAuditor("minimal-modern").run_audit(p_mem)

            clay_cm = [v for v in rep_clay["violations"] if v["type"] == "corporate_memphis_drift"]
            neu_cm = [v for v in rep_neu["violations"] if v["type"] == "corporate_memphis_drift"]
            mem_cm = [v for v in rep_mem["violations"] if v["type"] == "corporate_memphis_drift"]

            self.assertFalse(any(v["severity"] == "CRITICAL" for v in clay_cm))
            self.assertFalse(any(v["severity"] == "CRITICAL" for v in neu_cm))
            self.assertTrue(any(v["severity"] == "CRITICAL" for v in mem_cm))

    def test_domain_routing_substring_false_positives(self):
        """Regression: keyword matching must use word boundaries. Substrings previously
        misrouted: st-ART-up -> Creator, CRE-ate -> Real Estate, re-VENUE -> Events,
        prev-EVENT -> Events, agri-CULTURE -> Creator."""
        b = extract_design_brief("Build me a website for my startup.")
        self.assertEqual(b["product_type"], "Web Application",
                         "'startup' (contains 'art') misrouted to a domain bucket")

        b = extract_design_brief("A dashboard to create invoices and track revenue per account.")
        self.assertEqual(b["product_type"], "Web Application",
                         "'create'/'revenue' misrouted to Real Estate or Events")

        b = extract_design_brief("A firewall appliance that helps prevent intrusions.")
        self.assertEqual(b["product_type"], "Web Application",
                         "'prevent' misrouted to Events/Entertainment")

        b = extract_design_brief("Software for modern agriculture cooperatives.")
        self.assertEqual(b["product_type"], "Web Application",
                         "'agriculture' (contains 'culture') misrouted to Creator")

    def test_audit_cli_rejects_unknown_style(self):
        """Regression: a typo'd style id must hard-fail in the CLI, not silently report PASSED with zero rules."""
        import subprocess
        import sys
        from audit_code import VALID_STYLES

        # Sync guard: the auditor's CLI whitelist must match the director's taxonomy exactly.
        self.assertEqual(set(VALID_STYLES), set(SUPPORTED_STYLES))

        fixture = ROOT_DIR / "tests" / "fixtures" / "seeded_code" / "deviant_quiet_luxury.html"
        proc = subprocess.run(
            [sys.executable, str(ROOT_DIR / "skills" / "design-audit" / "audit_code.py"),
             "quiet-luxury-TYPO", str(fixture)],
            capture_output=True, text=True
        )
        self.assertNotEqual(proc.returncode, 0, "CLI accepted an unknown style id")
        self.assertIn("Unknown style id", proc.stderr)

    def test_illustration_placeholder_comment_signal(self):
        """Regression: `<!-- illustration: ... -->` comments are a documented Corporate Memphis
        signal and must survive the comment-line skip guard; doc comments must still be ignored."""
        import tempfile
        from pathlib import Path

        # illustration comment + purple accent = 2 signals -> WARNING memphis drift
        slop_html = '''<!-- illustration: friendly hero characters waving -->
<div class="p-4"><span class="text-purple-600">Welcome</span></div>
'''
        # A contract-doc comment quoting banned utilities must NOT create violations.
        doc_html = '''<!-- NEVER use rounded-lg, shadow-md, or bg-blue-600 per DESIGN_CONTRACT.md -->
<div class="p-4 rounded-none">Compliant</div>
'''
        with tempfile.TemporaryDirectory() as tmpdir:
            p_slop = Path(tmpdir) / "slop.html"
            p_slop.write_text(slop_html)
            p_doc = Path(tmpdir) / "doc.html"
            p_doc.write_text(doc_html)

            rep_slop = DesignAuditor("minimal-modern").run_audit(p_slop)
            cm = [v for v in rep_slop["violations"] if v["type"] == "corporate_memphis_drift"]
            self.assertTrue(cm, "Illustration placeholder comment did not contribute a Memphis signal")
            self.assertIn("illustration_placeholder", cm[0]["offending_code"])
            self.assertEqual(cm[0]["severity"], "WARNING")

            rep_doc = DesignAuditor("quiet-luxury").run_audit(p_doc)
            self.assertEqual(rep_doc["summary"]["total_violations"], 0,
                             "Documentation comment produced false positives")

    def test_ambient_shadow_word_boundary(self):
        """Regression: ambient_shadow signal must not fire on substrings like `dropshadow-md`
        (double-backslash regex bug previously matched inside words)."""
        import tempfile
        from pathlib import Path

        # purple + bubbly = 2 signals -> WARNING. A false ambient_shadow hit would make it CRITICAL.
        html = '''<div class="card rounded-2xl dropshadow-md"><span class="text-purple-600">x</span></div>
'''
        with tempfile.TemporaryDirectory() as tmpdir:
            p = Path(tmpdir) / "boundary.html"
            p.write_text(html)
            rep = DesignAuditor("minimal-modern").run_audit(p)
            cm = [v for v in rep["violations"] if v["type"] == "corporate_memphis_drift"]
            self.assertTrue(cm)
            self.assertEqual(cm[0]["severity"], "WARNING",
                             "ambient_shadow fired inside the word 'dropshadow-md'")
            self.assertNotIn("ambient_shadow", cm[0]["offending_code"])


if __name__ == "__main__":
    unittest.main()
