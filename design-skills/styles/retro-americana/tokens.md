# Retro Americana — Design Tokens

## Color Tokens

```css
:root {
  /* Warm Incandescent Canvas */
  --color-cream: #F9F0DC;           /* Parchment paper base */
  --color-linen: #EDE5CB;           /* Aged linen panel */
  --color-offwhite: #FBF7EF;        /* Warm off-white */

  /* Ink & Print Colors */
  --color-ink: #1C1410;             /* Deep carbon ink (never pure #000) */
  --color-ink-faded: #3D2E22;       /* Aged print, faded letterpress */

  /* Incandescent Accents */
  --color-vermilion: #C8391E;       /* Roadside diner red */
  --color-amber: #E8A126;           /* Neon sign amber-yellow */
  --color-teal: #2A7F7F;            /* Diner tile teal */
  --color-mustard: #C4861A;         /* Depression-era mustard gold */
  --color-burnt-sienna: #9E4222;    /* WPA poster terra cotta */

  /* Type Colors */
  --color-text-primary: #1C1410;
  --color-text-secondary: #4A3828;
  --color-text-muted: #7A6450;
  --color-text-on-dark: #F9F0DC;
}
```

## Border & Texture Tokens

```css
:root {
  /* Ink Press Borders */
  --border-ink-sm: 2px solid #1C1410;
  --border-ink-md: 3px solid #1C1410;
  --border-ink-lg: 5px solid #1C1410;

  /* Halftone / Grain Texture (applied via background-image) */
  --texture-halftone: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Ccircle cx='1' cy='1' r='0.8' fill='rgba(28,20,16,0.06)'/%3E%3C/svg%3E");
  --texture-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
}
```

## Shadow Tokens

```css
:root {
  --shadow-ink-press: 3px 3px 0px #1C1410;
  --shadow-ink-heavy: 5px 5px 0px #1C1410;
  --shadow-none: none;
  /* Blurry drop-shadows are forbidden */
}
```

## Border Radius

```css
:root {
  --radius-none: 0px;     /* Cards, containers, inputs */
  --radius-tab: 4px 4px 0px 0px;  /* Tab tops only */
  /* rounded-full / rounded-xl: FORBIDDEN */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px', none: '0px', sm: '2px', md: '2px', lg: '2px', full: '2px',
      },
      boxShadow: {
        DEFAULT: '3px 3px 0px #1C1410',
        ink: '3px 3px 0px #1C1410',
        'ink-heavy': '5px 5px 0px #1C1410',
        none: '0 0 #0000',
      },
      colors: {
        retro: {
          cream: '#F9F0DC', linen: '#EDE5CB', ink: '#1C1410',
          vermilion: '#C8391E', amber: '#E8A126', teal: '#2A7F7F',
          mustard: '#C4861A', sienna: '#9E4222',
        }
      }
    }
  }
}
```
