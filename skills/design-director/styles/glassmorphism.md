---
name: style-glassmorphism
description: Implementation rules for Glassmorphism style. Dark #0A0A0F canvas with frosted translucent panels, backdrop-filter blur, 1px rgba border lines, and layered ambient depth. Domain — OS-level UI, media/creative dashboards, overlay-heavy apps.
---

# Style Pack: Glassmorphism

A tactile, depth-driven visual system built on the physics of frosted glass. All surfaces are semi-transparent layers floating above a richly colored or darkly textured canvas. Depth is created through translucency gradients and ambient diffuse shadows — never opaque fills, never hard-offset cartoon shadows. Designed for creative dashboards, media applications, and OS-level system UIs where layered visual hierarchy must feel physical.

## Core Principles

1. **Translucency First:** Every panel, card, nav, and modal is a frosted glass pane — `background: rgba(255,255,255,0.06)` to `rgba(255,255,255,0.12)`. No surface is opaque. The canvas bleeds through every layer. Opacity is the primary depth cue.
2. **Blur as Structure:** `backdrop-filter: blur(16px)` on cards, `blur(20px)` on elevated overlays, `blur(24px)` on modals. Blur radius directly communicates elevation — more blur = closer to viewer.
3. **Hairline Glass Borders:** Every glass surface carries exactly `1px solid rgba(255,255,255,0.12)` on all edges. This edge-lit refraction line is what makes glass legible. Never increase border width; never use opaque border colors.
4. **Canvas & Glow:** Base canvas `#0A0A0F`. Background enriched with 1–2 radial gradient glows in the accent hue at ≤15% opacity — this creates the "light source behind the glass" effect. Never a flat matte dark background.
5. **Accent:** Electric violet `#7C3AED` or cyan `#06B6D4`. Use for interactive elements, active states, and glow sources. Never apply full-opacity accent as a card fill — only as a light source, border tint, or icon/text highlight.
6. **Typography:** Inter or SF Pro. Hairline weight labels (300–400) for tertiary info, 500 for body, 600 for emphasis. Text on dark glass is always near-white — `rgba(255,255,255,0.90)` primary, `rgba(255,255,255,0.55)` secondary, `rgba(255,255,255,0.35)` muted.
7. **Motion:** Blur transitions animate at 200ms `ease-out`. Panel opacity fades at 150ms. Never animate blur with `linear` timing — always `ease-out` or `cubic-bezier(0.25, 0.46, 0.45, 0.94)`.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use opaque flat card backgrounds (e.g., `background: #1E1E2E` solid fills destroy the glass illusion).
- **NEVER** use hard offset drop-shadows (e.g., `box-shadow: 4px 4px 0px #000` is brutalist, not glass).
- **NEVER** apply `backdrop-filter: blur` on a light background canvas — glass only works on dark or richly saturated backgrounds.
- **NEVER** use `border-radius: 0px` on any panel or card — minimum 12px.
- **NEVER** use borders thicker than 1px on glass surfaces — 2px+ kills the refraction effect.
- **NEVER** use high-chroma solid color fills for card backgrounds — frosted translucency only.
- **NEVER** use heavy black text on glass panels in dark mode — always rgba white-tinted text.
- **NEVER** use more than 2 accent colors simultaneously — electric violet OR cyan, not both as primaries.

---

