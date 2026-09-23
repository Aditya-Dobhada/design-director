---
name: style-aurora-gradient
description: Implementation rules for Aurora Gradient style. Soft multi-color atmospheric gradients (purple/pink/cyan) at low opacity over dark #0B0F1A base, 12px–16px radii, gradient-border cards, large display headings. Domain: AI products, creative tools, generative platforms.
---

# Style Pack: Aurora Gradient

A warm, atmospheric, depth-rich visual system inspired by polar aurora light. Dark near-void base surfaces receive soft multi-color radial gradients at controlled low opacity — never neon, never cyberpunk. Cards use gradient borders via pseudo-elements. Display headings carry gradient fill. The effect is serene, expansive, and premium — the visual language of intelligent, creative software.

## Core Principles

1. **Typography:** Primary: `Plus Jakarta Sans` or `Inter`. Display headings: weight 700–800, `font-size: 32px–56px`, gradient text fill (`background-clip: text; -webkit-text-fill-color: transparent`). UI labels: `Inter` 12px–14px / 400–500. Data values: `Inter` 13px–14px / 600, white. Tracking: `-0.03em` on display, `-0.01em` on body. Never use a condensed or slab font.
2. **Color:** Base canvas `#0B0F1A`. Primary aurora gradient: `linear-gradient(135deg, #8B5CF6 0%, #EC4899 50%, #06B6D4 100%)` at opacity `0.12–0.20` over dark surfaces as radial ambient glow. Card surfaces: `#0F1628`. Text primary: `#F0F4FF`. Text secondary: `#8892AA`. Accent interactive: `#8B5CF6` (violet). Accent secondary: `#06B6D4` (cyan). No solid neon fills — all color appears as gradient or at reduced opacity.
3. **Geometry:** Soft, welcoming radii. Cards and panels: `border-radius: 16px`. Buttons: `border-radius: 12px`. Inputs: `border-radius: 12px`. Badges: `border-radius: 8px`. Modal overlays: `border-radius: 20px`. Never use `0px` or `2px` radius. Never use `border-radius > 24px` on rectangles.
4. **Gradient Borders:** Cards use a `1px` gradient border applied via CSS pseudo-element or `border-image: linear-gradient(135deg, rgba(139,92,246,0.5), rgba(236,72,153,0.3), rgba(6,182,212,0.5)) 1`. Alternatively: `background: linear-gradient(#0F1628, #0F1628) padding-box, linear-gradient(135deg, ...) border-box`. Never use a plain solid-color border on a primary card.
5. **Atmosphere:** Background always carries at least one radial gradient ambient orb at low opacity: `radial-gradient(ellipse 60% 40% at 30% 20%, rgba(139,92,246,0.15) 0%, transparent 70%)`. Layered with a second orb at a different position (cyan or pink). Never let the background be flat black — aurora ambience is required.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use flat solid-color-only backgrounds without the aurora gradient overlay — the atmospheric gradient is a non-negotiable visual contract.
- **NEVER** use harsh saturated neon (`#FF00FF`, `#00FF00`, `#FF0000` at full saturation) — aurora palette is soft, desaturated, and atmospheric.
- **NEVER** use hard offset drop-shadows (`box-shadow: 8px 8px 0 #000` style) — elevation uses soft ambient glow (`rgba(139,92,246,0.25)` blur shadows).
- **NEVER** use `border-radius: 0` or `border-radius < 8px` on cards, buttons, or panels — minimum 8px, standard 12px–16px.
- **NEVER** use heavy solid borders (1px plain `#333` borders) on cards — gradient borders or transparent surfaces with glow only.
- **NEVER** apply strobing or high-speed animation — transitions max `600ms ease`, aurora shimmer animation max 8s cycle, gentle and slow.
- **NEVER** use a multi-color solid icon set — prefer monochrome or single-accent icons with subtle gradient fill.

---

