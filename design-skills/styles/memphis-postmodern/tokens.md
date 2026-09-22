# Memphis Postmodern — Design Tokens

## Color Tokens

```css
:root {
  /* Canvas */
  --color-memphis-white: #FFFFFF;
  --color-memphis-lemon: #FFF9C4;
  --color-memphis-pale-pink: #FFEBEE;

  /* Core Memphis Primaries */
  --color-memphis-coral: #FF6B6B;
  --color-memphis-electric-blue: #1565C0;
  --color-memphis-yellow: #FFD600;
  --color-memphis-teal: #00BCD4;
  --color-memphis-magenta: #E91E63;
  --color-memphis-lime: #CDDC39;
  --color-memphis-orange: #FF9800;
  --color-memphis-purple: #7B1FA2;

  /* Outlines */
  --color-memphis-black: #000000;

  /* Text */
  --color-text-primary: #000000;
  --color-text-secondary: #1A1A1A;
}
```

## Pattern Fill Tokens

```css
/* Apply these as background-image on panels and section backgrounds */
:root {
  /* Polka dot fill */
  --pattern-dots: radial-gradient(circle, #000 1.5px, transparent 1.5px);
  --pattern-dots-size: 12px 12px;

  /* Diagonal hatch */
  --pattern-hatch: repeating-linear-gradient(45deg, #000 0px, #000 1px, transparent 1px, transparent 8px);

  /* Squiggle (use SVG inline for best result) */
  /* Checkerboard */
  --pattern-checker: conic-gradient(#000 90deg, transparent 90deg) 0 0 / 12px 12px;

  /* Stripe */
  --pattern-stripe: repeating-linear-gradient(0deg, #FFD600 0px, #FFD600 6px, #FFFFFF 6px, #FFFFFF 12px);
}
```

## Shadow & Border Tokens

```css
:root {
  --border-memphis: 2px solid #000000;
  --border-memphis-thick: 4px solid #000000;
  --shadow-none: none; /* All shadows are forbidden — flat planes only */

  --radius-none: 0px;
  --radius-circle: 50%;  /* For circular Memphis medallion elements */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px', none: '0px', sm: '0px', md: '0px', lg: '0px',
        full: '9999px', // Only for circular medallion elements, not cards
      },
      boxShadow: {
        DEFAULT: 'none', none: 'none',
      },
      colors: {
        memphis: {
          coral: '#FF6B6B', blue: '#1565C0', yellow: '#FFD600',
          teal: '#00BCD4', magenta: '#E91E63', lime: '#CDDC39',
          orange: '#FF9800', purple: '#7B1FA2',
        }
      }
    }
  }
}
```
