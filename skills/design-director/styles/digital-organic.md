---
name: style-digital-organic
description: Implementation rules for Digital Organic style. Organic blob shapes with natural gradient fills, warm #FAFAF8 canvas, humanist Bricolage Grotesque/DM Sans typography mixed with thin monospace for data. Domain: AI wellness, biotech, regenerative platforms.
---

# Style Pack: Digital Organic

A living, breathing visual system that fuses biological form language with precise digital typography. Organic blob shapes — achieved via multi-value CSS `border-radius` — carry natural gradient fills in sage, moss, amber, and gold palettes. The canvas breathes in warm near-white. Data reads through thin monospace; experience reads through humanist sans. The result: technology that feels grown, not manufactured.

## Core Principles

1. **Typography:** Primary UI: `Bricolage Grotesque` or `DM Sans`, weight 400 (body), 600 (headings), 700 (display). Data and metrics: `DM Mono` or `JetBrains Mono` at weight 300–400 — deliberately thin and quiet against the lush blob forms. Display headings: 32px–48px / weight 700. Body text: 14px–16px / weight 400. Tracking: `0em` on all sizes. Never mix more than two font families.
2. **Color:** Canvas warm near-white `#FAFAF8`. Deep forest dark mode: `#0D1A12`. Primary text light: `#1A2E1A`. Primary text dark: `#D4E8D0`. Earthy accent palette: forest green `#2D6A4F`, mint `#74C69D`, sage `#52B788`, sand `#D4A373`, gold `#E9C46A`. All surfaces carry subtle warm tint — never pure white or pure black. Color appears primarily in blob shapes, not in text or borders.
3. **Geometry:** Organic blob shapes are the defining visual element. Use multi-value CSS `border-radius`: e.g., `60% 40% 30% 70% / 60% 30% 70% 40%`. Standard UI elements (cards, buttons, inputs) use `border-radius: 16px–20px` — soft but not blobby. Never use `border-radius: 0` or `border-radius: 4px` on primary containers. Never use hard geometric shapes as decorative elements — blobs only.
4. **Blob Fills:** All decorative blobs use CSS gradient fills from the earthy palette. Examples: `linear-gradient(135deg, #2D6A4F, #74C69D)`, `linear-gradient(135deg, #D4A373, #E9C46A)`, `radial-gradient(circle, #52B788, #2D6A4F)`. Blobs sit behind content at `opacity: 0.30–0.60`, blur filter `blur(40px)–blur(80px)`. Never use flat opaque solid fills on blobs — gradient is required.
5. **Surfaces:** Light mode cards: `background: #FFFFFF`, subtle warm border `1px solid rgba(212,163,115,0.20)`. Dark mode: `background: rgba(255,255,255,0.04)`, border `1px solid rgba(116,198,157,0.15)`. No heavy shadows — soft `box-shadow: 0 2px 16px rgba(45,106,79,0.10)`.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use hard geometric shapes (rectangles with 0px radius) as decorative elements — organic radii and blob forms only.
- **NEVER** apply flat opaque solid fills to decorative blob elements — gradient fills are mandatory.
- **NEVER** use a pure tech-cold color palette (`#0000FF`, `#00FFFF` at full saturation, steel grays) — all colors must carry warmth or natural origin.
- **NEVER** use `border-radius: 0px` or `border-radius < 12px` on cards, buttons, or primary UI containers.
- **NEVER** use sharp offset box-shadows (`4px 4px 0 #000` brutalist style) — only soft ambient shadows.
- **NEVER** use a geometric display font (condensed grotesque, slab serif) — humanist sans only.
- **NEVER** place blobs over text regions without sufficient opacity reduction (`opacity < 0.25`) or blur filter.

---

