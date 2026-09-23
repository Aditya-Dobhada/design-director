---
name: style-web-brutalism
description: Implementation rules for Web Brutalism style. Raw browser-native HTML aesthetics, unstyled default controls, Courier/system typography, classic hyperlink blue (#0000EE), stark black/white contrast, 0px radius, and zero drop-shadows.
---

# Style Pack: Web Brutalism

An uncompromising, web-native visual language rooted in early browser defaults, raw HTML markup, document-centric layout, and deliberate anti-design. Distinct from Neo-Brutalism (which is stylized graphic pop-art), Web Brutalism treats the web browser as an unadorned document viewer.

## Core Principles

1. **Typography:** Raw browser default typography: `Courier New`, `Courier`, `ui-monospace`, or raw `system-ui`, `Times New Roman`. Hyperlinks must display browser-default blue (`#0000EE`) with an underline (`text-decoration: underline`).
2. **Canvas & Surfaces:** Stark `#FFFFFF` canvas or pure `#000000`. Content panels use transparent or plain white surfaces with strict black borders. Zero background gradients.
3. **Geometry:** Strict `0px` radius everywhere (`border-radius: 0px`, `rounded-none`). No rounded buttons, no rounded cards, no rounded pill tags.
4. **Borders & Rules:** Hard solid rules: `1px` or `2px solid #000000`. Raw HTML table styling with visible borders. Horizontal rules `<hr>` used as explicit structural dividers.
5. **Elevation & Shadows:** Zero box-shadow blur (`box-shadow: none`). No soft ambient shadows, no offset colorful pop shadows.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners (`rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-full` are strictly forbidden; use `0px`).
- **NEVER** use blurry drop shadows or ambient elevation (`box-shadow: 0 4px ...` is forbidden; use `none`).
- **NEVER** remove underlines from hyperlinks (`text-decoration: underline` is mandatory for links).
- **NEVER** use pastel gradient backgrounds, blurred glassmorphic surfaces, or floating cards.
- **NEVER** use friendly corporate illustrations, modern micro-interactions, or spring animations.
- **NEVER** use custom stylized dropdowns that conceal native browser select elements.

---

## Web Brutalism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Stark Document Canvas */
  --color-web-bg: #FFFFFF;
  --color-web-surface: #FFFFFF;
  --color-web-surface-dark: #000000;

  /* Raw Web Ink */
  --color-text-primary: #000000;
  --color-text-secondary: #333333;
  --color-text-muted: #666666;

  /* Classic Browser Links */
  --color-link-default: #0000EE;
  --color-link-visited: #551A8B;
  --color-link-active: #FF0000;

  /* Raw Lines */
  --color-border: #000000;
  --color-border-heavy: #000000;
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px; /* HARD ENFORCEMENT: 0px universally */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-none: none; /* HARD ENFORCEMENT: 0px blur */
}
```

## Spacing & Grid Tokens

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-8: 32px;
  --space-12: 48px;
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
        canvas: '#FFFFFF',
        surface: '#FFFFFF',
        border: '#000000',
        ink: {
          primary: '#000000',
          secondary: '#333333',
          muted: '#666666',
        },
        link: {
          DEFAULT: '#0000EE',
          visited: '#551A8B',
          active: '#FF0000',
        },
      },
      fontFamily: {
        sans: ['Courier New', 'Courier', 'ui-monospace', 'monospace'],
        mono: ['Courier New', 'Courier', 'ui-monospace', 'monospace'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 34px, `border-radius: 0px`, `border: 2px solid #000000`, background `#FFFFFF` or `#000000`, `color: #FFFFFF`. Active state: reverse colors immediately.
- **Cards / Containers:** Background `#FFFFFF`, `border: 1px solid #000000`, `border-radius: 0px`, padding `16px`. Zero shadows.
- **Inputs:** Standard native HTML text field styling, `border: 1px solid #000000`, `border-radius: 0px`, font-family `monospace`.
- **Tables:** Full border grid (`border: 1px solid #000000`), padding `8px 12px`, header cells with bottom double border.
