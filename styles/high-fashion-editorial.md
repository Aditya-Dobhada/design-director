---
name: style-high-fashion-editorial
description: Implementation rules for High Fashion Editorial style. Dramatic high-contrast black/white canvas (#0A0A0A / #FFFFFF), monumental Didot/Bodoni display typography, micro-grotesque labels, asymmetric runway grids, 0px radius, and zero drop-shadows.
---

# Style Pack: High Fashion Editorial

A monumental, high-drama visual language derived from Parisian couture lookbooks, avant-garde runway magazines (Vogue Italia, Dazed, 032c), luxury maisons, and haute horlogerie monographs. Grounded in extreme typographic scale contrast, severe monochrome palettes, asymmetric grid tension, and deliberate editorial space.

## Core Principles

1. **Typography:** Extreme typographic tension: monumental display headlines in `Bodoni Moda`, `Playfair Display`, or `Italian Plate` (weight 700–900, size 64px–120px+) colliding with micro-scale grotesque sans (`Neue Haas Grotesk`, `Helvetica Neue`, `Inter` at 10px–12px with wide tracking `0.12em` and uppercase metadata).
2. **Canvas & Surfaces:** Stark monochrome: pure pitch black `#0A0A0A` or absolute white `#FFFFFF`. Card surfaces use transparent fills framed by razor-thin dividers. Never soft pastel tints, never warm cozy beiges.
3. **Geometry:** Strict `0px` radius everywhere (`border-radius: 0px`, `rounded-none`). Every container, button, image frame, and dialog has knife-edge 90-degree corners.
4. **Borders & Dividers:** Razor hairlines: `1px solid #0A0A0A` (on white) or `1px solid rgba(255, 255, 255, 0.2)` (on black). Dividers span full container widths without padding breaks.
5. **Elevation & Shadows:** Zero drop shadows universally (`box-shadow: none`). Elevation is expressed purely through typographic scale, contrast inversion, and spatial hierarchy.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners on any element (`rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-full` are strictly forbidden; use `0px`).
- **NEVER** use blurry drop shadows (`box-shadow: 0 4px ...` is forbidden; use `none`).
- **NEVER** use standard corporate SaaS blue, purple gradients, or friendly startup accents.
- **NEVER** use playful, rounded, or cartoonish typography.
- **NEVER** center-align dense text blocks. Align to severe left margins or strict asymmetric column rags.
- **NEVER** use standard 3-column cookie-cutter feature grids with floating icons in colored circles.
- **NEVER** use friendly emoji badges or informal pill tags.

---

## High Fashion Editorial — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Stark Couture Monochrome */
  --color-fashion-bg: #FFFFFF;
  --color-fashion-bg-dark: #0A0A0A;
  --color-fashion-surface: #FFFFFF;
  --color-fashion-surface-dark: #121212;

  /* Ink Hierarchy */
  --color-text-primary: #0A0A0A;
  --color-text-secondary: #404040;
  --color-text-muted: #737373;
  --color-text-inverse: #FFFFFF;

  /* Razor Hairlines */
  --color-border: #0A0A0A;
  --color-border-hairline: rgba(10, 10, 10, 0.15);
  --color-border-dark: rgba(255, 255, 255, 0.2);

  /* Rare Couture Accent (Single deliberate pop) */
  --color-accent-vermilion: #E31837;
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px; /* HARD ENFORCEMENT: 0px universally */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-none: none; /* HARD ENFORCEMENT: 0px blur */
}
```

## Spacing & Grid Tokens

```css
:root {
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
  --grid-baseline: 8px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px',
        none: '0px',
        sm: '0px',
        md: '0px',
        lg: '0px',
        full: '0px',
      },
      boxShadow: {
        DEFAULT: 'none',
        none: 'none',
      },
      colors: {
        canvas: '#FFFFFF',
        canvasDark: '#0A0A0A',
        border: '#0A0A0A',
        ink: {
          primary: '#0A0A0A',
          secondary: '#404040',
          muted: '#737373',
          inverse: '#FFFFFF',
        },
        accent: '#E31837',
      },
      fontFamily: {
        serif: ['Bodoni Moda', 'Playfair Display', 'Didot', 'serif'],
        sans: ['Neue Haas Grotesk', 'Helvetica Neue', 'Inter', 'sans-serif'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 44px, `border-radius: 0px`, `border: 1px solid #0A0A0A`, background `#0A0A0A`, color `#FFFFFF`, `font-family: sans-serif`, `font-size: 11px`, `letter-spacing: 0.15em`, `text-transform: uppercase`.
- **Cards / Editorial Panels:** Background `#FFFFFF` or `#0A0A0A`, `border: 1px solid var(--color-border-hairline)`, `border-radius: 0px`, padding `32px`.
- **Inputs:** Height 44px, `border-radius: 0px`, `border: none`, `border-bottom: 1px solid #0A0A0A`, background `transparent`, uppercase placeholder text.
- **Tables / Lookbook Index:** Full-width rows, hairline borders `border-b: 1px solid rgba(10, 10, 10, 0.12)`, large index numbers (`01`, `02`, `03`) in serif display, labels in micro-uppercase sans.
