---
name: style-command-center
description: Implementation rules for Command Center style. Near-black #0B0D11 canvas, multi-panel functional grid, semantic status indicators (green/amber/red), compact Inter/JetBrains Mono typography. Domain: devops, security, infrastructure monitoring.
---

# Style Pack: Command Center

A mission-critical, zero-ambiguity visual system for real-time infrastructure, security, and DevOps dashboards. Every panel owns a distinct functional zone. Status is always explicit via semantic color. Typography stays tightly compact. No decorative surface survives — only operational signal.

## Core Principles

1. **Typography:** All UI text uses `Inter` at 11px–13px. Logs, metrics, and terminal output use `JetBrains Mono`. Label hierarchy: Section headers at 13px / 500 weight, inline labels at 11px / 400 weight, log lines at 11px mono. Tracking: `-0.01em` on UI labels, `0em` on mono. Never use a display font or serif in any panel.
2. **Color:** Canvas `#0B0D11`. Panels `#0F1219`. Borders `#1E2533`. Text primary `#E2E8F0`. Text secondary `#94A3B8`. Semantic status palette is strict: healthy `#22C55E`, warning `#F59E0B`, critical `#EF4444`, info `#3B82F6`. No other colors may appear except muted neutrals for scaffolding.
3. **Geometry:** Zero or 4px border-radius maximum on all panels and containers. Status pills: `border-radius: 4px` (rectangular, not round). Status dots: `6px` circle. Input fields: `4px`. Never exceed `4px` on any panel or widget.
4. **Panels & Grid:** 3–4 equal-width columns. Each column owns a functional zone (e.g., live metrics, logs, alerts, topology). Panels divided by `1px solid #1E2533`. Zero gap between panel columns — use border as separator. Panel headers: `32px` height, `border-bottom: 1px solid #1E2533`, font 11px uppercase `letter-spacing: 0.08em`.
5. **Status System:** Every status indicator must carry both a color and a label text. Pills: `background: rgba(color, 0.12); color: var(--status-color); border: 1px solid rgba(color, 0.25); font-size: 10px; font-weight: 600; padding: 1px 6px; border-radius: 4px`. Never use only a color without a label; never use only a label without a color.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use gradient backgrounds on any panel, header, or surface — flat solid fills only.
- **NEVER** exceed `4px` border-radius on panels, cards, or containers. Round-cornered panels destroy the operational aesthetic.
- **NEVER** use soft drop-shadows (`box-shadow` with large blur) — panels are separated by 1px borders only.
- **NEVER** leave excessive whitespace between panel sections — padding maximum `16px`, inner row padding `8px`.
- **NEVER** use status colors outside their semantic roles: green only for healthy/OK, amber only for warning/degraded, red only for critical/error/down.
- **NEVER** use a decorative typeface or font size above 14px anywhere except the primary dashboard title.
- **NEVER** render multi-column status as colored icons only — text label must always accompany the indicator.

---

