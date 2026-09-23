# Design Director

A design reasoning engine that transforms product context into implementation-ready visual direction for AI coding agents.

Design Director prevents coding agents (Cursor, Claude Code, Antigravity) from collapsing design into generic Tailwind SaaS defaults (`Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`) by establishing a binding, project-level **`DESIGN_CONTRACT.md`** before code is written, and verifying compliance afterward.

---

## Architecture: The 2-Skill Model

```
                    PRD / README / Product Context
                                  │
                                  ▼
                     [Skill 1: design-director]
                     • Scans product context
                     • Runs 3-question interview if context is thin
                     • Consults domain-style-defaults.yaml for candidate shortlist
                     • Recommends 2–3 styles with live gallery links
                     • User chooses or refines ("more like Linear")
                                  │
                                  ▼
                         DESIGN_CONTRACT.md
                    (Hard tokens + NEVER anti-patterns)
                                  │
                                  ▼
                         AI Coding Agent
                       (implements frontend)
                                  │
                                  ▼
                      [Skill 2: design-audit]
                    (Checks code against contract)
```

### Token-Optimized Design
- **Lean Entry Point:** `skills/design-director/SKILL.md` is strictly capped under **1,200 tokens**.
- **On-Demand Loading:** The agent loads **only the single chosen style pack** (`styles/<style_id>.md`, range: 1,205–3,669 tokens across the 27 styles) when generating the contract. The other 26 styles are never loaded into prompt context.
- **Project-Scoped:** Generates `DESIGN_CONTRACT.md` in the local workspace. Never mutates global system configurations.

---

## Visual Style Gallery

