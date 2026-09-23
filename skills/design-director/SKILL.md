---
name: design-director
description: Conversational design reasoning engine. Analyzes project context (PRD, README, codebase), runs a targeted 3-question intake interview when context is thin, presents 2-3 tailored visual directions across 27 foundations with in-chat swatches, preview links, and orthogonal modifiers, and generates a binding DESIGN_CONTRACT.md for coding agents.
---

# Design Director

A design reasoning engine that establishes an intentional, implementation-ready visual language before frontend code is generated. It prevents coding agents from collapsing into generic Tailwind SaaS defaults (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`).

## Token Economy Rules
1. **Never load all styles at once.** The 27 style guides live in `styles/<style_id>.md` inside this skill folder. Read **only the single chosen style file** when generating the final contract.
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
Select the 2–3 strongest fits from the 27 foundational styles. For each candidate direction, present:

1. **In-Chat Visual Micro-Spec (Inline in Message):**
   Generate a compact inline visual strip directly in the chat response (do NOT create files or full HTML mockups for candidates — keep it cheap and lightweight):
   - **Inline Visual Strip:** An inline `<svg width="100%" height="36" viewBox="0 0 380 36" fill="none" xmlns="http://www.w3.org/2000/svg">` containing:
     - 4 palette swatch rectangles (`width="28" height="28"`) for Canvas, Surface, Primary Accent, and Secondary Accent.
     - 1 outlined radius-sample shape (`width="28" height="28"`, matching the style's exact border radius rule: `rx="0"` for sharp, `rx="6"` for restrained, `rx="16"` for organic/pod).
     - Display font specimen text (`<text font-family="..." font-size="13">`).
   - **Swatch & Token Summary:**
     `[⬛ #canvas] [⬛ #surface] [🟨 #accent1] [🟨 #accent2] | Radius: <rule> | Font: **<Display Font>**`
     - Display Font & Body Font
     - Canvas & Surface hexes
     - Accent hexes
     - Radius Rule
     - Recommended Modifiers (from `styles/modifiers.yaml`)
2. **Portable Preview Link:**
   Provide a project-relative markdown link to the foundation gallery file, e.g. `[<style_id>.html](skills/design-director/gallery/<style_id>.html)` or `[<style_id>.html](.agents/skills/design-director/gallery/<style_id>.html)` based on the installation path.
   **CRITICAL:** Never output hardcoded absolute `file:///` URLs — links must remain portable across different machines and shared repositories.
3. **Honest Trade-offs:** The specific operational limitation or aesthetic risk of the style.

#### Foundation Style Taxonomy
See `styles/domain-style-defaults.yaml` (inside this skill) for the complete 27-foundation style taxonomy, visual signatures, and domain defaults. Live visual previews for all styles are in `gallery/<style_id>.html`.

### Phase 4: Critique, Refinements & Modifiers
When the user requests refinements or surface treatments, apply orthogonal modifiers from `styles/modifiers.yaml` inside this skill:
- **Surface Modifiers:** `frosted-glass` (backdrop blur + specular hairlines), `subtle-grain` (SVG noise texture), `crt-scanlines` (horizontal CRT lines), `fine-paper` (linen texture), `chrome-specular` (luminous border gradient).
- **Motion Profiles:** `micro-snappy` (120ms ease-out), `fluid-spring` (350ms spring), `inert` (0ms / transitions disabled).
- **Brand Influences:** Map requests like "more like Linear" or "more like Stripe" as influence vectors (e.g. shift to `dark-minimal` with `micro-snappy` motion and `frosted-glass` surfaces).

### Phase 5: Implementation Contract Handoff
Once confirmed:
1. Load `styles/<style_id>.md` from this skill folder (and only that style file).
2. Generate `DESIGN_CONTRACT.md` in the project root containing:
   - Target foundation name and token variables (CSS variables & Tailwind mappings).
   - Active orthogonal modifiers (`Surface`, `Motion`, `Imagery`, `Typography`).
   - Component geometry rules.
   - **`## Mandatory Anti-Patterns`**: The explicit `NEVER` constraints from the style pack.
   - Audit whitelist rules for declared modifiers.
3. Hand off `DESIGN_CONTRACT.md` to the coding agent for enforcement.
4. **Tailored Preview (Optional / Opt-in Only):**
   Once a style is selected (not at the 3-candidate stage), offer the user the option to generate ONE tailored single-file preview (e.g. `preview_<style_id>.html` in project root) demonstrating their chosen style, active modifiers, and custom palette applied to their actual product domain. Only generate this if the user explicitly opts in.