## Command Center — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas & Surface */
  --color-bg: #0B0D11;
  --color-surface: #0F1219;
  --color-surface-raised: #141922;
  --color-surface-hover: #1A2030;
  --color-surface-active: #1E2533;

  /* Typography */
  --color-text-primary: #E2E8F0;
  --color-text-secondary: #94A3B8;
  --color-text-muted: #475569;
  --color-text-inverse: #0B0D11;

  /* Lines & Dividers */
  --color-border: #1E2533;
  --color-border-strong: #2D3748;
  --color-border-subtle: #141922;

  /* Semantic Status */
  --color-healthy: #22C55E;
  --color-healthy-bg: rgba(34, 197, 94, 0.10);
  --color-healthy-border: rgba(34, 197, 94, 0.25);

  --color-warning: #F59E0B;
  --color-warning-bg: rgba(245, 158, 11, 0.10);
  --color-warning-border: rgba(245, 158, 11, 0.25);

  --color-critical: #EF4444;
  --color-critical-bg: rgba(239, 68, 68, 0.10);
  --color-critical-border: rgba(239, 68, 68, 0.25);

  --color-info: #3B82F6;
  --color-info-bg: rgba(59, 130, 246, 0.10);
  --color-info-border: rgba(59, 130, 246, 0.25);
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 2px;       /* Inline micro elements */
  --radius-sm: 4px;       /* Buttons, inputs, status pills — MAXIMUM */
  --radius-md: 4px;       /* Panels, dropdowns — same cap */
  --radius-lg: 4px;       /* No exceptions — 4px hard cap */
  --radius-dot: 9999px;   /* Status dots only */
}
```

## Shadow & Elevation Tokens

```css
:root {
  /* No shadow-based elevation — border separation only */
  --shadow-none: none;
  --shadow-inset-top: inset 0 1px 0 0 rgba(255, 255, 255, 0.03);
  --shadow-focus: 0 0 0 2px rgba(59, 130, 246, 0.35);
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
  --grid-baseline: 8px;

  /* Panel-specific */
  --panel-header-height: 32px;
  --panel-padding: 12px;
  --panel-row-height: 28px;
  --log-line-height: 18px;
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
        lg: '4px',      // Hard cap — never exceed
        full: '9999px', // Status dots only
      },
      boxShadow: {
        none: 'none',
        focus: '0 0 0 2px rgba(59, 130, 246, 0.35)',
        'inset-top': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.03)',
      },
      colors: {
        canvas: '#0B0D11',
        surface: '#0F1219',
        border: '#1E2533',
        ink: {
          primary: '#E2E8F0',
          secondary: '#94A3B8',
          muted: '#475569',
        },
        status: {
          healthy: '#22C55E',
          warning: '#F59E0B',
          critical: '#EF4444',
          info: '#3B82F6',
        },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      fontSize: {
        '2xs': ['10px', { lineHeight: '16px', letterSpacing: '0.08em' }],
        xs: ['11px', { lineHeight: '16px' }],
        sm: ['12px', { lineHeight: '18px' }],
        base: ['13px', { lineHeight: '20px' }],
        md: ['14px', { lineHeight: '20px' }],
      },
    },
  },
};
```

## Component Geometry Specs

- **Panel Container:** `background: #0F1219`, `border: 1px solid #1E2533`, `border-radius: 4px`. Panel header: height `32px`, `border-bottom: 1px solid #1E2533`, `padding: 0 12px`, `font-size: 10px`, `font-weight: 600`, `letter-spacing: 0.08em`, `text-transform: uppercase`, color `#94A3B8`.
- **Status Pills:** `font-size: 10px`, `font-weight: 600`, `padding: 1px 6px`, `border-radius: 4px`. Healthy: `background: rgba(34,197,94,0.10); color: #22C55E; border: 1px solid rgba(34,197,94,0.25)`. Warning: amber equivalents. Critical: red equivalents.
- **Status Dots:** `6px` × `6px`, `border-radius: 9999px`, inline with `4px` right-margin before label text.
- **Log Lines:** `font-family: JetBrains Mono`, `font-size: 11px`, `line-height: 18px`, `color: #94A3B8`. Timestamp prefix: color `#475569`. Error lines: color `#EF4444`. Warning lines: color `#F59E0B`.
- **Metric Cards (within panel):** No card wrapper — metric sits directly on panel background. Label: 10px / `#94A3B8`. Value: 20px–24px / `JetBrains Mono` / `#E2E8F0` / `font-weight: 600`. Delta: 11px with status color.
- **Buttons:** Height `28px`, `border-radius: 4px`, `font-size: 11px`, `font-weight: 500`, padding `0 10px`. Primary: `background: #3B82F6`. Destructive: `background: #EF4444`.
- **Grid Layout:** CSS Grid `grid-template-columns: repeat(3, 1fr)` or `repeat(4, 1fr)`. Column gap: `0` (border-separation only). Row gap: `0`. Full-viewport height panels.
