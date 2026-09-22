---
name: style-swiss-editorial
description: Implementation rules for Swiss / Editorial style. Asymmetric grids, rigorous typography hierarchy, high-contrast monochrome with single deliberate accent, zero-or-hairline borders, and zero-blur elevation.
---

# Style Pack: Swiss / Editorial

A visual language grounded in the International Typographic Style (Swiss Style) and contemporary high-end editorial broadsheets. Built on mathematical precision, asymmetric column grids, deliberate scale contrast, and total absence of decorative fluff.

## Core Principles

1. **Typography:** `font-family: 'Suisse Int\'l', 'Neue Haas Unica', Helvetica, sans-serif` for all body/UI. Editorial display: `Suisse Works` (serif) or `Playfair Display` at weight 700–900. Scale: 11px caption → 14px body → 22px section → 48px display. Never mix more than 2 type families.
2. **Color:** Canvas `#FFFFFF` or `#F8F8F6`. Primary `#0A0A0A`. Single accent (one of: vermilion `#E63946`, electric blue `#0052CC`, or warm amber `#F4A261`). No gradients. No Tailwind `bg-gray-*` — use custom CSS values.
3. **Geometry:** `border-radius: 0px` universally. Hairlines: `1px solid #0A0A0A` or `0.5px solid rgba(0,0,0,0.2)`. No box-shadow blur > 0px. Grid: strict 12-column, 8px baseline.
4. **Layout:** At least one asymmetric text offset per page section. Column text at 60–70% width max. Large typographic numbers as graphic elements (420px+ at breakpoints).
5. **Motion:** 150–200ms linear or ease-out transitions. No easing bounce. Page transitions: instant or 100ms fade — never slide.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use pill-shaped buttons (`rounded-full`, `border-radius: 9999px`). Radius must be 0px (`rounded-none`) or maximum 2px (`rounded-sm`).
- **NEVER** use diffuse, blurred box-shadows (`box-shadow: 0 10px 25px rgba(...)` or Tailwind `shadow-lg`, `shadow-xl`). Elevation is conveyed through 1px border lines or solid 1px/2px hard offset lines.
- **NEVER** use rainbow or multi-hue accent colors. Pick exactly ONE accent color and use it strictly for primary actions and active states.
- **NEVER** use floating gradient orbs, blurred mesh backdrops, or decorative background blobs.
- **NEVER** use icon-only decorative chips, pastel badge pills, or cartoonish illustrations.
- **NEVER** center-align long blocks of prose or primary hero copy. Align to left margins with deliberate typographic rag.
- **NEVER** use generic low-contrast gray text (`#9CA3AF`). Secondary text must remain crisp and readable (e.g., `#525252` on light, `#A3A3A3` on dark).

---

## Swiss / Editorial — Design Tokens

Exact tokens for CSS variables and Tailwind configuration. Coding agents must adhere strictly to these token definitions.

## Color Tokens

```css
:root {
  /* Surface & Base */
  --color-bg: #FFFFFF;
  --color-bg-paper: #F8F8F6;
  --color-surface: #FFFFFF;
  --color-surface-subtle: #F2F2F0;

  /* Typography / Ink */
  --color-text-primary: #111111;
  --color-text-secondary: #4A4A4A;
  --color-text-muted: #737373;
  --color-text-inverse: #FFFFFF;

  /* Lines & Dividers */
  --color-border: #111111;
  --color-border-subtle: #E5E5E5;
  --color-border-hairline: rgba(17, 17, 17, 0.12);

  /* Intentional Accent (Pick ONE: Red, Klein Blue, or Hunter Green) */
  --color-accent: #E30613; /* Swiss International Red */
  --color-accent-hover: #BF0410;
  --color-accent-subtle: #FDF2F2;

  /* Alternative Accent Option: Klein Blue: #002FA7, Hunter Green: #143829 */
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px;        /* Standard default for all cards, containers, inputs */
  --radius-subtle: 2px;      /* Maximum allowed on interactive micro-elements */
  --radius-max: 2px;         /* HARD LIMIT: rounded-md, rounded-lg, rounded-full are FORBIDDEN */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-none: none;
  --shadow-hairline: 0 0 0 1px var(--color-border-subtle);
  --shadow-solid-offset: 2px 2px 0px #111111;
  /* HARD LIMIT: blur-radius > 0px is FORBIDDEN on cards, modals, and buttons */
}
```

## Spacing & Grid Tokens