## Digital Organic — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Surface — Light (default) */
  --color-bg: #FAFAF8;
  --color-surface: #FFFFFF;
  --color-surface-hover: #F4F7F4;
  --color-surface-active: #EAF2EA;
  --color-surface-subtle: #F7FAF7;

  /* Canvas & Surface — Dark */
  --color-bg-dark: #0D1A12;
  --color-surface-dark: #122318;
  --color-surface-dark-raised: #1A3024;

  /* Typography — Light */
  --color-text-primary: #1A2E1A;
  --color-text-secondary: #4A6741;
  --color-text-muted: #8AAB82;
  --color-text-inverse: #FAFAF8;

  /* Typography — Dark */
  --color-text-primary-dark: #D4E8D0;
  --color-text-secondary-dark: #8AC89E;
  --color-text-muted-dark: #4A7A5A;

  /* Lines & Borders */
  --color-border: rgba(212, 163, 115, 0.20);
  --color-border-subtle: rgba(45, 106, 79, 0.10);
  --color-border-hover: rgba(45, 106, 79, 0.30);

  /* Earthy Accent Palette */
  --color-forest: #2D6A4F;
  --color-mint: #74C69D;
  --color-sage: #52B788;
  --color-sand: #D4A373;
  --color-gold: #E9C46A;
  --color-moss: #40916C;
  --color-bark: #B7895A;

  /* Interactive Accent */
  --color-accent: #2D6A4F;
  --color-accent-hover: #1B4332;
  --color-accent-subtle: rgba(45, 106, 79, 0.10);
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 12px;      /* Tags, small badges — minimum allowed */
  --radius-sm: 16px;      /* Buttons, inputs */
  --radius-md: 20px;      /* Standard cards, panels */
  --radius-lg: 24px;      /* Feature cards, modals */
  --radius-xl: 32px;      /* Hero containers */
  --radius-full: 9999px;  /* Avatar clips, circular elements */

  /* Organic Blob Shapes — multi-value border-radius */
  --blob-1: 60% 40% 30% 70% / 60% 30% 70% 40%;
  --blob-2: 40% 60% 70% 30% / 40% 70% 30% 60%;
  --blob-3: 50% 50% 35% 65% / 55% 45% 55% 45%;
  --blob-4: 70% 30% 50% 50% / 30% 70% 40% 60%;
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-xs: 0 2px 8px 0 rgba(45, 106, 79, 0.06);
  --shadow-sm: 0 4px 16px 0 rgba(45, 106, 79, 0.08), 0 1px 3px 0 rgba(0, 0, 0, 0.04);
  --shadow-md: 0 8px 32px 0 rgba(45, 106, 79, 0.10), 0 2px 6px 0 rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 16px 48px 0 rgba(45, 106, 79, 0.12), 0 4px 12px 0 rgba(0, 0, 0, 0.06);
  --shadow-blob: 0 0 80px rgba(45, 106, 79, 0.25);
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
  --space-16: 64px;
  --grid-baseline: 8px;
  --card-padding: 24px;
  --blob-size-sm: 200px;
  --blob-size-md: 360px;
  --blob-size-lg: 500px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '20px',
        sm: '16px',
        md: '20px',
        lg: '24px',
        xl: '32px',
        full: '9999px',
      },
      boxShadow: {
        DEFAULT: '0 8px 32px 0 rgba(45, 106, 79, 0.10)',
        xs: '0 2px 8px 0 rgba(45, 106, 79, 0.06)',
        sm: '0 4px 16px 0 rgba(45, 106, 79, 0.08)',
        lg: '0 16px 48px 0 rgba(45, 106, 79, 0.12)',
        blob: '0 0 80px rgba(45, 106, 79, 0.25)',
      },
      colors: {
        canvas: '#FAFAF8',
        surface: '#FFFFFF',
        border: 'rgba(212, 163, 115, 0.20)',
        ink: {
          primary: '#1A2E1A',
          secondary: '#4A6741',
          muted: '#8AAB82',
        },
        earthy: {
          forest: '#2D6A4F',
          mint: '#74C69D',
          sage: '#52B788',
          sand: '#D4A373',
          gold: '#E9C46A',
          moss: '#40916C',
        },
        accent: {
          DEFAULT: '#2D6A4F',
          hover: '#1B4332',
          subtle: 'rgba(45, 106, 79, 0.10)',
        },
      },
      fontFamily: {
        sans: ['Bricolage Grotesque', 'DM Sans', '-apple-system', 'sans-serif'],
        mono: ['DM Mono', 'JetBrains Mono', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Decorative Blobs:** Absolutely positioned, `pointer-events: none`, `z-index: 0`. Size: 200px–500px square div. `border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%` (vary per blob). Fill: `linear-gradient(135deg, #2D6A4F, #74C69D)` or `linear-gradient(135deg, #D4A373, #E9C46A)`. `opacity: 0.35–0.55`. `filter: blur(50px)`. Positioned partially off-screen or behind content areas.
- **Cards:** `background: #FFFFFF`, `border-radius: 20px`, `border: 1px solid rgba(212,163,115,0.20)`, `box-shadow: var(--shadow-sm)`, padding `24px`. Never sharp corners.
- **Buttons:** Height 44px (standard) or 36px (compact), `border-radius: 16px`, `font-family: DM Sans`, `font-weight: 600`, `font-size: 14px`, padding `0 20px`. Primary: `background: #2D6A4F; color: #FAFAF8`. Secondary: `background: rgba(45,106,79,0.10); color: #2D6A4F; border: 1px solid rgba(45,106,79,0.25)`.
- **Data Values:** `font-family: DM Mono`, `font-weight: 300`, `font-size: 13px–14px`, `color: #1A2E1A`. Numeric values always right-aligned with `font-variant-numeric: tabular-nums`.
- **Inputs:** Height 44px, `border-radius: 16px`, `border: 1px solid rgba(212,163,115,0.25)`, `background: #FFFFFF`, `font-family: DM Sans`, `font-size: 14px`. Focus: `border-color: #2D6A4F; box-shadow: 0 0 0 3px rgba(45,106,79,0.12)`.
- **Tables:** Container `border-radius: 16px`, `overflow: hidden`. Row height `44px`, `border-bottom: 1px solid rgba(212,163,115,0.15)`. Header: 11px / `#8AAB82` / `letter-spacing: 0.06em`. Numeric cells: `DM Mono` / `font-weight: 300`.
