# Neo-Brutalism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Outlines & Contrast Base */
  --color-border-main: #000000;
  --color-text-main: #000000;
  --color-text-sub: #1F2937;
  --color-surface-white: #FFFFFF;

  /* Saturated High-Energy Accents */
  --color-neo-yellow: #FFE600;
  --color-neo-pink: #FF69B4;
  --color-neo-green: #00F0A8;
  --color-neo-cyan: #00C4FF;
  --color-neo-orange: #FF5C00;
  --color-neo-purple: #A358DF;

  /* Canvas / Background Options */
  --color-bg-base: #FFFDF5; /* Warm off-white poster canvas */
  --color-bg-alt: #FFE600;  /* High-impact section canvas */
}
```

## Border Width & Radius Tokens

```css
:root {
  /* Border Widths: Heavy, structural, unapologetic */
  --border-width-default: 3px;
  --border-width-thick: 4px;
  --border-width-heavy: 5px;

  /* Radius: Sharp boxy OR playful chunky (never full pill) */
  --radius-sharp: 0px;       /* Classic brutalist */
  --radius-chunky: 6px;      /* Contemporary neo-brutalist standard */
  --radius-max: 8px;         /* Absolute maximum. rounded-full is FORBIDDEN on cards/containers */
}
```

## Shadow & Depth Tokens

```css
:root {
  /* Hard Offset Shadows - BLUR IS STRICTLY ZERO */
  --shadow-neo-sm: 2px 2px 0px #000000;
  --shadow-neo-md: 4px 4px 0px #000000;
  --shadow-neo-lg: 6px 6px 0px #000000;
  --shadow-neo-xl: 8px 8px 0px #000000;
  --shadow-neo-active: 0px 0px 0px #000000; /* When button is pressed */
}
```

## Spacing & Metrics

```css
:root {
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderWidth: {
        DEFAULT: '3px',
        2: '2px',
        3: '3px',
        4: '4px',
        5: '5px',
      },
      borderRadius: {
        DEFAULT: '0px',
        none: '0px',
        sm: '4px',
        md: '6px',
        lg: '8px',
        full: '8px', // Prevent rounded-full from creating circles/pills on cards
      },
      boxShadow: {
        DEFAULT: '4px 4px 0px #000000',
        sm: '2px 2px 0px #000000',
        md: '4px 4px 0px #000000',
        lg: '6px 6px 0px #000000',
        xl: '8px 8px 0px #000000',
        none: '0 0 #0000',
      },
      colors: {
        neo: {
          border: '#000000',
          yellow: '#FFE600',
          pink: '#FF69B4',
          green: '#00F0A8',
          cyan: '#00C4FF',
          orange: '#FF5C00',
          purple: '#A358DF',
          cream: '#FFFDF5',
        }
      }
    }
  }
}
```