```css
:root {
  --space-2: 8px;
  --space-3: 12px;
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
        sm: '2px',
        md: '2px', // Override to prevent inadvertent rounding
        lg: '2px', // Override
        full: '2px', // Strict ban on pills
      },
      boxShadow: {
        DEFAULT: 'none',
        hairline: '0 0 0 1px #E5E5E5',
        solid: '2px 2px 0px #111111',
      },
      colors: {
        swiss: {
          bg: '#FFFFFF',
          paper: '#F8F8F6',
          ink: '#111111',
          secondary: '#4A4A4A',
          border: '#E5E5E5',
          accent: '#E30613',
        }
      }
    }
  }
}
```

---

## Swiss / Editorial — Typography

## Type System Principles

The typography system relies on stark contrasts in size, weight, and classification. It pairs an authoritative editorial serif or stark grotesque display with an objective, highly legible body neo-grotesk.

## Recommended Font Stacks

### Option A: Editorial Broadside (Serif Headings + Neo-Grotesk Body)
- **Headings (Display / H1 / H2):** `Playfair Display`, `Newsreader`, `Instrument Serif`, `Cormorant Garamond`, or `Bodoni MT`, serif
- **Body & Functional (H3 / Body / Code / Badges):** `Inter`, `Neue Haas Grotesk`, `Helvetica Neue`, `Arial`, sans-serif
- **Metadata / Accents:** `JetBrains Mono`, `Space Mono`, monospace

### Option B: Pure Neo-Grotesk (Purist International Style)
- **Headings & Body:** `Inter`, `Helvetica Neue`, `Neue Haas Grotesk`, `Geist Sans`, sans-serif
- **Execution:** Extreme scale ratios (Display: 56px Bold / Body: 14px Regular), tight negative tracking on display titles, generous line-height on text.

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 56px - 72px | 700 / Bold or 400 Italic Serif | -0.03em | 1.05 | Sentence case |
| **H1** | 40px - 48px | 600 / SemiBold | -0.025em | 1.15 | Sentence case |
| **H2** | 28px - 32px | 600 / SemiBold | -0.02em | 1.25 | Sentence case |
| **H3 / Section** | 20px - 22px | 500 / Medium | -0.01em | 1.35 | Sentence case |
| **Body (Default)** | 15px - 16px | 400 / Regular | 0.00em | 1.55 | Sentence case |
| **Small / Meta** | 12px - 13px | 500 / Medium | +0.04em | 1.40 | Uppercase or Sentence |
| **Eyebrow / Overline**| 11px - 12px | 600 / SemiBold | +0.10em | 1.20 | UPPERCASE |

## Typographic Rules

1. **Left Alignment Only:** Center-aligned body text and multi-line headings are forbidden. Left-align copy with intentional, clean ragging.
2. **Tabular Numerals:** Use `font-variant-numeric: tabular-nums` for all pricing, statistics, data tables, and metrics.
3. **Subtle Metadata Footers:** Mark metadata, timestamps, and categories with uppercase small type and generous letter-spacing.
4. **No Artificial Bolding:** Do not use bold weight (700) on long paragraphs. Use weight shifts strictly for semantic anchors.

## Anti-Patterns (Fonts to Avoid)
- **Comic Sans, Papyrus, Pacifico** (obviously)
- **Rounded Sans** (`Quicksand`, `Comfortaa`, `Nunito`): Destroys the disciplined architectural feel.
- **Overly generic geometric sans** (`Poppins`, `Montserrat`): Read as generic template landing pages.

---

## Swiss / Editorial — Layout & Spatial Composition

## Grid & Structural Foundation

1. **Modular 12-Column Asymmetric Grid:**
   - Instead of symmetrical 3-column or 4-column card matrices, divide layouts asymmetrically:
     - 4 cols (Sidebar / Overview / Index) + 8 cols (Primary Content / Editorial Stream)
     - 5 cols (Hero Statement / Thesis) + 7 cols (Supporting Evidence / Metric Matrix)
2. **Explicit Structural Lines:**
   - Section breaks are marked by crisp 1px horizontal hairlines spanning full viewport width or grid bounds (`border-t border-black` or `border-neutral-200`).
   - Vertical column boundaries can have visible 1px hairline dividers between content blocks.
3. **Generous White & Paper Space:**
   - Margins: 32px (mobile), 64px to 96px (desktop).
   - Generous breathing space between major editorial blocks (64px to 120px) creates gravitas and focus.
4. **Number-Indexed Sections:**
   - Prefix major sections or lists with tabular numeral indices (`01 /`, `02 /`, `[03]`) in small monospace or small-caps.

