---
name: design-director
description: Conversational design reasoning engine. Analyzes project context (PRD, README, codebase), runs a targeted 3-question intake interview when context is thin, presents 2-3 tailored visual directions with in-chat swatches and live gallery preview links, and generates a binding project-level DESIGN_CONTRACT.md for frontend coding agents.
---

# Design Director

A design reasoning engine that establishes an intentional, implementation-ready visual language before frontend code is generated. It prevents coding agents from collapsing into generic Tailwind SaaS defaults (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`).

## Token Economy Rules
1. **Never load all styles at once.** The 12 full style guides live in `styles/<style_id>.md`. Read **only the single chosen style file** when generating the final contract.
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
Select the 2–3 strongest fits from the 12 design styles. Present each direction with:
1. **In-Chat Visual Micro-Spec:** Display font, canvas hex, accent hex, and radius rule directly in the response so the user can decide without switching context.
2. **Local Preview Link:** Provide a clickable link to the local preview file: `gallery/<style_id>.html`.
3. **Honest Trade-offs:** The specific operational limitation of the style (e.g., whitespace cost, sensory intensity, daylight contrast).

#### Style Taxonomy Index
| Style ID | Visual Signature | Ideal For | Preview File |
|---|---|---|---|
| `quiet-luxury` | Alabaster (`#FBFBF9`), Cormorant Garamond 300, 0px radius, hairline dividers | Private wealth, high-end advisory, luxury | [quiet_luxury.html](file:///gallery/quiet_luxury.html) |
| `swiss-editorial` | Pure white (`#FFFFFF`), Playfair 600 + JetBrains Mono, Swiss Red (`#E30613`), 0px radius | Media, architecture, dense editorial data | [swiss_editorial.html](file:///gallery/swiss_editorial.html) |
| `neo-brutalism` | 3px solid ink borders, 4px solid black offset shadows, saturated color pops, Space Grotesk | Creator platforms, dev tools, zines | [neo_brutalism.html](file:///gallery/neo_brutalism.html) |
| `cyberpunk` | Obsidian (`#050508`), cyan HUD (`#00F5FF`), Rajdhani 700 + Mono, 8px chamfer clip-paths | CLI telemetry, terminals, security consoles | [cyberpunk.html](file:///gallery/cyberpunk.html) |
| `space-age-optimism` | Warm white (`#FAFAF8`), molded fiberglass pods (32px), NASA orange (`#FF5C00`), DM Serif | Edtech, aerospace, optimistic platforms | [space_age_optimism.html](file:///gallery/space_age_optimism.html) |
| `bauhaus` | Constructivist 8px grid, primary triad (`#E03A3E`/`#FFD100`/`#004B97`), IBM Plex Sans 700 lc | Engineering, industrial software, tools | [bauhaus.html](file:///gallery/bauhaus.html) |
| `japanese-wabi-sabi` | Rice paper (`#FAF7F0`), charcoal ink wash, Mingei craft, Noto Serif JP 300, empty ma space | Mindfulness, tea/craft, contemplative apps | [japanese_wabi_sabi.html](file:///gallery/japanese_wabi_sabi.html) |
| `organic-natural` | Bone canvas (`#F5F1E8`), clay/moss/sap pigments, river-stone pod containers (24–40px) | Sustainability, climate, botanicals | [organic_natural.html](file:///gallery/organic_natural.html) |
| `retro-americana` | Cream parchment (`#F9F0DC`), vermilion (`#C8391E`), slab serifs (Alfa Slab One), 3px ink borders | Food, heritage brands, national parks | [retro_americana.html](file:///gallery/retro_americana.html) |
| `y2k-frutiger-aero` | Aqua/lime glossy gradients, specular glassmorphism, 9999px pills, Nunito 800 | Consumer productivity, playful apps | [y2k_frutiger_aero.html](file:///gallery/y2k_frutiger_aero.html) |
| `memphis-postmodern` | Flat graphic planes, diagonal hatch/polka patterns, geometric squiggles, Syne 800 | Drops, fashion, experimental portfolios | [memphis_postmodern.html](file:///gallery/memphis_postmodern.html) |
| `maximalist-dopamine` | Acid yellow (`#FFF500`), colliding neon hues, multi-colored drop shadows, sticker badges | Streetwear, music, youth culture | [maximalist_dopamine.html](file:///gallery/maximalist_dopamine.html) |

### Phase 4: Critique & Refinement
When the user requests refinements, map brand references directly:
- **"More like Linear / Raycast":** Shift surfaces to obsidian dark (`#08090A`), 1px translucent borders (`rgba(255,255,255,0.08)`), single violet accent (`#5E6AD2`), micro-snappy 120ms transitions.
- **"More like Stripe":** Shift to crisp white cards, refined typographic scale, and vibrant gradient accents.
- **"More like Gumroad":** Shift to 3px solid black outlines and 4px hard solid offset shadows.
- **"More like Aesop":** Shift to warm cream paper tones, stone hairlines, and literary serif headings.

### Phase 5: Implementation Contract Handoff
Once the user confirms the style:
1. Use `view_file` to read the corresponding `styles/<style_id>.md` (and **only** that style file).
2. Generate `DESIGN_CONTRACT.md` in the project root with:
   - Target style name and core tokens (CSS variables & Tailwind mappings).
   - Component geometry (buttons, cards, inputs).
   - **`## Mandatory Anti-Patterns`**: The explicit `NEVER` constraints from the style pack.
   - The product specification to implement.
3. Inform the user that the frontend coding agent should execute implementation using `DESIGN_CONTRACT.md` as its hard constraint contract.
