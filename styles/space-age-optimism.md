---
name: style-space-age-optimism
description: Implementation rules for Space Age Optimism style. 1960s NASA/Eero Saarinen futurism, warm white and orange-chrome palette, tulip-pod organic geometry, atomic age moiré patterns, optimistic technological aspiration without darkness or aggression.
---

# Style Pack: Space Age Optimism

A visual language celebrating the luminous technological optimism of the 1960s: NASA mission graphics, Eero Saarinen's Tulip Chair, Olivetti Valentina, TWA terminal, and Braun product design. Curved forms, warm-white surfaces, chrome accents, and a persistent belief that the future is beautiful.

## Core Principles

1. **Canvas:** Warm optical white `#FAFAF8` body background. Never dark canvas — this is radiant, daylit design. Section alternates: warm white `#FAFAF8` and soft warm gray `#F0EDE8`.
2. **Color:** Dominant white base with single Mission Orange accent `#E8521A` (or NASA blue `#1B4FBF`). Chrome metallic: `#C0C0C0` / `#A8A8A8` for borders and structural lines. No neon. No pastels.
3. **Geometry (Pods):** Primary containers: `border-radius: 24px–40px`. Buttons: `border-radius: 48px` (capsule). Icon containers: `border-radius: 50%`. No sharp corners on interactive surfaces. Hard-edged geometric shapes only as decorative background elements.
4. **Typography:** `font-family: 'Euclid Circular', 'DM Sans', 'Neue Haas Grotesk', sans-serif` — clean geometric humanist sans. Weight 400–600 for body, 700–800 for display. No slab serifs, no condensed display fonts, no italics.
5. **Motion:** Smooth `cubic-bezier(0.25, 0.46, 0.45, 0.94)` at 250–350ms. Hover: lift with `transform: translateY(-2px)` and `box-shadow: 0 8px 24px rgba(0,0,0,0.12)`. No hard mechanical clicks. No bounce.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use dark or obsidian backgrounds. Space Age Optimism is radiant, luminous, and warm-white.
- **NEVER** use multiple accent colors. The contrast of ONE vivid accent against white is the entire visual power move.
- **NEVER** use heavy black brutalist borders (`3px solid #000`). Boundaries are fine chrome lines or no lines at all.
- **NEVER** use grunge, halftone, or analog texture. This aesthetic is precision-molded, clean, and futuristic.
- **NEVER** use sharp angular 0px corners on primary containers. Organic curves are essential — minimum 16px radius on cards.
- **NEVER** use neon fluorescent colors. The palette is warm-spectrum, natural material–inspired.
- **NEVER** use condensed aggressive display type. Type is wide, geometric, optimistic, and spacious.

---

## Space Age Optimism — Design Tokens

## Color Tokens

```css
:root {
  /* Warm White & Chrome Canvas */
  --color-space-white: #FAFAF8;
  --color-space-chrome: #F0EFEB;
  --color-space-silver: #E4E2DC;
  --color-space-dark: #1C1C1A;

  /* Accent: Choose ONE */
  --color-accent-orange: #FF5C00;    /* NASA Mission Orange */
  --color-accent-red: #E82528;       /* Atomic Age Red */
  --color-accent-green: #00B87C;     /* Mission Console Green */

  /* Typography */
  --color-text-primary: #1C1C1A;
  --color-text-secondary: #4A4A46;
  --color-text-muted: #8C8C88;
  --color-text-on-accent: #FFFFFF;
}
```

## Border Radius Tokens

```css
:root {
  --radius-pod-sm: 16px;
  --radius-pod-md: 24px;
  --radius-pod-lg: 40px;
  --radius-capsule: 9999px;  /* For pill-shaped nav items and tags */
  /* 0px radius is FORBIDDEN on primary containers */
}
```

## Shadow Tokens

```css
:root {
  /* Warm, small, diffuse — evokes plastic casting seam depth */
  --shadow-pod-sm: 0 2px 8px rgba(28, 28, 26, 0.08), 0 1px 2px rgba(28, 28, 26, 0.04);
  --shadow-pod-md: 0 4px 20px rgba(28, 28, 26, 0.1), 0 1px 4px rgba(28, 28, 26, 0.06);
  --shadow-pod-lg: 0 8px 40px rgba(28, 28, 26, 0.12);
  /* Heavy black hard-offset shadows: FORBIDDEN */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '24px',
        pod: '24px', 'pod-lg': '40px', capsule: '9999px',
        none: '0px', sm: '8px', md: '16px', lg: '24px', xl: '32px',
      },
      boxShadow: {
        'pod-sm': '0 2px 8px rgba(28, 28, 26, 0.08), 0 1px 2px rgba(28, 28, 26, 0.04)',
        'pod-md': '0 4px 20px rgba(28, 28, 26, 0.10)',
        DEFAULT: '0 4px 20px rgba(28, 28, 26, 0.10)',
      },
      colors: {
        space: {
          white: '#FAFAF8', chrome: '#F0EFEB', silver: '#E4E2DC',
          dark: '#1C1C1A', orange: '#FF5C00', red: '#E82528', green: '#00B87C',
        }
      }
    }
  }
}
```

---

## Space Age Optimism — Typography

## Recommended Font Stacks

