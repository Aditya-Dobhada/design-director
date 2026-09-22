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
STYLES_DIR = Path(__file__).parent.parent / "styles"

SUPPORTED_STYLES = [
    "swiss-editorial",
    "neo-brutalism",
    "y2k-frutiger-aero",
    "quiet-luxury",
    "cyberpunk"
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
    """
    text_lower = context_text.lower()
    
    # 1. Product type & audience
    if any(k in text_lower for k in ["wealth", "portfolio", "banking", "finance", "invest", "fintech"]):
        product_type = "FinTech / Wealth Management"
        audience = "High-Net-Worth Individuals, Family Offices, and Wealth Advisory Teams"
    elif re.search(r'\b(developer|engineers|api|cli|telemetry|kubernetes|terminal|sre)\b', text_lower):
        product_type = "Developer Tool / Platform"
        audience = "Software Engineers and Technical Operators"
    elif any(k in text_lower for k in ["creator", "commerce", "art", "music", "zine"]):
        product_type = "Creator Marketplace / Community"
        audience = "Independent Creators, Artists, and Cultural Enthusiasts"
    elif any(k in text_lower for k in ["enterprise", "internal", "operations"]):
        product_type = "Enterprise Operations Platform"
        audience = "Operations Teams and Enterprise Administrators"
    else:
        product_type = "Web Application"
        audience = "General Users"

    # 2. Personality traits
    traits = []
    if any(k in text_lower for k in ["trust", "wealth", "security", "discretion"]):
        traits.extend(["authoritative", "understated", "meticulous", "discreet"])
    if re.search(r'\b(developer|terminal|fast|telemetry|sre|kubernetes)\b', text_lower):
        traits.extend(["tactical", "high-performance", "keyboard-first", "focused"])
    if re.search(r'\b(creator|zine|comic|rebellious|risograph)\b', text_lower):
        traits.extend(["unapologetic", "expressive", "tactile", "energetic"])
    if re.search(r'\b(editorial|monograph|swiss|broadsheet|minimal|disciplined)\b', text_lower):
        traits.extend(["disciplined", "objective", "content-first", "typographic"])
    if not traits:
        traits = ["intentional", "crafted", "clear", "distinctive"]

    # 3. UX requirements
    if re.search(r'\b(telemetry|data|dense|terminal|cluster)\b', text_lower):
        density = "high"
        info_load = "dense-tabular"
        workflow = "keyboard-driven-operational"
    elif re.search(r'\b(reading|wealth|luxury|monograph|ledger)\b', text_lower):
        density = "spacious"
        info_load = "curated-editorial"
        workflow = "contemplative-decision-making"
    elif re.search(r'\b(creator|shop|storefront|marketplace)\b', text_lower):
        density = "balanced"
        info_load = "visual-grid"
        workflow = "exploratory-browsing"
    else:
        density = "balanced"
        info_load = "modular"
        workflow = "guided-task-completion"

    # 4. Brand positioning axes (qualitative)
    playful_serious = "Strongly Serious" if any(k in text_lower for k in ["wealth", "security", "telemetry", "trust"]) else ("Strongly Playful" if re.search(r'\b(game|toy|zine|pop)\b', text_lower) else "Balanced")
    premium_accessible = "Ultra Premium" if any(k in text_lower for k in ["luxury", "wealth", "boutique"]) else ("Accessible / Mass Appeal" if re.search(r'\b(consumer|grassroots)\b', text_lower) else "Refined Professional")
    futuristic_institutional = "Futuristic / Avant-Garde" if re.search(r'\b(cyber|futurism|telemetry|terminal)\b', text_lower) else ("Institutional / Traditional" if any(k in text_lower for k in ["bank", "ledger", "estate", "wealth"]) else "Contemporary Modern")

    # 5. Visual constraints
    accessibility = "Strict WCAG AAA readability for critical numerical/tabular data" if "wealth" in text_lower or "telemetry" in text_lower else "Standard WCAG AA compliance"
    readability = "Critical: tabular numbers, high contrast ratios, zero ambiguous glyphs"
    motion_tolerance = "Restrained / Minimal: strictly functional transitions, zero bouncing" if ("wealth" in text_lower or "telemetry" in text_lower) else "Dynamic and fluid"

    brief = {
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
    return brief

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
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Good fit",
            "reasoning": "Rigorous asymmetric grid, razor-sharp hairlines, and high-contrast typography give financial data objective clarity and architectural prestige.",
            "tradeoffs": [
                "Stark monochrome palette can feel overly sterile or clinical if not softened with an intentional warm accent.",
                "Demands high typographic discipline in tabular layouts."
            ]
        })
        recs.append({
            "name": "Cyberpunk",
            "style_id": "cyberpunk",
            "fit_rating": "Possible",
            "reasoning": "Obsidian dark mode and neon telemetry could appeal to algorithmic crypto traders or quantitative hedge funds.",
            "tradeoffs": [
                "High visual aggression and dark-room aesthetic will alienate traditional wealth management clients seeking stability.",
                "Neon glows can fatigue eyes over long reading sessions."
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
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Good fit",
            "reasoning": "Objective typographic hierarchy, tabular data discipline, and modular asymmetric layouts turn dense technical data into an effortless, readable broadsheet.",
            "tradeoffs": [
                "Lacks the futuristic, high-octane gaming or hacker excitement of dark telemetry consoles.",
                "Strict monochrome structure requires crisp copy and icon discipline."
            ]
        })
        recs.append({
            "name": "Neo-Brutalism",
            "style_id": "neo-brutalism",
            "fit_rating": "Possible",
            "reasoning": "Solid black borders and tactile button switches give command modules a physical retro-hardware / Teenage Engineering vibe.",
            "tradeoffs": [
                "Heavy 3px borders and offset shadows consume valuable screen real estate in high-density data views."
            ]
        })
    elif "creator" in p_type or "marketplace" in p_type:
        recs.append({
            "name": "Neo-Brutalism",
            "style_id": "neo-brutalism",
            "fit_rating": "Strong fit",
            "reasoning": "Chunky solid black outlines, hard offset shadows, and saturated color pops communicate authentic grassroots energy, anti-corporate rebellion, and tactile physicality.",
            "tradeoffs": [
                "High visual volume can overwhelm subtle product imagery or art if colors compete directly.",
                "Not suitable for enterprise stakeholders who equate heavy borders with amateurism."
            ]
        })
        recs.append({
            "name": "Y2K / Frutiger Aero",
            "style_id": "y2k-frutiger-aero",
            "fit_rating": "Good fit",
            "reasoning": "Glossy glass buttons, sky-cyan gradients, and optimistic rounded capsules evoke nostalgic digital delight and consumer approachability.",
            "tradeoffs": [
                "Translucent backdrop filters and specular reflections increase CSS implementation complexity.",
                "Requires careful contrast auditing to prevent aqua text from washing out on pale backgrounds."
            ]
        })
        recs.append({
            "name": "Swiss / Editorial",
            "style_id": "swiss-editorial",
            "fit_rating": "Possible",
            "reasoning": "Elevates indie creators into museum-grade cultural curators through stark typography and broadside framing.",
            "tradeoffs": [
                "May feel overly formal, cold, or academic for a casual creator community."
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

def refine_spec(current_spec: Dict[str, Any], critique: str) -> Dict[str, Any]:
    """
    Applies free-text critique layer-by-layer using reference library mappings.
    Unrelated layers remain completely stable.
    Reports which layers changed and why.
    """
    updated_spec = json.loads(json.dumps(current_spec))
    critique_lower = critique.lower()
    changes_made = []

    # Check for references in the critique
    refs = load_reference_library()
    matched_ref = None
    for r in refs:
        if r["id"] in critique_lower or r["name"].lower() in critique_lower:
            matched_ref = r
            break

    # 1. "More like Linear" / "Like Linear"
    if "linear" in critique_lower or (matched_ref and matched_ref["id"] == "linear"):
        if "more" in critique_lower or "like" in critique_lower:
            updated_spec["layers"]["surfaces"] = "cyberpunk/tokens.md"  # Hairline dark surfaces
            updated_spec["layers"]["color"] = "obsidian-monochrome-with-violet-accent"
            updated_spec["layers"]["motion"] = "swiss-editorial/motion.md"  # Micro-snappy
            changes_made.append({
                "layer": "surfaces",
                "old": current_spec["layers"]["surfaces"],
                "new": updated_spec["layers"]["surfaces"],
                "reason": "Linear-inspired shift: hairline dark depth with subtle translucent borders."
            })
            changes_made.append({
                "layer": "color",
                "old": current_spec["layers"]["color"],
                "new": updated_spec["layers"]["color"],
                "reason": "Linear-inspired shift: deep obsidian base (#08090a) with single violet interactive accent (#5e6ad2)."
            })
            changes_made.append({
                "layer": "motion",
                "old": current_spec["layers"]["motion"],
                "new": updated_spec["layers"]["motion"],
                "reason": "Linear-inspired shift: micro-snappy 120ms transitions."
            })

    # 2. "Less like a bank" / "Not corporate"
    elif "bank" in critique_lower or "corporate" in critique_lower:
        if "less" in critique_lower or "not" in critique_lower or "too" in critique_lower:
            # Shift away from generic corporate blue/gray and generic cards
            if "quiet-luxury" in current_spec["chosen_primary_style"]:
                updated_spec["layers"]["typography"] = "quiet-luxury/typography.md" # Distinctive editorial serif
                updated_spec["layers"]["color"] = "quiet-luxury/tokens.md" # Alabaster and deep espresso
                changes_made.append({
                    "layer": "typography",
                    "old": current_spec["layers"]["typography"],
                    "new": updated_spec["layers"]["typography"],
                    "reason": "Eliminated standard corporate sans; instituted authoritative literary serif hierarchy."
                })
            else:
                updated_spec["layers"]["typography"] = "swiss-editorial/typography.md"
                updated_spec["layers"]["surfaces"] = "neo-brutalism/tokens.md"
                changes_made.append({
                    "layer": "surfaces",
                    "old": current_spec["layers"]["surfaces"],
                    "new": updated_spec["layers"]["surfaces"],
                    "reason": "Replaced timid gray-bordered corporate cards with tangible, purposeful border contrast."
                })

    # 3. "More playful" / "More tactile" / "Like Gumroad"
    elif "gumroad" in critique_lower or "playful" in critique_lower or "tactile" in critique_lower:
        updated_spec["layers"]["surfaces"] = "neo-brutalism/tokens.md"
        updated_spec["layers"]["components"] = "neo-brutalism/components.md"
        changes_made.append({
            "layer": "surfaces",
            "old": current_spec["layers"]["surfaces"],
            "new": updated_spec["layers"]["surfaces"],
            "reason": "Shifted to physical paper cards with 3px solid black outlines and 4px solid offset shadows."
        })
        changes_made.append({
            "layer": "components",
            "old": current_spec["layers"]["components"],
            "new": updated_spec["layers"]["components"],
            "reason": "Physical button switch behavior: depression translation on active click."
        })

    # 4. "Too dark" / "Make it light" / "More readable"
    elif "too dark" in critique_lower or "make it light" in critique_lower or "light mode" in critique_lower:
        updated_spec["layers"]["color"] = "swiss-editorial/tokens.md"
        changes_made.append({
            "layer": "color",
            "old": current_spec["layers"]["color"],
            "new": updated_spec["layers"]["color"],
            "reason": "Switched surface and canvas to crisp high-contrast light mode (#FFFFFF / #F8F8F6)."
        })

    # Generic layer-targeted refinement fallback
    else:
        # Check if user mentioned typography, borders, shadows, motion
        if "font" in critique_lower or "typography" in critique_lower:
            updated_spec["layers"]["typography"] = "swiss-editorial/typography.md"
            changes_made.append({
                "layer": "typography",
                "old": current_spec["layers"]["typography"],
                "new": updated_spec["layers"]["typography"],
                "reason": "Refined typographic scale to high-contrast asymmetric Swiss hierarchy."
            })
        elif "shadow" in critique_lower or "border" in critique_lower or "surface" in critique_lower:
            updated_spec["layers"]["surfaces"] = "swiss-editorial/tokens.md"
            changes_made.append({
                "layer": "surfaces",
                "old": current_spec["layers"]["surfaces"],
                "new": updated_spec["layers"]["surfaces"],
                "reason": "Cleaned surfaces to 0px border-radius and crisp hairlines."
            })

    result = {
        "updated_spec": updated_spec,
        "diff_report": {
            "critique_received": critique,
            "layers_changed_count": len(changes_made),
            "layers_preserved_count": len(updated_spec["layers"]) - len(changes_made),
            "changes": changes_made,
            "stable_layers": [k for k in updated_spec["layers"].keys() if not any(c["layer"] == k for c in changes_made)]
        }
    }
    return result

def generate_implementation_contract(spec: Dict[str, Any], product_spec: str, tech_stack: str = "Tailwind CSS + React") -> str:
    """
    Assembles the Design Spec + Style Pack rules + tech stack into a binding contract
    for the coding agent.
    """
    primary_style = spec.get("chosen_primary_style", "swiss-editorial")
    layers = spec.get("layers", {})
    
    # Load specific style tokens and anti-patterns
    style_dir = STYLES_DIR / primary_style
    skill_md = ""
    tokens_md = ""
    anti_patterns = []
    
    if (style_dir / "SKILL.md").exists():
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
