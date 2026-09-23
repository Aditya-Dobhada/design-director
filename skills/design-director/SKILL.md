---
name: design-director
description: Design reasoning engine. Analyzes project context (PRD, README, codebase), recommends 2-3 visual directions with in-chat swatches and preview links, and generates a binding DESIGN_CONTRACT.md for coding agents.
---

# Design Director

Establishes an intentional visual language before code is generated, preventing collapse into generic Tailwind defaults (`Inter`, `rounded-lg`, `bg-blue-600`).

## Token Economy Rules
1. **Never load all styles at once.** The 27 style guides live in `styles/<style_id>.md` inside this skill. Read **only the single chosen style file** when generating the contract.
2. **Load `reference-library.yaml` only for named-brand refinements** (e.g. "more like Stripe"): it costs ~10k tokens, so never load it for anything else.
3. **Keep contracts project-scoped.** Write `DESIGN_CONTRACT.md` to the project root; never mutate global config.
4. **Link gallery previews, never read them.** Reference `gallery/<style_id>.html` via markdown links only — reading one costs 1.7–6.5k tokens.

---

## 5-Phase Workflow

### Phase 1: Context Analysis
Inspect `README.md`, `PRD.md`, `SPEC.md`, `package.json`, or UI files; identify domain, audience, and density/workflow needs.

### Phase 2: Diagnostic Interview Gate
- Rich context (domain, tone, density clear): **skip interview, recommend immediately.**
- If context is vague or incomplete, ask **at most 3 targeted questions**:
  1. **Information Density:** High-density operational data (tables, metrics) or spacious editorial reading?
  2. **Brand Character:** Quiet institutional authority, energetic creator/grassroots, playful maximalist, or futuristic tactical?
  3. **Visual Constraints:** Strict dark mode, WCAG AAA readability, or specific brand colors?

### Phase 3: Recommendations (2–3 Candidate Directions)
Select the 2–3 strongest fits from the 27 foundational styles. For each candidate direction, present:

1. **In-Chat Visual Micro-Spec (Inline in Message):**
   Render inline in chat (never create files or mockups during shortlisting):
   - **Inline SVG Strip:** `<svg width="100%" height="34" viewBox="0 0 380 34" fill="none">` with 4 palette swatches (Canvas, Surface, Primary Accent, Secondary Accent), a radius-sample outline (`rx="0"`, `rx="6"`, or `rx="12"`), and display font text.
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
   - Foundation name, token variables (CSS vars, Tailwind mappings).
   - Active orthogonal modifiers (`Surface`, `Motion`, `Imagery`, `Typography`).
   - Component geometry rules.
   - **`## Mandatory Anti-Patterns`**: Explicit `NEVER` constraints from the style pack.
   - Audit whitelist rules for declared modifiers.
3. Hand off `DESIGN_CONTRACT.md` to the coding agent for enforcement.
4. **Tailored Preview (opt-in only):** offer ONE single-file preview (`preview_<style_id>.html`) in the chosen style; generate only on explicit opt-in.
