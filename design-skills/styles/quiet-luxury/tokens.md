# Quiet Luxury — Design Tokens

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
