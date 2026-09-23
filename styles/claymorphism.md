---
name: style-claymorphism
description: Implementation rules for Claymorphism style. Warm cream #FFFBF5 canvas with 3D pastel clay-like elements, heavy border-radius (20px–32px), layered soft outer drop + inner highlight shadows. Domain — consumer mobile apps, wellness products, children's interfaces, playful B2C tools.
---

# Style Pack: Claymorphism

A joyful, tactile visual system that makes every UI element look like it was sculpted from soft, colorful clay. Elements appear to be three-dimensional objects sitting on a warm canvas — they have volume, roundness, and a satisfying chunky weight. Depth is achieved through the combination of a soft external drop shadow and an internal specular highlight that simulates light reflecting off a curved clay surface. Nothing is flat, nothing is sharp, and nothing is dark.

## Core Principles

1. **Extreme Rounding:** `border-radius: 20px`–`32px` on cards and panels. `border-radius: 50%` on circular elements. `border-radius: 24px` minimum on buttons. No sharp edge is ever acceptable — the rounded silhouette is the clay metaphor.
2. **Pastel Element Fills:** Each card or element uses a distinct soft pastel fill — coral `#FFB5A7`, sky `#C8E6FF`, mint `#B8F0D8`, lemon `#FFF3B0`, lavender `#E2D9F3`, peach `#FFD9B5`. Fills are the personality; never grey, never neutral, never dark.
3. **Layered Clay Shadow:** The clay depth effect requires two shadow layers stacked: an outer ambient drop shadow (`0 8px 24px rgba(0,0,0,0.12)`) for ground clearance, and an inner highlight (`inset 0 2px 6px rgba(255,255,255,0.80)`) for the top-surface light catch. Both are always present together.
4. **Warm Cream Canvas:** Background `#FFFBF5` (warm cream) or `#FFF8F0` (peach cream). Never white, never grey, never dark. The warmth of the canvas is what makes the pastels glow.
5. **Round Typography:** Nunito, Poppins, or DM Sans — fonts with rounded letterforms that match the visual tone. Never geometric grotesques, never serifs, never monospace as primary. Font weights: 600–700 for values and headings, 500 for labels, 400 for body.
6. **Friendly Color Scale:** Text is always warm and readable — primary `#2D1F0E` (warm near-black), secondary `#7A5E48` (warm medium brown), muted `#B09880` (warm gray-brown). Never cold grey text on warm backgrounds.
7. **No Darkness, No Sharpness:** Dark backgrounds, dark fills, dark borders — all forbidden. The design system lives entirely in a light, airy, candy-colored world.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use `border-radius: 0px` or anything below `16px` — sharp corners destroy the clay illusion.
- **NEVER** use dark backgrounds, dark card fills, or dark overlays of any kind.
- **NEVER** use flat single-layer shadows — the paired outer-drop + inner-highlight is mandatory for clay depth.
- **NEVER** use desaturated, grey, or neutral card fills — pastels only, always warm or cheerful.
- **NEVER** use Inter, Roboto, or other cold geometric sans-serifs as the primary typeface — use rounded fonts.
- **NEVER** use neon or electric accent colors — clay palette is always soft and approachable, never harsh.
- **NEVER** use hairline 1px borders in dark colors — any border must be subtle: `1px solid rgba(0,0,0,0.06)` maximum.
- **NEVER** use tabular/monospace figures for primary value display — round letterforms throughout.

---