## Anti-Pattern Layouts
- **Centered SaaS Feature Cards:** The classic "3 identical rounded cards in a row with purple icons in soft circles" is strictly prohibited.
- **Card-Soup UI:** Do not wrap every piece of content in its own bordered, elevated box. Let typography and rule-lines structure the content.
- **Floating Pill Navbars:** Floating detached navigation pills with blurred backdrops are prohibited. Navigation must be a top-pinned, sharp-edged bar or minimalist architectural header line.

---

## Swiss / Editorial — Component Rules

Concrete specifications for core UI components. All values are strict and testable.

## 1. Buttons

### Primary Button
- **Shape:** Sharp rectangle (`border-radius: 0px` or `2px`). No pills.
- **Background:** Solid Black (`#111111`) or Accent (`#E30613`).
- **Text:** White (`#FFFFFF`), 14px, weight 500, letter-spacing +0.02em.
- **Padding:** 10px 20px (Desktop), 8px 16px (Compact).
- **Border:** 1px solid `#111111` or `#E30613`.
- **Hover State:** Background shifts to `#2A2A2A` or accent hover (`#BF0410`). No bounce, no scale pop.
- **Active State:** Instant 1px press down or inverse color flip.

### Secondary / Outline Button
- **Shape:** Sharp rectangle (`border-radius: 0px` or `2px`).
- **Background:** Transparent or Pure White (`#FFFFFF`).
- **Text:** Solid Black (`#111111`), 14px, weight 500.
- **Border:** 1px solid `#111111`.
- **Hover State:** Background inverts to `#111111`, text becomes `#FFFFFF`.

### Text / Underline Action
- **Shape:** Inline text with 1px solid underline.
- **Hover State:** Underline thickens to 2px or transitions color to accent.

## 2. Cards & Containers

- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#E5E5E5` or `#111111`. Never 2px soft pastel.
- **Shadow:** None (`box-shadow: none`). Alternatively, hard 2px solid black shadow (`box-shadow: 2px 2px 0px #111111`) if high contrast is needed.
- **Padding:** 24px to 32px.
- **Internal Dividers:** 1px hairline horizontal divider between card header and body.

## 3. Inputs & Forms

- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#CCCCCC` or bottom-border only (`border-b border-black`).
- **Background:** `#FFFFFF` or `#F8F8F6`.
- **Focus State:** 1px solid `#111111` outline, or bottom-border becomes 2px solid `#111111`. No diffuse blue/purple focus ring glow.
- **Placeholder:** Text muted `#737373`, italicized serif or neutral sans.

## 4. Badges & Status Chips

- **Shape:** Sharp rectangular tags (`border-radius: 0px`).
- **Border:** 1px solid `#111111` or `#E5E5E5`.
- **Background:** `#F2F2F0` or `#FFFFFF`.
- **Typography:** 11px uppercase, medium weight, letter-spacing +0.06em.
- **Anti-Pattern:** Never use rounded pill badges with soft colored backgrounds (`bg-blue-100 text-blue-700 rounded-full`).

## 5. Tables & Data Display

- **Borders:** Crisp horizontal 1px lines (`#E5E5E5`). No vertical column borders.
- **Headers:** 12px uppercase, tracking +0.05em, text muted `#4A4A4A`.
- **Numbers:** Tabular figures, right-aligned.

---

## Swiss / Editorial — Motion & Transitions

## Motion Philosophy

Motion is utilitarian, immediate, and restrained. It serves strictly to confirm state transitions and orient the eye across architectural shifts. Never use playful bounces, rubber-banding, or dramatic zooms.

## Timing & Easing Curves

```css
:root {
  /* Durations */
  --duration-instant: 80ms;
  --duration-snappy: 140ms;
  --duration-standard: 200ms;

  /* Easings */
  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-linear: cubic-bezier(0, 0, 1, 1);
}
```

## Transition Specifications

1. **Hover Transitions (Buttons & Links):**
   - Property: `background-color`, `color`, `border-color`
   - Duration: `140ms`
   - Timing Function: `cubic-bezier(0.16, 1, 0.3, 1)`
2. **Page & Section Shifts:**
   - Subtle vertical fade: opacity 0 -> 1, transform translateY(6px -> 0px)
   - Duration: `200ms`
3. **Disclosure / Accordion:**
   - Height transition with zero overshoot. Snappy 180ms ease-out.

## Motion Anti-Patterns
- **No Spring / Bouncy Physics:** `cubic-bezier(0.34, 1.56, 0.64, 1)` is strictly forbidden.
- **No Floating Hover Elevators:** Do not translate cards upwards with `translateY(-6px)` and expanding blur shadows.
- **No Parallax Backgrounds:** Static, architectural stability only.
