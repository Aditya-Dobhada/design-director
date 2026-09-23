---
name: style-quiet-luxury
description: Implementation rules for Quiet Luxury style. Warm alabaster and ecru palettes, immaculate serif headings with whisper-thin hairlines, zero border-radius, generous literary whitespace, and slow graceful cinematic easing.
---

# Style Pack: Quiet Luxury

A design language founded on discretion, bespoke craft, understatement, and expansive breathing room. Rather than clamoring for attention with loud accents or heavy borders, Quiet Luxury achieves authority through typographic perfection, tactile paper tones, and radical restraint.

## Core Principles

1. **Typography:** `font-family: 'Cormorant Garamond', Georgia, serif` at `font-weight: 300–400` for all h1–h2. Body copy: `Suisse Int'l` or `Neue Haas Unica` at weight 300–400, 17–18px, 1.65 line-height. Never Inter, Helvetica, or Roboto for display headings.
2. **Color:** Canvas `#FBFBF9` (warm alabaster). Primary text `#1C1C1A`. Stone dividers `#E8E4DF`. Single deep-ink accent `#2C2C28`. No bright hues, no Tailwind color classes except `bg-neutral-*`, `text-neutral-*` (custom values only).
3. **Geometry:** `border-radius: 0px` on all containers, cards, and buttons. No `rounded-*` Tailwind class except `rounded-none`. No drop shadows — separation via 1px stone dividers `#E8E4DF`.
4. **Spacing:** Minimum 80px section padding. Grid gutters ≥ 40px. Never collapse to mobile gutters < 24px. Whitespace IS the design — never fill it.
5. **Motion:** Max 300ms ease transitions. `cubic-bezier(0.4, 0, 0.2, 1)` only. No bounce, spring, or keyframe animations. No parallax.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners (`rounded-md`, `rounded-lg`, `rounded-full`). Border-radius must be strictly `0px` (`rounded-none`).
- **NEVER** use dark or blurry drop shadows (`box-shadow: 0 4px 12px rgba(0,0,0,0.15)`). Shadows must be `none`.
- **NEVER** use high-saturation neon or primary colors (e.g. electric blue, bright red, hot pink). All accents are muted earth or mineral tones (champagne, warm espresso, olive bronze, muted brass).
- **NEVER** use heavy borders (`border: 2px` or `3px`). Borders are at most `1px solid rgba(0,0,0,0.08)`.
- **NEVER** crowd content into dense multi-row card grids. Whitespace is the primary asset; margins must be wide and unhurried.
- **NEVER** use bouncy, elastic, or frantic animations. Motion must be slow, fluid, and cinematic (400ms to 600ms).
- **NEVER** use badges with colored pills (`bg-green-100 text-green-800`). Labels are small-caps text with generous letter-spacing.

---

