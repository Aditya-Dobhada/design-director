# Y2K / Frutiger Aero — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Sky, Water & Aero Accents */
  --color-aero-cyan: #00C4FF;
  --color-aero-blue: #0078D7;
  --color-aero-sky: #E8F4FD;
  --color-aero-lime: #76B900;
  --color-aero-aqua: #00D2BA;

  /* Gloss & Glass Surfaces */
  --color-glass-base: rgba(255, 255, 255, 0.72);
  --color-glass-surface: rgba(255, 255, 255, 0.85);
  --color-glass-border: rgba(255, 255, 255, 0.8);
  --color-glass-border-subtle: rgba(0, 120, 215, 0.18);

  /* Typography */
  --color-text-primary: #0F2744;
  --color-text-secondary: #3B577D;
  --color-text-muted: #6B88B0;
  --color-text-white: #FFFFFF;
}
```

## Border Radius Tokens

```css
:root {
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-pill: 9999px; /* Core Frutiger Aero element */
}
```

## Shadow & Gloss Depth Tokens

```css
:root {
  /* Dual-layer depth: inner specular highlight + soft cyan drop glow */
  --shadow-aero-card: 
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    0 4px 16px rgba(0, 120, 215, 0.12),
    0 1px 3px rgba(0, 0, 0, 0.05);

  --shadow-aero-button: 
    inset 0 1px 0 rgba(255, 255, 255, 0.8),
    inset 0 -2px 0 rgba(0, 0, 0, 0.15),
    0 4px 12px rgba(0, 196, 255, 0.35);

  --shadow-aero-glow: 0 0 16px rgba(0, 196, 255, 0.5);
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        'aero': '14px',
        'aero-pill': '9999px',
      },
      boxShadow: {
        'aero-card': 'inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 4px 16px rgba(0, 120, 215, 0.12)',
        'aero-btn': 'inset 0 1px 0 rgba(255, 255, 255, 0.8), inset 0 -2px 0 rgba(0, 0, 0, 0.15), 0 4px 12px rgba(0, 196, 255, 0.35)',
      },
      colors: {
        aero: {
          cyan: '#00C4FF',
          blue: '#0078D7',
          sky: '#E8F4FD',
          lime: '#76B900',
          aqua: '#00D2BA',
          text: '#0F2744',
          subtext: '#3B577D',
        }
      }
    }
  }
}
```