## Aurora Gradient — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Surface */
  --color-bg: #0B0F1A;
  --color-surface: #0F1628;
  --color-surface-raised: #131D35;
  --color-surface-hover: rgba(139, 92, 246, 0.06);
  --color-surface-active: rgba(139, 92, 246, 0.12);

  /* Typography */
  --color-text-primary: #F0F4FF;
  --color-text-secondary: #8892AA;
  --color-text-muted: #4A5470;
  --color-text-inverse: #0B0F1A;

  /* Lines & Borders */
  --color-border: rgba(139, 92, 246, 0.20);
  --color-border-subtle: rgba(255, 255, 255, 0.06);
  --color-border-strong: rgba(139, 92, 246, 0.40);

  /* Aurora Gradient Palette */
  --aurora-violet: #8B5CF6;
  --aurora-pink: #EC4899;
  --aurora-cyan: #06B6D4;
  --aurora-gradient: linear-gradient(135deg, #8B5CF6, #EC4899, #06B6D4);

  /* Interactive Accents */
  --color-accent: #8B5CF6;
  --color-accent-hover: #7C3AED;
  --color-accent-subtle: rgba(139, 92, 246, 0.12);
  --color-accent-secondary: #06B6D4;

  /* Functional */
  --color-positive: #34D399;
  --color-negative: #F87171;
  --color-warning: #FBBF24;
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 8px;      /* Inline badges, chips — minimum allowed */
  --radius-sm: 12px;     /* Buttons, inputs */
  --radius-md: 16px;     /* Standard cards, panels */
  --radius-lg: 20px;     /* Modals, large overlays */
  --radius-xl: 24px;     /* Hero sections, feature cards */
  --radius-full: 9999px; /* Avatar clips, circular buttons */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-xs: 0 2px 8px 0 rgba(139, 92, 246, 0.08);
  --shadow-sm: 0 4px 16px 0 rgba(139, 92, 246, 0.12), 0 1px 3px 0 rgba(0, 0, 0, 0.20);
  --shadow-md: 0 8px 32px 0 rgba(139, 92, 246, 0.18), 0 2px 8px 0 rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 16px 64px 0 rgba(139, 92, 246, 0.22), 0 4px 16px 0 rgba(0, 0, 0, 0.30);
  --shadow-glow-violet: 0 0 24px rgba(139, 92, 246, 0.35);
  --shadow-glow-cyan: 0 0 24px rgba(6, 182, 212, 0.30);
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
  --section-gap: 32px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '16px',
        sm: '12px',
        md: '16px',
        lg: '20px',
        xl: '24px',
        full: '9999px',
      },
      boxShadow: {
        DEFAULT: '0 8px 32px 0 rgba(139, 92, 246, 0.18)',
        xs: '0 2px 8px 0 rgba(139, 92, 246, 0.08)',
        sm: '0 4px 16px 0 rgba(139, 92, 246, 0.12)',
        lg: '0 16px 64px 0 rgba(139, 92, 246, 0.22)',
        'glow-violet': '0 0 24px rgba(139, 92, 246, 0.35)',
        'glow-cyan': '0 0 24px rgba(6, 182, 212, 0.30)',
      },
      colors: {
        canvas: '#0B0F1A',
        surface: '#0F1628',
        aurora: {
          violet: '#8B5CF6',
          pink: '#EC4899',
          cyan: '#06B6D4',
        },
        ink: {
          primary: '#F0F4FF',
          secondary: '#8892AA',
          muted: '#4A5470',
        },
        accent: {
          DEFAULT: '#8B5CF6',
          hover: '#7C3AED',
          subtle: 'rgba(139, 92, 246, 0.12)',
          secondary: '#06B6D4',
        },
      },
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'Inter', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Cards:** `background: #0F1628`, `border-radius: 16px`, gradient border via `background-clip: padding-box` + pseudo-element or `border-image`. Padding `24px`. Shadow `var(--shadow-md)`. Optional soft inner glow at top edge: `box-shadow: inset 0 1px 0 rgba(139,92,246,0.20)`.
- **Buttons:** Height 44px (standard) or 36px (compact), `border-radius: 12px`, `font-weight: 600`, `font-size: 14px`, padding `0 20px`. Primary: `background: linear-gradient(135deg, #8B5CF6, #EC4899)`, white text. Ghost: `border: 1px solid rgba(139,92,246,0.35)`, `color: #8B5CF6`, transparent background.
- **Inputs:** Height 44px, `border-radius: 12px`, `border: 1px solid rgba(139,92,246,0.20)`, `background: rgba(15,22,40,0.80)`, `color: #F0F4FF`, `font-size: 14px`. Focus: `border-color: #8B5CF6; box-shadow: 0 0 0 3px rgba(139,92,246,0.15)`.
- **Display Headings:** `font-family: Plus Jakarta Sans`, `font-weight: 800`, `font-size: 40px–56px`, `background: linear-gradient(135deg, #F0F4FF 0%, #8B5CF6 50%, #06B6D4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent`.
- **Background Atmosphere:** At minimum two radial gradient orbs at `opacity: 1` (opacity encoded in color): `radial-gradient(ellipse 50% 35% at 20% 15%, rgba(139,92,246,0.15), transparent)` and `radial-gradient(ellipse 40% 30% at 75% 70%, rgba(6,182,212,0.12), transparent)`.
- **Tables:** `border-radius: 12px` container, row height `44px`, `border-bottom: 1px solid rgba(255,255,255,0.06)`. Header: `font-size: 11px; letter-spacing: 0.06em; color: #8892AA`.
