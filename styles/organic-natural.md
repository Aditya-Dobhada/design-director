---
name: style-organic-natural
description: Implementation rules for Organic Natural style. Biophilic design philosophy, botanical illustration aesthetic, seed-pod and mycelium-network geometry, clay/moss/sap/bark earth palette, hand-drawn SVG mark accents, and fluid unhurried motion that breathes.
---

# Style Pack: Organic Natural

A design philosophy grounded in the biophilic turn in contemporary design — organizations like Patagonia, Aesop, and Le Labo applied to digital interfaces. Surfaces feel like handmade paper, glazed ceramic, and pressed botanical specimens. The geometry is imperfect, alive, and continuous rather than mechanical and gridded.

## Core Principles

1. **Color:** Earth palette: clay `#C4714F`, moss `#5C7A4E`, sap green `#3D5C2E`, bone white `#F5F0E8`, warm linen `#EDE6D6`, deep charcoal `#2A2622`. No bright saturated hues. Never neon. Palette max 4 colors per composition.
2. **Geometry:** `border-radius: 16px–32px` (river-stone curves) on cards. `border-radius: 48px–9999px` on pills and tags. Organic blob shapes as background SVG fills. No sharp corners on primary content containers.
3. **Typography:** `font-family: 'Lora', 'Fraunces', 'Libre Baskerville', serif` for headings at weight 400–600. Body: `font-family: 'DM Sans', 'Plus Jakarta Sans', sans-serif` at weight 300–400. Slightly warm `line-height: 1.7–1.8`.
4. **Surfaces:** Off-white linen cards `#EDE6D6` with `box-shadow: 0 2px 12px rgba(42,38,34,0.08)` (soft, warm-tinted shadow). No cold blue-gray shadows. Card borders: none or `1px solid rgba(196,113,79,0.2)` (clay-translucent).
5. **Motion:** `cubic-bezier(0.34, 1.56, 0.64, 1)` (gentle organic spring) at 350–450ms. Hover: warm shadow lift `box-shadow: 0 8px 32px rgba(42,38,34,0.16)`. No linear/mechanical easing. No hard clicks.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use neon or electric colors. Every pigment must be traceable to a natural material (clay, bark, leaf, sap, stone, mineral).
- **NEVER** use sharp 0px rectangular containers for primary content surfaces. Use organic blob clip-paths, large radii (24px–60px), or continuous flowing shapes.
- **NEVER** use mechanical, grid-locked symmetrical layouts. Content should feel grown, not engineered.
- **NEVER** use heavy drop shadows or offset box shadows. Depth is expressed through layered paper tones or subtle material casting shadow (2-4px warm, very-low-opacity).
- **NEVER** use geometric grotesks (Inter, Neue Haas, Helvetica). Typography must be humanist, literary, or handwritten-adjacent.
- **NEVER** use fast, snappy animations. Motion is slow, breathing, and tidal.
- **NEVER** use cold whites (`#FFFFFF`). Warm bone white (`#F5F1E8`) or raw linen are required.

---

## Organic Natural — Design Tokens

## Color Tokens

```css
:root {
  /* Earth Canvas */
  --color-bone-white: #F5F1E8;       /* Primary background */
  --color-raw-linen: #EDE8DA;        /* Panel surface */
  --color-aged-paper: #E0D9C8;       /* Subtle surface depth */

  /* Earth & Plant Pigments */
  --color-charcoal: #2A2824;         /* Primary text */
  --color-bark: #5C5248;             /* Secondary text */
  --color-stone-muted: #8A7E74;      /* Muted / meta text */
  --color-clay: #C4956A;             /* Clay accent warm */
  --color-terracotta: #AA6244;       /* Deeper warm accent */
  --color-moss: #5D7A52;             /* Forest moss green */
  --color-sap-green: #3E5C3A;        /* Deep forest sap */
  --color-bark-gray: #7A7068;        /* Natural bark gray */
  --color-sand: #C9A87C;             /* River sand */
}
```

