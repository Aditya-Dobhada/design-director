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
- **On-Demand Loading:** The agent loads **only the single chosen style pack** (`styles/<style_id>.md`, ~2.2k tokens) when generating the contract. The 11 other styles are never loaded into prompt context.
- **Project-Scoped Enforcement:** Outputs a local, project-level `DESIGN_CONTRACT.md`. Never mutates global system configurations.

---

## 3. Supported Design Taxonomy (20 Foundations across 7 Families)

Each foundation style is delivered as a consolidated, self-contained specification in [`styles/<style_id>.md`](file:///styles/) with complete tokens, typography, component geometry, and mandatory `NEVER` anti-patterns:

| Family | Style ID | Name | Visual Signature | Ideal Domain | Gallery Preview |
|---|---|---|---|---|---|
| **Modern** | `minimal-modern` | **Minimal Modern** | High whitespace, neutral slate, 4–8px radius, Sohne/Inter | SaaS, productivity, developer tooling | [minimal_modern.html](file:///gallery/minimal_modern.html) |
| **Modern** | `dark-minimal` | **Dark Minimal** | Obsidian dark canvas, hairline borders, muted slate, Inter | Developer consoles, terminal tooling, dark SaaS | [dark_minimal.html](file:///gallery/dark_minimal.html) |
| **Modern** | `swiss-editorial` | **Swiss / Editorial** | Pure white (`#FFFFFF`), Playfair 600, Swiss red (`#E30613`), 4+8 asymmetric grid | Media, architecture, dense data broadsheets | [swiss_editorial.html](file:///gallery/swiss_editorial.html) |
| **Historical** | `bauhaus` | **Bauhaus** | Constructivist 8px grid, primary triad (`#E03A3E`/`#FFD100`/`#004B97`), IBM Plex Sans | Engineering, industrial software, tools | [bauhaus.html](file:///gallery/bauhaus.html) |
| **Historical** | `art-deco` | **Art Deco** | Obsidian & rich gold, stepped geometry, hairpin borders, 0px radius | Luxury hospitality, prestige fintech, editorial | [art_deco.html](file:///gallery/art_deco.html) |
| **Historical** | `mid-century-modern` | **Mid-Century Modern** | Warm olive & mustard, teak brown, organic curved pods (16px) | Architecture, curated retail, lifestyle | [mid_century_modern.html](file:///gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | **Retro Americana** | Cream parchment (`#F9F0DC`), vermilion (`#C8391E`), Saul Bass geometry, slab type | Food, heritage brands, national parks | [retro_americana.html](file:///gallery/retro_americana.html) |
| **Retro** | `terminal-cli` | **Terminal / CLI** | Fixed pitch amber/green phosphor, 0px radius, character cell borders | Devops telemetry, network monitoring, hacking consoles | [terminal_cli.html](file:///gallery/terminal_cli.html) |
| **Retro** | `y2k-frutiger-aero` | **Y2K / Frutiger Aero** | Glossy specular glassmorphism, aqua-to-lime gradients, Nunito 800 | Consumer productivity, playful apps | [y2k_frutiger_aero.html](file:///gallery/y2k_frutiger_aero.html) |
| **Futuristic** | `cyberpunk` | **Cyberpunk** | Obsidian dark (`#050508`), cyan HUD (`#00F5FF`), Rajdhani 700, chamfers | CLI telemetry, terminals, security consoles | [cyberpunk.html](file:///gallery/cyberpunk.html) |
| **Futuristic** | `space-age-optimism` | **Space Age Optimism** | Warm optical white (`#FAFAF8`), molded pods (32px), NASA orange (`#FF5C00`) | Edtech, aerospace, optimistic platforms | [space_age_optimism.html](file:///gallery/space_age_optimism.html) |
| **Organic** | `japanese-wabi-sabi` | **Japanese Wabi-Sabi** | Rice paper (`#FAF7F0`), charcoal ink wash, Mingei craft, Noto Serif JP 300 | Mindfulness, tea/craft, contemplative apps | [japanese_wabi_sabi.html](file:///gallery/japanese_wabi_sabi.html) |
| **Organic** | `organic-natural` | **Organic Natural** | Bone canvas (`#F5F1E8`), living earth pigments (clay, moss, sap), river-stone pods | Sustainability, climate, botanicals | [organic_natural.html](file:///gallery/organic_natural.html) |
| **Experimental** | `neo-brutalism` | **Neo-Brutalism** | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | Creator platforms, dev tools, zines | [neo_brutalism.html](file:///gallery/neo_brutalism.html) |
| **Experimental** | `web-brutalism` | **Web Brutalism** | Default browser box-model, pure raw HTML typography, unstyled blue links | Web archives, hacker forums, anti-design manifestos | [web_brutalism.html](file:///gallery/web_brutalism.html) |
| **Experimental** | `memphis-postmodern` | **Memphis Postmodern** | Polka dots, diagonal hatch patterns, geometric squiggles, Syne 800 | Drops, fashion, experimental portfolios | [memphis_postmodern.html](file:///gallery/memphis_postmodern.html) |
| **Experimental** | `maximalist-dopamine` | **Maximalist Dopamine** | Acid yellow (`#FFF500`), colliding neon hues, multi-color drop shadows | Streetwear, music, youth culture | [maximalist_dopamine.html](file:///gallery/maximalist_dopamine.html) |
| **Experimental** | `vaporwave` | **Vaporwave** | Sunset purple-pink gradients, wireframe horizons, retro aesthetic | Creative platforms, synthwave, digital audio | [vaporwave.html](file:///gallery/vaporwave.html) |
| **Luxury** | `quiet-luxury` | **Quiet Luxury** | Alabaster (`#FBFBF9`), Cormorant Garamond 300, 0px radius, hairline dividers | Private wealth, high-end advisory, luxury | [quiet_luxury.html](file:///gallery/quiet_luxury.html) |
| **Luxury** | `high-fashion-editorial` | **High Fashion Editorial** | Stark runway broadsheet, stark all-caps, razor 0px lines, flash contrast | Haute couture, avant-garde design, high fashion | [high_fashion_editorial.html](file:///gallery/high_fashion_editorial.html) |

---

## 3.1 Modifiers Architecture (`styles/modifiers.yaml`)

Rather than multiplying styles combinatorially, four orthogonal modifier dimensions compose cleanly over any foundation:
1. **Surface:** `frosted-glass` (specular translucent blur), `subtle-grain` (film grain overlay), `crt-scanlines` (phosphor scanlines), `fine-paper` (tactile fibrous texture).
2. **Imagery:** `monochrome-photography`, `wireframe-technical`, `duotone-accent`, `candid-flash`.
3. **Typography:** `monospace-accent`, `extended-caps`, `ink-trap-emphasis`.
4. **Motion:** `kinetic-pop` (snappy spring), `slow-drift` (ambient cinematic glide), `instant` (zero-latency keystroke).

---

## 4. Functional Requirements

### 4.1 Context Analysis & Diagnostic Interview
- Inspects project files (`README.md`, `PRD.md`, `package.json`, source code).
- Detects product domain, audience, and workflow density.
- **Interview Gate:** If the domain or density is ambiguous, asks up to 3 targeted questions before guessing.

### 4.2 Recommendation & Visual Previews
- Recommends 2–3 candidate styles tailored to the domain.
- Displays an **in-chat visual micro-spec** (display font, primary hex swatches, radius rule) directly in chat.
- Provides clickable links to live standalone HTML preview files in [`gallery/`](file:///gallery/).
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
- Returns a structured report with file paths, line numbers, and actionable remediation notes.

---

## 5. Repository Structure

```
design-director/
├── skills/
│   ├── design-director/
│   │   ├── SKILL.md            # Conversational director skill (<1.2k tokens)
│   │   ├── director_engine.py  # Programmatic engine (for deterministic pipelines)
│   │   └── reference-library.yaml
│   └── design-audit/
│       ├── SKILL.md            # Audit skill prompt
│       └── audit_code.py       # Standalone static linter
│
├── styles/                     # 12 consolidated, single-file style packs
│   ├── quiet-luxury.md
│   ├── swiss-editorial.md
│   ├── neo-brutalism.md
│   └── ... (9 other styles)
│
├── gallery/                    # 13 standalone HTML visual previews
│   ├── quiet_luxury.html
│   ├── swiss_editorial.html
│   └── ... (11 other styles + baseline)
│
├── tests/                      # CI verification suites
│   ├── fixtures/               # Seeded code and test PRDs
│   ├── test_director.py        # 10 unit tests
│   └── e2e/
│       ├── test_pipeline_e2e.py    # 22 pipeline integration tests
│       └── browser_dom_audit.spec.js # Playwright DOM computed style audit
│
├── package.json
└── README.md
```

---

## 6. Verification & Quality Standards

- **Unit Testing:** 10/10 tests passing via `npm run test:unit`.
- **Pipeline Integration Testing:** 22/22 tests passing via `npm run test:e2e:pipeline`.
- **Browser DOM Audit:** Headless Chromium testing via Playwright asserting computed CSS values (`borderRadius === 0px`, `boxShadow === none`, font loading, and contrast luminance).
