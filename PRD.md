# PRD: Design Director

**A design reasoning engine that turns product context into implementation-ready visual direction for AI coding agents.**

---

## 1. Problem Statement

AI coding agents produce technically valid, functionally correct UI that is visually indistinguishable from generic AI SaaS. This happens because agents collapse **design direction** and **implementation** into a single prompt-to-code step, defaulting to the statistical median of their training data (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`).

Design Director introduces an intentional reasoning and constraint layer that:
1. Analyzes what a product should feel like based on its actual context (users, domain, workflow density, constraints).
2. Interactively aligns with the user through a low-friction diagnostic interview when context is thin.
3. Provides concrete visual previews from a live gallery before code generation starts.
4. Hands that direction to a coding agent as a hard **`DESIGN_CONTRACT.md`** rather than a vague aesthetic vibe.
5. Verifies after implementation that the contract was strictly followed using an automated audit.

---

## 2. Core Architecture: The 2-Skill Model

```
PRD / README / Codebase Context
               │
               ▼
   [Skill 1: design-director]
   ├── Context Analysis
   ├── Diagnostic Interview Gate (max 3 questions if context is thin)
   ├── Domain-Style Lookup (styles/domain-style-defaults.yaml)
   ├── Curated Style Recommendations (2–3 candidates with gallery links)
   └── Contract Handoff (DESIGN_CONTRACT.md generation)
               │
               ▼
        AI Coding Agent
      (implements frontend)
               │
               ▼
    [Skill 2: design-audit]
 (Inspects code against contract)
```

### Token Economy & Zero-Bloat Guardrails
- **Lean Router Skill:** `skills/design-director/SKILL.md` is capped under **1,200 tokens**.
- **On-Demand Loading:** The agent loads **only the single chosen style pack** (`styles/<style_id>.md`, range: 1,205–3,669 tokens across the 27 styles) when generating the contract. The other 26 styles are never loaded into prompt context.
- **Project-Scoped Enforcement:** Outputs a local, project-level `DESIGN_CONTRACT.md`. Never mutates global system configurations.

---

## 3. Supported Design Taxonomy (27 Foundations across 8 Families)

Each foundation style is delivered as a consolidated, self-contained specification in [`styles/<style_id>.md`](styles/) with complete tokens, typography, component geometry, and mandatory `NEVER` anti-patterns:

| Family | Style ID | Name | Visual Signature | Ideal Domain | Gallery Preview |
|---|---|---|---|---|---|
| **Modern** | `minimal-modern` | **Minimal Modern** | High whitespace, neutral slate, 4–8px radius, Sohne/Inter | SaaS, productivity, developer tooling | [minimal_modern.html](gallery/minimal_modern.html) |
| **Modern** | `dark-minimal` | **Dark Minimal** | Obsidian dark canvas, hairline borders, muted slate, Inter | Developer consoles, terminal tooling, dark SaaS | [dark_minimal.html](gallery/dark_minimal.html) |
| **Modern** | `swiss-editorial` | **Swiss / Editorial** | Pure white (`#FFFFFF`), Playfair 600, Swiss red (`#E30613`), 4+8 asymmetric grid | Media, architecture, dense data broadsheets | [swiss_editorial.html](gallery/swiss_editorial.html) |
| **Historical** | `bauhaus` | **Bauhaus** | Constructivist 8px grid, primary triad (`#E03A3E`/`#FFD100`/`#004B97`), IBM Plex Sans | Engineering, industrial software, tools | [bauhaus.html](gallery/bauhaus.html) |
| **Historical** | `art-deco` | **Art Deco** | Obsidian & rich gold, stepped geometry, hairpin borders, 0px radius | Luxury hospitality, prestige fintech, editorial | [art_deco.html](gallery/art_deco.html) |
| **Historical** | `mid-century-modern` | **Mid-Century Modern** | Warm olive & mustard, teak brown, organic curved pods (16px) | Architecture, curated retail, lifestyle | [mid_century_modern.html](gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | **Retro Americana** | Cream parchment (`#F9F0DC`), vermilion (`#C8391E`), Saul Bass geometry, slab type | Food, heritage brands, national parks | [retro_americana.html](gallery/retro_americana.html) |
| **Retro** | `terminal-cli` | **Terminal / CLI** | Fixed pitch amber/green phosphor, 0px radius, character cell borders | Devops telemetry, network monitoring, hacking consoles | [terminal_cli.html](gallery/terminal_cli.html) |
| **Retro** | `y2k-frutiger-aero` | **Y2K / Frutiger Aero** | Glossy specular glassmorphism, aqua-to-lime gradients, Nunito 800 | Consumer productivity, playful apps | [y2k_frutiger_aero.html](gallery/y2k_frutiger_aero.html) |
| **Futuristic** | `cyberpunk` | **Cyberpunk** | Obsidian dark (`#050508`), cyan HUD (`#00F5FF`), Rajdhani 700, chamfers | CLI telemetry, terminals, security consoles | [cyberpunk.html](gallery/cyberpunk.html) |
| **Futuristic** | `space-age-optimism` | **Space Age Optimism** | Warm optical white (`#FAFAF8`), molded pods (32px), NASA orange (`#FF5C00`) | Edtech, aerospace, optimistic platforms | [space_age_optimism.html](gallery/space_age_optimism.html) |
| **Futuristic** | `aurora-gradient` | **Aurora Gradient** | Soft multi-color atmospheric gradients (`#8B5CF6`/`#EC4899`/`#06B6D4`) over dark base | AI products, creative tools, generative platforms | [aurora_gradient.html](gallery/aurora_gradient.html) |
| **Organic** | `japanese-wabi-sabi` | **Japanese Wabi-Sabi** | Rice paper (`#FAF7F0`), charcoal ink wash, Mingei craft, Noto Serif JP 300 | Mindfulness, tea/craft, contemplative apps | [japanese_wabi_sabi.html](gallery/japanese_wabi_sabi.html) |
| **Organic** | `organic-natural` | **Organic Natural** | Bone canvas (`#F5F1E8`), living earth pigments (clay, moss, sap), river-stone pods | Sustainability, climate, botanicals | [organic_natural.html](gallery/organic_natural.html) |
| **Organic** | `digital-organic` | **Digital Organic** | Organic blobs + technological typography + natural gradients | AI/wellness/biotech, living-system interfaces | [digital_organic.html](gallery/digital_organic.html) |
| **Experimental** | `neo-brutalism` | **Neo-Brutalism** | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | Creator platforms, dev tools, zines | [neo_brutalism.html](gallery/neo_brutalism.html) |
| **Experimental** | `web-brutalism` | **Web Brutalism** | Default browser box-model, pure raw HTML typography, unstyled blue links | Web archives, hacker forums, anti-design manifestos | [web_brutalism.html](gallery/web_brutalism.html) |
| **Experimental** | `memphis-postmodern` | **Memphis Postmodern** | Polka dots, diagonal hatch patterns, geometric squiggles, Syne 800 | Drops, fashion, experimental portfolios | [memphis_postmodern.html](gallery/memphis_postmodern.html) |
| **Experimental** | `maximalist-dopamine` | **Maximalist Dopamine** | Acid yellow (`#FFF500`), colliding neon hues, multi-color drop shadows | Streetwear, music, youth culture | [maximalist_dopamine.html](gallery/maximalist_dopamine.html) |
| **Experimental** | `vaporwave` | **Vaporwave** | Sunset purple-pink gradients, wireframe horizons, retro aesthetic | Creative platforms, synthwave, digital audio | [vaporwave.html](gallery/vaporwave.html) |
| **Luxury** | `quiet-luxury` | **Quiet Luxury** | Alabaster (`#FBFBF9`), Cormorant Garamond 300, 0px radius, hairline dividers | Private wealth, high-end advisory, luxury | [quiet_luxury.html](gallery/quiet_luxury.html) |
| **Luxury** | `high-fashion-editorial` | **High Fashion Editorial** | Stark runway broadsheet, stark all-caps, razor 0px lines, flash contrast | Haute couture, avant-garde design, high fashion | [high_fashion_editorial.html](gallery/high_fashion_editorial.html) |
| **Tactile** | `glassmorphism` | **Glassmorphism** | Frosted translucent panels, backdrop-blur (16–24px), 1px rgba borders, layered depth | OS-level UI, media/creative dashboards, overlay-heavy apps | [glassmorphism.html](gallery/glassmorphism.html) |
| **Tactile** | `neumorphism` | **Neumorphism** | Soft extruded UI, canvas-matched surfaces, dual soft shadow (light+dark), no borders | Settings/control panels, IoT/hardware companion apps | [neumorphism.html](gallery/neumorphism.html) |
| **Tactile** | `claymorphism` | **Claymorphism** | 3D pastel clay-like elements (20–32px radius), soft inner shadows, pastel element fills | Consumer mobile apps, wellness/kids products | [claymorphism.html](gallery/claymorphism.html) |
| **Utility** | `data-native` | **Data-Native** | Dense tables, monospace numerics (JetBrains Mono), 11–12px labels, restrained chroma | Analytics, finance, telemetry, BI tools | [data_native.html](gallery/data_native.html) |
| **Utility** | `command-center` | **Command Center** | Multi-panel layouts, semantic status indicators (red/amber/green), compact Inter typography | DevOps, security, infrastructure operations | [command_center.html](gallery/command_center.html) |

---

## 3.1 Modifiers Architecture (`styles/modifiers.yaml`)

Rather than multiplying styles combinatorially, six orthogonal modifier dimensions compose cleanly over any foundation:

1. **Surface:** `frosted-glass` (specular translucent blur), `subtle-grain` (film grain overlay), `crt-scanlines` (phosphor scanlines), `fine-paper` (tactile fibrous texture), `chrome-specular` (luminous metallic border).
2. **Imagery:** `editorial` (high-contrast art-directed photography), `technical` (monochromatic schematics), `photographic` (authentic documentary), `collage` (mixed-media), `pixel` (8/16-bit), `hand-drawn` (ink linework).
3. **Typography:** `monospace` (metrics & keys), `display-serif` (monumental headings), `condensed` (tight editorial), `handwritten` (personal annotations).
4. **Motion:** `micro-snappy` (120ms instant), `fluid-spring` (350ms organic), `inert` (0ms zero-motion).
5. **Density:** `ultra-dense` → `dense` → `balanced` → `spacious` → `ultra-spacious`. Controls spacing scale, information-per-viewport, and interactive control sizing.
6. **Layout:** `bento-grid` — masonry-style irregular card grid with heterogeneous cell spans. Composition-only: no independent color/radius/shadow logic. Pairs with any foundation style.

---

## 3.2 Anti-Pattern References (`styles/reference-anti-patterns.md`)

**Corporate Memphis / Alegria** is documented as a named anti-pattern (not a selectable style). `styles/reference-anti-patterns.md` serves as a human-reference document detailing the design history, visual indicators, and remediation guidelines for this pattern. The `design-audit` engine (`audit_code.py`) statically implements and enforces drift detection via hardcoded rule heuristics (`_check_line()` and `_check_corporate_memphis_drift()`) using signal accumulation across purple accents, bubbly containers, ambient shadow saturation, gradient blob decoration, and illustration placeholders (2 signals = WARNING; 3+ = CRITICAL).

---

## 3.3 Domain-Style Defaults (`styles/domain-style-defaults.yaml`)

A lookup table mapping common product domains (fintech, healthcare, legal, government, edtech, devops, ecommerce, real estate, hospitality, AI products, biotech, creative tools, media, social, analytics) to 2–3 recommended foundation-style IDs. Consumed by the diagnostic interview logic (§4.1) when a domain is detected or stated. This is a routing table, not a list of new foundation styles, and domain names do not appear in the §3 taxonomy table.

---

## 4. Functional Requirements

### 4.1 Context Analysis & Diagnostic Interview
- Inspects project files (`README.md`, `PRD.md`, `package.json`, source code).
- Detects product domain, audience, and workflow density.
- Consults `styles/domain-style-defaults.yaml` for domain-aware candidate shortlisting.
- **Interview Gate:** If the domain or density is ambiguous, asks up to 3 targeted questions before guessing.

### 4.2 Recommendation & Visual Previews
- Recommends 2–3 candidate styles tailored to the domain.
- Displays an **in-chat visual micro-spec** (display font, primary hex swatches, radius rule) directly in chat.
- Provides clickable links to live standalone HTML preview files in [`gallery/`](gallery/).
- Details honest operational trade-offs for each candidate style.

### 4.3 Critique & Layer Refinement
- Maps free-text user feedback directly to concrete style layers:
  - *"More like Linear / Raycast"* → Obsidian dark surfaces, translucent hairlines, single violet accent, micro-snappy 120ms transitions.
  - *"More like Stripe"* → Crisp white cards, refined typographic scale, vibrant gradient accents.
  - *"More like Gumroad"* → 3px solid ink borders, 4px solid black offset shadows.
  - *"More like Aesop"* → Warm cream parchment, stone hairlines, literary serif headings.

### 4.4 Contract Handoff
- Assembles a binding `DESIGN_CONTRACT.md` file in the project root containing:
  - Exact token variables (CSS variables and Tailwind mappings).
  - Component geometry (buttons, cards, inputs).
  - **`## Mandatory Anti-Patterns`**: Explicit `NEVER` constraints.
  - Product specifications for the coding agent.

### 4.5 Post-Implementation Audit
- The `design-audit` tool statically inspects generated `.html`, `.jsx`, `.tsx`, `.vue`, `.svelte`, and `.css` files.
- Flags forbidden border-radius, diffuse blur drop shadows, invalid heading fonts, and illegal color classes.
- Detects Corporate Memphis / Alegria drift as a cross-cutting check.
- Returns a structured report with file paths, line numbers, and actionable remediation notes.

---

## 5. Repository Structure

```
design-director/
├── skills/
│   ├── design-director/
│   │   ├── SKILL.md            # Conversational director skill (<1.2k tokens)
│   │   ├── director_engine.py  # Programmatic engine (for deterministic pipelines)
│   │   └── reference-library.yaml # 26 reference brand influences mapped to foundations
│   └── design-audit/
│       ├── SKILL.md            # Audit skill prompt
│       └── audit_code.py       # Standalone static linter with modifier whitelists + Memphis detection
│
├── styles/                     # 27 consolidated style packs + modifiers + references
│   ├── modifiers.yaml          # Surface, imagery, typography, motion, density, and layout dimensions
│   ├── domain-style-defaults.yaml  # Domain → style ID lookup table (consumed by §4.1)
│   ├── reference-anti-patterns.md  # Corporate Memphis / Alegria anti-pattern reference
│   ├── minimal-modern.md
│   ├── dark-minimal.md
│   ├── swiss-editorial.md
│   ├── terminal-cli.md
│   ├── web-brutalism.md
│   ├── art-deco.md
│   ├── mid-century-modern.md
│   ├── vaporwave.md
│   ├── high-fashion-editorial.md
│   ├── glassmorphism.md        # Tactile family
│   ├── neumorphism.md          # Tactile family
│   ├── claymorphism.md         # Tactile family
│   ├── data-native.md          # Utility family
│   ├── command-center.md       # Utility family
│   ├── aurora-gradient.md      # Futuristic family
│   ├── digital-organic.md      # Organic family
│   └── ... (11 other foundation style packs)
│
├── gallery/                    # 27 standalone HTML visual previews (canonical "Aurelia" product)
│   ├── minimal_modern.html
│   ├── dark_minimal.html
│   ├── glassmorphism.html
│   ├── neumorphism.html
│   ├── claymorphism.html
│   ├── data_native.html
│   ├── command_center.html
│   ├── aurora_gradient.html
│   ├── digital_organic.html
│   └── ... (18 other canonical previews)
│
├── tests/                      # CI verification suites
│   ├── fixtures/               # Seeded code and test PRDs
│   ├── test_director.py        # Unit tests (specs, contracts, modifiers, routing, 7 new styles)
│   └── e2e/
│       ├── test_pipeline_e2e.py    # Pipeline tests (audits all 27 gallery previews)
│       └── browser_dom_audit.spec.js # Playwright DOM computed style audit
│
├── package.json
└── README.md
```

---

## 6. Verification & Quality Standards

- **Unit Testing:** All tests passing via `npm run test:unit` (validating brief extraction, 27-foundation specs, modifier contracts including density/bento-grid, multi-defensible routing, layer-scoped refinements, domain-style-defaults YAML integrity, and 7 new style packs completeness).
- **Pipeline Integration Testing:** All tests passing via `npm run test:e2e:pipeline` (statically auditing all 27 gallery HTML fixtures with 0 critical violations).
- **Browser DOM Audit:** Headless Chromium testing via Playwright asserting computed CSS values (`borderRadius === 0px`, `boxShadow === none`, font loading, and contrast luminance).
