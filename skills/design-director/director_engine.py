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

import json
import re
from pathlib import Path
from typing import Any

import yaml

REFERENCE_LIBRARY_PATH = Path(__file__).parent / "reference-library.yaml"
_LOCAL_STYLES = Path(__file__).resolve().parent / "styles"
STYLES_DIR = _LOCAL_STYLES if _LOCAL_STYLES.exists() else Path(__file__).resolve().parent.parent.parent / "styles"
MODIFIERS_PATH = STYLES_DIR / "modifiers.yaml"
DOMAIN_DEFAULTS_PATH = STYLES_DIR / "domain-style-defaults.yaml"

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
    "maximalist-dopamine",
    # 8 Modern / Utility Foundations
    "minimal-modern",
    "dark-minimal",
    "terminal-cli",
    "web-brutalism",
    "art-deco",
    "mid-century-modern",
    "vaporwave",
    "high-fashion-editorial",
    # 3 Tactile Foundations (new family)
    "glassmorphism",
    "neumorphism",
    "claymorphism",
    # 4 Additional Foundations (Utility + Futuristic + Organic)
    "data-native",
    "command-center",
    "aurora-gradient",
    "digital-organic",
]

def load_modifiers() -> dict[str, Any]:
    if not MODIFIERS_PATH.exists():
        return {}
    with open(MODIFIERS_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data.get("modifiers", {})

_REFERENCE_LIBRARY_CACHE: list[dict[str, Any]] | None = None

def load_reference_library() -> list[dict[str, Any]]:
    global _REFERENCE_LIBRARY_CACHE
    if _REFERENCE_LIBRARY_CACHE is not None:
        return _REFERENCE_LIBRARY_CACHE
    if not REFERENCE_LIBRARY_PATH.exists():
        _REFERENCE_LIBRARY_CACHE = []
        return _REFERENCE_LIBRARY_CACHE
    with open(REFERENCE_LIBRARY_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        _REFERENCE_LIBRARY_CACHE = data.get("references", [])
        return _REFERENCE_LIBRARY_CACHE

def find_reference(query: str) -> dict[str, Any] | None:
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

def extract_design_brief(context_text: str) -> dict[str, Any]:
    """
    Parses product context (PRD, README, spec) into a structured Design Brief.
    Covers 11 domain buckets. Falls through to a neutral SaaS default only when
    no domain signals are found.
    """
    text_lower = context_text.lower()

    # ── 1. FinTech / Wealth ──────────────────────────────────────────────────
    if re.search(r'\b(wealth|portfolio|banking|finance|invest(?:ment|ing)?|fintech|asset|equity|funds?|endowment|trust|estate planning)\b', text_lower):
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
    elif re.search(r'\b(learning|education|student|students|teacher|teachers|course|courses|curriculum|curricula|lesson|lessons|quiz|quizzes|edtech|academy|academies|tutoring|classroom|classrooms|lms)\b', text_lower):
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
    elif re.search(r'\b(patient|patients|clinical|medical|health|healthcare|healthtech|ehr|hipaa|hospital|hospitals|physician|physicians|diagnosis|pharmacy|telehealth|wellness)\b', text_lower):
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
    elif re.search(r'\b(logistics|supply chain|warehouse|warehouses|fleet|fleets|freight|shipping|dispatch|dispatchers|inventory|fulfilment|fulfillment|depot|depots|hos violations?)\b', text_lower):
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
    elif re.search(r'\b(legal|law firms?|contracts?|compliance|regulatory|litigation|counsel|attorneys?|paralegals?|due diligence)\b', text_lower):
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
    elif re.search(r'\b(organic|nature|botanical|botanicals|climate|sustainable|sustainability|ecology|earth|biophilic|regenerative|conservation)\b', text_lower):
        product_type = "Ecological / Organic Living"
        audience = "Conscious Consumers, Environmental Stewards, and Botanical Enthusiasts"
        traits = ["grounded", "authentic", "mindful", "tactile"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 8. Architecture / Spatial Design ─────────────────────────────────────
    elif re.search(r'\b(architect|architects|architecture|architectural|interior design|furniture|mid-century|eames|building|buildings)\b', text_lower):
        product_type = "Architecture & Spatial Design"
        audience = "Architects, Designers, and Spatial Curators"
        traits = ["architectural", "geometric", "crafted", "warm"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 9. Luxury / Premium Consumer ─────────────────────────────────────────
    # Must come before Creator so "boutique" and "artisanal" don't fall into the
    # Creator bucket (which sets Accessible/Mass Appeal premium positioning).
    elif re.search(r'\b(luxury|boutique|premium|exclusive|bespoke|couture|artisanal|high-end|atelier)\b', text_lower):
        product_type = "Luxury / Premium Consumer"
        audience = "Affluent Consumers Seeking Premium Experiences"
        traits = ["refined", "understated", "exclusive", "crafted"]
        density = "spacious"
        info_load = "curated-editorial"
        workflow = "contemplative-decision-making"
        playful_serious = "Strongly Serious"
        premium_accessible = "Ultra Premium"
        futuristic_institutional = "Contemporary Modern"

    # ── 10. Creator / Commerce / Cultural ────────────────────────────────────
    elif re.search(r'\b(creator|creators|commerce|art|arts|music|zine|zines|indie|marketplace|marketplaces|storefront|storefronts|streetwear|fashion|culture|editorial)\b', text_lower):
        product_type = "Creator Marketplace / Community"
        audience = "Independent Creators, Artists, and Cultural Enthusiasts"
        traits = ["unapologetic", "expressive", "tactile", "energetic"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Accessible / Mass Appeal"
        futuristic_institutional = "Contemporary Modern"

    # ── 11. Real Estate / Property ────────────────────────────────────────────
    elif re.search(r'\b(real estate|property|properties|listing|listings|mortgage|mortgages|broker|brokers|mls|rental|rentals|cre|proptech)\b', text_lower):
        product_type = "Real Estate / Property Platform"
        audience = "Home Buyers, Property Investors, and Real Estate Agents"
        traits = ["trustworthy", "clear", "aspirational", "approachable"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Balanced"
        premium_accessible = "Refined Professional"
        futuristic_institutional = "Contemporary Modern"

    # ── 12. Events / Entertainment / Community ────────────────────────────────
    elif re.search(r'\b(event|events|concert|concerts|ticket|tickets|venue|venues|entertainment|community|social|gaming|esports|streaming)\b', text_lower):
        product_type = "Events / Entertainment Platform"
        audience = "General Consumers and Community Members"
        traits = ["energetic", "social", "vibrant", "accessible"]
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
        playful_serious = "Strongly Playful"
        premium_accessible = "Accessible / Mass Appeal"
        futuristic_institutional = "Contemporary Modern"

    # ── 13. Generic SaaS / Web Application ───────────────────────────────────
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
        "raw_context": context_text,
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

def load_domain_style_defaults() -> dict[str, Any]:
    if not DOMAIN_DEFAULTS_PATH.exists():
        return {}
    with open(DOMAIN_DEFAULTS_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data.get("domain_style_defaults", {})

STYLE_METADATA: dict[str, dict[str, Any]] = {
    "art-deco": {
        "default_reasoning": "Geometric symmetry, caviar black canvas, and burnished gold hairlines communicate formal luxury, heritage pedigree, and architectural permanence.",
        "name": "Art Deco",
        "tradeoffs": [
            "High visual ornamentation and strict symmetry may feel too ornate for purely utilitarian data tables."
        ],
    },
    "aurora-gradient": {
        "default_reasoning": "Soft atmospheric multi-color gradients over obsidian canvas create an ethereal, calm, futuristic AI environment.",
        "name": "Aurora Gradient",
        "tradeoffs": [
            "Atmospheric gradient overlays require dedicated dark canvas to maintain sufficient text legibility."
        ],
    },
    "bauhaus": {
        "default_reasoning": "Form strictly follows function: 8px constructivist grid and functional geometric typography mirror modernist architectural heritage.",
        "name": "Bauhaus",
        "tradeoffs": [
            "Primary color blocks can feel austere or unyielding for softer lifestyle contexts."
        ],
    },
    "claymorphism": {
        "default_reasoning": "Voluminous rounded clay geometry (20-32px), layered inner highlights, and friendly pastel fills communicate approachable, tactile warmth.",
        "name": "Claymorphism",
        "tradeoffs": [
            "Voluminous 20-32px rounded clay geometry and pastel fills consume high padding and reduce screen density."
        ],
    },
    "command-center": {
        "default_reasoning": "Near-black multi-panel operational grid with strict semantic status indicators (healthy/warning/critical) built for incident response.",
        "name": "Command Center",
        "tradeoffs": [
            "High information density and multi-panel ops layout can overwhelm casual or non-technical operators."
        ],
    },
    "cyberpunk": {
        "default_reasoning": "Obsidian canvas, monospace telemetry, and neon HUD brackets provide an immersive, high-voltage environment ideal for real-time monitoring streams.",
        "name": "Cyberpunk",
        "tradeoffs": [
            "High sensory intensity is unsuitable for calm documentation or administrative configuration flows."
        ],
    },
    "dark-minimal": {
        "default_reasoning": "Obsidian canvas (#09090B), hairline translucent borders, 6-8px micro-radii, and a single electric accent create a calm, focused, high-density environment ideal for modern developer tools, AI command surfaces, and telemetry.",
        "name": "Dark Minimal",
        "tradeoffs": [
            "Low-sensory dark canvas requires disciplined contrast checking in bright daylight environments.",
            "Requires strict micro-typography hierarchy to prevent dense data from blurring together."
        ],
    },
    "data-native": {
        "default_reasoning": "Ultra-dense monospace numerical hierarchy, 32px compact table rows, and disciplined status dots maximize information density for deep analytics.",
        "name": "Data-Native",
        "tradeoffs": [
            "Ultra-dense monospace numerical hierarchy leaves minimal room for expressive brand personality."
        ],
    },
    "digital-organic": {
        "default_reasoning": "Living biomorphic blob geometry, natural gradient fills, and humanist typography bridge organic living systems with modern digital precision.",
        "name": "Digital Organic",
        "tradeoffs": [
            "Asymmetric organic blob containers and earthy palettes require disciplined asset art-direction."
        ],
    },
    "glassmorphism": {
        "default_reasoning": "Translucent frosted glass panels over dark canvas with specular 1px hairlines provide OS-native depth cues.",
        "name": "Glassmorphism",
        "tradeoffs": [
            "Multi-layer backdrop blur and translucent panels can cause GPU performance overhead on lower-end devices."
        ],
    },
    "high-fashion-editorial": {
        "default_reasoning": "Monumental Bodoni display headlines, micro-grotesque metadata, razor-thin hairlines, and asymmetric runway grids bring high-drama couture sophistication.",
        "name": "High Fashion Editorial",
        "tradeoffs": [
            "Severe typographic scale contrast requires strict editorial discipline and short, punchy copy.",
            "Zero drop shadows and knife-edge corners demand immaculate layout composition."
        ],
    },
    "japanese-wabi-sabi": {
        "default_reasoning": "Handmade ceramic warmth, ink wash textures, and profound empty space reflect environmental humility and artisanal mindfulness.",
        "name": "Japanese Wabi-Sabi",
        "tradeoffs": [
            "Asymmetric unhurried layouts require disciplined content curation."
        ],
    },
    "maximalist-dopamine": {
        "default_reasoning": "Sticker-bomb badges, candy neon explosions, and chaotic typography shifts create hyper-sensory joy for youth culture, streetwear, and drops.",
        "name": "Maximalist Dopamine",
        "tradeoffs": [
            "Visual density and colliding hues can cause fatigue during prolonged administrative tasks."
        ],
    },
    "memphis-postmodern": {
        "default_reasoning": "Ettore Sottsass pattern collisions (polka dots, diagonal hatch, squiggles) celebrate creative freedom and intentional kitsch.",
        "name": "Memphis Postmodern",
        "tradeoffs": [
            "Ornamental pattern fills require careful layering to avoid competing with actual creator products."
        ],
    },
    "mid-century-modern": {
        "default_reasoning": "Warm architectural parchment, atomic pod curves (16-24px), terracotta and olive palette, and modernist geometric typography celebrate organic materials and structural clarity.",
        "name": "Mid-Century Modern",
        "tradeoffs": [
            "Warm color blocks and organic radii reduce raw tabular line density.",
            "Requires high-quality photography and intentional spatial balance."
        ],
    },
    "minimal-modern": {
        "default_reasoning": "Clean neutral zinc canvas, 6-8px micro-radii, crisp 1px borders, and disciplined typography (Geist/Inter) elevate standard SaaS workflows with modern restraint and high whitespace clarity.",
        "name": "Minimal Modern",
        "tradeoffs": [
            "Subtle aesthetic requires disciplined typographic hierarchy to avoid feeling generic if content is sparse."
        ],
    },
    "neo-brutalism": {
        "default_reasoning": "Chunky solid black outlines, hard offset shadows, and saturated color pops communicate authentic grassroots energy, anti-corporate rebellion, and tactile physicality.",
        "name": "Neo-Brutalism",
        "tradeoffs": [
            "High visual volume can overwhelm subtle product imagery or art if colors compete directly."
        ],
    },
    "neumorphism": {
        "default_reasoning": "Canvas-matched monochromatic surfaces with dual light/dark soft extruded shadows create tactile physical controls without hard borders.",
        "name": "Neumorphism",
        "tradeoffs": [
            "Low contrast between extruded surface shapes and canvas requires strict accessibility verification."
        ],
    },
    "organic-natural": {
        "default_reasoning": "Earth and botanical pigment palette (clay, moss, sap), river-stone pod containers, and living-system geometry authentically connect users to nature and regenerative craft.",
        "name": "Organic Natural",
        "tradeoffs": [
            "Organic rounded geometry consumes more padding and reduces raw data density.",
            "Requires careful contrast calibration to ensure accessible contrast on linen backgrounds."
        ],
    },
    "quiet-luxury": {
        "default_reasoning": "Understated alabaster palette, immaculate serif typography, and generous whitespace convey deep institutional trust, bespoke advisory craft, and financial gravitas without screaming.",
        "name": "Quiet Luxury",
        "tradeoffs": [
            "Generous whitespace reduces immediate above-the-fold information density.",
            "Zero border-radius and pale stone dividers require rigorous content discipline to prevent looking sparse or unstyled on smaller screens."
        ],
    },
    "retro-americana": {
        "default_reasoning": "Evokes National Parks heritage, WPA conservation posters, and rustic outdoorsmanship.",
        "name": "Retro Americana",
        "tradeoffs": [
            "Heavy ink borders and slab serifs lean nostalgic rather than contemporary biophilic."
        ],
    },
    "space-age-optimism": {
        "default_reasoning": "Warm optical white canvas, molded pod curves (24-40px), and single Mission Orange accent celebrate discovery and aerospace optimism.",
        "name": "Space Age Optimism",
        "tradeoffs": [
            "Generous 24-40px pod container radii reduce maximum tabular information density."
        ],
    },
    "swiss-editorial": {
        "default_reasoning": "Rigorous asymmetric grid, razor-sharp hairlines, and high-contrast typography give financial data objective clarity and architectural prestige.",
        "name": "Swiss / Editorial",
        "tradeoffs": [
            "Stark monochrome palette can feel overly sterile or clinical if not softened with an intentional warm accent.",
            "Demands high typographic discipline in tabular layouts."
        ],
    },
    "terminal-cli": {
        "default_reasoning": "100% monospace typography, amber/emerald phosphors on black, ASCII box-drawing borders, and zero-blur elevation deliver authentic Unix command-line utility and keyboard-first speed.",
        "name": "Terminal CLI",
        "tradeoffs": [
            "Complete absence of proportional typography or rounded corners can feel stark or intimidating to non-technical users."
        ],
    },
    "vaporwave": {
        "default_reasoning": "Pastel sunset gradients, Windows 95 dialog chrome, and classical Roman statues celebrate retro-digital net art and nostalgia.",
        "name": "Vaporwave",
        "tradeoffs": [
            "Heavy retro-digital styling is polarizing for conventional commercial storefronts."
        ],
    },
    "web-brutalism": {
        "default_reasoning": "Raw browser-default HTML, Courier typography, blue underlined links, and 0px radius strip all decorative distraction.",
        "name": "Web Brutalism",
        "tradeoffs": [
            "Raw default browser styling and unstyled controls can feel unpolished or harsh for conventional consumer apps."
        ],
    },
    "y2k-frutiger-aero": {
        "default_reasoning": "Glossy aqua-to-lime specular glassmorphism, pill containers, and vibrant optimism evoke late-90s/early-2000s consumer software.",
        "name": "Y2K / Frutiger Aero",
        "tradeoffs": [
            "High glossy complexity and skeuomorphic gradients require custom asset rendering and careful contrast calibration."
        ],
    },
}

def detect_domain_from_brief(brief: dict[str, Any]) -> str | None:
    """Matches a design brief to a domain key in domain-style-defaults.yaml."""
    p_type = brief.get("product_type", "")
    raw_ctx = (brief.get("raw_context", "") or "").lower()
    full = f"{p_type} {raw_ctx}".lower()

    product_type_to_domain = {
        "FinTech / Wealth Management": "wealth_management",
        "EdTech / Learning Platform": "edtech",
        "Healthcare / Clinical Platform": "healthcare",
        "Enterprise Operations Platform": "devops",
        "Legal / Compliance Platform": "legal",
        "Ecological / Organic Living": "digital_health",
        "Architecture & Spatial Design": "real_estate",
        "Luxury / Premium Consumer": "luxury_retail",
        "Creator Marketplace / Community": "ecommerce",
        "Real Estate / Property Platform": "real_estate",
        "Events / Entertainment Platform": "social",
    }

    if p_type in product_type_to_domain and "Developer Tool" not in p_type:
        return product_type_to_domain[p_type]

    # AI Products
    if any(k in full for k in ["llm", "ai assistant", "artificial intelligence", "gpt", "generative ai", "model interface"]) or ("ai" in full.split() and any(k in full for k in ["interface", "platform", "tool", "agent"])):
        return "ai_product"

    # DevOps vs Developer Tools
    if "Developer Tool" in p_type or "developer" in p_type.lower():
        if any(k in full for k in ["devops", "sre", "infrastructure", "observability", "incident response", "runbook", "kubernetes", "monitoring"]):
            return "devops"
        return "developer_tools"

    return None

def recommend_styles(brief: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Given a Design Brief, recommends 2-4 candidate directions.
    Consults domain-style-defaults.yaml first, then falls back to neutral SaaS defaults.
    Qualitative fit ratings only: Strong fit / Good fit / Possible / Poor fit.
    Every recommendation must include at least one honest tradeoff/risk.
    """
    domain_defaults = load_domain_style_defaults()
    domain_key = detect_domain_from_brief(brief)

    fit_ratings = {0: "Strong fit", 1: "Good fit", 2: "Possible", 3: "Possible"}

    if domain_key and domain_key in domain_defaults:
        recs = []
        for idx, item in enumerate(domain_defaults[domain_key].get("recommended_styles", [])):
            sid = item["style_id"]
            meta = STYLE_METADATA.get(sid, {})
            recs.append({
                "name": meta.get("name", sid),
                "style_id": sid,
                "id": sid,
                "fit_rating": fit_ratings.get(idx, "Good fit"),
                "reasoning": item.get("rationale") or meta.get("default_reasoning", ""),
                "tradeoffs": meta.get("tradeoffs", ["Specific operational tradeoffs require disciplined asset and layout pairing."])
            })
        return recs

    # Fallback to neutral modern SaaS defaults when domain is completely unrecognized
    fallback_ids = ["minimal-modern", "swiss-editorial", "dark-minimal"]
    recs = []
    for idx, sid in enumerate(fallback_ids):
        meta = STYLE_METADATA.get(sid, {})
        recs.append({
            "name": meta.get("name", sid),
            "style_id": sid,
            "id": sid,
            "fit_rating": fit_ratings.get(idx, "Good fit"),
            "reasoning": meta.get("default_reasoning", ""),
            "tradeoffs": meta.get("tradeoffs", ["Requires disciplined typographic hierarchy and layout pairing."])
        })
    return recs

def create_design_spec(style_id: str, custom_layers: dict[str, str] | None = None) -> dict[str, Any]:
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
        },
        "minimal-modern": {
            "layout": "minimal-modern/layout.md",
            "typography": "minimal-modern/typography.md",
            "surfaces": "minimal-modern/tokens.md",
            "color": "minimal-modern/tokens.md",
            "motion": "minimal-modern/motion.md",
            "imagery": "clean-product-ui-screenshots",
            "components": "minimal-modern/components.md"
        },
        "dark-minimal": {
            "layout": "dark-minimal/layout.md",
            "typography": "dark-minimal/typography.md",
            "surfaces": "dark-minimal/tokens.md",
            "color": "dark-minimal/tokens.md",
            "motion": "dark-minimal/motion.md",
            "imagery": "monochrome-isometric-schematics",
            "components": "dark-minimal/components.md"
        },
        "terminal-cli": {
            "layout": "terminal-cli/layout.md",
            "typography": "terminal-cli/typography.md",
            "surfaces": "terminal-cli/tokens.md",
            "color": "terminal-cli/tokens.md",
            "motion": "terminal-cli/motion.md",
            "imagery": "ascii-diagrams-and-telemetry",
            "components": "terminal-cli/components.md"
        },
        "web-brutalism": {
            "layout": "web-brutalism/layout.md",
            "typography": "web-brutalism/typography.md",
            "surfaces": "web-brutalism/tokens.md",
            "color": "web-brutalism/tokens.md",
            "motion": "web-brutalism/motion.md",
            "imagery": "raw-html-tables-and-document-charts",
            "components": "web-brutalism/components.md"
        },
        "art-deco": {
            "layout": "art-deco/layout.md",
            "typography": "art-deco/typography.md",
            "surfaces": "art-deco/tokens.md",
            "color": "art-deco/tokens.md",
            "motion": "art-deco/motion.md",
            "imagery": "stepped-geometric-and-gold-foil",
            "components": "art-deco/components.md"
        },
        "mid-century-modern": {
            "layout": "mid-century-modern/layout.md",
            "typography": "mid-century-modern/typography.md",
            "surfaces": "mid-century-modern/tokens.md",
            "color": "mid-century-modern/tokens.md",
            "motion": "mid-century-modern/motion.md",
            "imagery": "architectural-photography-and-fiberglass-pods",
            "components": "mid-century-modern/components.md"
        },
        "vaporwave": {
            "layout": "vaporwave/layout.md",
            "typography": "vaporwave/typography.md",
            "surfaces": "vaporwave/tokens.md",
            "color": "vaporwave/tokens.md",
            "motion": "vaporwave/motion.md",
            "imagery": "classical-marble-and-pastel-synth-grid",
            "components": "vaporwave/components.md"
        },
        "high-fashion-editorial": {
            "layout": "high-fashion-editorial/layout.md",
            "typography": "high-fashion-editorial/typography.md",
            "surfaces": "high-fashion-editorial/tokens.md",
            "color": "high-fashion-editorial/tokens.md",
            "motion": "high-fashion-editorial/motion.md",
            "imagery": "monumental-couture-photography",
            "components": "high-fashion-editorial/components.md"
        },
        # ── Tactile Family ────────────────────────────────────────────────────
        "glassmorphism": {
            "layout": "glassmorphism/layout.md",
            "typography": "glassmorphism/typography.md",
            "surfaces": "glassmorphism/tokens.md",
            "color": "glassmorphism/tokens.md",
            "motion": "glassmorphism/motion.md",
            "imagery": "translucent-layered-depth-renders",
            "components": "glassmorphism/components.md"
        },
        "neumorphism": {
            "layout": "neumorphism/layout.md",
            "typography": "neumorphism/typography.md",
            "surfaces": "neumorphism/tokens.md",
            "color": "neumorphism/tokens.md",
            "motion": "neumorphism/motion.md",
            "imagery": "monochromatic-soft-extrusion-renders",
            "components": "neumorphism/components.md"
        },
        "claymorphism": {
            "layout": "claymorphism/layout.md",
            "typography": "claymorphism/typography.md",
            "surfaces": "claymorphism/tokens.md",
            "color": "claymorphism/tokens.md",
            "motion": "claymorphism/motion.md",
            "imagery": "pastel-3d-clay-render-stickers",
            "components": "claymorphism/components.md"
        },
        # ── Utility Family additions ──────────────────────────────────────────
        "data-native": {
            "layout": "data-native/layout.md",
            "typography": "data-native/typography.md",
            "surfaces": "data-native/tokens.md",
            "color": "data-native/tokens.md",
            "motion": "data-native/motion.md",
            "imagery": "monospace-ascii-telemetry-charts",
            "components": "data-native/components.md"
        },
        "command-center": {
            "layout": "command-center/layout.md",
            "typography": "command-center/typography.md",
            "surfaces": "command-center/tokens.md",
            "color": "command-center/tokens.md",
            "motion": "command-center/motion.md",
            "imagery": "status-panel-network-topology",
            "components": "command-center/components.md"
        },
        # ── Futuristic Family additions ───────────────────────────────────────
        "aurora-gradient": {
            "layout": "aurora-gradient/layout.md",
            "typography": "aurora-gradient/typography.md",
            "surfaces": "aurora-gradient/tokens.md",
            "color": "aurora-gradient/tokens.md",
            "motion": "aurora-gradient/motion.md",
            "imagery": "atmospheric-gradient-abstract",
            "components": "aurora-gradient/components.md"
        },
        # ── Organic Family additions ──────────────────────────────────────────
        "digital-organic": {
            "layout": "digital-organic/layout.md",
            "typography": "digital-organic/typography.md",
            "surfaces": "digital-organic/tokens.md",
            "color": "digital-organic/tokens.md",
            "motion": "digital-organic/motion.md",
            "imagery": "organic-blob-biomorphic-illustration",
            "components": "digital-organic/components.md"
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

def _resolve_layers_from_reference(ref: dict[str, Any], direction: str) -> dict[str, str]:
    """
    Translates a reference library entry into concrete spec layer overrides.
    direction is either 'more_like' or 'less_like'.
    Reads the reference's mode, borders, motion, typography, and color fields
    to produce actionable file-path overrides.
    """
    overrides: dict[str, str] = {}
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

    # ── Foundation seeding ───────────────────────────────────────────────────
    prim = ref.get("primary_foundation")
    if direction == "more_like" and prim:
        overrides["color"] = f"{prim}/tokens.md"
        overrides["surfaces"] = f"{prim}/tokens.md"
        overrides["motion"] = f"{prim}/motion.md"
        return overrides

    # ── Mode / canvas ────────────────────────────────────────────────────────
    if direction == "more_like":
        if "dark" in mode or "obsidian" in palette_type:
            overrides["color"] = "dark-minimal/tokens.md"
            overrides["surfaces"] = "dark-minimal/tokens.md"
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
            overrides["color"] = "minimal-modern/tokens.md"
            overrides["surfaces"] = "minimal-modern/tokens.md"
        if "saturated" in palette_type or "neon" in palette_type:
            overrides["color"] = "quiet-luxury/tokens.md"
            overrides["surfaces"] = "quiet-luxury/tokens.md"

    # ── Borders / surfaces (override color above if borders are more specific) ──
    if direction == "more_like":
        if "heavy" in borders or "thick" in borders or "3px" in borders or "4px" in borders:
            overrides["surfaces"] = "neo-brutalism/tokens.md"
        elif "hairline" in borders or "0.5px" in borders or "subtle" in borders:
            overrides["surfaces"] = "dark-minimal/tokens.md" if "dark" in mode else "swiss-editorial/tokens.md"
        elif "none" in borders or "zero" in borders or "flat" in borders:
            overrides["surfaces"] = "swiss-editorial/tokens.md"
        if "hard" in shadows and "offset" in shadows:
            overrides["surfaces"] = "neo-brutalism/tokens.md"

        typography = ref.get("typography", {})
        heading = typography.get("heading_font", "").lower()
        if any(k in heading for k in ["garamond", "serif", "canela", "fraunces", "suisse works"]):
            overrides["typography"] = "quiet-luxury/typography.md"
        elif any(k in heading for k in ["slab", "condensed", "rockwell", "alfa"]):
            overrides["typography"] = "retro-americana/typography.md"
        elif any(k in heading for k in ["mono", "consolas", "courier", "fixed"]):
            overrides["typography"] = "terminal-cli/typography.md"

        if motion_ms <= 120 or any(k in motion_char for k in ["snappy", "instant", "immediate", "fast"]):
            overrides["motion"] = "swiss-editorial/motion.md"
        elif motion_ms >= 400 or any(k in motion_char for k in ["slow", "contemplative", "cinematic"]):
            overrides["motion"] = "quiet-luxury/motion.md"

    return overrides


def refine_spec(current_spec: dict[str, Any], critique: str) -> dict[str, Any]:
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
    elif "digital" not in critique_lower and any(k in critique_lower for k in ["organic", "natural", "biophilic", "earthy"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "organic-natural/tokens.md",
            "color": "organic-natural/tokens.md",
            "typography": "organic-natural/typography.md",
        }, reasons={
            "surfaces": "Organic shift: river-stone rounding and bone-white canvas.",
            "color": "Natural earth palette: raw clay, moss green, and bone white.",
            "typography": "Humanist oldstyle serif hierarchy with warm reading proportions.",
        })

    elif any(k in critique_lower for k in ["minimal modern", "clean modern", "notion"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "minimal-modern/tokens.md",
            "color": "minimal-modern/tokens.md",
            "typography": "minimal-modern/typography.md",
            "motion": "minimal-modern/motion.md",
        }, reasons={
            "surfaces": "Minimal Modern shift: 6-8px micro-radii and crisp 1px neutral borders.",
            "color": "Pristine neutral zinc canvas (#FAFAFA / #FFFFFF) with single functional accent.",
            "typography": "Geist/Inter clean grotesque typographic hierarchy with tight tracking.",
            "motion": "Micro-snappy 120ms transitions.",
        })
    elif any(k in critique_lower for k in ["dark minimal", "raycast", "linear"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "dark-minimal/tokens.md",
            "color": "dark-minimal/tokens.md",
            "typography": "dark-minimal/typography.md",
            "motion": "dark-minimal/motion.md",
        }, reasons={
            "surfaces": "Dark Minimal shift: obsidian canvas, translucent 1px hairlines, and 6-8px micro-radii.",
            "color": "Obsidian deep charcoal (#09090B) with single electric violet/indigo accent.",
            "typography": "Geist Mono metadata readouts and clean sans labels.",
            "motion": "Micro-snappy 120ms transitions.",
        })
    elif any(k in critique_lower for k in ["terminal", "tui", "cli", "ascii"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "terminal-cli/tokens.md",
            "color": "terminal-cli/tokens.md",
            "typography": "terminal-cli/typography.md",
            "motion": "terminal-cli/motion.md",
        }, reasons={
            "surfaces": "Terminal CLI shift: 0px radius, pitch black canvas, and ASCII box-drawing borders.",
            "color": "Phosphor monochrome: amber/emerald on black canvas.",
            "typography": "100% Monospace typography (JetBrains Mono/IBM Plex Mono).",
            "motion": "Inert 0ms instant feedback.",
        })
    elif any(k in critique_lower for k in ["web brutalism", "raw web", "raw html"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "web-brutalism/tokens.md",
            "color": "web-brutalism/tokens.md",
            "typography": "web-brutalism/typography.md",
            "components": "web-brutalism/components.md",
        }, reasons={
            "surfaces": "Web Brutalism shift: raw document HTML, 0px radius, and standard table borders.",
            "color": "Stark black/white contrast with default browser blue links (#0000EE).",
            "typography": "Courier monospace and default browser typography with underlined links.",
            "components": "Unstyled default browser controls.",
        })
    elif any(k in critique_lower for k in ["art deco", "gatsby"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "art-deco/tokens.md",
            "color": "art-deco/tokens.md",
            "typography": "art-deco/typography.md",
        }, reasons={
            "surfaces": "Art Deco shift: stepped geometric symmetry, dual gold hairlines, and 0px radius.",
            "color": "Caviar black (#0E0E10) and burnished gold (#D4AF37) luxury metallics.",
            "typography": "Dramatic Bodoni/Cinzel geometric serifs with wide tracking.",
        })
    elif any(k in critique_lower for k in ["mid century", "eames", "palm springs"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "mid-century-modern/tokens.md",
            "color": "mid-century-modern/tokens.md",
            "typography": "mid-century-modern/typography.md",
        }, reasons={
            "surfaces": "Mid-Century Modern shift: warm architectural parchment and 16-24px atomic pod curves.",
            "color": "California modernist palette: terracotta, olive moss, mustard, and walnut.",
            "typography": "Josefin Sans / Futura geometric modernist typography.",
        })
    elif any(k in critique_lower for k in ["vaporwave", "vapor"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "vaporwave/tokens.md",
            "color": "vaporwave/tokens.md",
            "typography": "vaporwave/typography.md",
        }, reasons={
            "surfaces": "Vaporwave shift: Windows 95 dialog bevels and pastel cyan/pink drop shadows.",
            "color": "Twilight lavender horizon with pastel pink (#FF71CE) and cyan (#01CDFE) glows.",
            "typography": "Playfair Display serifs colliding with VT323 pixel typography.",
        })
    elif any(k in critique_lower for k in ["high fashion", "runway", "couture", "vogue"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "high-fashion-editorial/tokens.md",
            "color": "high-fashion-editorial/tokens.md",
            "typography": "high-fashion-editorial/typography.md",
        }, reasons={
            "surfaces": "High Fashion Editorial shift: knife-edge 0px radius, razor hairlines, and zero drop shadows.",
            "color": "Stark high-contrast monochrome (#0A0A0A / #FFFFFF).",
            "typography": "Monumental Bodoni display headlines colliding with micro-grotesque metadata.",
        })
    elif any(k in critique_lower for k in ["glassmorphism", "frosted panel", "glass panel", "backdrop blur"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "glassmorphism/tokens.md",
            "color": "glassmorphism/tokens.md",
            "motion": "glassmorphism/motion.md",
        }, reasons={
            "surfaces": "Glassmorphism shift: rgba translucent panels with backdrop-filter blur and 1px specular hairlines.",
            "color": "Dark obsidian base with electric violet or cyan glass accent layering.",
            "motion": "Smooth 200ms fluid spring for panel entrance and layering transitions.",
        })
    elif any(k in critique_lower for k in ["neumorphism", "neumorphic", "soft extrude", "extruded"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "neumorphism/tokens.md",
            "color": "neumorphism/tokens.md",
        }, reasons={
            "surfaces": "Neumorphism shift: dual soft shadow extrusion (light/dark), no borders, canvas-matched surface color.",
            "color": "Monochromatic mid-tone canvas with matched UI elements and subdued desaturated accent.",
        })
    elif any(k in critique_lower for k in ["claymorphism", "clay", "pastel 3d", "chunky rounded"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "claymorphism/tokens.md",
            "color": "claymorphism/tokens.md",
            "typography": "claymorphism/typography.md",
        }, reasons={
            "surfaces": "Claymorphism shift: heavy rounding (20–32px), layered clay inner shadow, pastel element fills.",
            "color": "Warm cream canvas with soft pastel element colors (coral, sky, mint, lemon).",
            "typography": "Rounded humanist sans (Nunito/Poppins) to reinforce the tactile clay feel.",
        })
    elif any(k in critique_lower for k in ["cyberpunk", "neon hud", "hud", "cyber", "sci-fi", "scifi", "high-voltage"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "cyberpunk/tokens.md",
            "color": "cyberpunk/tokens.md",
            "typography": "cyberpunk/typography.md",
            "motion": "cyberpunk/motion.md",
        }, reasons={
            "surfaces": "Cyberpunk shift: obsidian canvas, chamfer corner clips, and neon HUD brackets.",
            "color": "High-voltage neon palette: electric cyan (#00F5FF), neon magenta, and obsidian canvas.",
            "typography": "Rajdhani angular geometric display headers colliding with monospace telemetry.",
            "motion": "Fast 100ms snappy tactical transitions with glitch hover effects.",
        })
    elif any(k in critique_lower for k in ["data native", "data-native", "dense data", "tabular analytics", "analytics", "dense tabular", "data dashboard", "tabular analytics dashboard"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "data-native/tokens.md",
            "color": "data-native/tokens.md",
            "typography": "data-native/typography.md",
        }, reasons={
            "surfaces": "Data-Native shift: hairline 1px dividers, zero decorative fills, ultra-compact 32px rows.",
            "color": "Dark #0D1117 canvas with single blue/green accent for positive delta values only.",
            "typography": "JetBrains Mono for all numerics; 11–12px Inter labels.",
        })
    elif any(k in critique_lower for k in ["y2k", "frutiger aero", "frutiger-aero", "glossy aero", "aqua gloss"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "y2k-frutiger-aero/tokens.md",
            "color": "y2k-frutiger-aero/tokens.md",
            "typography": "y2k-frutiger-aero/typography.md",
            "motion": "y2k-frutiger-aero/motion.md",
        }, reasons={
            "surfaces": "Frutiger Aero shift: glossy specular glassmorphism, pill containers, and aqua gradients.",
            "color": "Sky gradient canvas with aqua and lime specular highlights.",
            "typography": "Rounded humanist sans typography (Nunito).",
            "motion": "Springy 350ms bounce transitions.",
        })
    elif any(k in critique_lower for k in ["neo brutalism", "neo-brutalism", "chunky border", "offset shadow"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "neo-brutalism/tokens.md",
            "color": "neo-brutalism/tokens.md",
            "components": "neo-brutalism/components.md",
        }, reasons={
            "surfaces": "Neo-Brutalism shift: chunky 3px black borders and 4px solid black offset shadows.",
            "color": "High-saturation poster color accents on stark white/cream canvas.",
            "components": "Physical button switch behavior with active click depression.",
        })
    elif any(k in critique_lower for k in ["quiet luxury", "quiet-luxury", "old money", "alabaster"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "quiet-luxury/tokens.md",
            "color": "quiet-luxury/tokens.md",
            "typography": "quiet-luxury/typography.md",
        }, reasons={
            "surfaces": "Quiet Luxury shift: alabaster canvas, razor stone dividers, and zero border radius.",
            "color": "Understated alabaster, warm ecru, and deep charcoal/espresso.",
            "typography": "Authoritative Cormorant Garamond editorial serif hierarchy.",
        })
    elif any(k in critique_lower for k in ["swiss editorial", "swiss-editorial", "international typographic"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "swiss-editorial/tokens.md",
            "color": "swiss-editorial/tokens.md",
            "typography": "swiss-editorial/typography.md",
            "layout": "swiss-editorial/layout.md",
        }, reasons={
            "surfaces": "Swiss Editorial shift: 0px radius, razor hairlines, and strict asymmetric grid.",
            "color": "Stark monochrome canvas with single Swiss Red (#E30613) accent.",
            "typography": "High-contrast Playfair / Grotesque asymmetric hierarchy.",
            "layout": "Modular asymmetric grid broadsheet layout.",
        })
    elif any(k in critique_lower for k in ["command center", "command-center", "multi panel", "ops panel", "devops"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "command-center/tokens.md",
            "color": "command-center/tokens.md",
            "layout": "command-center/layout.md",
        }, reasons={
            "surfaces": "Command Center shift: near-black panels, 1px structural borders, semantic status indicators.",
            "color": "Near-black #0B0D11 with red/amber/green semantic status palette.",
            "layout": "Multi-panel 3–4 column grid with dedicated functional zones.",
        })
    elif any(k in critique_lower for k in ["aurora", "aurora gradient", "ai gradient", "atmospheric gradient"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "aurora-gradient/tokens.md",
            "color": "aurora-gradient/tokens.md",
            "motion": "aurora-gradient/motion.md",
        }, reasons={
            "surfaces": "Aurora Gradient shift: dark #0B0F1A base with soft radial aurora glow overlays.",
            "color": "Atmospheric violet/pink/cyan gradient palette at restrained opacity; no hard neon.",
            "motion": "Fluid 300ms spring for gradient panel reveals and aurora shimmer effects.",
        })
    elif any(k in critique_lower for k in ["digital organic", "digital-organic", "biomorphic", "blob", "organic tech"]):
        _apply_layers(updated_spec, current_spec, changes_made, {
            "surfaces": "digital-organic/tokens.md",
            "color": "digital-organic/tokens.md",
            "typography": "digital-organic/typography.md",
        }, reasons={
            "surfaces": "Digital Organic shift: CSS blob shapes with asymmetric border-radius and natural gradient fills.",
            "color": "Warm earthy palette (sage, moss, sand, gold) combined with thin monospace data typography.",
            "typography": "Bricolage Grotesque/DM Sans for UI, thin monospace for metrics.",
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
    updated_spec: dict[str, Any],
    current_spec: dict[str, Any],
    changes_made: list[dict[str, Any]],
    layer_map: dict[str, str],
    reasons: dict[str, str]
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

def generate_implementation_contract(
    spec: dict[str, Any],
    product_spec: str,
    tech_stack: str = "Tailwind CSS + React",
    modifiers: list[str] | None = None
) -> str:
    """
    Assembles the Design Spec + Style Pack rules + active modifiers + tech stack
    into a binding contract for the coding agent.
    """
    primary_style = spec.get("chosen_primary_style", "swiss-editorial")
    layers = spec.get("layers", {})
    
    # Load specific style tokens and anti-patterns
    style_file = STYLES_DIR / f"{primary_style}.md"
    style_dir = STYLES_DIR / primary_style
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
            if "## Mandatory Anti-Patterns" in skill_md:
                anti_patterns_block = skill_md.split("## Mandatory Anti-Patterns")[1]
                anti_patterns = [line.strip() for line in anti_patterns_block.split("\n") if line.strip().startswith("-")]

    # Load modifier specs if specified
    active_modifier_blocks = []
    if modifiers:
        all_mods = load_modifiers()
        for mod_id in modifiers:
            # Search across modifier categories
            for cat, mod_list in all_mods.items():
                for m in mod_list:
                    if m.get("id") == mod_id:
                        m_desc = m.get("description", "")
                        m_whitelist = m.get("audit_whitelist", {})
                        active_modifier_blocks.append((mod_id, m.get("name", mod_id), cat, m_desc, m_whitelist))

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
"""

    if active_modifier_blocks:
        contract += "\n---\n\n## 2. Active Orthogonal Modifiers\n"
        for m_id, m_name, m_cat, m_desc, m_wl in active_modifier_blocks:
            contract += f"- **[{m_cat.upper()}] {m_name} (`{m_id}`):** {m_desc}\n"
            if "tailwind_classes" in m_wl:
                contract += f"  - Whitelisted Utilities: `{'`, `'.join(m_wl['tailwind_classes'])}`\n"
            if "css_properties" in m_wl:
                contract += f"  - Whitelisted CSS: `{'`, `'.join(m_wl['css_properties'])}`\n"

    section_num = 3 if active_modifier_blocks else 2
    contract += f"""
---

## {section_num}. Hard Anti-Patterns (BANNED CLASSES & PATTERNS)
The coding agent MUST NOT output any of the following patterns. Doing so triggers an immediate post-implementation audit rejection:

"""
    for ap in anti_patterns:
        contract += f"{ap}\n"

    section_num += 1
    contract += f"""
---

## {section_num}. Product Specification & Requirements
{product_spec.strip()}

---

## {section_num + 1}. Contract Verification Notice
Upon code generation, the post-implementation `design-audit` will statically scan all `.html`, `.jsx`, `.tsx`, and `.css` files.
Deviations in border-radius, shadow blur, font substitutions, or color values will be flagged as audit failures.
"""
    return contract
