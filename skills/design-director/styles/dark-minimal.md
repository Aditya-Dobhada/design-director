---
name: style-dark-minimal
description: Implementation rules for Dark Minimal style. Obsidian canvas (#09090B), hairline translucent borders (rgba(255,255,255,0.08)), 6px-8px micro-radii, single focused electric accent, and micro-snappy transitions for modern developer tools and AI products.
---

# Style Pack: Dark Minimal

A sophisticated, low-sensory dark interface system engineered for developer platforms, AI command consoles, telemetry dashboards, and modern productivity apps. Grounded in near-black charcoal surfaces, translucent hairline borders, micro-radii, and precise typographic hierarchy.

## Core Principles

1. **Canvas:** Void background `#09090B` (pitch charcoal). Card and panel surfaces `#121215`. Elevated interactive dropdowns `#18181B`. Never pure white, never washed-out gray `#374151`.
2. **Typography:** Primary font `Geist Sans`, `Inter`, or `SF Pro Display`. Metadata, timestamps, shortcuts, and telemetry in `Geist Mono` or `JetBrains Mono`. High legibility hierarchy: Primary text `#EDEDED`, Secondary `#A1A1AA`, Muted `#71717A`.
3. **Geometry:** Micro-calibrated curvature: `6px` (`rounded-md`) for buttons, badges, and search inputs; `8px` (`rounded-lg`) for cards and command palette surfaces. Never sharp `0px` brutalist corners; never pill-shaped container cards.
4. **Surfaces & Borders:** 1px hairline translucent borders: `rgba(255, 255, 255, 0.08)` standard, rising to `rgba(255, 255, 255, 0.16)` on hover/focus. Elevation is achieved via tonal surface stepping and deep ambient shadows (`0 8px 30px rgba(0,0,0,0.5)`).
5. **Color & Accents:** Exactly ONE electric accent color used sparingly for active selections, focus rings, and primary action triggers. Standard accent: Violet/Indigo (`#6366F1`), Emerald (`#10B981`), or Cyan (`#06B6D4`). Never use accent colors as solid card fills.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use light mode or white background panels (`bg-white`, `bg-gray-50` are strictly forbidden).
- **NEVER** use sharp 0px corners on cards (`rounded-none` is forbidden on cards; use 8px).
- **NEVER** use bubbly or exaggerated pill shapes on containers (`rounded-full`, `rounded-3xl` are forbidden on cards).
- **NEVER** use thick solid opaque borders (2px–4px borders are forbidden; use 1px translucent borders).
- **NEVER** use multi-color rainbow gradients or glowing neon text halos.
- **NEVER** use low-contrast muddy gray backgrounds like `#2D3748` or `#4A5568`. Canvas must be pitch charcoal (`#09090B`).
- **NEVER** use slow or springy animations. Transitions must be micro-snappy (100ms–150ms).

---

## Dark Minimal — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Obsidian Base Canvas */
  --color-bg-void: #09090B;
  --color-surface-base: #121215;
  --color-surface-elevated: #18181B;
  --color-surface-hover: #222226;
  --color-surface-active: #27272A;

  /* Typography / Light Ink */
  --color-text-primary: #EDEDED;
  --color-text-secondary: #A1A1AA;
  --color-text-muted: #71717A;
  --color-text-dim: #52525B;

  /* Translucent Hairlines */
  --color-border: rgba(255, 255, 255, 0.08);
  --color-border-hover: rgba(255, 255, 255, 0.16);
  --color-border-active: rgba(255, 255, 255, 0.24);

  /* Single Electric Accent (Default: Violet) */
  --color-accent: #6366F1;
  --color-accent-hover: #4F46E5;
  --color-accent-subtle: rgba(99, 102, 241, 0.12);
  --color-accent-glow: rgba(99, 102, 241, 0.25);
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 4px;      /* Badges, keyboard shortcuts <kbd> */
  --radius-sm: 6px;      /* Buttons, command inputs */
  --radius-md: 8px;      /* Standard card, modal dialog */
  --radius-lg: 12px;     /* Command palette overlay */
  --radius-full: 9999px; /* Status pips, user avatars only */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-dark-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.6);
  --shadow-dark-md: 0 4px 12px 0 rgba(0, 0, 0, 0.7);
  --shadow-dark-lg: 0 8px 30px 0 rgba(0, 0, 0, 0.85);
  --shadow-focus-ring: 0 0 0 2px var(--color-bg-void), 0 0 0 4px var(--color-accent);
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
        DEFAULT: '0 4px 12px 0 rgba(0, 0, 0, 0.7)',
        popover: '0 8px 30px 0 rgba(0, 0, 0, 0.85)',
      },
      colors: {
        canvas: '#09090B',
        surface: {
          DEFAULT: '#121215',
          elevated: '#18181B',
          hover: '#222226',
        },
        border: 'rgba(255, 255, 255, 0.08)',
        ink: {
          primary: '#EDEDED',
          secondary: '#A1A1AA',
          muted: '#71717A',
        },
        accent: {
          DEFAULT: '#6366F1',
          hover: '#4F46E5',
          subtle: 'rgba(99, 102, 241, 0.12)',
        },
      },
      fontFamily: {
        sans: ['Geist Sans', 'Inter', '-apple-system', 'sans-serif'],
        mono: ['Geist Mono', 'JetBrains Mono', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 34px–38px, `border-radius: 6px`, `font-size: 13px`, `font-weight: 500`. Primary: Solid `#EDEDED` text with `#18181B` background and 1px translucent border, or solid accent background with white text.
- **Cards:** Background `#121215`, `border-radius: 8px`, `border: 1px solid rgba(255, 255, 255, 0.08)`, padding `20px`.
- **Command Inputs:** Height 40px, `border-radius: 8px`, background `#18181B`, `border: 1px solid rgba(255, 255, 255, 0.12)`.
- **Data Tables:** Hairline divider `rgba(255, 255, 255, 0.06)`, header uppercase tracking `0.05em` font-size `11px` in muted text, numeric cells right-aligned in mono.