## Border & Organic Shape Tokens

```css
:root {
  /* Radii — organic rounding */
  --radius-stone: 24px;     /* River-stone rounding */
  --radius-pod: 40px;       /* Seed pod container */
  --radius-blob: 60% 40% 55% 45% / 50% 55% 45% 50%; /* CSS organic blob */

  /* Borders */
  --border-organic: 1px solid rgba(42, 40, 36, 0.15);
  --border-organic-visible: 1.5px solid rgba(42, 40, 36, 0.35);
}
```

## Shadow Tokens

```css
:root {
  /* Warm casting shadow — very subtle */
  --shadow-material-sm: 0 2px 8px rgba(42, 40, 36, 0.08);
  --shadow-material-md: 0 4px 20px rgba(42, 40, 36, 0.10);
  /* Hard offset or blurry purple/blue shadows: FORBIDDEN */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '24px', sm: '12px', md: '24px',
        lg: '40px', xl: '60px', full: '9999px',
        none: '0px',
      },
      boxShadow: {
        DEFAULT: '0 4px 20px rgba(42, 40, 36, 0.10)',
        material: '0 2px 8px rgba(42, 40, 36, 0.08)',
        none: '0 0 #0000',
      },
      colors: {
        organic: {
          bone: '#F5F1E8', linen: '#EDE8DA', paper: '#E0D9C8',
          charcoal: '#2A2824', clay: '#C4956A', moss: '#5D7A52',
          sap: '#3E5C3A', bark: '#7A7068', sand: '#C9A87C',
        }
      }
    }
  }
}
```

---

## Organic Natural — Typography

## Recommended Font Stacks

### Primary Humanist Serif (feels like pressed botanical printing)
- `Source Serif 4` (300/400/600 — warm, breathing)
- `Lora` (400/500/700)
- `Playfair Display` (400 — used lightly, never at 900)
- `EB Garamond` (400 — historic warmth)
- `Spectral` (300/400 — luminous literary)

### Secondary Humanist Sans (functional but warm)
- `Jost` (300/400/500)
- `Cabin` (400/500)
- `Nunito` (300/400 — rounded organic feel)
- `Tenor Sans`

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display** | 48px - 64px | 400 Serif or 300 Light Serif | -0.01em | 1.20 | Sentence case |
| **H1** | 34px - 42px | 400 Serif | -0.01em | 1.30 | Sentence case |
| **H2** | 24px - 30px | 400 Serif / 500 Sans | 0.00em | 1.40 | Sentence case |
| **H3** | 18px - 22px | 500 Sans or Serif | +0.01em | 1.50 | Sentence case |
| **Body** | 15px - 16px | 400 | +0.01em | 1.70 | Sentence case |
| **Caption / Note** | 12px - 13px | 400 Light | +0.03em | 1.60 | Sentence case |

## Rules

1. **Serif Headings + Humanist Sans Body:** Most Organic Natural projects pair the literary warmth of an oldstyle serif for headlines with a quiet humanist sans for interface labels.
2. **Generous Line-Height on Body:** 1.70–1.80 for body reading; this is a slow, contemplative reading environment.
3. **Warm Charcoal Text:** Always `#2A2824`, never harsh `#000000`.

## Anti-Patterns
- **Geometric grotesks** (`Neue Haas`, `Inter`, `Helvetica`): Too industrial and mechanical.
- **All-caps headings**: Agricultural — never authoritative industrial command.
- **Monospace type**: Wrong material register entirely.

---

## Organic Natural — Layout

## Composition Rules

1. **Blob-Shaped Feature Areas:** Hero sections and feature panels use CSS organic blob shapes (`border-radius: 60% 40% 55% 45% / 50% 55% 45% 50%`) or SVG organic outlines rather than rectangular blocks.
2. **River-Stone Card Grid:** Cards use 24px–40px border-radius and are deliberately unevenly sized — a mix of portrait and landscape cards mimicking a river-stone arrangement.
3. **Botanical Illustration Margins:** Botanical SVG illustrations (fine line drawings of leaves, root systems, seed cross-sections) float in the generous whitespace margins as ambient content.
4. **Tidal Horizontal Rhythms:** Content sections alternate between bone-white and raw-linen backgrounds, creating a gentle rhythmic tide between panels.