## Claymorphism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas */
  --color-bg: #FFFBF5;
  --color-bg-alt: #FFF8F0;

  /* Pastel Element Fills */
  --color-clay-coral: #FFB5A7;
  --color-clay-sky: #C8E6FF;
  --color-clay-mint: #B8F0D8;
  --color-clay-lemon: #FFF3B0;
  --color-clay-lavender: #E2D9F3;
  --color-clay-peach: #FFD9B5;

  /* Inner highlight surface tints */
  --color-clay-coral-light: #FFCFC5;
  --color-clay-sky-light: #DFF0FF;
  --color-clay-mint-light: #D4F7E8;

  /* Typography — warm brown scale */
  --color-text-primary: #2D1F0E;
  --color-text-secondary: #7A5E48;
  --color-text-muted: #B09880;
  --color-text-inverse: #FFFBF5;

  /* Accent — warm rose (interactive) */
  --color-accent: #FF6B6B;
  --color-accent-hover: #FF5252;
  --color-accent-subtle: rgba(255, 107, 107, 0.12);

  /* Supporting accent — teal (secondary interactive) */
  --color-teal: #4ECDC4;
  --color-teal-subtle: rgba(78, 205, 196, 0.15);

  /* State */
  --color-positive: #52B788;
  --color-negative: #E07A5F;
}
```

## Border Radius Tokens

```css
:root {
  --radius-sm: 16px;     /* Minimum — badges, small chips */
  --radius-md: 20px;     /* Buttons, inputs */
  --radius-lg: 24px;     /* Standard clay card */
  --radius-xl: 32px;     /* Large panels, hero sections */
  --radius-full: 9999px; /* Circular elements, toggles, dots */
}
```

## Shadow & Elevation Tokens

```css
:root {
  /* Standard clay depth — outer drop + inner highlight */
  --shadow-clay-sm: 0 4px 12px rgba(0, 0, 0, 0.10), inset 0 1px 4px rgba(255, 255, 255, 0.75);
  --shadow-clay-md: 0 8px 24px rgba(0, 0, 0, 0.12), inset 0 2px 6px rgba(255, 255, 255, 0.80);
  --shadow-clay-lg: 0 14px 36px rgba(0, 0, 0, 0.14), inset 0 3px 8px rgba(255, 255, 255, 0.85);

  /* Pressed / active state — flatten + deepen inset */
  --shadow-clay-pressed: 0 2px 8px rgba(0, 0, 0, 0.10), inset 0 4px 10px rgba(0, 0, 0, 0.08);

  /* Hover / lifted — more elevation */
  --shadow-clay-hover: 0 16px 40px rgba(0, 0, 0, 0.16), inset 0 2px 6px rgba(255, 255, 255, 0.80);
}
```

## Spacing & Grid Tokens

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --grid-baseline: 8px;
  --grid-gap: 20px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '24px',
        sm: '16px',
        md: '20px',
        lg: '24px',
        xl: '32px',
      },
      boxShadow: {
        clay: '0 8px 24px rgba(0,0,0,0.12), inset 0 2px 6px rgba(255,255,255,0.80)',
        'clay-sm': '0 4px 12px rgba(0,0,0,0.10), inset 0 1px 4px rgba(255,255,255,0.75)',
        'clay-lg': '0 14px 36px rgba(0,0,0,0.14), inset 0 3px 8px rgba(255,255,255,0.85)',
        'clay-hover': '0 16px 40px rgba(0,0,0,0.16), inset 0 2px 6px rgba(255,255,255,0.80)',
        'clay-pressed': '0 2px 8px rgba(0,0,0,0.10), inset 0 4px 10px rgba(0,0,0,0.08)',
      },
      colors: {
        canvas: '#FFFBF5',
        clay: {
          coral: '#FFB5A7',
          sky: '#C8E6FF',
          mint: '#B8F0D8',
          lemon: '#FFF3B0',
          lavender: '#E2D9F3',
          peach: '#FFD9B5',
        },
        ink: {
          primary: '#2D1F0E',
          secondary: '#7A5E48',
          muted: '#B09880',
        },
        accent: {
          DEFAULT: '#FF6B6B',
          hover: '#FF5252',
          subtle: 'rgba(255,107,107,0.12)',
        },
      },
      fontFamily: {
        sans: ['Nunito', 'Poppins', 'DM Sans', 'sans-serif'],
        display: ['Poppins', 'Nunito', 'sans-serif'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons (Primary):** Height 44px, `border-radius: 20px`, `background: #FF6B6B`, `border: none`, `box-shadow: var(--shadow-clay-md)`, `color: #FFFBF5`, `font-weight: 700`, `font-family: Nunito`. Hover: `box-shadow: var(--shadow-clay-hover)`, translateY(-1px). Active: `box-shadow: var(--shadow-clay-pressed)`, translateY(1px).
- **Buttons (Secondary):** Same geometry, `background: #FFFBF5` (canvas color), `border: 1px solid rgba(0,0,0,0.06)`, `color: var(--color-text-primary)`, `box-shadow: var(--shadow-clay-sm)`.
- **Cards (Clay Panel):** `background: <pastel fill>`, `border-radius: 24px`, `border: 1px solid rgba(0,0,0,0.04)`, `box-shadow: var(--shadow-clay-md)`, padding `24px`. Each card should use a distinct pastel from the clay palette.
- **Nav:** `background: #FFFBF5`, `border-radius: 0`, `box-shadow: 0 4px 20px rgba(0,0,0,0.06), inset 0 -1px 0 rgba(0,0,0,0.04)`, height `64px`, padding `0 32px`. Nav brand uses a warm accent color.
- **Inputs:** Height 44px, `border-radius: 20px`, `background: #FFFBF5`, `border: 1px solid rgba(0,0,0,0.06)`, `box-shadow: inset 0 2px 6px rgba(0,0,0,0.06)`, `color: var(--color-text-primary)`, `font-family: Nunito`. Focus: `outline: 3px solid rgba(255,107,107,0.30); outline-offset: 1px`.
- **Tables:** Contained within a clay card panel. Hairline row divider `border-bottom: 1px solid rgba(0,0,0,0.05)`. Row height 48px. Header `font-weight: 700`, `color: var(--color-text-secondary)`, `text-transform: uppercase`, `font-size: 11px`.
- **Badges:** `border-radius: 9999px`, `padding: 4px 12px`, pastel fill matching the nearest card color (slightly lighter), `border: 1px solid rgba(0,0,0,0.06)`, `box-shadow: var(--shadow-clay-sm)`, `font-size: 11px`, `font-weight: 700`, `font-family: Nunito`.
