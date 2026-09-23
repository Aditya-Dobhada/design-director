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

Live HTML implementations for all 27 foundations are available in [`gallery/`](gallery/):

| Family | Style ID | Name | Visual Signature | Key Hex Values | Preview Reference |
|---|---|---|---|---|---|
| **Modern** | `minimal-modern` | **Minimal Modern** | High whitespace, neutral slate, 4–8px radius, Sohne/Inter | `#FFFFFF`, `#0F172A`, `#2563EB` | [minimal_modern.html](gallery/minimal_modern.html) |
| **Modern** | `dark-minimal` | **Dark Minimal** | Obsidian dark canvas, hairline borders, muted slate, Inter | `#08090A`, `#111215`, `#5E6AD2` | [dark_minimal.html](gallery/dark_minimal.html) |
| **Modern** | `swiss-editorial` | **Swiss / Editorial** | Pure white, Playfair Display 600, Swiss red, asymmetric 4+8 grid | `#FFFFFF`, `#111111`, `#E30613` | [swiss_editorial.html](gallery/swiss_editorial.html) |
| **Historical** | `bauhaus` | **Bauhaus** | Constructivist 8px grid, primary triad accents, IBM Plex Sans 700 lc | `#FFFFFF`, `#E03A3E`, `#004B97` | [bauhaus.html](gallery/bauhaus.html) |
| **Historical** | `art-deco` | **Art Deco** | Obsidian & rich gold, stepped geometry, hairpin borders, 0px radius | `#0D0D11`, `#D4AF37`, `#F3E5AB` | [art_deco.html](gallery/art_deco.html) |
| **Historical** | `mid-century-modern` | **Mid-Century Modern** | Warm olive & mustard, teak brown, organic curved pods (16px) | `#FDFBF7`, `#5B7053`, `#D4973B` | [mid_century_modern.html](gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | **Retro Americana** | Cream parchment, vermilion, Saul Bass geometry, Alfa Slab One | `#F9F0DC`, `#C8391E`, `#E8A126` | [retro_americana.html](gallery/retro_americana.html) |
| **Retro** | `terminal-cli` | **Terminal / CLI** | Fixed pitch amber/green phosphor, 0px radius, character cell borders | `#000000`, `#00FF66`, `#FFB000` | [terminal_cli.html](gallery/terminal_cli.html) |
| **Retro** | `y2k-frutiger-aero` | **Y2K / Frutiger Aero** | Glossy specular glassmorphism, aqua-to-lime gradients, Nunito 800 | Gradient `#00E5FF`→`#76FF03` | [y2k_frutiger_aero.html](gallery/y2k_frutiger_aero.html) |
| **Futuristic** | `cyberpunk` | **Cyberpunk** | Obsidian dark mode, cyan HUD, Rajdhani 700 + Mono, 8px chamfers | `#050508`, `#00F5FF`, `#FF00A0` | [cyberpunk.html](gallery/cyberpunk.html) |
| **Futuristic** | `space-age-optimism` | **Space Age Optimism** | Warm optical white, molded fiberglass pods (32px), NASA Mission Orange | `#FAFAF8`, `#FF5C00`, `#3A4B5C` | [space_age_optimism.html](gallery/space_age_optimism.html) |
| **Futuristic** | `aurora-gradient` | **Aurora Gradient** | Soft atmospheric violet/pink/cyan gradients over dark base | `#0B0F1A`, `#8B5CF6`, `#06B6D4` | [aurora_gradient.html](gallery/aurora_gradient.html) |
| **Organic** | `japanese-wabi-sabi` | **Japanese Wabi-Sabi** | Rice paper, charcoal ink wash, Mingei craft, Noto Serif JP 300 | `#FAF7F0`, `#2B2B28`, `#A07E6A` | [japanese_wabi_sabi.html](gallery/japanese_wabi_sabi.html) |
| **Organic** | `organic-natural` | **Organic Natural** | Bone canvas, living earth pigments (clay, moss, sap), river-stone pods | `#F5F1E8`, `#4A5844`, `#8C533C` | [organic_natural.html](gallery/organic_natural.html) |
| **Organic** | `digital-organic` | **Digital Organic** | Organic CSS blobs, natural gradients, technological typography | `#FAFAF8`, `#2D6A4F`, `#D4A373` | [digital_organic.html](gallery/digital_organic.html) |
| **Experimental** | `neo-brutalism` | **Neo-Brutalism** | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | `#FFFDF5`, `#FFE600`, `#000000` | [neo_brutalism.html](gallery/neo_brutalism.html) |
| **Experimental** | `web-brutalism` | **Web Brutalism** | Default browser box-model, pure raw HTML typography, unstyled blue links | `#FFFFFF`, `#0000EE`, `#551A8B` | [web_brutalism.html](gallery/web_brutalism.html) |
| **Experimental** | `memphis-postmodern` | **Memphis Postmodern** | Polka dots, diagonal hatch patterns, geometric squiggles, Syne 800 | `#FFFFFF`, `#FFE600`, `#FF007F` | [memphis_postmodern.html](gallery/memphis_postmodern.html) |
| **Experimental** | `maximalist-dopamine` | **Maximalist Dopamine** | Acid yellow, colliding candy neon hues, multi-color drop shadows | `#FFF500`, `#FF007F`, `#00E5FF` | [maximalist_dopamine.html](gallery/maximalist_dopamine.html) |
| **Experimental** | `vaporwave` | **Vaporwave** | Sunset purple-pink gradients, wireframe horizons, retro aesthetic | `#120422`, `#FF71CE`, `#01CDFE` | [vaporwave.html](gallery/vaporwave.html) |
| **Luxury** | `quiet-luxury` | **Quiet Luxury** | Warm alabaster, Cormorant Garamond 300, 0px radius, hairline dividers | `#FBFBF9`, `#1C1A17`, `#8A7258` | [quiet_luxury.html](gallery/quiet_luxury.html) |
| **Luxury** | `high-fashion-editorial` | **High Fashion Editorial** | Stark runway broadsheet, stark all-caps, razor 0px lines, flash contrast | `#FFFFFF`, `#000000`, `#E50000` | [high_fashion_editorial.html](gallery/high_fashion_editorial.html) |
| **Tactile** | `glassmorphism` | **Glassmorphism** | Frosted translucent panels, backdrop-blur, 1px rgba borders, layered depth | `#0A0A0F`, `rgba(255,255,255,0.08)`, `#7C3AED` | [glassmorphism.html](gallery/glassmorphism.html) |
| **Tactile** | `neumorphism` | **Neumorphism** | Soft extruded UI, canvas-matched surfaces, dual soft shadow (light+dark) | `#E0E5EC`, shadow pair | [neumorphism.html](gallery/neumorphism.html) |
| **Tactile** | `claymorphism` | **Claymorphism** | 3D pastel clay, heavy rounding (20–32px), soft inner shadows, pastel fills | `#FFFBF5`, `#FFB5A7`, `#C8E6FF` | [claymorphism.html](gallery/claymorphism.html) |
| **Utility** | `data-native` | **Data-Native** | Dense tables, JetBrains Mono numerics, 11px labels, restrained chroma | `#0D1117`, `#3B82F6`, `#22C55E` | [data_native.html](gallery/data_native.html) |
| **Utility** | `command-center` | **Command Center** | Multi-panel layouts, red/amber/green status indicators, compact Inter | `#0B0D11`, `#EF4444`, `#22C55E` | [command_center.html](gallery/command_center.html) |

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

## Install & Publish

Both skills follow the open [Agent Skills](https://agentskills.io/specification) format (`SKILL.md` + supporting files), so they work across Claude Code, Cursor, Codex CLI, GitHub Copilot, Gemini CLI, VS Code, Zed, and any agent that reads `SKILL.md`.

> **Packaging note:** `design-audit` is fully self-contained. `design-director` additionally reads `styles/` and links `gallery/` from the repo root — when installing into an agent, keep those directories reachable (clone the repo, or install from the repo root so the skill and its supporting folders travel together).

### Use in Claude Code
```bash
# Personal (all projects) — clone once, symlink the skills:
git clone https://github.com/Aditya-Dobhada/design-director.git ~/design-director
ln -s ~/design-director/skills/design-director ~/.claude/skills/design-director
ln -s ~/design-director/skills/design-audit   ~/.claude/skills/design-audit

# Or per-project (team, committed to version control):
cp -r skills/design-director skills/design-audit <your-project>/.claude/skills/
```
Invoke with `/design-director`, `@design-director`, or just describe the task — the skill's `description` triggers it automatically. Run audits with `python3 skills/design-audit/audit_code.py …` (requires Python 3.10+; `pip install -r requirements.txt` for the director engine's YAML parsing).

### Publish / distribute via skills.sh (Vercel open skills ecosystem)
There is no submission flow — a public GitHub repo containing `skills/<name>/SKILL.md` **is** published. Anyone installs with:
```bash
npx skills add Aditya-Dobhada/design-director                    # both skills
npx skills add Aditya-Dobhada/design-director --skill design-audit  # one skill
```
Installs are telemetry-reported, and the skill then appears/climbs on the [skills.sh](https://skills.sh) leaderboard automatically. Naming conventions (directory name = frontmatter `name`, lowercase-hyphen) are already satisfied.

### Publish as a Claude Code / Copilot plugin marketplace
Add a `.claude-plugin/marketplace.json` (and `.github/plugin.json` for Copilot CLI/VS Code) to this repo; users then run `/plugin marketplace add Aditya-Dobhada/design-director` and `/plugin install design-director@…`. This route lets you bundle `styles/` + `gallery/` with the plugin.

### Other discovery channels
- **GitHub Copilot**: copy the skill folders to `.github/skills/` in any repo (supported since Dec 2025).
- **SkillsMP / LobeHub**: crawlers index any public GitHub repo containing `SKILL.md` files — nothing to do beyond publishing the repo.
- **anthropics/skills**: Anthropic's official skills repo accepts community PRs for high-visibility distribution.

Before announcing widely: add a `LICENSE` at the repo root (required by most directories), and keep CI green (`.github/workflows/ci.yml`).

---

## Testing & Quality Assurance

All tests run in CI (`.github/workflows/ci.yml`):
```bash
# Install python deps once (PyYAML for the director engine; audit_code.py is stdlib-only)
pip install -r requirements.txt

# Run unit tests (brief extraction, contract generation, reference mapping, audit regressions)
npm run test:unit

# Run pipeline integration tests on unseen PRDs (and audit all 27 gallery previews)
npm run test:e2e:pipeline

# Run browser DOM computed style audit (Playwright)
npm run test:e2e:browser
```
