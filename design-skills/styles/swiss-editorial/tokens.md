# Swiss / Editorial — Design Tokens

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
