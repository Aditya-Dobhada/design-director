---
name: style-mid-century-modern
description: Implementation rules for Mid-Century Modern style. Warm parchment canvas (#F6F3EB), atomic color blocks (terracotta #D95D39, olive #606C38, mustard #E0A96D), organic curved pod geometry (16px-24px), and geometric sans typography (Futura/Josefin).
---

# Style Pack: Mid-Century Modern

A warm, human-centric design system inspired by 1950s California modernism, Eames furniture craft, Palm Springs architecture, and Scandinavian industrial design. Characterized by warm organic earth tones, atomic geometric curves, walnut accents, and optimistic typographic clarity.

## Core Principles

1. **Typography:** Primary display in geometric modernist sans: `Josefin Sans`, `Futura`, or `Century Gothic` with open tracking. Body typography in warm humanist sans: `Work Sans`, `DM Sans`, or `Nunito Sans` (weight 400).
2. **Canvas & Surfaces:** Canvas `#F6F3EB` (warm architectural parchment) or `#FDFBF7`. Card surfaces `#FFFFFF` with warm cream undertones. Accent panels in deep walnut `#2D221E` or mustard `#E0A96D`.
3. **Geometry:** Organic atomic curvature: `16px`–`24px` radius on card corners (`rounded-2xl`). Asymmetrical rounded panels and oblong pill tags. Never sharp `0px` harsh industrial edges.
4. **Color & Palette:** Grounded California architectural palette: Burnt Terracotta (`#D95D39`), Olive Moss (`#606C38`), Mustard Maize (`#E0A96D`), Teal Blue (`#2A6F7F`), and Warm Walnut (`#2D221E`).
5. **Borders & Shadows:** Clean 1px–2px warm ink borders (`#4A3E39` or `#D9CEB2`). Soft, diffuse ambient shadows (`rgba(74, 62, 57, 0.08)`) with zero neon intensity.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use cold gray or tech zinc backgrounds (`#09090B`, `#18181B`, `#F4F4F5` are forbidden; use warm parchment `#F6F3EB`).
- **NEVER** use sharp 0px corners on cards or primary containers (`rounded-none` is forbidden on cards; mandate 16px–24px).
- **NEVER** use neon cyan, electric purple, or fluorescent synthetic colors.
- **NEVER** use clinical monochrome palettes. Must feature at least one warm architectural hue (terracotta, olive, mustard).
- **NEVER** use futuristic HUD telemetry, chamfered cuts, or scanline overlays.
- **NEVER** use dense tabular layouts without generous padding and breathable whitespace.

---

## Mid-Century Modern — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Warm Parchment Canvas */
  --color-mcm-bg: #F6F3EB;
  --color-mcm-surface: #FFFFFF;
  --color-mcm-surface-warm: #EFE9DC;
  --color-mcm-surface-dark: #2D221E;

  /* Architectural Earth & Atomic Hues */
  --color-terracotta: #D95D39;
  --color-terracotta-hover: #BF4C2A;
  --color-olive: #606C38;
  --color-mustard: #E0A96D;
  --color-teal: #2A6F7F;
  --color-walnut: #2D221E;

  /* Typography / Walnut Ink */
  --color-text-primary: #2D221E;
  --color-text-secondary: #5C4D44;
  --color-text-muted: #8D7B70;
  --color-text-inverse: #F6F3EB;

  /* Hairlines & Borders */
  --color-border: #DCD4C4;
  --color-border-heavy: #4A3E39;
}
```

## Border Radius Tokens

```css
:root {
  --radius-sm: 8px;       /* Inputs, small controls */
  --radius-md: 16px;      /* Standard buttons, badges */
  --radius-lg: 24px;      /* Main cards, container panels */
  --radius-xl: 32px;      /* Hero banners, feature pods */
  --radius-full: 9999px;  /* Pill buttons and badges */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-warm-sm: 0 2px 4px rgba(45, 34, 30, 0.05);
  --shadow-warm-md: 0 6px 16px rgba(45, 34, 30, 0.08);
  --shadow-warm-lg: 0 12px 28px rgba(45, 34, 30, 0.12);
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
  --grid-baseline: 8px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '16px',
        sm: '8px',
        md: '16px',
        lg: '24px',
        xl: '32px',
        full: '9999px',
      },
      boxShadow: {
        DEFAULT: '0 6px 16px rgba(45, 34, 30, 0.08)',
        warm: '0 6px 16px rgba(45, 34, 30, 0.08)',
        card: '0 12px 28px rgba(45, 34, 30, 0.12)',
      },
      colors: {
        canvas: '#F6F3EB',
        surface: '#FFFFFF',
        terracotta: '#D95D39',
        olive: '#606C38',
        mustard: '#E0A96D',
        walnut: '#2D221E',
        ink: {
          primary: '#2D221E',
          secondary: '#5C4D44',
          muted: '#8D7B70',
        },
      },
      fontFamily: {
        display: ['Josefin Sans', 'Futura', 'sans-serif'],
        sans: ['Work Sans', 'DM Sans', 'sans-serif'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 44px, `border-radius: 9999px` (pill) or `16px`, `font-family: 'Josefin Sans', sans-serif`, `font-weight: 600`, padding `0 24px`. Primary in terracotta `#D95D39`, secondary in olive outline `#606C38`.
- **Cards:** Background `#FFFFFF`, `border-radius: 24px`, `border: 1px solid #DCD4C4`, `box-shadow: var(--shadow-warm-md)`, padding `28px`.
- **Inputs:** Height 44px, `border-radius: 12px`, background `#FFFFFF`, `border: 1px solid #DCD4C4`, warm walnut text.
- **Tables:** Generous padding (`16px 20px`), subtle warm dividers (`border-b: 1px solid #EFE9DC`), bold geometric section headers.
