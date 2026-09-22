---
name: style-terminal-cli
description: Implementation rules for Terminal CLI style. Pitch command-line black canvas (#0C0C0C), 100% monospace typography, 0px radius, amber/emerald phosphors, ASCII box-drawing borders, and zero-blur elevation for developer tools and SRE consoles.
---

# Style Pack: Terminal CLI

An authentic, utility-first visual language derived from Unix terminals, curses/TUI interfaces, VT100 consoles, and operational SRE command centers. Built for maximum information density, keyboard navigation, and pure monospace typographic clarity.

## Core Principles

1. **Typography:** 100% Monospace everywhere: `JetBrains Mono`, `IBM Plex Mono`, `Fira Code`, or system `ui-monospace`. All headings, body text, buttons, and inputs must use monospace. Never proportional sans-serif, never serifs.
2. **Canvas & Surfaces:** Canvas `#0C0C0C` (terminal void) or `#000000`. Panel surfaces `#141414`. High contrast, zero ambient wash. Never white or light gray canvas.
3. **Geometry:** Strict `0px` radius everywhere (`border-radius: 0px`, `rounded-none`). No rounded buttons, no rounded cards, no rounded pill badges.
4. **Borders & Elevation:** 1px crisp borders (`#262626` standard, phosphor accent when active). Text-based ASCII framing (`+---+-+`) is encouraged for section headers and status blocks. Zero drop-shadow blur (`box-shadow: none`).
5. **Color & Phosphor:** Phosphor monochrome with single operational hue: Amber (`#FFB000`), Emerald (`#00FF66`), or Electric Cyan (`#00F5FF`). Secondary text `#888888`. Status colors restricted to ANSI red (`#EF4444`) and green (`#22C55E`).

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners on any element (`rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-full` are strictly forbidden; use `0px`).
- **NEVER** use proportional sans-serif (Inter, Roboto, Arial) or serif fonts anywhere in the document.
- **NEVER** use light mode or white background panels.
- **NEVER** use blurry drop shadows (`box-shadow: 0 4px ...` is forbidden; use `none` or 1px solid stroke).
- **NEVER** use gradients, pastel tints, or soft watercolor tones.
- **NEVER** use fluid, bouncing, or springy animations. UI updates must be instantaneous (0ms) or micro-blink.
- **NEVER** use floating abstract vector illustrations or marketing fluff.

---

## Terminal CLI — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Terminal Black Canvas */
  --color-term-bg: #0C0C0C;
  --color-term-surface: #141414;
  --color-term-surface-elevated: #1C1C1C;
  --color-term-surface-hover: #242424;

  /* Phosphor Output */
  --color-term-green: #00FF66;
  --color-term-amber: #FFB000;
  --color-term-cyan: #00F5FF;
  --color-term-white: #E6E6E6;

  /* Text Hierarchy */
  --color-text-primary: #E6E6E6;
  --color-text-secondary: #888888;
  --color-text-muted: #555555;
  --color-text-cursor: #00FF66;

  /* Grid & Dividers */
  --color-term-border: #262626;
  --color-term-border-bright: #404040;
  --color-term-border-active: #00FF66;
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px; /* HARD ENFORCEMENT: 0px across all elements */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-none: none; /* HARD ENFORCEMENT: Zero blur elevation */
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
        canvas: '#0C0C0C',
        surface: '#141414',
        border: '#262626',
        ink: {
          primary: '#E6E6E6',
          secondary: '#888888',
          muted: '#555555',
        },
        phosphor: {
          green: '#00FF66',
          amber: '#FFB000',
          cyan: '#00F5FF',
        },
      },
      fontFamily: {
        sans: ['JetBrains Mono', 'IBM Plex Mono', 'monospace'],
        mono: ['JetBrains Mono', 'IBM Plex Mono', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 32px, `border-radius: 0px`, `font-family: monospace`, `border: 1px solid var(--color-term-border)`. Hover: inverted colors (background becomes phosphor or light gray, text becomes black).
- **Cards / Windows:** Background `#141414`, `border: 1px solid #262626`, `border-radius: 0px`, padding `16px`. Title bar with simulated ASCII header: `[ STATUS: ONLINE ]`.
- **Inputs:** Height 32px, `border-radius: 0px`, background `#0C0C0C`, `border: 1px solid #262626`, `font-family: monospace`. Prompt indicator prefix: `> `.
- **Tables:** Dense rows (32px height), `border-collapse: collapse`, cell borders `1px solid #262626`, monospace alignment with fixed character widths.
