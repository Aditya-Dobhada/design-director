---
name: style-vaporwave
description: Implementation rules for Vaporwave style. Pastel pink (#FF71CE) and cyan (#01CDFE) gradients, retro Windows 95 chrome, Japanese typography, classical marble references, CRT scanline artifacts, and surreal nostalgia.
---

# Style Pack: Vaporwave

A surreal, nostalgic visual system exploring 1980s and 1990s consumer technology, Japanese economic boom aesthetics, early graphical user interfaces, classical Roman sculpture, and pastel sunset horizons. Defined by dreamy purple/pink/cyan palettes, beveled window chrome, pixel accents, and retro digital surrealism.

## Core Principles

1. **Typography:** Uncanny juxtaposition of classical Roman serif typography (`Playfair Display`, `Cinzel`, `Cormorant`) with retro pixel/monospace fonts (`VT323`, `Silkscreen`, `MS Gothic`). Japanese typographic flourishes and full-width Roman characters.
2. **Canvas & Surfaces:** Deep twilight lavender (`#1F132B` void) or gradient sunset horizons (pink-to-cyan `linear-gradient(135deg, #2E1A47 0%, #150B24 100%)`). Window surfaces `#2A1B3D` with beveled chrome highlights.
3. **Geometry:** Classical desktop window geometry: `0px` or `4px` radius (`rounded-sm`). Beveled 3D borders (`box-shadow: inset 2px 2px #FF71CE, inset -2px -2px #01CDFE` or Windows 95 grey bevels).
4. **Color & Palette:** Iconic pastel synth palette: Neon Pink (`#FF71CE`), Aqua Cyan (`#01CDFE`), Cyber Lavender (`#B967FF`), Sunset Yellow (`#FFE373`), and Mint Teal (`#05FFA1`).
5. **Textures & Atmosphere:** CRT scanline gradients, marble bust imagery, wireframe vector horizons, and checkerboard grid floors.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use sterile corporate gray or neutral zinc palettes (`#FAFAFA`, `#E4E4E7` are forbidden; canvas must feature vapor lavender or gradient depth).
- **NEVER** use earthy muted tones like terracotta, forest green, or beige.
- **NEVER** use generic flat SaaS cards with soft diffuse gray shadows.
- **NEVER** use modern clean sans-serif typography exclusively. Must feature classical serif or pixel typography.
- **NEVER** use standard responsive mobile-app pill buttons without retro bevels or pastel neon borders.
- **NEVER** hide the retro-digital personality behind plain monochromatic cards.

---

## Vaporwave — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Twilight Canvas & Horizons */
  --color-vapor-void: #150B24;
  --color-vapor-bg: #1F132B;
  --color-vapor-surface: #2A1B3D;
  --color-vapor-surface-light: #F7E8FA;

  /* Iconic Neon & Pastel Hues */
  --color-vapor-pink: #FF71CE;
  --color-vapor-cyan: #01CDFE;
  --color-vapor-purple: #B967FF;
  --color-vapor-yellow: #FFE373;
  --color-vapor-mint: #05FFA1;

  /* Typography / Phosphor */
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #E8D5F5;
  --color-text-pink: #FF71CE;
  --color-text-cyan: #01CDFE;
  --color-text-muted: #9578A8;

  /* Borders & Bevels */
  --color-border-pink: #FF71CE;
  --color-border-cyan: #01CDFE;
  --color-border-subtle: rgba(255, 113, 206, 0.3);
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px;  /* Windows 95 dialogs, classic tables */
  --radius-sm: 4px;    /* Surface containers, buttons */
  --radius-md: 6px;    /* Modal popups */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-vapor-glow: 0 0 12px rgba(255, 113, 206, 0.4), 0 0 24px rgba(1, 205, 254, 0.2);
  --shadow-bevel-outset: 2px 2px 0px #01CDFE, -2px -2px 0px #FF71CE;
  --shadow-bevel-inset: inset 2px 2px 0px #000000, inset -2px -2px 0px #FFFFFF;
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
  --grid-baseline: 8px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '2px',
        none: '0px',
        sm: '4px',
        md: '6px',
      },
      boxShadow: {
        DEFAULT: '0 0 12px rgba(255, 113, 206, 0.4)',
        vapor: '0 0 12px rgba(255, 113, 206, 0.4), 0 0 24px rgba(1, 205, 254, 0.2)',
        bevel: '2px 2px 0px #01CDFE, -2px -2px 0px #FF71CE',
      },
      colors: {
        canvas: '#1F132B',
        surface: '#2A1B3D',
        vapor: {
          pink: '#FF71CE',
          cyan: '#01CDFE',
          purple: '#B967FF',
          yellow: '#FFE373',
          mint: '#05FFA1',
        },
      },
      fontFamily: {
        serif: ['Playfair Display', 'Cinzel', 'serif'],
        pixel: ['VT323', 'Silkscreen', 'monospace'],
        mono: ['MS Gothic', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 36px, `border-radius: 2px`, `border: 2px solid #FF71CE`, `box-shadow: 2px 2px 0px #01CDFE`, `font-family: 'VT323', monospace`, `font-size: 16px`. Hover: inverse background with glowing cyan drop shadow.
- **Cards / Desktop Windows:** Background `#2A1B3D`, `border: 1px solid #FF71CE`, `box-shadow: var(--shadow-vapor-glow)`, padding `20px`. Header simulated with gradient title bar.
- **Inputs:** Height 36px, background `#150B24`, `border: 1px solid #01CDFE`, pink text, pixel font.
- **Tables:** Wireframe cyan borders (`border: 1px solid rgba(1, 205, 254, 0.4)`), alternating pastel rows, Japanese glyph headers.