## Layout Anti-Patterns
- **Strict rectangular card grids** with equal gutters: Too engineered. Vary sizes.
- **Dense multi-column data tables**: Wrong context — use charts with organic SVG paths instead.
- **Floating action buttons**: Incompatible with the meditative reading pace.

---

## Organic Natural — Component Rules

## 1. Buttons

### Primary — River Stone Pill
- **Background:** Clay `#C4956A` or Forest Moss `#5D7A52`
- **Color:** Bone White `#F5F1E8`
- **Border:** none
- **Border Radius:** `9999px` (capsule pill) or `24px` (river stone)
- **Shadow:** `0 2px 8px rgba(42, 40, 36, 0.12)`
- **Font:** 14px Humanist Sans, weight 500, sentence case, tracking +0.02em
- **Padding:** 13px 30px
- **Hover:** Background deepens slightly (Moss → Sap Green `#3E5C3A`), subtle gentle lift `translateY(-1px)`
- **Active:** `translateY(1px)`, opacity 0.9

### Secondary — Linen Outline
- **Background:** Raw Linen `#EDE8DA`
- **Border:** `1.5px solid rgba(42, 40, 36, 0.25)`
- **Border Radius:** `9999px`
- **Color:** Charcoal `#2A2824`
- **Hover:** Border shifts to Clay `#C4956A`, color becomes Clay

## 2. Cards

- **Background:** Raw Linen `#EDE8DA` or Bone White `#F5F1E8`
- **Border:** `1px solid rgba(42, 40, 36, 0.10)`
- **Border Radius:** `28px` to `40px` (or organic blob)
- **Shadow:** `0 4px 20px rgba(42, 40, 36, 0.08)`
- **Padding:** 36px to 48px
- **Texture:** Subtle organic paper noise or warm tone gradient

## 3. Inputs

- **Border Radius:** `16px`
- **Border:** `1.5px solid rgba(42, 40, 36, 0.20)`
- **Background:** Bone White `#F5F1E8`
- **Color:** Charcoal `#2A2824`
- **Padding:** 14px 20px
- **Focus:** Border shifts to Forest Moss `#5D7A52`; `box-shadow: 0 0 0 3px rgba(93, 122, 82, 0.15)`

## 4. Badges & Organic Tags

- **Shape:** Pill (`rounded-full`) or irregular 16px capsule
- **Background:** Raw Linen `#EDE8DA` or tint of Moss/Clay
- **Color:** Forest Moss `#5D7A52` or Clay `#C4956A`
- **Border:** `1px solid rgba(42, 40, 36, 0.15)`
- **Font:** 12px Humanist Sans, weight 500, sentence case

---

## Organic Natural — Motion

## Philosophy

Motion is breathing, tidal, and fluid — mimicking natural phenomena like the swaying of grass, the growth of vines, or water flowing over river stones. No abrupt stops, no mechanical snaps.

## Tokens

```css
:root {
  --duration-organic-breath: 350ms;
  --duration-organic-tide: 550ms;
  --duration-organic-growth: 800ms;

  --ease-organic: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-organic-in-out: cubic-bezier(0.45, 0, 0.55, 1);
}
```

## Transitions

1. **Button hover:** 350ms gentle color shift, 1px lift.
2. **Page element reveals:** Gentle unfurl — opacity 0 -> 1, translateY(12px -> 0), 550ms smooth deceleration.
3. **Botanical illustration stroke draw:** 1200ms SVG stroke-dashoffset transition on first viewport entry.

## Anti-Patterns
- No sub-150ms snap cuts.
- No bouncy cartoon springs.
- No linear robotic movements.
