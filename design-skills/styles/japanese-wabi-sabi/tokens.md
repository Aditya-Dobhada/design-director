# Japanese Wabi-Sabi — Design Tokens

## Color Tokens

```css
:root {
  /* Natural Canvas */
  --color-rice-paper: #FAF7F0;     /* Primary background */
  --color-bamboo-cream: #EDE8D0;   /* Panel background */
  --color-aged-linen: #DDD5BC;     /* Subtle surface distinction */

  /* Ink & Earth */
  --color-ink-stone: #2A2622;      /* Primary text — deep ink, never #000 */
  --color-ink-faded: #4A4240;      /* Secondary text */
  --color-ink-muted: #7D7268;      /* Muted / meta text */
  --color-clay: #A07E6A;           /* Fired clay accent */
  --color-terracotta: #9C5B3E;     /* Warm terracotta emphasis */

  /* Plant Pigments */
  --color-matcha: #5C6E4C;         /* Matcha green accent */
  --color-indigo-wash: #3D4E6D;    /* Natural indigo dye */
  --color-persimmon: #C8613E;      /* Kaki persimmon warm red */
}
```

## Border & Divider Tokens

```css
:root {
  /* Ink brushstroke dividers — single pixel warm-tone */
  --border-ink-wash: 1px solid rgba(42, 38, 34, 0.15);
  --border-ink-visible: 1px solid rgba(42, 38, 34, 0.40);

  /* No sharp mechanical borders */
  --radius-organic: 2px;   /* Slight hand-cut irregularity on some elements */
  --radius-none: 0px;      /* Default for most surfaces */
}
```

## Shadow Tokens

```css
:root {
  --shadow-none: none; /* Drop shadows: FORBIDDEN */
  /* Tonal elevation via background color shift only */
}
```

## Spacing (Ma — Meaningful Empty Space)

```css
:root {
  --space-ma-sm: 32px;
  --space-ma-md: 64px;
  --space-ma-lg: 96px;
  --space-ma-xl: 128px;
  --space-ma-2xl: 160px;  /* Hero margins at desktop */
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
        DEFAULT: 'none', none: 'none',
      },
      colors: {
        wabi: {
          rice: '#FAF7F0', bamboo: '#EDE8D0', linen: '#DDD5BC',
          ink: '#2A2622', clay: '#A07E6A', matcha: '#5C6E4C',
          indigo: '#3D4E6D', persimmon: '#C8613E',
        }
      }
    }
  }
}
```