## Quiet Luxury — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Warm Alabaster & Ecru Canvas */
  --color-bg-base: #FBFBF9;       /* Alabaster / Chalk Paper */
  --color-bg-surface: #F5F2EB;    /* Warm ecru panel */
  --color-bg-subtle: #EBE7DF;     /* Muted linen tone */

  /* Ink & Typography */
  --color-text-primary: #1C1A17;  /* Deep Espresso Ink (never pure #000) */
  --color-text-secondary: #59554E;/* Warm Umber */
  --color-text-muted: #8C867A;    /* Weathered Stone */

  /* Hairlines & Boundaries */
  --color-border-hairline: rgba(28, 26, 23, 0.08);
  --color-border-stone: #E4E0D6;

  /* Restrained Mineral Accents */
  --color-accent-bronze: #8A7258;
  --color-accent-champagne: #C8B89C;
  --color-accent-charcoal: #2C2926;
}
```

## Border Radius Tokens

```css
:root {
  --radius-default: 0px;  /* STRICT RULE: Zero radius across all components */
  --radius-max: 0px;      /* Any rounded-md/lg/full is a hard violation */
}
```

## Shadow & Depth Tokens

```css
:root {
  --shadow-none: none;    /* Elevated states use tonal color shifts, never blurry shadows */
  --shadow-subtle-tone: 0 1px 0 rgba(28, 26, 23, 0.04);
}
```

## Spacing & Metrics

```css
:root {
  --space-unit: 8px;
  --space-editorial-sm: 16px;
  --space-editorial-md: 32px;
  --space-editorial-lg: 64px;
  --space-editorial-xl: 96px;
  --space-editorial-2xl: 128px;
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
        luxury: {
          base: '#FBFBF9',
          surface: '#F5F2EB',
          subtle: '#EBE7DF',
          espresso: '#1C1A17',
          umber: '#59554E',
          stone: '#8C867A',
          border: '#E4E0D6',
          bronze: '#8A7258',
          champagne: '#C8B89C',
        }
      }
    }
  }
}
```

---

## Quiet Luxury — Typography

## Type System Principles

Typography is the supreme carrier of brand identity. It relies on exquisite, high-contrast editorial serifs for headings, paired with a disciplined, understated neo-grotesk or humanist sans for body copy. Tracking is deliberate: generous on small capitals, natural and comfortable on body prose.

## Recommended Font Stacks

### Headings (Display / H1 / H2)
- `Cormorant Garamond`
- `Fraunces`
- `Canela`
- `Ogg`
- `Minion Pro`
- `Playfair Display` (Light / Regular weights only)

### Body & Functional Text
- `Inter Tight`
- `Geist Sans`
- `Tenor Sans`
- `Neue Haas Unica`
- `Source Serif 4` (for long-form editorial reading)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 48px - 68px | 300 / 400 Light | -0.015em | 1.15 | Sentence case |
| **H1** | 36px - 44px | 400 Regular | -0.01em | 1.25 | Sentence case |
| **H2** | 26px - 32px | 400 Regular / Italic | 0.00em | 1.30 | Sentence case |
| **H3** | 18px - 22px | 500 Medium | +0.02em | 1.40 | Sentence case |
| **Body (Default)** | 15px - 16px | 400 Regular | +0.01em | 1.65 | Sentence case |
| **Eyebrow / Overline**| 11px - 12px | 500 Medium | +0.15em | 1.30 | UPPERCASE |
| **Caption / Note** | 12px - 13px | 400 Regular | +0.04em | 1.50 | Sentence case |

## Typographic Rules

1. **Light to Regular Weights:** Avoid heavy bolding (weights 700-900 are forbidden). Contrast is created through font size scale and italicized serif accents, not brute force weight.
2. **Generous Letter-Spacing on Uppercase:** Small uppercase metadata labels use tracking between `+0.12em` and `+0.18em`.
3. **Warm Ink Color:** Text is styled in deep espresso (`#1C1A17`), never harsh `#000000`.

## Anti-Patterns (Fonts to Avoid)
- **Monospace fonts for non-code:** Monospaced type disrupts the bespoke, tailored atmosphere.
- **Heavy Display Sans** (`Impact`, `Archivo Black`): Far too loud and aggressive.
- **Quirky or Playful fonts**: Clashes with quiet sophistication.

---

## Quiet Luxury — Layout & Spatial Composition

## Grid & Composition Rules

1. **Expansive Whitespace:**
   - Margins and padding are generous (desktop section vertical padding: 96px to 144px).
   - Content breathes. Avoid dense clusters of cards.
2. **Editorial Column Splits:**
   - Asymmetric two-column layouts: e.g. Left column (35% width) holds a lingering typographic premise or sticky table of contents; Right column (65% width) contains flowing narrative and quiet artifact cards.
3. **Hairline Boundaries:**
   - Sections are separated by delicate 1px borders in warm stone (`border-t border-[#E4E0D6]` or `rgba(28, 26, 23, 0.08)`).
