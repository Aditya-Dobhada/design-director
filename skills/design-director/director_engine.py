"""
Design Director Core Reasoning Engine
Handles:
- Context analysis & Design Brief extraction
- Style recommendations with qualitative ratings & honest tradeoffs
- Reference library property lookup & diff resolution
- Fully-resolved layered Design Spec generation (no percentage blending)
- Layer-scoped iterative refinement
- Implementation handoff contract generation
"""

import sys
import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional

REFERENCE_LIBRARY_PATH = Path(__file__).parent / "reference-library.yaml"
STYLES_DIR = Path(__file__).resolve().parent.parent.parent / "styles"

SUPPORTED_STYLES = [
    "swiss-editorial",
    "neo-brutalism",
    "y2k-frutiger-aero",
    "quiet-luxury",
    "cyberpunk",
    "retro-americana",
    "memphis-postmodern",
    "space-age-optimism",
    "japanese-wabi-sabi",
    "bauhaus",
    "organic-natural",
    "maximalist-dopamine"
]

def load_reference_library() -> List[Dict[str, Any]]:
    if not REFERENCE_LIBRARY_PATH.exists():
        return []
    with open(REFERENCE_LIBRARY_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data.get("references", [])

def find_reference(query: str) -> Optional[Dict[str, Any]]:
    refs = load_reference_library()
    query_norm = query.lower().strip()
    
    # Direct match on id or name
    for r in refs:
        if r["id"] == query_norm or r["name"].lower() == query_norm:
            return r
            
    # Substring match
    for r in refs:
        if query_norm in r["id"] or query_norm in r["name"].lower():
            return r
        for trait in r.get("personality", {}).get("traits", []):
            if query_norm in trait:
                return r
    return None

def extract_design_brief(context_text: str) -> Dict[str, Any]:
    """
    Parses product context (PRD, README, spec) into a structured Design Brief.
    Covers 11 domain buckets. Falls through to a neutral SaaS default only when
    no domain signals are found.
    """
    text_lower = context_text.lower()

    # ── 1. FinTech / Wealth ──────────────────────────────────────────────────
    if any(k in text_lower for k in ["wealth", "portfolio", "banking", "finance", "invest", "fintech", "asset", "equity", "fund", "endowment", "trust", "estate planning"]):
        product_type = "FinTech / Wealth Management"
        audience = "High-Net-Worth Individuals, Family Offices, and Wealth Advisory Teams"
        traits = ["authoritative", "understated", "meticulous", "discreet"]
        density = "spacious"
        info_load = "curated-editorial"
        workflow = "contemplative-decision-making"
        playful_serious = "Strongly Serious"
        premium_accessible = "Ultra Premium"
        futuristic_institutional = "Institutional / Traditional"

    # ── 2. Developer Tools / Infrastructure ─────────────────────────────────
    elif re.search(r'\b(developer|engineers?|api|cli|telemetry|kubernetes|terminal|sre|devops|sdk|ci/cd|pipeline|codebase|repository|deployment|observability)\b', text_lower):
        product_type = "Developer Tool / Platform"
        audience = "Software Engineers and Technical Operators"
        traits = ["tactical", "high-performance", "keyboard-first", "focused"]
        density = "high"
        info_load = "dense-tabular"
        workflow = "keyboard-driven-operational"
        playful_serious = "Strongly Serious"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Futuristic / Avant-Garde"

    # ── 3. EdTech / Learning ─────────────────────────────────────────────────
    elif any(k in text_lower for k in ["learning", "education", "student", "teacher", "course", "curriculum", "lesson", "quiz", "edtech", "academy", "tutoring", "classroom", "lms"]):
        product_type = "EdTech / Learning Platform"
        audience = "Students, Educators, and Learning Institutions"
        traits = ["clear", "encouraging", "structured", "accessible"]
        density = "balanced"
        info_load = "modular"
        workflow = "guided-task-completion"
        playful_serious = "Balanced"
        premium_accessible = "Accessible / Mass Appeal"
        futuristic_institutional = "Contemporary Modern"

    # ── 4. Healthcare / Clinical ─────────────────────────────────────────────
    elif any(k in text_lower for k in ["patient", "clinical", "medical", "health", "ehr", "hipaa", "hospital", "physician", "diagnosis", "pharmacy", "telehealth", "wellness"]):
        product_type = "Healthcare / Clinical Platform"
        audience = "Clinical Staff, Patients, and Healthcare Administrators"
        traits = ["trustworthy", "calm", "legible", "compliant"]
        density = "balanced"
        info_load = "curated-editorial"
        workflow = "guided-task-completion"
        playful_serious = "Strongly Serious"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Institutional / Traditional"

    # ── 5. Logistics / Operations / Supply Chain ──────────────────────────────
    # Must come before Legal to prevent "compliance alerts" in freight PRDs from matching Legal.
    elif any(k in text_lower for k in ["logistics", "supply chain", "warehouse", "fleet", "freight", "shipping", "dispatch", "inventory", "fulfilment", "depot", "hos violation"]):
        product_type = "Enterprise Operations Platform"
        audience = "Operations Teams, Logistics Managers, and Enterprise Administrators"
        traits = ["dependable", "functional", "efficient", "clear"]
        density = "high"
        info_load = "dense-tabular"
        workflow = "keyboard-driven-operational"
        playful_serious = "Strongly Serious"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 6. Legal / Compliance ────────────────────────────────────────────────
    elif any(k in text_lower for k in ["legal", "law firm", "contract", "compliance", "regulatory", "litigation", "counsel", "attorney", "paralegal", "due diligence"]):
        product_type = "Legal / Compliance Platform"
        audience = "Attorneys, Legal Operations Teams, and Compliance Officers"
        traits = ["authoritative", "meticulous", "precise", "institutional"]
        density = "balanced"
        info_load = "dense-tabular"
        workflow = "guided-task-completion"
        playful_serious = "Strongly Serious"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Institutional / Traditional"

    # ── 7. Ecological / Organic / Sustainability ─────────────────────────────
    elif any(k in text_lower for k in ["organic", "nature", "botanical", "climate", "sustainable", "sustainability", "ecology", "earth", "biophilic", "regenerative", "conservation"]):
        product_type = "Ecological / Organic Living"
        audience = "Conscious Consumers, Environmental Stewards, and Botanical Enthusiasts"
        traits = ["grounded", "authentic", "mindful", "tactile"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 8. Luxury / Premium Consumer ─────────────────────────────────────────
    # Must come before Creator so "boutique" and "artisanal" don't fall into the
    # Creator bucket (which sets Accessible/Mass Appeal premium positioning).
    elif any(k in text_lower for k in ["luxury", "boutique", "premium", "exclusive", "bespoke", "couture", "artisanal", "high-end", "atelier"]):
        product_type = "Luxury / Premium Consumer"
        audience = "Affluent Consumers Seeking Premium Experiences"
        traits = ["refined", "understated", "exclusive", "crafted"]
        density = "spacious"
        info_load = "curated-editorial"
        workflow = "contemplative-decision-making"
        playful_serious = "Strongly Serious"
        premium_accessible = "Ultra Premium"
        futuristic_institutional = "Contemporary Modern"

    # ── 9. Creator / Commerce / Cultural ─────────────────────────────────────
    elif any(k in text_lower for k in ["creator", "commerce", "art", "music", "zine", "indie", "marketplace", "storefront", "streetwear", "fashion", "culture", "editorial"]):
        product_type = "Creator Marketplace / Community"
        audience = "Independent Creators, Artists, and Cultural Enthusiasts"
        traits = ["unapologetic", "expressive", "tactile", "energetic"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Accessible / Mass Appeal"
        futuristic_institutional = "Contemporary Modern"

    # ── 10. Real Estate / Property ────────────────────────────────────────────
    elif any(k in text_lower for k in ["real estate", "property", "listing", "mortgage", "broker", "mls", "rental", "cre", "proptech"]):
        product_type = "Real Estate / Property Platform"
        audience = "Home Buyers, Property Investors, and Real Estate Agents"
        traits = ["trustworthy", "clear", "aspirational", "approachable"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 11. Events / Entertainment / Community ────────────────────────────────
    elif any(k in text_lower for k in ["event", "concert", "ticket", "venue", "entertainment", "community", "social", "gaming", "esports", "streaming"]):
        product_type = "Events / Entertainment Platform"
        audience = "General Consumers and Community Members"
        traits = ["energetic", "social", "vibrant", "accessible"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Strongly Playful"
        premium_accessible = "Accessible / Mass Appeal"
        futuristic_institutional = "Contemporary Modern"

    # ── 12. Generic SaaS / Web Application ───────────────────────────────────
    else:
        product_type = "Web Application"
        audience = "General Users"
        traits = ["intentional", "crafted", "clear", "distinctive"]
        density = "balanced"
        info_load = "modular"
        workflow = "guided-task-completion"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── Visual constraints (cross-cutting) ──────────────────────────────────
    strict_readability = product_type in ["FinTech / Wealth Management", "Healthcare / Clinical Platform", "Legal / Compliance Platform", "Enterprise Operations Platform", "Developer Tool / Platform"]
    accessibility = (
        "Strict WCAG AAA readability for critical numerical/tabular data"
        if strict_readability
        else "Standard WCAG AA compliance"
    )
    readability = "Critical: tabular numbers, high contrast ratios, zero ambiguous glyphs" if strict_readability else "Standard readability requirements"
    motion_tolerance = (
        "Restrained / Minimal: strictly functional transitions, zero bouncing"
        if product_type in ["FinTech / Wealth Management", "Healthcare / Clinical Platform", "Legal / Compliance Platform", "Enterprise Operations Platform", "Developer Tool / Platform"]
        else "Dynamic and fluid"
    )

    return {
        "product_type": product_type,
        "target_audience": audience,
        "personality_traits": traits,
        "ux_requirements": {
            "density": density,
            "information_load": info_load,
            "workflow_orientation": workflow
        },
        "brand_positioning_axes": {
            "playful_vs_serious": playful_serious,
            "premium_vs_accessible": premium_accessible,
            "futuristic_vs_institutional": futuristic_institutional
        },
        "visual_constraints": {
            "accessibility_needs": accessibility,
            "readability_criticality": readability,
            "motion_tolerance": motion_tolerance
        }
    }

def recommend_styles(brief: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Given a Design Brief, recommends 2-4 candidate directions.
    Qualitative fit ratings only: Strong fit / Good fit / Possible / Poor fit.
    Every recommendation must include at least one honest tradeoff/risk.
    """
    recs = []
    p_type = brief.get("product_type", "").lower()
    density = brief.get("ux_requirements", {}).get("density", "")
    axes = brief.get("brand_positioning_axes", {})
    pos_prem = axes.get("premium_vs_accessible", "")
    pos_fut = axes.get("futuristic_vs_institutional", "")

    if "wealth" in p_type or "fintech" in p_type or "ultra premium" in pos_prem.lower():
        recs.append({
            "name": "Quiet Luxury",
            "style_id": "quiet-luxury",
            "fit_rating": "Strong fit",
            "reasoning": "Understated alabaster palette, immaculate serif typography, and generous whitespace convey deep institutional trust, bespoke advisory craft, and financial gravitas without screaming.",
            "tradeoffs": [
                "Generous whitespace reduces immediate above-the-fold information density.",
                "Zero border-radius and pale stone dividers require rigorous content discipline to prevent looking sparse or unstyled on smaller screens."
            ]
        })
        recs.append({
            "name": "Japanese Wabi-Sabi",
            "style_id": "japanese-wabi-sabi",
            "fit_rating": "Good fit",
            "reasoning": "Contemplative rice-paper tones, Mingei craft philosophy, and profound ma (whitespace) communicate timeless permanence, humility, and generational stewardship.",
            "tradeoffs": [
                "Extreme quietness and organic asymmetry can feel unfamiliar to users expecting traditional financial dashboards."
            ]
        })
        recs.append({
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Good fit",
            "reasoning": "Rigorous asymmetric grid, razor-sharp hairlines, and high-contrast typography give financial data objective clarity and architectural prestige.",
            "tradeoffs": [
                "Stark monochrome palette can feel overly sterile or clinical if not softened with an intentional warm accent.",
                "Demands high typographic discipline in tabular layouts."
            ]
        })
    elif "organic" in p_type or "ecological" in p_type:
        recs.append({
            "name": "Organic Natural",
            "style_id": "organic-natural",
            "fit_rating": "Strong fit",
            "reasoning": "Earth and botanical pigment palette (clay, moss, sap), river-stone pod containers, and living-system geometry authentically connect users to nature and regenerative craft.",
            "tradeoffs": [
                "Organic rounded geometry consumes more padding and reduces raw data density.",
                "Requires careful contrast calibration to ensure accessible contrast on linen backgrounds."
            ]
        })
        recs.append({
            "name": "Japanese Wabi-Sabi",
            "style_id": "japanese-wabi-sabi",
            "fit_rating": "Good fit",
            "reasoning": "Handmade ceramic warmth, ink wash textures, and profound empty space reflect environmental humility and artisanal mindfulness.",
            "tradeoffs": [
                "Asymmetric unhurried layouts require disciplined content curation."
            ]
        })
        recs.append({
            "name": "Retro Americana",
            "style_id": "retro-americana",
            "fit_rating": "Possible",
            "reasoning": "Evokes National Parks heritage, WPA conservation posters, and rustic outdoorsmanship.",
            "tradeoffs": [
                "Heavy ink borders and slab serifs lean nostalgic rather than contemporary biophilic."
            ]
        })
    elif "developer" in p_type or "platform" in p_type or "telemetry" in p_type or density == "high":
        recs.append({
            "name": "Cyberpunk",
            "style_id": "cyberpunk",
            "fit_rating": "Strong fit",
            "reasoning": "Obsidian canvas, monospace telemetry, and neon HUD brackets provide an immersive, high-density environment ideal for monitoring streams, terminals, and complex technical metrics.",
            "tradeoffs": [
                "Dark-only aesthetic makes daylight readability challenging.",
                "High sensory intensity is unsuitable for calm documentation or administrative configuration flows."
            ]
        })
        recs.append({
            "name": "Bauhaus",
            "style_id": "bauhaus",
            "fit_rating": "Good fit",
            "reasoning": "Form strictly follows function: rigorous constructivist 8px grid, primary triad accents, Herbert Bayer functional type, and zero extraneous ornament.",
            "tradeoffs": [
                "Radical functionalism and stark primary color blocks can feel rigid or austere for consumer audiences."
            ]
        })
        recs.append({
            "name": "Space Age Optimism",
            "style_id": "space-age-optimism",
            "fit_rating": "Good fit",
            "reasoning": "Warm white fiberglass pods, NASA mission orange accents, and clean geometric typography bring high technical capability with radiant human optimism.",
            "tradeoffs": [
                "Pod curves require generous padding that slightly limits maximum line density compared to monospace terminals."
            ]
        })
        recs.append({
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Good fit",
            "reasoning": "Objective typographic hierarchy, tabular data discipline, and modular asymmetric layouts turn dense technical data into an effortless, readable broadsheet.",
            "tradeoffs": [
                "Lacks the futuristic, high-octane gaming or hacker excitement of dark telemetry consoles."
            ]
        })
    elif "creator" in p_type or "marketplace" in p_type:
        recs.append({
            "name": "Neo-Brutalism",
            "style_id": "neo-brutalism",
            "fit_rating": "Strong fit",
            "reasoning": "Chunky solid black outlines, hard offset shadows, and saturated color pops communicate authentic grassroots energy, anti-corporate rebellion, and tactile physicality.",
            "tradeoffs": [
                "High visual volume can overwhelm subtle product imagery or art if colors compete directly."
            ]
        })
        recs.append({
            "name": "Maximalist Dopamine",
            "style_id": "maximalist-dopamine",
            "fit_rating": "Good fit",
            "reasoning": "Sticker-bomb badges, candy neon explosions, and chaotic typography shifts create hyper-sensory joy for youth culture, streetwear, and drops.",
            "tradeoffs": [
                "Visual density and colliding hues can cause fatigue during prolonged administrative tasks."
            ]
        })
        recs.append({
            "name": "Memphis Postmodern",
            "style_id": "memphis-postmodern",
            "fit_rating": "Good fit",
            "reasoning": "Ettore Sottsass pattern collisions (polka dots, diagonal hatch, squiggles) celebrate creative freedom and intentional kitsch.",
            "tradeoffs": [
                "Ornamental pattern fills require careful layering to avoid competing with actual creator products."
            ]
        })
        recs.append({
            "name": "Retro Americana",
            "style_id": "retro-americana",
            "fit_rating": "Possible",
            "reasoning": "Roadside diner warmth, Saul Bass poster silhouettes, and letterpress ink slabs bring authentic heritage craft.",
            "tradeoffs": [
                "Nostalgic 1950s-70s aesthetic may feel dated for bleeding-edge digital art."
            ]
        })
    else:
        recs.append({
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Strong fit",
            "reasoning": "Universal architectural clarity, disciplined modular grids, and timeless typography elevate standard workflows into premium editorial experiences.",
            "tradeoffs": [
                "Requires high-quality typographic assets and rigorous alignment discipline.",
                "Zero-radius aesthetic can feel austere if not balanced with purposeful accent color."
            ]
        })
        recs.append({
            "name": "Quiet Luxury",
            "style_id": "quiet-luxury",
            "fit_rating": "Good fit",
            "reasoning": "Warm alabaster tones and immaculate serif headings create an immediate sense of craft, calm focus, and premium quality.",
            "tradeoffs": [
                "Requires generous whitespace which may not suit compact desktop dashboards."
            ]
        })
        recs.append({
            "name": "Neo-Brutalism",
            "style_id": "neo-brutalism",
            "fit_rating": "Possible",
            "reasoning": "Brings bold, high-contrast personality that immediately differentiates the product from cookie-cutter SaaS competitors.",
            "tradeoffs": [
                "Polarizing aesthetic that may be considered too unconventional for conservative enterprise users."
            ]
        })
    return recs

def create_design_spec(style_id: str, custom_layers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Creates a layered Design Spec where every layer resolves to a single source of truth.
    No ambiguous percentage blending.
    """
    # Base layer mappings per canonical style
    style_bases = {
        "swiss-editorial": {
            "layout": "swiss-editorial/layout.md",
            "typography": "swiss-editorial/typography.md",
            "surfaces": "swiss-editorial/tokens.md",
            "color": "swiss-editorial/tokens.md",
            "motion": "swiss-editorial/motion.md",
            "imagery": "conceptual-duotone-linework",
            "components": "swiss-editorial/components.md"
        },
        "neo-brutalism": {
            "layout": "neo-brutalism/layout.md",
            "typography": "neo-brutalism/typography.md",
            "surfaces": "neo-brutalism/tokens.md",
            "color": "neo-brutalism/tokens.md",
            "motion": "neo-brutalism/motion.md",
            "imagery": "bold-graphic-stickers-linework",
            "components": "neo-brutalism/components.md"
        },
        "quiet-luxury": {
            "layout": "quiet-luxury/layout.md",
            "typography": "quiet-luxury/typography.md",
            "surfaces": "quiet-luxury/tokens.md",
            "color": "quiet-luxury/tokens.md",
            "motion": "quiet-luxury/motion.md",
            "imagery": "architectural-still-life-monochrome",
            "components": "quiet-luxury/components.md"
        },
        "y2k-frutiger-aero": {
            "layout": "y2k-frutiger-aero/layout.md",
            "typography": "y2k-frutiger-aero/typography.md",
            "surfaces": "y2k-frutiger-aero/tokens.md",
            "color": "y2k-frutiger-aero/tokens.md",
            "motion": "y2k-frutiger-aero/motion.md",
            "imagery": "optimistic-3d-gloss-renders",
            "components": "y2k-frutiger-aero/components.md"
        },
        "cyberpunk": {
            "layout": "cyberpunk/layout.md",
            "typography": "cyberpunk/typography.md",
            "surfaces": "cyberpunk/tokens.md",
            "color": "cyberpunk/tokens.md",
            "motion": "cyberpunk/motion.md",
            "imagery": "wireframe-hud-schematics",
            "components": "cyberpunk/components.md"
        },
        "retro-americana": {
            "layout": "retro-americana/layout.md",
            "typography": "retro-americana/typography.md",
            "surfaces": "retro-americana/tokens.md",
            "color": "retro-americana/tokens.md",
            "motion": "retro-americana/motion.md",
            "imagery": "screenprint-woodblock-halftone",
            "components": "retro-americana/components.md"
        },
        "memphis-postmodern": {
            "layout": "memphis-postmodern/layout.md",
            "typography": "memphis-postmodern/typography.md",
            "surfaces": "memphis-postmodern/tokens.md",
            "color": "memphis-postmodern/tokens.md",
            "motion": "memphis-postmodern/motion.md",
            "imagery": "geometric-squiggle-polka-patterns",
            "components": "memphis-postmodern/components.md"
        },
        "space-age-optimism": {
            "layout": "space-age-optimism/layout.md",
            "typography": "space-age-optimism/typography.md",
            "surfaces": "space-age-optimism/tokens.md",
            "color": "space-age-optimism/tokens.md",
            "motion": "space-age-optimism/motion.md",
            "imagery": "molded-fiberglass-moiré-vector",
            "components": "space-age-optimism/components.md"
        },
        "japanese-wabi-sabi": {
            "layout": "japanese-wabi-sabi/layout.md",
            "typography": "japanese-wabi-sabi/typography.md",
            "surfaces": "japanese-wabi-sabi/tokens.md",
            "color": "japanese-wabi-sabi/tokens.md",
            "motion": "japanese-wabi-sabi/motion.md",
            "imagery": "shodō-ink-wash-botanical-ceramic",
            "components": "japanese-wabi-sabi/components.md"
        },
        "bauhaus": {
            "layout": "bauhaus/layout.md",
            "typography": "bauhaus/typography.md",
            "surfaces": "bauhaus/tokens.md",
            "color": "bauhaus/tokens.md",
            "motion": "bauhaus/motion.md",
            "imagery": "constructivist-circle-square-triangle",
            "components": "bauhaus/components.md"
        },
        "organic-natural": {
            "layout": "organic-natural/layout.md",
            "typography": "organic-natural/typography.md",
            "surfaces": "organic-natural/tokens.md",
            "color": "organic-natural/tokens.md",
            "motion": "organic-natural/motion.md",
            "imagery": "botanical-specimen-fine-linework",
            "components": "organic-natural/components.md"
        },
        "maximalist-dopamine": {
            "layout": "maximalist-dopamine/layout.md",
            "typography": "maximalist-dopamine/typography.md",
            "surfaces": "maximalist-dopamine/tokens.md",
            "color": "maximalist-dopamine/tokens.md",
            "motion": "maximalist-dopamine/motion.md",
            "imagery": "sticker-bomb-net-art-collages",
            "components": "maximalist-dopamine/components.md"
        }
    }

    base = style_bases.get(style_id, style_bases["swiss-editorial"]).copy()
    
    # Layer overrides if custom composition is specified
    if custom_layers:
        for layer, source in custom_layers.items():
            if layer in base:
                base[layer] = source

    spec = {
        "chosen_primary_style": style_id,
        "layers": {
            "layout": base["layout"],
            "typography": base["typography"],
            "surfaces": base["surfaces"],
            "color": base["color"],
            "motion": base["motion"],
            "imagery": base["imagery"],
            "components": base["components"]
        },
        "constraints": {
            "no_percentage_blends": True,
            "single_source_of_truth_per_layer": True
        }
    }
    return spec

def _resolve_layers_from_reference(ref: Dict[str, Any], direction: str) -> Dict[str, str]:
    """
    Translates a reference library entry into concrete spec layer overrides.
    direction is either 'more_like' or 'less_like'.
    Reads the reference's mode, borders, motion, typography, and color fields
    to produce actionable file-path overrides.
    """
    overrides: Dict[str, str] = {}
    shift_key = "when_requested_more_like" if direction == "more_like" else "when_requested_less_like"
    shift_rules = ref.get("shift_rules", {}).get(shift_key, {})
    mode = ref.get("mode", "")
    color = ref.get("color", {})
    palette_type = color.get("palette_type", "")
    borders = ref.get("borders", "")
    shadows = ref.get("shadows", "")
    motion = ref.get("motion", {})
    motion_char = motion.get("character", "")
    motion_ms = motion.get("duration_ms", 200)

    # ── Mode / canvas ────────────────────────────────────────────────────────
    if direction == "more_like":
        if "dark" in mode or "obsidian" in palette_type:
            overrides["color"] = "cyberpunk/tokens.md"
            overrides["surfaces"] = "cyberpunk/tokens.md"
        elif "warm" in mode or "warm" in palette_type or "earth" in palette_type or "linen" in palette_type:
            overrides["color"] = "quiet-luxury/tokens.md"
            overrides["surfaces"] = "quiet-luxury/tokens.md"
        elif "monochrome" in palette_type and "stark" in palette_type:
            overrides["color"] = "swiss-editorial/tokens.md"
            overrides["surfaces"] = "swiss-editorial/tokens.md"
        elif "saturated" in palette_type or "pop" in palette_type or "neon" in palette_type:
            overrides["color"] = "neo-brutalism/tokens.md"
            overrides["surfaces"] = "neo-brutalism/tokens.md"
        elif "gradient" in palette_type or "fluid" in palette_type:
            overrides["color"] = "y2k-frutiger-aero/tokens.md"
            overrides["surfaces"] = "y2k-frutiger-aero/tokens.md"
    else:  # less_like: invert the dominant signal
        if "dark" in mode:
            overrides["color"] = "swiss-editorial/tokens.md"
        if "saturated" in palette_type or "neon" in palette_type:
            overrides["color"] = "quiet-luxury/tokens.md"
            overrides["surfaces"] = "quiet-luxury/tokens.md"

    # ── Borders / surfaces (override color above if borders are more specific) ──
    if direction == "more_like":
        if "heavy" in borders or "thick" in borders or "3px" in borders or "4px" in borders:
            overrides["surfaces"] = "neo-brutalism/tokens.md"
        elif "hairline" in borders or "0.5px" in borders or "subtle" in borders:
            if "dark" in mode:
                overrides["surfaces"] = "cyberpunk/tokens.md"
            else:
                overrides["surfaces"] = "swiss-editorial/tokens.md"
        elif "none" in borders or "zero" in borders or "flat" in borders:
            overrides["surfaces"] = "swiss-editorial/tokens.md"
        if "hard" in shadows and "offset" in shadows:
            overrides["surfaces"] = "neo-brutalism/tokens.md"

    # ── Typography ───────────────────────────────────────────────────────────
    if direction == "more_like":
        typography = ref.get("typography", {})
        heading = typography.get("heading_font", "").lower()
        tracking = typography.get("tracking", "")
        if any(k in heading for k in ["garamond", "serif", "canela", "fraunces", "suisse works"]):
            overrides["typography"] = "quiet-luxury/typography.md"
        elif any(k in heading for k in ["slab", "condensed", "rockwell", "alfa"]):
            overrides["typography"] = "retro-americana/typography.md"
        elif any(k in heading for k in ["mono", "consolas", "courier", "fixed"]):
            overrides["typography"] = "cyberpunk/typography.md"
        elif any(k in heading for k in ["playfair", "editorial"]):
            overrides["typography"] = "swiss-editorial/typography.md"
        elif any(k in heading for k in ["ibm plex", "geometric sans", "bayer"]):
            overrides["typography"] = "bauhaus/typography.md"

    # ── Motion ───────────────────────────────────────────────────────────────
    if direction == "more_like":
        if motion_ms <= 120 or any(k in motion_char for k in ["snappy", "instant", "immediate", "fast"]):
            overrides["motion"] = "swiss-editorial/motion.md"
        elif motion_ms >= 400 or any(k in motion_char for k in ["slow", "contemplative", "cinematic"]):
            overrides["motion"] = "quiet-luxury/motion.md"
        elif any(k in motion_char for k in ["bounce", "spring", "fluid"]):
            overrides["motion"] = "y2k-frutiger-aero/motion.md"
        elif any(k in motion_char for k in ["mechanical", "click", "toggle"]):
            overrides["motion"] = "neo-brutalism/motion.md"

    # ── Shift-rule overrides (explicit YAML shift_rules take priority) ────────
    sr_mode = shift_rules.get("mode", "")
    sr_borders = shift_rules.get("borders", "")
    sr_typography = shift_rules.get("typography", "")
    sr_motion = shift_rules.get("motion", "")
    if "dark" in sr_mode:
        overrides["color"] = "cyberpunk/tokens.md"
        overrides["surfaces"] = "cyberpunk/tokens.md"
    if "light" in sr_mode or "warm" in sr_mode:
        overrides["color"] = "swiss-editorial/tokens.md"
    if "heavy" in sr_borders or "solid" in sr_borders:
        overrides["surfaces"] = "neo-brutalism/tokens.md"
    if "hairline" in sr_borders or "hairline" in sr_borders:
        overrides["surfaces"] = "cyberpunk/tokens.md" if "dark" in sr_mode else "swiss-editorial/tokens.md"
    if "serif" in sr_typography:
        overrides["typography"] = "quiet-luxury/typography.md"
    if "snappy" in sr_motion or "fast" in sr_motion:
        overrides["motion"] = "swiss-editorial/motion.md"

    return overrides


def refine_spec(current_spec: Dict[str, Any], critique: str) -> Dict[str, Any]:
    """
    Applies free-text critique layer-by-layer.

    Priority order:
      1. Named brand/product from reference library → use _resolve_layers_from_reference()
      2. Named style family shortcuts (wabi, bauhaus, memphis, etc.)
      3. Generic directional keywords (too dark, more playful, etc.)
      4. Layer-targeted fallback (font, shadow, border)

    Unrelated layers remain completely stable.
    """
    updated_spec = json.loads(json.dumps(current_spec))
    critique_lower = critique.lower()
    changes_made = []

    # ── Determine direction ──────────────────────────────────────────────────
    is_more_like = "more" in critique_lower or "like" in critique_lower or "feel" in critique_lower
    is_less_like = "less" in critique_lower or "not" in critique_lower or "too" in critique_lower
    direction = "more_like" if is_more_like and not is_less_like else ("less_like" if is_less_like else "more_like")

    # ── 1. Reference library brand match ────────────────────────────────────
    refs = load_reference_library()
    matched_ref = None
    for r in refs:
        if r["id"] in critique_lower or r["name"].lower() in critique_lower:
            matched_ref = r
            break

    if matched_ref:
        layer_overrides = _resolve_layers_from_reference(matched_ref, direction)
        brand_name = matched_ref["name"]
        for layer, new_val in layer_overrides.items():
            old_val = updated_spec["layers"].get(layer, "")
            if old_val != new_val:
                updated_spec["layers"][layer] = new_val
                changes_made.append({
                    "layer": layer,
                    "old": old_val,
                    "new": new_val,
                    "reason": f"{direction.replace('_', ' ').title()} {brand_name}: derived from reference library (mode={matched_ref.get('mode', '?')}, palette={matched_ref.get('color', {}).get('palette_type', '?')})."
                })

    # ── 2. Named style family shortcuts ─────────────────────────────────────
    elif any(k in critique_lower for k in ["wabi", "sabi", "zen", "japanese"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "japanese-wabi-sabi/tokens.md",
            "color": "japanese-wabi-sabi/tokens.md",
            "motion": "japanese-wabi-sabi/motion.md",
        }, reasons={
            "surfaces": "Mingei craft shift: rice-paper surfaces and ink-wash dividers.",
            "color": "Natural pigments: charcoal ink stone, bamboo cream, and matcha accents.",
            "motion": "Contemplative, breath-paced motion transitions.",
        })
    elif any(k in critique_lower for k in ["bauhaus", "constructivist"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "bauhaus/tokens.md",
            "color": "bauhaus/tokens.md",
            "typography": "bauhaus/typography.md",
        }, reasons={
            "surfaces": "Constructivist functionalism: 0px radius, structural black outlines.",
            "color": "Pure primary triad: Red, Yellow, Blue on black and white.",
            "typography": "Herbert Bayer Universal functional geometric sans.",
        })
    elif any(k in critique_lower for k in ["space age", "space-age", "nasa"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "space-age-optimism/tokens.md",
            "color": "space-age-optimism/tokens.md",
            "layout": "space-age-optimism/layout.md",
        }, reasons={
            "surfaces": "Space Age shift: molded pod fiberglass containers (24px–40px radius).",
            "color": "Warm optical white with single NASA Mission Orange accent.",
            "layout": "Capsule pod grid and moiré concentric circle framing.",
        })
    elif any(k in critique_lower for k in ["maximalist", "dopamine", "sticker"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "maximalist-dopamine/tokens.md",
            "color": "maximalist-dopamine/tokens.md",
            "components": "maximalist-dopamine/components.md",
        }, reasons={
            "surfaces": "Maximalist shift: multi-colored hard offset drop shadows.",
            "color": "Colliding candy neon palette (Yellow, Magenta, Cyan, Lime).",
            "components": "Sticker-bomb tags and pop-up button hover mechanics.",
        })
    elif any(k in critique_lower for k in ["memphis", "postmodern", "sottsass"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "memphis-postmodern/tokens.md",
            "color": "memphis-postmodern/tokens.md",
            "layout": "memphis-postmodern/layout.md",
        }, reasons={
            "surfaces": "Memphis shift: flat graphic planes and polka-dot/diagonal hatch patterns.",
            "color": "Contrasting primaries and pastels on stark white canvas.",
            "layout": "Pattern-filled panels and eccentric geometric arrangements.",
        })
    elif any(k in critique_lower for k in ["americana", "diner", "saul bass"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "retro-americana/tokens.md",
            "color": "retro-americana/tokens.md",
            "typography": "retro-americana/typography.md",
        }, reasons={
            "surfaces": "Retro Americana shift: ink-press borders and parchment paper canvas.",
            "color": "Warm incandescent palette: vermilion, neon amber, and deep carbon ink.",
            "typography": "Slab serif display headers and condensed poster typography.",
        })
    elif any(k in critique_lower for k in ["organic", "natural", "biophilic", "earthy"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "organic-natural/tokens.md",
            "color": "organic-natural/tokens.md",
            "typography": "organic-natural/typography.md",
        }, reasons={
            "surfaces": "Organic shift: river-stone rounding and bone-white canvas.",
            "color": "Natural earth palette: raw clay, moss green, and bone white.",
            "typography": "Humanist oldstyle serif hierarchy with warm reading proportions.",
        })

    # ── 3. Generic directional keywords ─────────────────────────────────────
    elif "bank" in critique_lower or "corporate" in critique_lower:
        if is_less_like:
            if "quiet-luxury" in current_spec["chosen_primary_style"]:
                _apply_layers(updated_spec, current_spec, changes_made, {
                    "typography": "quiet-luxury/typography.md",
                    "color": "quiet-luxury/tokens.md",
                }, reasons={
                    "typography": "Eliminated standard corporate sans; instituted authoritative literary serif hierarchy.",
                    "color": "Alabaster and deep espresso — no corporate navy or generic Tailwind grays.",
                })
            else:
                _apply_layers(updated_spec, current_spec, changes_made, {
                    "typography": "swiss-editorial/typography.md",
                    "surfaces": "neo-brutalism/tokens.md",
                }, reasons={
                    "typography": "High-contrast editorial sans instead of rounded corporate defaults.",
                    "surfaces": "Replaced timid gray-bordered corporate cards with tangible, purposeful border contrast.",
                })
    elif "playful" in critique_lower or "tactile" in critique_lower:
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "neo-brutalism/tokens.md",
            "components": "neo-brutalism/components.md",
        }, reasons={
            "surfaces": "Physical paper cards with 3px solid black outlines and 4px solid offset shadows.",
            "components": "Physical button switch behavior: depression translation on active click.",
        })
    elif "too dark" in critique_lower or "light mode" in critique_lower or "make it light" in critique_lower:
        _apply_layers(updated_spec, current_spec, changes_made, {
            "color": "swiss-editorial/tokens.md",
        }, reasons={
            "color": "Switched canvas to crisp high-contrast light mode (#FFFFFF / #F8F8F6).",
        })

    # ── 4. Layer-targeted fallback ───────────────────────────────────────────
    else:
        if "font" in critique_lower or "typography" in critique_lower:
            _apply_layers(updated_spec, current_spec, changes_made, {
                "typography": "swiss-editorial/typography.md",
            }, reasons={
                "typography": "Refined typographic scale to high-contrast asymmetric Swiss hierarchy.",
            })
        elif "shadow" in critique_lower or "border" in critique_lower or "surface" in critique_lower:
            _apply_layers(updated_spec, current_spec, changes_made, {
                "surfaces": "swiss-editorial/tokens.md",
            }, reasons={
                "surfaces": "Cleaned surfaces to 0px border-radius and crisp hairlines.",
            })

    result = {
        "updated_spec": updated_spec,
        "diff_report": {
            "critique_received": critique,
            "matched_reference": matched_ref["name"] if matched_ref else None,
            "layers_changed_count": len(changes_made),
            "layers_preserved_count": len(updated_spec["layers"]) - len(changes_made),
            "changes": changes_made,
            "stable_layers": [k for k in updated_spec["layers"].keys() if not any(c["layer"] == k for c in changes_made)]
        }
    }
    return result


def _apply_layers(
    updated_spec: Dict[str, Any],
    current_spec: Dict[str, Any],
    changes_made: List[Dict[str, Any]],
    layer_map: Dict[str, str],
    reasons: Dict[str, str]
) -> None:
    """Helper: apply layer overrides and record diffs."""
    for layer, new_val in layer_map.items():
        old_val = current_spec["layers"].get(layer, "")
        updated_spec["layers"][layer] = new_val
        changes_made.append({
            "layer": layer,
            "old": old_val,
            "new": new_val,
            "reason": reasons.get(layer, "")
        })

def generate_implementation_contract(spec: Dict[str, Any], product_spec: str, tech_stack: str = "Tailwind CSS + React") -> str:
    """
    Assembles the Design Spec + Style Pack rules + tech stack into a binding contract
    for the coding agent.
    """
    primary_style = spec.get("chosen_primary_style", "swiss-editorial")
    layers = spec.get("layers", {})
    
    # Load specific style tokens and anti-patterns
    style_file = STYLES_DIR / f"{primary_style}.md"
    style_dir = STYLES_DIR / primary_style
    skill_md = ""
    anti_patterns = []
    
    if style_file.exists():
        with open(style_file, "r", encoding="utf-8") as f:
            content = f.read()
            if "## Mandatory Anti-Patterns" in content:
                anti_patterns_block = content.split("## Mandatory Anti-Patterns")[1].split("\n\n---\n\n")[0]
                anti_patterns = [line.strip() for line in anti_patterns_block.split("\n") if line.strip().startswith("-")]
    elif (style_dir / "SKILL.md").exists():
        with open(style_dir / "SKILL.md", "r", encoding="utf-8") as f:
            skill_md = f.read()
            # Extract anti-patterns section
            if "## Mandatory Anti-Patterns" in skill_md:
                anti_patterns_block = skill_md.split("## Mandatory Anti-Patterns")[1]
                anti_patterns = [line.strip() for line in anti_patterns_block.split("\n") if line.strip().startswith("-")]

    contract = f"""# HARD IMPLEMENTATION DESIGN CONTRACT
**Target Style:** {primary_style.upper()}
**Tech Stack:** {tech_stack}
**Execution Mode:** STRICT CONTRACT (Not a vibe. Zero tolerance for generic AI defaults.)

---

## 1. Resolved Design Spec Layers
- **Layout Source:** `{layers.get('layout')}`
- **Typography Source:** `{layers.get('typography')}`
- **Surfaces & Shadows:** `{layers.get('surfaces')}`
- **Color Palette:** `{layers.get('color')}`
- **Motion & Transitions:** `{layers.get('motion')}`
- **Component Geometry:** `{layers.get('components')}`

---

## 2. Hard Anti-Patterns (BANNED CLASSES & PATTERNS)
The coding agent MUST NOT output any of the following patterns. Doing so triggers an immediate post-implementation audit rejection:

"""
    for ap in anti_patterns:
        contract += f"{ap}\n"

    contract += f"""
---

## 3. Product Specification & Requirements
{product_spec.strip()}

---

## 4. Contract Verification Notice
Upon code generation, the post-implementation `design-audit` will statically scan all `.html`, `.jsx`, `.tsx`, and `.css` files.
Deviations in border-radius, shadow blur, font substitutions, or color values will be flagged as audit failures.
"""
    return contract
