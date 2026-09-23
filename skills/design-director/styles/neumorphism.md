---
name: style-neumorphism
description: Implementation rules for Neumorphism style. Monochromatic #E0E5EC canvas with soft extruded surfaces, dual-direction box-shadows (light + dark), color-matched fills, and zero borders. Domain — settings/control panels, IoT companion apps, hardware dashboards.
---

# Style Pack: Neumorphism

A tactile, monochromatic visual system that simulates physical extrusion of elements from the canvas material. Every element appears to be molded from the same substance as the background — same hue, same lightness range — with dual soft shadows (one light-source highlight, one cast shadow) creating the illusion of depth and press-ability. There are no borders, no contrasting fills, no neon. The interface feels like a physical object you could reach into.

## Core Principles

1. **Monochromatic Canvas Lock:** Canvas `#E0E5EC` (light mode) or `#2D3748` (dark mode). Every surface — cards, buttons, inputs, nav — uses exactly the canvas color or a ±4% lightness variant. Never introduce a contrasting surface color.
2. **Dual Shadow Extrusion:** All extruded elements carry two shadows simultaneously: a dark cast shadow (`rgba(0,0,0,0.15)`) offset bottom-right, and a light highlight (`rgba(255,255,255,0.70)`) offset top-left. Equal offset magnitude; equal blur radius. This symmetry is the signature of neumorphism.
3. **No Borders:** `border: none` on all surfaces. The shape is defined entirely by shadow, not edge lines. Even inputs and buttons have zero border.
4. **Pressed State:** Invert the shadow direction and add inset shadows for pressed/active elements: `box-shadow: inset 6px 6px 12px rgba(0,0,0,0.15), inset -6px -6px 12px rgba(255,255,255,0.70)`. This creates the "pushed in" tactile illusion.
5. **Typography:** Inter, weight 400 (body) and 500–600 (label/value). Text is always subdued — never pure black or high-contrast white. Primary text `#5C6B8A`, secondary `#8A99B0`, muted `#A8B4C8` on light canvas.
6. **Accent:** Desaturated teal `#4DA8A0` or soft indigo `#7986CB`. Used only for active state highlights, focus rings, and small icons — never as a card fill.
7. **Radius:** 12px–20px for sculpted, press-able feel. Larger radius (20px) on cards and panels; tighter (12px) on buttons and inputs.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use hard borders on any surface (`border: 1px solid …` is forbidden — shadow defines the shape).
- **NEVER** use contrasting surface colors (e.g., white card on `#E0E5EC` background — both must be `#E0E5EC`).
- **NEVER** use `border-radius: 0px` — minimum 12px on all interactive elements.
- **NEVER** use a single unidirectional shadow — neumorphism always requires the dual light+dark pair.
- **NEVER** use flat one-color shadows — `box-shadow: 0 4px 6px rgba(0,0,0,0.1)` alone is not neumorphic.
- **NEVER** use high-chroma accent colors — neon, electric, or saturated fills break the monochromatic material metaphor.
- **NEVER** use very high text contrast — pure `#000000` text on `#E0E5EC` is too jarring; stay within the subdued zinc-blue palette.
- **NEVER** use colored card backgrounds — elements are extruded from the canvas, not placed on top of it.

---

