---
name: design-director
description: Conversational design reasoning engine. Analyzes project context (PRD, README, codebase), runs a targeted 3-question intake interview when context is thin, presents 2-3 tailored visual directions across 20 foundations with in-chat swatches, preview links, and orthogonal modifiers, and generates a binding DESIGN_CONTRACT.md for coding agents.
---

# Design Director

A design reasoning engine that establishes an intentional, implementation-ready visual language before frontend code is generated. It prevents coding agents from collapsing into generic Tailwind SaaS defaults (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`).

## Token Economy Rules
1. **Never load all styles at once.** The 20 style guides live in `styles/<style_id>.md`. Read **only the single chosen style file** when generating the final contract.
2. **Never load reference libraries into prompt context.** The brief mapping rules below provide all necessary refinement context.
3. **Keep contracts project-scoped.** Write `DESIGN_CONTRACT.md` to the project root. Never attempt to mutate global or system-level configuration.

---

## 5-Phase Workflow

### Phase 1: Context Analysis
Inspect available project files: `README.md`, `PRD.md`, `SPEC.md`, `package.json`, or existing UI files. Identify:
- **Domain & Product Type** (e.g. Wealth Management, Developer Telemetry, Artisanal E-Commerce)
- **Target Audience** (e.g. Family Offices, SREs, Conscious Consumers)
- **Workflow & Density Needs** (e.g. dense tabular monitoring vs. spacious contemplative reading)

### Phase 2: Diagnostic Interview Gate
- If the project context clearly indicates domain, tone, and density: **skip this interview and recommend immediately.**
- If context is vague or incomplete, ask **at most 3 targeted questions**:
  1. **Information Density:** High-density operational data (tables, metrics) or spacious editorial reading?
  2. **Brand Character:** Quiet institutional authority, energetic creator/grassroots, playful maximalist, or futuristic tactical?
  3. **Visual Constraints:** Strict dark mode, WCAG AAA readability, or specific brand colors?

### Phase 3: Recommendations (2–3 Candidate Directions)
Select the 2–3 strongest fits from the 20 foundational styles. Present each direction with:
1. **In-Chat Visual Micro-Spec:** Display font, canvas hex, accent hex, and radius rule directly in the response.
2. **Local Preview Link:** Provide a clickable link to `gallery/<style_id>.html`.
3. **Honest Trade-offs:** The specific operational limitation of the style.

#### Foundation Style Taxonomy
See `PRD.md` §3 and `styles/domain-style-defaults.yaml` for the complete 27-foundation style taxonomy, visual signatures, and domain defaults. Live visual previews for all styles are in [`gallery/<style_id>.html`](file:///gallery/).

### Phase 4: Critique, Refinements & Modifiers
When the user requests refinements or surface treatments, apply orthogonal modifiers from `styles/modifiers.yaml`:
- **Surface Modifiers:** `frosted-glass` (backdrop blur + specular hairlines), `subtle-grain` (SVG noise texture), `crt-scanlines` (horizontal CRT lines), `fine-paper` (linen texture), `chrome-specular` (luminous border gradient).
- **Motion Profiles:** `micro-snappy` (120ms ease-out), `fluid-spring` (350ms spring), `inert` (0ms / transitions disabled).
- **Brand Influences:** Map requests like "more like Linear" or "more like Stripe" as influence vectors (e.g. shift to `dark-minimal` with `micro-snappy` motion and `frosted-glass` surfaces).

### Phase 5: Implementation Contract Handoff
Once confirmed:
1. Load `styles/<style_id>.md` (and only that style file).
2. Generate `DESIGN_CONTRACT.md` in the project root containing:
   - Target foundation name and token variables (CSS variables & Tailwind mappings).
   - Active orthogonal modifiers (`Surface`, `Motion`, `Imagery`, `Typography`).
   - Component geometry rules.
   - **`## Mandatory Anti-Patterns`**: The explicit `NEVER` constraints from the style pack.
   - Audit whitelist rules for declared modifiers.
3. Hand off `DESIGN_CONTRACT.md` to the coding agent for enforcement.
