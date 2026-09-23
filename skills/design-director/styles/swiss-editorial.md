---
name: style-swiss-editorial
description: Implementation rules for Swiss / Editorial style. Asymmetric grids, rigorous typography hierarchy, high-contrast monochrome with single deliberate accent, zero-or-hairline borders, and zero-blur elevation.
---

# Style Pack: Swiss / Editorial

A visual language grounded in the International Typographic Style and contemporary editorial broadsheets. Built on mathematical precision, asymmetric column grids, deliberate scale contrast, and total absence of decorative fluff.

## Mandatory Anti-Patterns

- **NEVER** use pill-shaped buttons (`rounded-full`, `border-radius: 9999px`). Radius must be 0px (`rounded-none`) or maximum 2px (`rounded-sm`).
- **NEVER** use diffuse, blurred box-shadows (`box-shadow: 0 10px 25px rgba(...)` or Tailwind `shadow-lg`, `shadow-xl`). Elevation is conveyed through 1px border lines or solid 1px/2px hard offset lines.
- **NEVER** use rainbow or multi-hue accent colors. Pick exactly ONE accent color and use it strictly for primary actions and active states.
- **NEVER** use floating gradient orbs, blurred mesh backdrops, or decorative background blobs.
- **NEVER** use icon-only decorative chips, pastel badge pills, or cartoonish illustrations.
- **NEVER** center-align long blocks of prose or primary hero copy. Align to left margins with deliberate typographic rag.
- **NEVER** use generic low-contrast gray text (`#9CA3AF`). Secondary text must remain crisp and readable (e.g., `#525252` on light, `#A3A3A3` on dark).

---

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

---

## Typography

### Recommended Font Stacks
- **Headings (Display / H1 / H2):** `Playfair Display`, `Newsreader`, `Instrument Serif`, or `Bodoni MT`, serif
- **Body & Functional (H3 / Body / Metadata):** `Inter`, `Helvetica Neue`, `Neue Haas Grotesk`, sans-serif
- **Metadata / Accents:** `JetBrains Mono`, `Space Mono`, monospace

### Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 56px - 72px | 700 / Bold or 400 Italic Serif | -0.03em | 1.05 | Sentence case |
| **H1** | 40px - 48px | 600 / SemiBold | -0.025em | 1.15 | Sentence case |
| **H2** | 28px - 32px | 600 / SemiBold | -0.02em | 1.25 | Sentence case |
| **H3 / Section** | 20px - 22px | 500 / Medium | -0.01em | 1.35 | Sentence case |
| **Body (Default)** | 15px - 16px | 400 / Regular | 0.00em | 1.55 | Sentence case |
| **Small / Meta** | 12px - 13px | 500 / Medium | +0.04em | 1.40 | Uppercase or Sentence |
| **Eyebrow / Overline**| 11px - 12px | 600 / SemiBold | +0.10em | 1.20 | UPPERCASE |

### Typographic Rules
1. **Left Alignment Only:** Center-aligned body text and multi-line headings are forbidden. Left-align copy with clean ragging.
2. **Tabular Numerals:** Use `font-variant-numeric: tabular-nums` for all pricing, statistics, data tables, and metrics.
3. **Metadata Footers:** Mark metadata, timestamps, and categories with uppercase small type and generous letter-spacing (+0.04em to +0.10em).
4. **Banned Fonts:** `Comic Sans`, `Papyrus`, `Pacifico`, rounded sans (`Quicksand`, `Comfortaa`, `Nunito`), and generic geometric templates (`Poppins`, `Montserrat`).

---

## Layout & Spatial Composition

1. **Modular 12-Column Asymmetric Grid:**
   - Divide layouts asymmetrically: 4 cols (Index / Summary) + 8 cols (Primary Editorial Stream), or 5 cols (Statement) + 7 cols (Evidence / Metrics).
2. **Explicit Structural Lines:**
   - Section breaks are marked by crisp 1px horizontal hairlines spanning full viewport width or grid bounds (`border-t border-black` or `border-neutral-200`).
   - Vertical column boundaries can use 1px hairline dividers between content blocks.
3. **Whitespace Discipline:**
   - Margins: 32px (mobile), 64px to 96px (desktop). Spacing between major editorial blocks: 64px to 120px.
4. **Anti-Pattern Layouts:**
   - No centered SaaS feature cards (3 identical cards with soft circles).
   - No card-soup UI: let typography and rule-lines structure content rather than wrapping everything in elevated boxes.
   - No floating detached navbar pills with blurred backdrops. Use top-pinned, sharp-edged architectural headers.

---

## Component Rules

### 1. Buttons
- **Primary:** Sharp rectangle (`border-radius: 0px` or `2px`). Solid black (`#111111`) or accent (`#E30613`). Text white (`#FFFFFF`), 14px, weight 500. Padding: 10px 20px (Desktop), 8px 16px (Compact). Border: 1px solid `#111111` or `#E30613`. Hover: `#2A2A2A` or `#BF0410`. Active: 1px press down or inverse color flip.
- **Secondary / Outline:** Sharp rectangle (`0px` or `2px`). Transparent or white (`#FFFFFF`). Text solid black (`#111111`), 14px, weight 500. Border: 1px solid `#111111`. Hover: Inverts to `#111111` background, `#FFFFFF` text.
- **Text Action:** Inline text with 1px solid underline. Hover: underline thickens to 2px or switches to accent.

### 2. Cards & Containers
- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#E5E5E5` or `#111111`. Never 2px soft pastel.
- **Shadow:** None (`box-shadow: none`) or hard 2px solid black offset (`2px 2px 0px #111111`).
- **Padding:** 24px to 32px.
- **Internal Dividers:** 1px hairline horizontal divider between card header and body.

### 3. Inputs & Forms
- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#CCCCCC` or bottom-border only (`border-b border-black`).
- **Background:** `#FFFFFF` or `#F8F8F6`.
- **Focus State:** 1px solid `#111111` outline, or bottom-border 2px solid `#111111`. No diffuse glow.
- **Placeholder:** Text muted `#737373`, italicized serif or neutral sans.

### 4. Badges & Status Chips
- **Shape:** Sharp rectangular tags (`border-radius: 0px`).
- **Border:** 1px solid `#111111` or `#E5E5E5`. Background: `#F2F2F0` or `#FFFFFF`.
- **Typography:** 11px uppercase, medium weight, tracking +0.06em.
- **Anti-Pattern:** Never use rounded pill badges with soft colored backgrounds (`rounded-full`).

### 5. Tables & Data Display
- **Borders:** Crisp horizontal 1px lines (`#E5E5E5`). No vertical column borders.
- **Headers:** 12px uppercase, tracking +0.05em, text muted `#4A4A4A`.
- **Numbers:** Tabular figures, right-aligned.

---

## Motion & Transitions

```css
:root {
  --duration-instant: 80ms;
  --duration-snappy: 140ms;
  --duration-standard: 200ms;
  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-linear: cubic-bezier(0, 0, 1, 1);
}
```

- **Hover Transitions:** `background-color`, `color`, `border-color` over 140ms with `var(--ease-editorial)`.
- **Page Shifts:** Opacity 0 -> 1, transform translateY(6px -> 0px) over 200ms.
- **Disclosures:** Snappy 180ms ease-out with zero overshoot.
- **Motion Anti-Patterns:** No bouncy springs (`cubic-bezier(0.34, 1.56, ...)`), no floating hover elevators (`translateY(-6px)` with expanding blur shadows), and no parallax backgrounds.