## Neumorphism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Canvas — the single material color */
  --color-bg: #E0E5EC;
  --color-surface: #E0E5EC;       /* All surfaces match canvas exactly */
  --color-surface-inset: #D6DBE4; /* Slightly darker for recessed/pressed areas */
  --color-surface-raised: #E8ECF2; /* Slightly lighter for raised highlights */

  /* Typography — subdued blue-gray scale */
  --color-text-primary: #5C6B8A;
  --color-text-secondary: #8A99B0;
  --color-text-muted: #A8B4C8;
  --color-text-label: #4A5568;

  /* Accent — desaturated teal (primary interactive) */
  --color-accent: #4DA8A0;
  --color-accent-hover: #3D9890;
  --color-accent-subtle: rgba(77, 168, 160, 0.12);

  /* Accent — soft indigo (secondary interactive) */
  --color-indigo: #7986CB;
  --color-indigo-subtle: rgba(121, 134, 203, 0.12);

  /* State colors — desaturated */
  --color-positive: #68B09F;
  --color-negative: #C0837A;
  --color-warning: #C9A76A;
}
```

## Border Radius Tokens

```css
:root {
  --radius-xs: 8px;      /* Small tags, micro elements */
  --radius-sm: 12px;     /* Buttons, inputs, chips */
  --radius-md: 16px;     /* Standard card, panel */
  --radius-lg: 20px;     /* Larger panels, modals */
  --radius-full: 9999px; /* Toggle knobs, avatar clips */
}
```

## Shadow & Elevation Tokens

```css
:root {
  /* Standard extruded (raised) — offset 6px, blur 12px */
  --shadow-neu-sm: 4px 4px 8px rgba(0, 0, 0, 0.12), -4px -4px 8px rgba(255, 255, 255, 0.70);
  --shadow-neu-md: 6px 6px 12px rgba(0, 0, 0, 0.15), -6px -6px 12px rgba(255, 255, 255, 0.70);
  --shadow-neu-lg: 10px 10px 20px rgba(0, 0, 0, 0.15), -10px -10px 20px rgba(255, 255, 255, 0.70);

  /* Pressed / inset (active state) */
  --shadow-neu-inset-sm: inset 3px 3px 7px rgba(0, 0, 0, 0.12), inset -3px -3px 7px rgba(255, 255, 255, 0.70);
  --shadow-neu-inset-md: inset 6px 6px 12px rgba(0, 0, 0, 0.15), inset -6px -6px 12px rgba(255, 255, 255, 0.70);

  /* Flat — no depth, used for disabled states */
  --shadow-neu-flat: none;
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
  --grid-gap: 20px;
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
      },
      boxShadow: {
        neu: '6px 6px 12px rgba(0,0,0,0.15), -6px -6px 12px rgba(255,255,255,0.70)',
        'neu-sm': '4px 4px 8px rgba(0,0,0,0.12), -4px -4px 8px rgba(255,255,255,0.70)',
        'neu-lg': '10px 10px 20px rgba(0,0,0,0.15), -10px -10px 20px rgba(255,255,255,0.70)',
        'neu-inset': 'inset 6px 6px 12px rgba(0,0,0,0.15), inset -6px -6px 12px rgba(255,255,255,0.70)',
      },
      colors: {
        canvas: '#E0E5EC',
        surface: '#E0E5EC',
        ink: {
          primary: '#5C6B8A',
          secondary: '#8A99B0',
          muted: '#A8B4C8',
          label: '#4A5568',
        },
        accent: {
          DEFAULT: '#4DA8A0',
          hover: '#3D9890',
          subtle: 'rgba(77,168,160,0.12)',
        },
        indigo: {
          DEFAULT: '#7986CB',
          subtle: 'rgba(121,134,203,0.12)',
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

- **Buttons (Primary):** Height 40px, `border-radius: 12px`, `background: #E0E5EC`, `border: none`, `box-shadow: var(--shadow-neu-md)`, `color: var(--color-accent)`, `font-weight: 600`. Active state: `box-shadow: var(--shadow-neu-inset-md)`. No fill color change on hover — only shadow depth shift.
- **Buttons (Ghost/Label):** Same geometry, no shadow, text-only, color `var(--color-text-secondary)`. Active: inset shadow.
- **Cards:** `background: #E0E5EC`, `border-radius: 16px`, `border: none`, `box-shadow: var(--shadow-neu-lg)`, padding `24px`. Content sits in the "extruded plateau" above the canvas.
- **Inputs:** Height 40px, `border-radius: 12px`, `background: #E0E5EC`, `border: none`, `box-shadow: var(--shadow-neu-inset-sm)`, `color: var(--color-text-primary)`. Focus ring: `outline: 2px solid rgba(77,168,160,0.40); outline-offset: 2px`.
- **Nav:** `background: #E0E5EC`, `border: none`, `box-shadow: 0 4px 12px rgba(0,0,0,0.10), 0 -1px 0 rgba(255,255,255,0.70)`, height `64px`, padding `0 32px`.
- **Tables:** No border dividers — use alternating `background: rgba(0,0,0,0.02)` for even rows. Row height 48px. Header text `font-weight: 500`, `color: var(--color-text-muted)`, `text-transform: uppercase`, `letter-spacing: 0.06em`. Numeric cells right-aligned.
- **Badges/Chips:** `border-radius: 9999px`, `background: #E0E5EC`, `box-shadow: var(--shadow-neu-sm)`, `padding: 3px 12px`, `font-size: 11px`, `color: var(--color-accent)`, `font-weight: 500`.