### Primary Geometric Sans
- `Futura` (if available via system or embed)
- `ITC Avant Garde Gothic`
- `Nunito` (as modern fallback — rounded, geometric)
- `Raleway` (300/400/600)
- `Josefin Sans` (300/400/600)
- `DM Sans` (300/400)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Mission** | 52px - 68px | 300 Light / 600 SemiBold | +0.04em | 1.15 | Title case / UPPERCASE |
| **H1** | 36px - 44px | 400 / 600 | +0.02em | 1.25 | Title case |
| **H2** | 26px - 32px | 400 / 500 | +0.01em | 1.30 | Title case |
| **H3** | 18px - 22px | 500 / 600 | 0.00em | 1.40 | Title case |
| **Body** | 15px - 16px | 300 / 400 Light | +0.01em | 1.60 | Sentence |
| **Mission Tag** | 11px - 12px | 600 | +0.12em | 1.20 | UPPERCASE |

## Rules

1. **Generous Tracking on Headings:** Space Age type breathes — tracking from +0.02em to +0.12em.
2. **Light-to-Regular Weight Range:** Heavy display type (700–900) feels aggressive, not optimistic.
3. **Capsule Category Tags:** Short uppercase labels inside pill-radius capsules with accent border.

## Anti-Patterns
- **Heavy compressed grotesks**: Too aggressive and earthbound.
- **Warm slab serifs**: Evokes retro Americana, not clean space-age.
- **Monospace / terminal fonts**: That's Cyberpunk, not Space Age.

---

## Space Age Optimism — Layout

## Composition Rules

1. **Pod-Form Card Grid:** Cards are rounded capsule containers (`border-radius: 24px–40px`) floating on warm white, separated by generous gutters.
2. **Concentric Circle Accents:** Decorative SVG moiré-style concentric circles used as section dividers or background motifs (hairline strokes in chrome gray).
3. **Wide Single-Column Focus:** Many Space Age interfaces use generous centered single-column reading lines (65–75ch) with heroic whitespace margins.
4. **Floating Capsule Navigation:** Pill navigation bar centered horizontally, floating 20px from top viewport edge, with subtle pod shadow.

## Layout Anti-Patterns
- **Dense data grids:** This aesthetic is spacious and breathing, not compressed.
- **Hard-edge section backgrounds with 0px joins:** Sections flow with organic curves or simply white continuation.
- **Scattered asymmetric layouts:** Space Age is structured and architectural — not chaotic.

---

## Space Age Optimism — Component Rules

## 1. Buttons

### Primary — Mission Capsule
- **Background:** Accent Orange `#FF5C00`
- **Color:** `#FFFFFF`
- **Border:** `none`
- **Border Radius:** `9999px` (capsule pill)
- **Shadow:** `0 4px 16px rgba(255, 92, 0, 0.35)`
- **Font:** 14px Geometric sans, weight 600, tracking +0.04em, UPPERCASE
- **Padding:** 14px 32px
- **Hover:** Shadow expands: `0 6px 24px rgba(255, 92, 0, 0.5)`, slight lift `translateY(-2px)`
- **Active:** `translateY(1px)`, shadow reduces

### Secondary — Chrome Outline Capsule
- **Background:** Transparent
- **Border:** `1.5px solid #8C8C88`
- **Border Radius:** `9999px`
- **Color:** `#1C1C1A`
- **Hover:** Border shifts to accent orange, text shifts to accent

## 2. Cards

- **Background:** `#FAFAF8` or warm chrome `#F0EFEB`
- **Border Radius:** `24px` or `32px`
- **Border:** none or `1px solid #E4E2DC`
- **Shadow:** `0 4px 20px rgba(28, 28, 26, 0.10)`
- **Padding:** 32px to 40px

## 3. Inputs

- **Border Radius:** `12px` or `9999px` (capsule style)
- **Border:** `1.5px solid #E4E2DC`
- **Background:** `#FAFAF8`
- **Focus:** Border becomes accent orange, `box-shadow: 0 0 0 3px rgba(255, 92, 0, 0.15)`

## 4. Tags & Labels

- **Shape:** Capsule pill (`rounded-full`)
- **Background:** Chrome `#F0EFEB`
- **Border:** `1.5px solid #E4E2DC`
- **Font:** 11px, weight 600, UPPERCASE, tracking +0.08em
- **Accent variant:** Accent orange background, white text

---

## Space Age Optimism — Motion

## Philosophy

Motion is smooth, confident, and slightly slower than the modern web default — like a Space Age mechanism opening precisely. No snap-cuts, no bounces. Deliberate, elegant, purposeful kinetics.

## Tokens

```css
:root {
  --duration-space-quick: 200ms;
  --duration-space-standard: 350ms;
  --duration-space-slow: 500ms;
  --ease-space: cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Classic ease-out */
  --ease-space-in-out: cubic-bezier(0.45, 0, 0.55, 1);
}
```

## Transitions

1. **Button hover lift:** 200ms `ease-out`, `translateY(-2px)`, shadow glow expands.
2. **Card reveal on scroll:** Scale `0.97 → 1.0`, opacity `0 → 1`, 350ms.
3. **Navigation capsule active indicator:** 200ms sliding underline or background fill.

## Anti-Patterns
- No spring bounces or rubber-band effects.
- No sub-100ms snap transitions.
- No glitch or flicker effects (that's Cyberpunk).