Live HTML implementations for all 27 foundations are available in [`gallery/`](file:///gallery/):

| Family | Style ID | Name | Visual Signature | Key Hex Values | Preview Reference |
|---|---|---|---|---|---|
| **Modern** | `minimal-modern` | **Minimal Modern** | High whitespace, neutral slate, 4–8px radius, Sohne/Inter | `#FFFFFF`, `#0F172A`, `#2563EB` | [minimal_modern.html](file:///gallery/minimal_modern.html) |
| **Modern** | `dark-minimal` | **Dark Minimal** | Obsidian dark canvas, hairline borders, muted slate, Inter | `#08090A`, `#111215`, `#5E6AD2` | [dark_minimal.html](file:///gallery/dark_minimal.html) |
| **Modern** | `swiss-editorial` | **Swiss / Editorial** | Pure white, Playfair Display 600, Swiss red, asymmetric 4+8 grid | `#FFFFFF`, `#111111`, `#E30613` | [swiss_editorial.html](file:///gallery/swiss_editorial.html) |
| **Historical** | `bauhaus` | **Bauhaus** | Constructivist 8px grid, primary triad accents, IBM Plex Sans 700 lc | `#FFFFFF`, `#E03A3E`, `#004B97` | [bauhaus.html](file:///gallery/bauhaus.html) |
| **Historical** | `art-deco` | **Art Deco** | Obsidian & rich gold, stepped geometry, hairpin borders, 0px radius | `#0D0D11`, `#D4AF37`, `#F3E5AB` | [art_deco.html](file:///gallery/art_deco.html) |
| **Historical** | `mid-century-modern` | **Mid-Century Modern** | Warm olive & mustard, teak brown, organic curved pods (16px) | `#FDFBF7`, `#5B7053`, `#D4973B` | [mid_century_modern.html](file:///gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | **Retro Americana** | Cream parchment, vermilion, Saul Bass geometry, Alfa Slab One | `#F9F0DC`, `#C8391E`, `#E8A126` | [retro_americana.html](file:///gallery/retro_americana.html) |
| **Retro** | `terminal-cli` | **Terminal / CLI** | Fixed pitch amber/green phosphor, 0px radius, character cell borders | `#000000`, `#00FF66`, `#FFB000` | [terminal_cli.html](file:///gallery/terminal_cli.html) |
| **Retro** | `y2k-frutiger-aero` | **Y2K / Frutiger Aero** | Glossy specular glassmorphism, aqua-to-lime gradients, Nunito 800 | Gradient `#00E5FF`→`#76FF03` | [y2k_frutiger_aero.html](file:///gallery/y2k_frutiger_aero.html) |
| **Futuristic** | `cyberpunk` | **Cyberpunk** | Obsidian dark mode, cyan HUD, Rajdhani 700 + Mono, 8px chamfers | `#050508`, `#00F5FF`, `#FF00A0` | [cyberpunk.html](file:///gallery/cyberpunk.html) |
| **Futuristic** | `space-age-optimism` | **Space Age Optimism** | Warm optical white, molded fiberglass pods (32px), NASA Mission Orange | `#FAFAF8`, `#FF5C00`, `#3A4B5C` | [space_age_optimism.html](file:///gallery/space_age_optimism.html) |
| **Futuristic** | `aurora-gradient` | **Aurora Gradient** | Soft atmospheric violet/pink/cyan gradients over dark base | `#0B0F1A`, `#8B5CF6`, `#06B6D4` | [aurora_gradient.html](file:///gallery/aurora_gradient.html) |
| **Organic** | `japanese-wabi-sabi` | **Japanese Wabi-Sabi** | Rice paper, charcoal ink wash, Mingei craft, Noto Serif JP 300 | `#FAF7F0`, `#2B2B28`, `#A07E6A` | [japanese_wabi_sabi.html](file:///gallery/japanese_wabi_sabi.html) |
| **Organic** | `organic-natural` | **Organic Natural** | Bone canvas, living earth pigments (clay, moss, sap), river-stone pods | `#F5F1E8`, `#4A5844`, `#8C533C` | [organic_natural.html](file:///gallery/organic_natural.html) |
| **Organic** | `digital-organic` | **Digital Organic** | Organic CSS blobs, natural gradients, technological typography | `#FAFAF8`, `#2D6A4F`, `#D4A373` | [digital_organic.html](file:///gallery/digital_organic.html) |
| **Experimental** | `neo-brutalism` | **Neo-Brutalism** | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | `#FFFDF5`, `#FFE600`, `#000000` | [neo_brutalism.html](file:///gallery/neo_brutalism.html) |
| **Experimental** | `web-brutalism` | **Web Brutalism** | Default browser box-model, pure raw HTML typography, unstyled blue links | `#FFFFFF`, `#0000EE`, `#551A8B` | [web_brutalism.html](file:///gallery/web_brutalism.html) |
| **Experimental** | `memphis-postmodern` | **Memphis Postmodern** | Polka dots, diagonal hatch patterns, geometric squiggles, Syne 800 | `#FFFFFF`, `#FFE600`, `#FF007F` | [memphis_postmodern.html](file:///gallery/memphis_postmodern.html) |
| **Experimental** | `maximalist-dopamine` | **Maximalist Dopamine** | Acid yellow, colliding candy neon hues, multi-color drop shadows | `#FFF500`, `#FF007F`, `#00E5FF` | [maximalist_dopamine.html](file:///gallery/maximalist_dopamine.html) |
| **Experimental** | `vaporwave` | **Vaporwave** | Sunset purple-pink gradients, wireframe horizons, retro aesthetic | `#120422`, `#FF71CE`, `#01CDFE` | [vaporwave.html](file:///gallery/vaporwave.html) |
| **Luxury** | `quiet-luxury` | **Quiet Luxury** | Warm alabaster, Cormorant Garamond 300, 0px radius, hairline dividers | `#FBFBF9`, `#1C1A17`, `#8A7258` | [quiet_luxury.html](file:///gallery/quiet_luxury.html) |
| **Luxury** | `high-fashion-editorial` | **High Fashion Editorial** | Stark runway broadsheet, stark all-caps, razor 0px lines, flash contrast | `#FFFFFF`, `#000000`, `#E50000` | [high_fashion_editorial.html](file:///gallery/high_fashion_editorial.html) |
| **Tactile** | `glassmorphism` | **Glassmorphism** | Frosted translucent panels, backdrop-blur, 1px rgba borders, layered depth | `#0A0A0F`, `rgba(255,255,255,0.08)`, `#7C3AED` | [glassmorphism.html](file:///gallery/glassmorphism.html) |
| **Tactile** | `neumorphism` | **Neumorphism** | Soft extruded UI, canvas-matched surfaces, dual soft shadow (light+dark) | `#E0E5EC`, shadow pair | [neumorphism.html](file:///gallery/neumorphism.html) |
| **Tactile** | `claymorphism` | **Claymorphism** | 3D pastel clay, heavy rounding (20–32px), soft inner shadows, pastel fills | `#FFFBF5`, `#FFB5A7`, `#C8E6FF` | [claymorphism.html](file:///gallery/claymorphism.html) |
| **Utility** | `data-native` | **Data-Native** | Dense tables, JetBrains Mono numerics, 11px labels, restrained chroma | `#0D1117`, `#3B82F6`, `#22C55E` | [data_native.html](file:///gallery/data_native.html) |
| **Utility** | `command-center` | **Command Center** | Multi-panel layouts, red/amber/green status indicators, compact Inter | `#0B0D11`, `#EF4444`, `#22C55E` | [command_center.html](file:///gallery/command_center.html) |

---

## Modifiers Architecture (`styles/modifiers.yaml`)

Rather than multiplying the foundation taxonomy into combinations, orthogonal visual treatments are composed as **Modifiers**. Six independent dimensions:

- **Surface:** `frosted-glass` (translucent blur), `subtle-grain` (film grain overlay), `crt-scanlines` (phosphor scanlines), `fine-paper` (tactile fibrous texture), `chrome-specular` (metallic border shimmer).
- **Imagery:** `editorial`, `technical`, `photographic`, `collage`, `pixel`, `hand-drawn`.
- **Typography:** `monospace-accent`, `display-serif`, `condensed`, `handwritten`.
- **Motion:** `micro-snappy` (120ms), `fluid-spring` (350ms organic), `inert` (0ms zero-motion).
- **Density:** `ultra-dense` → `dense` → `balanced` → `spacious` → `ultra-spacious`. Controls spacing scale, information-per-viewport, and interactive control sizing.
- **Layout:** `bento-grid` — masonry-style irregular card grid (composition-only, no color/radius/shadow rules; inherits from active foundation).

---

## Anti-Pattern References

**Corporate Memphis / Alegria** is documented as a named anti-pattern in `styles/reference-anti-patterns.md` as a human-reference guide. The audit engine detects drift in code using signal accumulation across hardcoded heuristics (generic purple, bubbly containers, ambient shadows, blob decoration, illustration placeholders). Two signals = WARNING; three or more = CRITICAL.

---

## Domain-Style Defaults (`styles/domain-style-defaults.yaml`)

Maps 20+ product domains (fintech, healthcare, legal, government, edtech, devops, e-commerce, real estate, hospitality, AI products, biotech, creative tools, media, social, analytics) to 2–3 recommended foundation-style IDs. Used by the diagnostic interview's candidate shortlisting logic. Not a list of new foundation styles.

---

## Quick Start

### 1. In AI Coding Agents (Cursor, Claude Code, Antigravity)
Invoke the director skill in chat:
```text
@design-director
```
Or with specific intent:
```text
@design-director Analyze my PRD.md and recommend a visual direction.
```

The agent will:
1. Scan your project files.
2. Ask up to 3 diagnostic questions if context is sparse.
3. Recommend 2–3 directions with in-chat swatches and clickable local links to `gallery/*.html`.
4. Apply any critique ("more like Linear", "warmer tones").
5. Output `DESIGN_CONTRACT.md`.

### 2. Post-Implementation Audit
After code generation, verify that the contract was followed:
```bash
python3 skills/design-audit/audit_code.py quiet-luxury ./src
```
Or check a specific file:
```bash
python3 skills/design-audit/audit_code.py swiss-editorial ./index.html
```

---

## Testing & Quality Assurance

All tests run in CI:
```bash
# Run unit tests (brief extraction, contract generation, reference mapping)
npm run test:unit

# Run pipeline integration tests on unseen PRDs (and audit all 27 gallery previews)
npm run test:e2e:pipeline

# Run browser DOM computed style audit (Playwright)
npm run test:e2e:browser
```