## Glassmorphism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Depth */
  --color-bg: #0A0A0F;
  --color-bg-glow-violet: rgba(124, 58, 237, 0.12);
  --color-bg-glow-cyan: rgba(6, 182, 212, 0.08);

  /* Glass Surfaces — translucent only */
  --color-glass-low: rgba(255, 255, 255, 0.06);
  --color-glass-mid: rgba(255, 255, 255, 0.09);
  --color-glass-high: rgba(255, 255, 255, 0.12);
  --color-glass-nav: rgba(255, 255, 255, 0.07);

  /* Glass Borders */
  --color-glass-border: rgba(255, 255, 255, 0.12);
  --color-glass-border-subtle: rgba(255, 255, 255, 0.07);
  --color-glass-border-accent: rgba(124, 58, 237, 0.40);

  /* Typography — white-tinted scale */
  --color-text-primary: rgba(255, 255, 255, 0.92);
  --color-text-secondary: rgba(255, 255, 255, 0.55);
  --color-text-muted: rgba(255, 255, 255, 0.35);

  /* Accent — Violet primary */
  --color-accent: #7C3AED;
  --color-accent-hover: #6D28D9;
  --color-accent-subtle: rgba(124, 58, 237, 0.15);
  --color-accent-glow: rgba(124, 58, 237, 0.30);

  /* Accent — Cyan secondary */
  --color-cyan: #06B6D4;
  --color-cyan-subtle: rgba(6, 182, 212, 0.15);

  /* Positive / Negative */
  --color-positive: #34D399;
  --color-negative: #F87171;
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 8px;      /* Badges, pills */
  --radius-sm: 12px;     /* Buttons, inputs, small chips */
  --radius-md: 14px;     /* Standard glass card, panel */
  --radius-lg: 18px;     /* Modal dialogs, elevated overlays */
  --radius-xl: 24px;     /* Hero sections, backdrop sheets */
  --radius-full: 9999px; /* Avatar clips, status dots only */
}
```

## Shadow & Elevation Tokens

```css
:root {
  /* Diffuse ambient depth — NO hard offset */
  --shadow-glass-sm: 0 4px 16px rgba(0, 0, 0, 0.25);
  --shadow-glass-md: 0 8px 32px rgba(0, 0, 0, 0.40);
  --shadow-glass-lg: 0 16px 48px rgba(0, 0, 0, 0.50);

  /* Accent glow halos — use on focus / active states only */
  --shadow-glow-violet: 0 0 24px rgba(124, 58, 237, 0.30);
  --shadow-glow-cyan: 0 0 20px rgba(6, 182, 212, 0.25);

  /* Inner edge highlight — simulates light hitting glass rim */
  --shadow-inner-rim: inset 0 1px 0 rgba(255, 255, 255, 0.15);
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
  --grid-gap: 16px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '14px',
        sm: '12px',
        md: '14px',
        lg: '18px',
        xl: '24px',
      },
      boxShadow: {
        glass: '0 8px 32px rgba(0, 0, 0, 0.40)',
        'glass-sm': '0 4px 16px rgba(0, 0, 0, 0.25)',
        'glass-lg': '0 16px 48px rgba(0, 0, 0, 0.50)',
        'glow-violet': '0 0 24px rgba(124, 58, 237, 0.30)',
        'glow-cyan': '0 0 20px rgba(6, 182, 212, 0.25)',
      },
      backdropBlur: {
        glass: '16px',
        'glass-elevated': '24px',
      },
      colors: {
        canvas: '#0A0A0F',
        glass: {
          low: 'rgba(255,255,255,0.06)',
          mid: 'rgba(255,255,255,0.09)',
          high: 'rgba(255,255,255,0.12)',
          border: 'rgba(255,255,255,0.12)',
        },
        accent: {
          DEFAULT: '#7C3AED',
          hover: '#6D28D9',
          subtle: 'rgba(124,58,237,0.15)',
        },
        cyan: {
          DEFAULT: '#06B6D4',
          subtle: 'rgba(6,182,212,0.15)',
        },
        ink: {
          primary: 'rgba(255,255,255,0.92)',
          secondary: 'rgba(255,255,255,0.55)',
          muted: 'rgba(255,255,255,0.35)',
        },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons (Primary):** Height 36px, `border-radius: 12px`, `background: rgba(124,58,237,0.80)`, `border: 1px solid rgba(124,58,237,0.60)`, `backdrop-filter: blur(8px)`, `color: #fff`, `font-weight: 500`. Hover: background shifts to `rgba(124,58,237,0.95)` + `box-shadow: var(--shadow-glow-violet)`.
- **Buttons (Secondary/Ghost):** Same height/radius, `background: rgba(255,255,255,0.08)`, `border: 1px solid rgba(255,255,255,0.12)`, `color: rgba(255,255,255,0.80)`. Hover: background `rgba(255,255,255,0.13)`.
- **Cards (Glass Panel):** `background: var(--color-glass-mid)`, `border-radius: 14px`, `border: 1px solid var(--color-glass-border)`, `backdrop-filter: blur(20px)`, `box-shadow: var(--shadow-glass-md)`, also includes `var(--shadow-inner-rim)`. Padding `20px` or `24px`.
- **Nav:** `background: var(--color-glass-nav)`, `border-bottom: 1px solid var(--color-glass-border-subtle)`, `backdrop-filter: blur(16px)`, height `60px`. Position `sticky top-0` with `z-index: 100`.
- **Inputs:** Height 36px, `border-radius: 10px`, `background: rgba(255,255,255,0.07)`, `border: 1px solid rgba(255,255,255,0.12)`, `color: rgba(255,255,255,0.90)`. Focus: `border-color: rgba(124,58,237,0.60)`, `box-shadow: 0 0 0 3px rgba(124,58,237,0.20)`.
- **Tables:** Row dividers `border-bottom: 1px solid rgba(255,255,255,0.06)`. Row height 44px. Header background `rgba(255,255,255,0.04)`. Numeric cells right-aligned, `font-variant-numeric: tabular-nums`.
- **Badges:** `border-radius: 9999px`, `padding: 2px 10px`, `background: rgba(124,58,237,0.20)`, `border: 1px solid rgba(124,58,237,0.35)`, `color: #A78BFA`, `font-size: 11px`, `font-weight: 500`.
