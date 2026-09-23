# Design Director

A design reasoning engine that turns product context into implementation-ready visual direction for AI coding agents.

AI coding agents default to the statistical median of their training data — `Inter`, `rounded-lg`, `shadow-sm`, `bg-blue-600`. Design Director inserts an intentional constraint layer: it reads your product context, recommends a visual direction with live previews, then hands a binding **`DESIGN_CONTRACT.md`** to the coding agent instead of a vague vibe. A second skill audits the generated code against the contract afterward.

Works with Claude Code, Cursor, Codex CLI, Gemini CLI / Antigravity, GitHub Copilot, VS Code, Zed — anything that reads `SKILL.md`.

---

## How It Works

```
PRD / README / Product Context
              │
              ▼
 [Skill 1: design-director]
 • Scans product context
 • Asks up to 3 questions if context is thin
 • Recommends 2–3 styles with gallery previews
 • User picks or refines ("more like Linear")
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

**Token budget:** `SKILL.md` is capped under 1,200 tokens. Only the single chosen style pack is loaded when generating a contract — the other 26 are never touched. `reference-library.json` (~10k tokens) loads only on explicit brand-refinement requests ("more like Stripe").

---

## Install

### Claude Code

```bash
# Personal — clone once, symlink the skills:
git clone https://github.com/Aditya-Dobhada/design-director.git ~/design-director
ln -s ~/design-director/skills/design-director ~/.claude/skills/design-director
ln -s ~/design-director/skills/design-audit   ~/.claude/skills/design-audit

# Per-project (committed to version control):
cp -r skills/design-director skills/design-audit <your-project>/.claude/skills/
```

Invoke with `@design-director` or describe the task. Run audits with `python3 skills/design-audit/audit_code.py …`.

### Cursor / Codex CLI / GitHub Copilot

Copy the skill folders to the agent's skill root the same way. GitHub Copilot supports `.github/skills/` since Dec 2025.

### Antigravity (Gemini CLI)

```bash
git clone https://github.com/Aditya-Dobhada/design-director.git ~/design-director
ln -s ~/design-director/skills/design-director ~/.gemini/config/skills/design-director
ln -s ~/design-director/skills/design-audit   ~/.gemini/config/skills/design-audit
```

### Requirements

Python 3.10+ (standard library only — zero pip dependencies for both `director_engine.py` and `audit_code.py`).

---

## Usage

```text
@design-director

