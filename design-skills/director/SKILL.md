---
name: design-director
description: Design reasoning engine that turns product context (PRD, README, spec, existing code) into implementation-ready visual direction for AI coding agents. Analyzes context into structured Design Briefs, recommends styles with qualitative fit ratings and honest tradeoffs, resolves composable layered Design Specs, supports layer-scoped iterative refinement, and packages binding implementation contracts.
---

# Design Director

A design reasoning engine that transforms product context into implementation-ready visual direction for AI coding agents. It prevents coding agents from collapsing design and code into generic Tailwind SaaS defaults by establishing a formal design contract before code is written.

## Core Invocations

The skill supports the following command workflows:

1. `/design analyze` — Reads product context and outputs a structured **Design Brief** YAML.
2. `/design recommend` — Produces 2–4 distinct visual directions with qualitative fit ratings and honest tradeoffs.
3. `/design choose <style>` — Resolves the chosen style into a layered **Design Spec** (single source of truth per layer; no percentage blending).
4. `/design refine "<critique>"` — Refines the Design Spec layer-by-layer based on user feedback using `reference-library.yaml`.
5. `/design implement` — Packages the Design Spec, Style Pack tokens, and constraints into a binding `DESIGN_CONTRACT.md` for the coding agent.
6. `/design audit` — Dispatches to `design-audit` to inspect implemented frontend code against the spec.

---

## 1. Analysis Workflow (`/design analyze`)

Read the available product inputs: `PRD.md`, `SPEC.md`, `README.md`, existing frontend code, target audience, brand requirements, and competitor references.

Extract and output a **Design Brief** in structured YAML:

```yaml
product_type: "FinTech / Wealth Management"
target_audience: "High-Net-Worth Individuals, Family Offices, and Advisory Teams"
personality_traits:
  - authoritative
  - understated
  - meticulous
  - discreet
ux_requirements:
  density: spacious
  information_load: curated-editorial
  workflow_orientation: contemplative-decision-making
brand_positioning_axes:
  playful_vs_serious: "Strongly Serious"
  premium_vs_accessible: "Ultra Premium"
  futuristic_vs_institutional: "Contemporary Modern"
visual_constraints:
  accessibility_needs: "Strict WCAG AAA readability for critical financial data"
  readability_criticality: "Critical: tabular numerals, high contrast ratios"
  motion_tolerance: "Restrained / Minimal: strictly functional transitions, zero bouncing"
```

**Rule:** Ensure the brief captures the true domain reality, not generic marketing buzzwords.

---

## 2. Style Recommendation (`/design recommend`)

Evaluate the Design Brief against the candidate style families:
- **Swiss / Editorial** (`swiss-editorial`)
- **Neo-Brutalism** (`neo-brutalism`)
- **Quiet Luxury** (`quiet-luxury`)
- **Y2K / Frutiger Aero** (`y2k-frutiger-aero`)
- **Cyberpunk** (`cyberpunk`)

Produce **2 to 4 candidate directions**. For each direction, output:
1. **Name & Style ID**
2. **Qualitative Fit Rating:** STRICTLY one of `Strong fit`, `Good fit`, `Possible`, or `Poor fit`.
   *(NEVER output percentages, numeric scores, or decimal weights!)*
3. **Reasoning for Fit:** Specific domain and architectural justification.
4. **Honest Tradeoffs & Risks:** At least one genuine risk or limitation (e.g., whitespace cost, daylight readability, sensory volume).

---

## 3. Layered Design Spec (`/design choose <style>`)

When a user selects a direction (e.g. `/design choose quiet-luxury`), generate the fully-resolved **Design Spec**.

Decompose the direction into independent, composable layers:
```yaml
design_spec:
  chosen_primary_style: quiet-luxury
  layers:
    layout: quiet-luxury/layout.md
    typography: quiet-luxury/typography.md
    surfaces: quiet-luxury/tokens.md
    color: quiet-luxury/tokens.md
    motion: quiet-luxury/motion.md
    imagery: architectural-still-life-monochrome
    components: quiet-luxury/components.md
  constraints:
    no_percentage_blends: true
    single_source_of_truth_per_layer: true
```

**Rule:** Every layer MUST resolve to exactly one concrete file or specification source. Do not leave any layer as a vague 50/50 blend.

---

## 4. Iterative Refinement (`/design refine "<critique>"`)

When the user provides free-text critique (e.g., `"Make it feel more like Linear, less like a bank"`, `"Too corporate"`, `"More playful"`):

1. **Consult `reference-library.yaml`:** Find matching products or traits (e.g., Linear, Traditional Bank, Gumroad, Stripe).
2. **Apply Layer-Scoped Diffs:** Update **only** the relevant layers. Unrelated layers remain completely stable.
3. **Report the Diff:** Clearly state which layers were altered, why they were altered, and confirm that untouched layers remained stable.

Example Output:
```markdown
### Design Spec Refinement Report
Critique: "More like Linear, less like a traditional bank"

Layers Updated:
- **surfaces**: Shifted to `cyberpunk/tokens.md` (dark hairline depth, 0.5px subtle border strokes).
- **color**: Shifted to obsidian base (`#08090A`) with single violet interactive accent (`#5E6AD2`).
- **motion**: Shifted to `swiss-editorial/motion.md` (micro-snappy 120ms transitions).

Stable Layers (Preserved):
- **layout**: swiss-editorial/layout.md (Unchanged)
- **typography**: swiss-editorial/typography.md (Unchanged)
- **imagery**: wireframe-schematics (Unchanged)
```

---

## 5. Implementation Handoff (`/design implement`)

Package the Design Spec, Style Pack tokens, concrete component values, and explicit **negative constraints** (anti-patterns) into a binding `DESIGN_CONTRACT.md` file for the frontend coding agent.

The frontend coding agent must follow this contract as hard constraints, not subjective inspiration.
