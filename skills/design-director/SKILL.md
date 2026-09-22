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

#### 20 Foundations Taxonomy (Grouped by Family)
| Family | Style ID | Visual Signature | Ideal For | Preview File |
|---|---|---|---|---|
| **Modern UI** | `minimal-modern` | Neutral zinc (`#FAFAFA`), 6–8px radius, Geist/Inter, 1px border (`#E4E4E7`) | Contemporary SaaS, productivity, apps | [minimal_modern.html](file:///gallery/minimal_modern.html) |
| | `dark-minimal` | Obsidian (`#09090B`), 6–8px radius, Geist Mono, 1px translucent border | Modern devtools, AI consoles, telemetry | [dark_minimal.html](file:///gallery/dark_minimal.html) |
| **Historical** | `swiss-editorial` | Pure white (`#FFFFFF`), Playfair 600 + Mono, Swiss Red (`#E30613`), 0px radius | Media, architecture, dense broadsheets | [swiss_editorial.html](file:///gallery/swiss_editorial.html) |
| | `bauhaus` | Constructivist 8px grid, primary triad (`#E03A3E`/`#FFD100`/`#004B97`), IBM Plex Sans | Industrial software, engineering tools | [bauhaus.html](file:///gallery/bauhaus.html) |
| | `art-deco` | Caviar black (`#0E0E10`), burnished gold (`#D4AF37`), Bodoni/Cinzel, 0px radius | High-end hospitality, formal luxury | [art_deco.html](file:///gallery/art_deco.html) |
| | `mid-century-modern` | Warm parchment (`#F6F3EB`), terracotta/olive/mustard, atomic pods (16–24px) | Architecture, furniture, lifestyle brands | [mid_century_modern.html](file:///gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | Cream parchment (`#F9F0DC`), vermilion (`#C8391E`), slab serifs, 3px ink borders | Food, heritage brands, national parks | [retro_americana.html](file:///gallery/retro_americana.html) |
| | `y2k-frutiger-aero` | Aqua/lime glossy gradients, specular glassmorphism, 9999px pills, Nunito 800 | Consumer productivity, playful apps | [y2k_frutiger_aero.html](file:///gallery/y2k_frutiger_aero.html) |
| | `vaporwave` | Twilight lavender, pastel pink/cyan, CRT scanlines, VT323 + Playfair, bevels | Music, culture, retro digital experiments | [vaporwave.html](file:///gallery/vaporwave.html) |
| **Futuristic** | `cyberpunk` | Obsidian (`#050508`), cyan HUD (`#00F5FF`), Rajdhani 700 + Mono, chamfer clips | Sci-fi telemetry, terminals, security consoles | [cyberpunk.html](file:///gallery/cyberpunk.html) |
| | `space-age-optimism` | Warm white (`#FAFAF8`), molded fiberglass pods (32px), NASA orange (`#FF5C00`) | Edtech, aerospace, optimistic platforms | [space_age_optimism.html](file:///gallery/space_age_optimism.html) |
| | `terminal-cli` | Pitch black (`#0C0C0C`), amber/emerald phosphors, 100% monospace, ASCII rules | Unix consoles, SRE dashboards, internal tools | [terminal_cli.html](file:///gallery/terminal_cli.html) |
| **Raw Web** | `web-brutalism` | Raw document HTML, Courier/system font, blue underlined links, 0px radius | Zines, dev blogs, experimental sites | [web_brutalism.html](file:///gallery/web_brutalism.html) |
| | `neo-brutalism` | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | Creator platforms, dev tools, zines | [neo_brutalism.html](file:///gallery/neo_brutalism.html) |
| **Organic** | `organic-natural` | Bone canvas (`#F5F1E8`), clay/moss/sap pigments, river-stone pod containers | Sustainability, climate, botanicals | [organic_natural.html](file:///gallery/organic_natural.html) |
| | `japanese-wabi-sabi` | Rice paper (`#FAF7F0`), charcoal ink wash, Mingei craft, Noto Serif JP 300 | Mindfulness, tea/craft, contemplative apps | [japanese_wabi_sabi.html](file:///gallery/japanese_wabi_sabi.html) |
| **Luxury** | `quiet-luxury` | Alabaster (`#FBFBF9`), Cormorant Garamond 300, 0px radius, hairline dividers | Private wealth, high-end advisory, luxury | [quiet_luxury.html](file:///gallery/quiet_luxury.html) |
| | `high-fashion-editorial` | Stark monochrome (`#0A0A0A`/`#FFFFFF`), Bodoni display + micro sans, 0px radius | Couture lookbooks, runway portfolios | [high_fashion_editorial.html](file:///gallery/high_fashion_editorial.html) |
| | `memphis-postmodern` | Flat graphic planes, diagonal hatch patterns, geometric squiggles, Syne 800 | Drops, fashion, experimental portfolios | [memphis_postmodern.html](file:///gallery/memphis_postmodern.html) |
| | `maximalist-dopamine` | Acid yellow (`#FFF500`), colliding neon hues, multi-color drop shadows | Streetwear, music, youth culture | [maximalist_dopamine.html](file:///gallery/maximalist_dopamine.html) |

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
