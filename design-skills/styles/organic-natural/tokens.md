# Organic Natural — Design Tokens

## Color Tokens

```css
:root {
  /* Earth Canvas */
  --color-bone-white: #F5F1E8;       /* Primary background */
  --color-raw-linen: #EDE8DA;        /* Panel surface */
  --color-aged-paper: #E0D9C8;       /* Subtle surface depth */

  /* Earth & Plant Pigments */
  --color-charcoal: #2A2824;         /* Primary text */
  --color-bark: #5C5248;             /* Secondary text */
  --color-stone-muted: #8A7E74;      /* Muted / meta text */
  --color-clay: #C4956A;             /* Clay accent warm */
  --color-terracotta: #AA6244;       /* Deeper warm accent */
  --color-moss: #5D7A52;             /* Forest moss green */
  --color-sap-green: #3E5C3A;        /* Deep forest sap */
  --color-bark-gray: #7A7068;        /* Natural bark gray */
  --color-sand: #C9A87C;             /* River sand */
}
```

## Border & Organic Shape Tokens

```css
:root {
  /* Radii — organic rounding */
  --radius-stone: 24px;     /* River-stone rounding */
  --radius-pod: 40px;       /* Seed pod container */
  --radius-blob: 60% 40% 55% 45% / 50% 55% 45% 50%; /* CSS organic blob */

  /* Borders */
  --border-organic: 1px solid rgba(42, 40, 36, 0.15);
  --border-organic-visible: 1.5px solid rgba(42, 40, 36, 0.35);
}
```

## Shadow Tokens

```css
:root {
  /* Warm casting shadow — very subtle */
  --shadow-material-sm: 0 2px 8px rgba(42, 40, 36, 0.08);
  --shadow-material-md: 0 4px 20px rgba(42, 40, 36, 0.10);
  /* Hard offset or blurry purple/blue shadows: FORBIDDEN */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '24px', sm: '12px', md: '24px',
        lg: '40px', xl: '60px', full: '9999px',
        none: '0px',
      },
      boxShadow: {
        DEFAULT: '0 4px 20px rgba(42, 40, 36, 0.10)',
        material: '0 2px 8px rgba(42, 40, 36, 0.08)',
        none: '0 0 #0000',
      },
      colors: {
        organic: {
          bone: '#F5F1E8', linen: '#EDE8DA', paper: '#E0D9C8',
          charcoal: '#2A2824', clay: '#C4956A', moss: '#5D7A52',
          sap: '#3E5C3A', bark: '#7A7068', sand: '#C9A87C',
        }
      }
    }
  }
}
```
