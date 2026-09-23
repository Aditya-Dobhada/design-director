---
name: style-minimal-modern
description: Implementation rules for Minimal Modern style. Pristine neutral zinc canvas, disciplined typographic hierarchy (Geist/Inter), 6px-8px micro-radii, 1px crisp borders, and subtle elevation for contemporary SaaS and productivity tools.
---

# Style Pack: Minimal Modern

A restrained, high-efficiency visual system designed for contemporary productivity software, developer consoles, and SaaS applications. Built on intentional whitespace, neutral zinc surfaces, micro-radii (6px–8px), subtle hairline borders, and pure typographic hierarchy.

## Core Principles

1. **Typography:** Primary interface font `Geist Sans`, `Inter`, or `SF Pro Display`. Tight negative tracking (`-0.02em` on titles, `-0.01em` on body). Weights restricted to 400 (regular), 500 (medium), and 600 (semi-bold). Never use decorative display serifs or playful fonts.
2. **Color:** Canvas `#FAFAFA` with pure white card surfaces (`#FFFFFF`). Text hierarchy anchored in zinc tones: Primary `#09090B`, Secondary `#71717A`, Tertiary `#A1A1AA`. Single intentional interactive accent: Electric Blue (`#2563EB`), Slate Black (`#18181B`), or Violet (`#6366F1`).
3. **Geometry:** Subtle, calibrated curvature: `6px` (`rounded-md`) for buttons, badges, and inputs; `8px` (`rounded-lg`) for cards and modal dialogs. Never sharp `0px` harsh brutalism, never exaggerated pill shapes on containers.
4. **Surfaces & Borders:** 1px solid hairline borders (`#E4E4E7` on light surfaces). Elevation uses clean ambient drop-shadows with low opacity (`rgba(0,0,0,0.04)`) and tight blur (`2px`–`6px`). Never colored neon halos or heavy drop shadows.
5. **Motion:** Micro-snappy 120ms–150ms transitions (`cubic-bezier(0.16, 1, 0.3, 1)`). Hover states trigger subtle surface shifts (`#F4F4F5`) rather than dramatic translations.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use sharp 0px corners on cards or primary containers (`rounded-none` is forbidden on cards; use 8px).
- **NEVER** use bubbly or exaggerated container radiuses (`rounded-2xl`, `rounded-3xl` are forbidden).
- **NEVER** use heavy solid ink borders (2px–4px black borders are forbidden; use 1px subtle zinc borders).
- **NEVER** use loud multi-color gradients or rainbow accent palettes. Pick one accent color for interactive focus.
- **NEVER** use high-saturation colored shadows or neon glows on static elements.
- **NEVER** use decorative serifs, comic typefaces, or hand-drawn icon styles.
- **NEVER** fill card backgrounds with dark or vibrant colors in light mode.

---

## Minimal Modern — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Surface */
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-surface-hover: #F4F4F5;
  --color-surface-active: #E4E4E7;
  --color-surface-subtle: #F8F8F8;

  /* Typography / Zinc */
  --color-text-primary: #09090B;
  --color-text-secondary: #71717A;
  --color-text-muted: #A1A1AA;
  --color-text-inverse: #FFFFFF;

  /* Lines & Dividers */
  --color-border: #E4E4E7;
  --color-border-subtle: #F4F4F5;
  --color-border-hover: #D4D4D8;

  /* Focus & Interactive Accent */
  --color-accent: #2563EB;
  --color-accent-hover: #1D4ED8;
  --color-accent-subtle: #EFF6FF;
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 4px;      /* Badges, tags */
  --radius-sm: 6px;      /* Buttons, text inputs */
  --radius-md: 8px;      /* Standard card, panel, dropdown */
  --radius-lg: 12px;     /* Modals, large surface overlays */
  --radius-full: 9999px; /* Status dots, circular avatar clips only */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.08), 0 1px 2px -1px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.03);
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
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '8px',
        sm: '6px',
        md: '8px',
        lg: '12px',
      },
      boxShadow: {
        DEFAULT: '0 1px 3px 0 rgba(0, 0, 0, 0.08)',
        subtle: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        card: '0 1px 3px 0 rgba(0, 0, 0, 0.08), 0 1px 2px -1px rgba(0, 0, 0, 0.04)',
        popover: '0 10px 15px -3px rgba(0, 0, 0, 0.08)',
      },
      colors: {
        canvas: '#FAFAFA',
        card: '#FFFFFF',
        border: '#E4E4E7',
        ink: {
          primary: '#09090B',
          secondary: '#71717A',
          muted: '#A1A1AA',
        },
        accent: {
          DEFAULT: '#2563EB',
          hover: '#1D4ED8',
          subtle: '#EFF6FF',
        },
      },
      fontFamily: {
        sans: ['Geist Sans', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono: ['Geist Mono', 'JetBrains Mono', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 36px (compact) or 40px (standard), `border-radius: 6px`, `font-weight: 500`, padding `0 14px`. Subtle 1px border on secondary, solid primary fill on main action.
- **Cards:** Background `#FFFFFF`, `border-radius: 8px`, `border: 1px solid #E4E4E7`, `box-shadow: var(--shadow-xs)`, padding `20px` or `24px`.
- **Inputs:** Height 36px, `border-radius: 6px`, `border: 1px solid #E4E4E7`, background `#FFFFFF`. Focus ring: `outline: 2px solid #2563EB; outline-offset: 1px`.
- **Tables:** Hairline dividers (`border-b: 1px solid #F4F4F5`), row height 44px, numeric cells aligned right with tabular figures (`font-variant-numeric: tabular-nums`).