@design-director Analyze my PRD.md and recommend a visual direction.
```

The agent will:
1. Scan your project files (`README.md`, `PRD.md`, `package.json`, etc.).
2. Ask up to 3 diagnostic questions if context is thin.
3. Recommend 2–3 directions — inline SVG swatch strip, font, palette tokens, radius rule, and a relative link to the gallery preview.
4. Apply refinements ("more like Linear", "warmer tones").
5. Write `DESIGN_CONTRACT.md` to your project root.

After code is generated:

```bash
python3 skills/design-audit/audit_code.py quiet-luxury ./src
python3 skills/design-audit/audit_code.py swiss-editorial ./index.html
python3 skills/design-audit/audit_code.py dark-minimal ./src --modifiers frosted-glass,subtle-grain
```

Unknown style IDs are rejected with exit code 2 — a typo can never silently pass an audit.

---

## Style Gallery (27 Foundations)

Live HTML previews are in [`skills/design-director/gallery/`](skills/design-director/gallery/).

| Family | Style ID | Visual Signature | Gallery |
|---|---|---|---|
| **Modern** | `minimal-modern` | High whitespace, neutral slate, 4–8px radius, Inter | [preview](skills/design-director/gallery/minimal_modern.html) |
| **Modern** | `dark-minimal` | Obsidian dark canvas, hairline borders, muted slate | [preview](skills/design-director/gallery/dark_minimal.html) |
| **Modern** | `swiss-editorial` | Pure white, Playfair Display 600, Swiss red, asymmetric grid | [preview](skills/design-director/gallery/swiss_editorial.html) |
| **Historical** | `bauhaus` | Constructivist 8px grid, primary triad, IBM Plex Sans 700 | [preview](skills/design-director/gallery/bauhaus.html) |
| **Historical** | `art-deco` | Obsidian & gold, stepped geometry, hairpin borders, 0px radius | [preview](skills/design-director/gallery/art_deco.html) |
| **Historical** | `mid-century-modern` | Warm olive & mustard, teak brown, organic curved pods (16px) | [preview](skills/design-director/gallery/mid_century_modern.html) |
| **Retro** | `retro-americana` | Cream parchment, vermilion, Saul Bass geometry, slab type | [preview](skills/design-director/gallery/retro_americana.html) |
| **Retro** | `terminal-cli` | Fixed-pitch amber/green phosphor, 0px radius, character-cell borders | [preview](skills/design-director/gallery/terminal_cli.html) |
| **Retro** | `y2k-frutiger-aero` | Glossy specular glassmorphism, aqua-to-lime gradients, Nunito 800 | [preview](skills/design-director/gallery/y2k_frutiger_aero.html) |
| **Futuristic** | `cyberpunk` | Obsidian dark, cyan HUD, Rajdhani 700, chamfers | [preview](skills/design-director/gallery/cyberpunk.html) |
| **Futuristic** | `space-age-optimism` | Warm optical white, molded pods (32px), NASA orange | [preview](skills/design-director/gallery/space_age_optimism.html) |
| **Futuristic** | `aurora-gradient` | Soft atmospheric violet/pink/cyan gradients over dark base | [preview](skills/design-director/gallery/aurora_gradient.html) |
| **Organic** | `japanese-wabi-sabi` | Rice paper, charcoal ink wash, Noto Serif JP 300 | [preview](skills/design-director/gallery/japanese_wabi_sabi.html) |
| **Organic** | `organic-natural` | Bone canvas, earth pigments (clay, moss, sap), river-stone pods | [preview](skills/design-director/gallery/organic_natural.html) |
| **Organic** | `digital-organic` | Organic CSS blobs, natural gradients, technological typography | [preview](skills/design-director/gallery/digital_organic.html) |
| **Experimental** | `neo-brutalism` | 3px solid ink borders, 4px solid black offset shadows, Space Grotesk | [preview](skills/design-director/gallery/neo_brutalism.html) |
| **Experimental** | `web-brutalism` | Default browser box-model, raw HTML typography, unstyled blue links | [preview](skills/design-director/gallery/web_brutalism.html) |
| **Experimental** | `memphis-postmodern` | Polka dots, diagonal hatch patterns, geometric squiggles, Syne 800 | [preview](skills/design-director/gallery/memphis_postmodern.html) |
| **Experimental** | `maximalist-dopamine` | Acid yellow, colliding candy neons, multi-color drop shadows | [preview](skills/design-director/gallery/maximalist_dopamine.html) |
| **Experimental** | `vaporwave` | Sunset purple-pink gradients, wireframe horizons | [preview](skills/design-director/gallery/vaporwave.html) |
| **Luxury** | `quiet-luxury` | Alabaster, Cormorant Garamond 300, 0px radius, hairline dividers | [preview](skills/design-director/gallery/quiet_luxury.html) |
| **Luxury** | `high-fashion-editorial` | Stark runway broadsheet, all-caps, razor 0px lines, flash contrast | [preview](skills/design-director/gallery/high_fashion_editorial.html) |
| **Tactile** | `glassmorphism` | Frosted translucent panels, backdrop-blur, 1px rgba borders | [preview](skills/design-director/gallery/glassmorphism.html) |
| **Tactile** | `neumorphism` | Soft extruded UI, canvas-matched surfaces, dual soft shadows | [preview](skills/design-director/gallery/neumorphism.html) |
| **Tactile** | `claymorphism` | 3D pastel clay, heavy rounding (20–32px), soft inner shadows | [preview](skills/design-director/gallery/claymorphism.html) |
| **Utility** | `data-native` | Dense tables, JetBrains Mono numerics, 11px labels, restrained chroma | [preview](skills/design-director/gallery/data_native.html) |
| **Utility** | `command-center` | Multi-panel layouts, red/amber/green status indicators, compact Inter | [preview](skills/design-director/gallery/command_center.html) |

---

## Modifiers

Six orthogonal dimensions that compose on top of any foundation:

- **Surface:** `frosted-glass`, `subtle-grain`, `crt-scanlines`, `fine-paper`, `chrome-specular`
- **Imagery:** `editorial`, `technical`, `photographic`, `collage`, `pixel`, `hand-drawn`
- **Typography:** `monospace-accent`, `display-serif`, `condensed`, `handwritten`
- **Motion:** `micro-snappy` (120ms), `fluid-spring` (350ms), `inert` (0ms)
- **Density:** `ultra-dense` → `dense` → `balanced` → `spacious` → `ultra-spacious`
- **Layout:** `bento-grid` (masonry-style irregular card grid; no color/radius/shadow rules, inherits from foundation)

Full modifier specs: [`skills/design-director/styles/modifiers.json`](skills/design-director/styles/modifiers.json).

---

## Running Tests

```bash
# Unit tests (brief extraction, contract generation, routing, audit regressions)
npm run test:unit

# Pipeline e2e tests (unseen PRDs + gallery audits)
npm run test:e2e:pipeline

# Browser DOM computed-style audit (requires Playwright + Chromium)
npx playwright install --with-deps chromium
npm run test:e2e:browser
```

76 tests, all deterministic. CI runs on every push via `.github/workflows/ci.yml`.

---

## License

[MIT](LICENSE) © 2026 Aditya Dobhada.
