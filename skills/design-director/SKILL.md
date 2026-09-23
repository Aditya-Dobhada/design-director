---
name: design-director
description: Conversational design reasoning engine. Analyzes project context (PRD, README, codebase), runs a targeted 3-question intake interview when context is thin, presents 2-3 tailored visual directions across 27 foundations with in-chat swatches, preview links, and orthogonal modifiers, and generates a binding DESIGN_CONTRACT.md for coding agents.
---

# Design Director

A design reasoning engine that establishes an intentional, implementation-ready visual language before frontend code is generated, preventing coding agents from collapsing into generic Tailwind SaaS defaults (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`).

## Token Economy Rules
1. **Never load all styles at once.** The 27 style guides live in `styles/<style_id>.md` inside this skill. Read **only the single chosen style file** when generating the contract.
2. **Never load reference libraries into prompt context.** The brief mapping rules below provide all necessary refinement context.
3. **Keep contracts project-scoped.** Write `DESIGN_CONTRACT.md` to the project root. Never mutate global or system configuration.

---

## 5-Phase Workflow

### Phase 1: Context Analysis
Inspect available project files: `README.md`, `PRD.md`, `SPEC.md`, `package.json`, or existing UI files. Identify domain & product type, target audience, and density/workflow needs.

### Phase 2: Diagnostic Interview Gate
- If project context clearly indicates domain, tone, and density: **skip interview and recommend immediately.**
- If context is vague or incomplete, ask **at most 3 targeted questions**:
  1. **Information Density:** High-density operational data (tables, metrics) or spacious editorial reading?
  2. **Brand Character:** Quiet institutional authority, energetic creator/grassroots, playful maximalist, or futuristic tactical?
  3. **Visual Constraints:** Strict dark mode, WCAG AAA readability, or specific brand colors?

### Phase 3: Recommendations (2–3 Candidate Directions)
Select the 2–3 strongest fits from the 27 foundational styles. For each candidate direction, present:

1. **In-Chat Visual Micro-Spec (Inline in Message):**
   Render a lightweight inline visual directly in chat (never create files or full HTML mockups during shortlisting):
   - **Inline SVG Strip:** `<svg width="100%" height="34" viewBox="0 0 380 34" fill="none">` with 4 palette swatches (Canvas, Surface, Primary Accent, Secondary Accent), an outlined radius-sample shape (`rx="0"`, `rx="6"`, or `rx="12"`), and display font text.
   - **Swatch & Token Summary:**
     `[⬛ #canvas] [⬛ #surface] [🟨 #accent1] [🟨 #accent2] | Radius: <rule> | Font: **<Display Font>**`
     - Display & Body Fonts, Canvas & Surface hexes, Accent hexes, Radius Rule, and Recommended Modifiers (from `styles/modifiers.yaml`).
2. **Portable Preview Link:**
   Provide a project-relative markdown link to the foundation gallery file, e.g. `[<style_id>.html](skills/design-director/gallery/<style_id>.html)` or `[<style_id>.html](.agents/skills/design-director/gallery/<style_id>.html)`.
   **CRITICAL:** Never output hardcoded absolute `file:///` URLs.
3. **Honest Trade-offs:** The specific operational limitation or aesthetic risk of the style.

#### Foundation Style Taxonomy
See `styles/domain-style-defaults.yaml` (inside this skill) for the 27-foundation style taxonomy, visual signatures, and domain defaults. Live previews are in `gallery/<style_id>.html`.

### Phase 4: Critique, Refinements & Modifiers
When the user requests refinements or surface treatments, apply orthogonal modifiers from `styles/modifiers.yaml`:
- **Surface Modifiers:** `frosted-glass`, `subtle-grain`, `crt-scanlines`, `fine-paper`, `chrome-specular`.
- **Motion Profiles:** `micro-snappy` (120ms), `fluid-spring` (350ms), `inert` (0ms).
- **Brand Influences:** Map requests like "more like Linear" or "more like Stripe" as influence vectors (e.g. shift to `dark-minimal` with `micro-snappy` motion and `frosted-glass` surfaces).

### Phase 5: Implementation Contract Handoff
Once confirmed:
1. Load `styles/<style_id>.md` from this skill folder (and only that style file).
2. Generate `DESIGN_CONTRACT.md` in project root containing:
   - Target foundation name and token variables (CSS variables & Tailwind mappings).
   - Active orthogonal modifiers (`Surface`, `Motion`, `Imagery`, `Typography`).
   - Component geometry rules.
   - **`## Mandatory Anti-Patterns`**: Explicit `NEVER` constraints from the style pack.
   - Audit whitelist rules for declared modifiers.
3. Hand off `DESIGN_CONTRACT.md` to the coding agent for enforcement.
4. **Tailored Preview (Optional / Opt-in Only):**
   Once a style is selected, offer the user the option to generate ONE tailored single-file preview (e.g. `preview_<style_id>.html` in project root) demonstrating their chosen style, active modifiers, and custom palette applied to their product domain. Only generate this if the user explicitly opts in.