4. **Header Architecture:**
   - Minimalist, non-sticky or silently integrated header. Centered brand serif wordmark with spaced navigation links on either side.

## Layout Anti-Patterns
- **Dense 4-Column Metric Grids:** Do not cram 4 metric boxes side-by-side with colored trend indicators.
- **Card-Soup UI:** Stacking 10 bordered cards in a row feels like an enterprise admin dashboard, not quiet luxury.
- **Sticky Floating Action Widgets:** No floating contact buttons or chat bubbles hovering in the bottom right corner.

---

## Quiet Luxury — Component Rules

Concrete specifications for core UI components.

## 1. Buttons & Interactive Links

### Primary Action
- **Border Radius:** `0px` (`rounded-none`).
- **Background:** Deep Espresso (`#1C1A17`) or Warm Charcoal (`#2C2926`).
- **Color:** Warm Alabaster (`#FBFBF9`).
- **Font:** 13px - 14px, weight 500, letter-spacing +0.06em, uppercase or sentence case.
- **Padding:** 14px 28px.
- **Border:** 1px solid `#1C1A17`.
- **Hover State:** Background shifts gently to `#383430` over 350ms. No scale, no shadow expansion.

### Underline Editorial Link
- **Shape:** Text element with an offset bottom hairline border (`border-b border-[#1C1A17] pb-1`).
- **Hover State:** Underline expands or deepens in tone; subtle rightward arrow translation (2px).

## 2. Cards & Panels

- **Border Radius:** `0px` (`rounded-none`).
- **Border:** 1px solid `#E4E0D6` or none (demarcated solely by subtle tonal shift from `#FBFBF9` to `#F5F2EB`).
- **Shadow:** None (`box-shadow: none`).
- **Padding:** 36px to 48px.
- **Typography Inside Card:** Editorial serif card title, followed by generous leading body text.

## 3. Inputs & Forms

- **Border Radius:** `0px` (`rounded-none`).
- **Border:** Bottom-border only (`border-b 1px solid #C8B89C` or `#D6D2C8`), background transparent.
- **Background:** Transparent.
- **Padding:** 12px 0px.
- **Focus State:** Bottom border deepens to `#1C1A17` over 300ms. No glowing rings.
- **Placeholder:** 14px, warm stone `#8C867A`, italicized serif or quiet sans.

## 4. Status Indicators & Metadata

- **Shape:** Text-only metadata with letter-spacing +0.12em.
- **Prefix:** Delicate typographic bullet (`•`) or small Roman numeral (`I.`, `II.`).
- **Anti-Pattern:** Never use colored pill badges with rounded borders.

---

## Quiet Luxury — Motion & Transitions

## Motion Philosophy

Motion is cinematic, unhurried, and poised. Transitions feel like turn-of-the-century film cuts or pages turning in a cloth-bound book. Zero bouncy springs, zero abrupt jarring cuts.

## Timing & Easing Curves

```css
:root {
  --duration-luxury-fast: 250ms;
  --duration-luxury-standard: 400ms;
  --duration-luxury-slow: 600ms;

  /* Custom cubic bezier for smooth, graceful deceleration */
  --ease-luxury: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-luxury-in-out: cubic-bezier(0.65, 0, 0.35, 1);
}
```

## Transition Specifications

1. **Button & Link Hover:**
   - Duration: `350ms`
   - Timing: `var(--ease-luxury)`
   - Property: `background-color, color, border-color`
2. **Page Section Reveals:**
   - Smooth subtle fade: opacity 0 -> 1, translateY(12px -> 0px) over 600ms.
3. **Image / Card Tonal Shift:**
   - Smooth subtle opacity or filter transition over 500ms.

## Motion Anti-Patterns
- **No Spring / Rubber-band Physics:** Strict prohibition against spring overshoots.
- **No Frantic Short Durations:** Durations under 150ms feel rushed and nervous.
