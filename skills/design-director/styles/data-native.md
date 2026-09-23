---
name: style-data-native
description: Implementation rules for Data Native style. Dense monospace-numeric tables, hairline dividers, dark #0D1117 canvas, restrained single-accent chroma, zero decorative elements. Domain: analytics, finance, telemetry.
---

# Style Pack: Data Native

A high-density, zero-ornamentation visual system engineered for raw data legibility. Every pixel serves the data. Monospace numerics, 32px compact table rows, hairline 1px dividers, and a single functional accent color. Built for analytics dashboards, financial terminals, and telemetry viewers where information density is the primary virtue.

## Core Principles

1. **Typography:** All numerics and metric values use `JetBrains Mono` or `IBM Plex Mono` at `font-variant-numeric: tabular-nums`. UI labels use `Inter` at 11px–12px, weight 400 (muted labels) or 500 (interactive). Never exceed 13px for secondary labels. Display headings max at 16px semi-bold. Tracking: `0em` on mono, `-0.01em` on sans labels.
2. **Color:** Default canvas `#0D1117` (dark). Surface panels `#161B22`. Primary text `#E6EDF3`. Secondary text `#8B949E`. Muted / tertiary `#484F58`. Single blue accent `#3B82F6` for interactive focus and links. Positive deltas only in `#22C55E`. Negative deltas in `#EF4444`. No other color is permitted for data values.
3. **Geometry:** Border radius hard cap of `4px`. Buttons and inputs: `4px`. Cards and panels: `4px`. Status indicators: `6px` circle (dot only — never pill badge). Never exceed `4px` radius on any container.
4. **Surfaces & Borders:** All dividers are `1px solid #1E2533`. Panel borders `1px solid #21262D`. No box-shadow elevation — panels are differentiated by background tone only. Zero decorative fills, gradients, or illustrations. Status is communicated only via `6px` colored SVG/CSS dots.
5. **Density:** Table rows fixed at `32px` height. Cell padding: `0 12px`. Column headers: 10px uppercase, `letter-spacing: 0.08em`, color `#8B949E`. Number cells right-aligned. Text cells left-aligned. Status cells center-aligned with dot indicator only.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use decorative chart fills, area gradients, or bubble chart visualizations — line and bar charts only, stroke-only style.
- **NEVER** use rounded pill badges or `border-radius` exceeding `4px` on any container or badge element.
- **NEVER** apply heavy card shadows (`box-shadow` with `blur > 4px` or opacity > `0.15`).
- **NEVER** use a multi-color accent palette — one blue for interactive, one green for positive delta, one red for negative delta. No orange, purple, or yellow accent.
- **NEVER** place illustrations, icons (beyond functional SVG status dots), or any decorative graphics near data regions.
- **NEVER** use gradient backgrounds — canvas and surfaces must be flat solid colors only.
- **NEVER** set table row height above `40px` or below `28px`; the standard is `32px`.

---

## Data Native — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Surface */
  --color-bg: #0D1117;
  --color-surface: #161B22;
  --color-surface-hover: #1C2128;
  --color-surface-active: #21262D;
  --color-surface-subtle: #0D1117;

  /* Typography */
  --color-text-primary: #E6EDF3;
  --color-text-secondary: #8B949E;
  --color-text-muted: #484F58;
  --color-text-inverse: #0D1117;

  /* Lines & Dividers */
  --color-border: #1E2533;
  --color-border-panel: #21262D;
  --color-border-hover: #30363D;

  /* Functional Accents */
  --color-accent: #3B82F6;
  --color-accent-hover: #2563EB;
  --color-accent-subtle: rgba(59, 130, 246, 0.08);

  /* Delta / Status */
  --color-positive: #22C55E;
  --color-negative: #EF4444;
  --color-neutral: #8B949E;
  --color-warning: #F59E0B;

  /* Status Dots */
  --dot-healthy: #22C55E;
  --dot-warning: #F59E0B;
  --dot-critical: #EF4444;
  --dot-inactive: #484F58;
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 2px;      /* Inline chips, micro tags */
  --radius-sm: 4px;      /* Buttons, inputs, cards — MAXIMUM allowed */
  --radius-md: 4px;      /* Panels, dropdowns — same cap */
  --radius-lg: 4px;      /* No exception — 4px hard cap on all containers */
  --radius-dot: 9999px;  /* Status dots only — circular */
}
```

## Shadow & Elevation Tokens

```css
:root {
  /* Elevation achieved via background tonal shift, not shadow */
  --shadow-none: none;
  --shadow-inset: inset 0 1px 0 0 rgba(255, 255, 255, 0.04);
  --shadow-panel: none; /* panels use border, not shadow */
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

  /* Table-specific */
  --table-row-height: 32px;
  --table-cell-padding: 0 12px;
  --table-header-height: 36px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '4px',
        sm: '2px',
        md: '4px',
        lg: '4px',     // Hard cap — never exceed
        full: '9999px', // Status dots only
      },
      boxShadow: {
        none: 'none',
        inset: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.04)',
      },
      colors: {
        canvas: '#0D1117',
        surface: '#161B22',
        border: '#1E2533',
        ink: {
          primary: '#E6EDF3',
          secondary: '#8B949E',
          muted: '#484F58',
        },
        accent: {
          DEFAULT: '#3B82F6',
          hover: '#2563EB',
          subtle: 'rgba(59, 130, 246, 0.08)',
        },
        delta: {
          positive: '#22C55E',
          negative: '#EF4444',
          neutral: '#8B949E',
          warning: '#F59E0B',
        },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono: ['JetBrains Mono', 'IBM Plex Mono', 'monospace'],
      },
      fontSize: {
        '2xs': ['10px', { lineHeight: '16px', letterSpacing: '0.08em' }],
        xs: ['11px', { lineHeight: '16px' }],
        sm: ['12px', { lineHeight: '18px' }],
        base: ['13px', { lineHeight: '20px' }],
        md: ['14px', { lineHeight: '20px' }],
        lg: ['16px', { lineHeight: '24px' }],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 28px (compact) or 32px (standard), `border-radius: 4px`, `font-size: 12px`, `font-weight: 500`, padding `0 10px`. Primary: `background: #3B82F6`. Secondary: `background: transparent; border: 1px solid #21262D`.
- **Table Rows:** Height `32px`, cell padding `0 12px`, `border-bottom: 1px solid #1E2533`. Numeric cells `font-family: JetBrains Mono; text-align: right; font-variant-numeric: tabular-nums`. Status cell: centered `6px` × `6px` circle dot only — no text badge.
- **Column Headers:** Height `36px`, `font-size: 10px`, `font-weight: 500`, `letter-spacing: 0.08em`, `text-transform: uppercase`, color `#8B949E`, `border-bottom: 1px solid #21262D`.
- **Panels / Cards:** `background: #161B22`, `border: 1px solid #1E2533`, `border-radius: 4px`, no box-shadow. Padding `16px`.
- **Status Dots:** Width/height `6px`, `border-radius: 9999px`. Inline with label, `4px` gap. Colors: healthy `#22C55E`, warning `#F59E0B`, critical `#EF4444`, inactive `#484F58`.
- **Inputs:** Height `28px`, `border-radius: 4px`, `border: 1px solid #21262D`, background `#0D1117`, `font-family: Inter; font-size: 12px`. Focus: `border-color: #3B82F6`.
