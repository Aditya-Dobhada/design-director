# Space Age Optimism — Design Tokens

## Color Tokens

```css
:root {
  /* Warm White & Chrome Canvas */
  --color-space-white: #FAFAF8;
  --color-space-chrome: #F0EFEB;
  --color-space-silver: #E4E2DC;
  --color-space-dark: #1C1C1A;

  /* Accent: Choose ONE */
  --color-accent-orange: #FF5C00;    /* NASA Mission Orange */
  --color-accent-red: #E82528;       /* Atomic Age Red */
  --color-accent-green: #00B87C;     /* Mission Console Green */

  /* Typography */
  --color-text-primary: #1C1C1A;
  --color-text-secondary: #4A4A46;
  --color-text-muted: #8C8C88;
  --color-text-on-accent: #FFFFFF;
}
```

## Border Radius Tokens

```css
:root {
  --radius-pod-sm: 16px;
  --radius-pod-md: 24px;
  --radius-pod-lg: 40px;
  --radius-capsule: 9999px;  /* For pill-shaped nav items and tags */
  /* 0px radius is FORBIDDEN on primary containers */
}
```

## Shadow Tokens

```css
:root {
  /* Warm, small, diffuse — evokes plastic casting seam depth */
  --shadow-pod-sm: 0 2px 8px rgba(28, 28, 26, 0.08), 0 1px 2px rgba(28, 28, 26, 0.04);
  --shadow-pod-md: 0 4px 20px rgba(28, 28, 26, 0.1), 0 1px 4px rgba(28, 28, 26, 0.06);
  --shadow-pod-lg: 0 8px 40px rgba(28, 28, 26, 0.12);
  /* Heavy black hard-offset shadows: FORBIDDEN */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '24px',
        pod: '24px', 'pod-lg': '40px', capsule: '9999px',
        none: '0px', sm: '8px', md: '16px', lg: '24px', xl: '32px',
      },
      boxShadow: {
        'pod-sm': '0 2px 8px rgba(28, 28, 26, 0.08), 0 1px 2px rgba(28, 28, 26, 0.04)',
        'pod-md': '0 4px 20px rgba(28, 28, 26, 0.10)',
        DEFAULT: '0 4px 20px rgba(28, 28, 26, 0.10)',
      },
      colors: {
        space: {
          white: '#FAFAF8', chrome: '#F0EFEB', silver: '#E4E2DC',
          dark: '#1C1C1A', orange: '#FF5C00', red: '#E82528', green: '#00B87C',
        }
      }
    }
  }
}
```
