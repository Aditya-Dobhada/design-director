---
name: style-art-deco
description: Implementation rules for Art Deco style. Stepped geometric symmetry, caviar black (#0E0E10) and champagne cream canvas, burnished gold accents (#D4AF37), dramatic serif/geometric typography, 0px radius, and ornamental hairlines.
---

# Style Pack: Art Deco

A glamorous, architectural visual system rooted in the 1920s Paris Exposition Internationale, Chrysler Building geometry, high-society luxury, and Gatsby-era opulence. Defined by strict symmetry, stepped chevron motifs, rich gold and bronze metallics on obsidian and champagne surfaces, and ornate dual-rule borders.

## Core Principles

1. **Typography:** Display titles in high-contrast geometric serifs: `Bodoni Moda`, `Playfair Display`, or `Cormorant Garamond` (weights 600–800) with wide tracking (`0.10em`–`0.15em`). Navigation and metadata in geometric uppercase sans: `Cinzel` or `Josefin Sans`.
2. **Canvas & Surfaces:** Primary canvas `#0E0E10` (caviar noir) or `#FBF8F1` (champagne cream). Card surfaces `#16161A` (dark) or `#FFFFFF` (light). High tonal contrast with luminous metallic highlights.
3. **Geometry:** Strict `0px` radius everywhere (`border-radius: 0px`). Corners use sharp angles or stepped 45-degree chamfers (`clip-path`). Never rounded pills or bubbly curves.
4. **Borders & Ornament:** Hairline dual-rules (`border: 1px solid #D4AF37` with an inset `box-shadow: 0 0 0 3px #16161A, 0 0 0 4px #D4AF37`). Stepped chevron brackets and geometric dividers.
5. **Color & Metallics:** Rich burnished gold (`#D4AF37`), bronze (`#A3702C`), champagne (`#EED9A6`), and deep caviar black (`#0E0E10`). Emerald (`#0F5132`) or sapphire (`#0D2F54`) permitted as secondary jewel tones.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners on cards, buttons, or badges (`rounded-sm`, `rounded-md`, `rounded-full` are strictly forbidden; use `0px`).
- **NEVER** use casual sans-serif fonts (Inter, Roboto, Arial) for primary headings.
- **NEVER** use casual tech SaaS colors like neon cyan, generic royal blue, or purple gradients.
- **NEVER** use soft, blurry, diffuse drop shadows. Elevation is conveyed through gold border rules and sharp contrast.
- **NEVER** use asymmetric, chaotic, or haphazard card grids. Layouts must respect rigorous geometric symmetry.
- **NEVER** use informal stickers, cartoon avatars, or flat emoji graphics.

---

## Art Deco — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Caviar & Champagne Canvas */
  --color-deco-bg: #0E0E10;
  --color-deco-surface: #16161A;
  --color-deco-surface-light: #FBF8F1;

  /* Gold & Metallic Accents */
  --color-gold-burnished: #D4AF37;
  --color-gold-bright: #F3E5AB;
  --color-gold-deep: #A3702C;
  --color-bronze: #8C6239;

  /* Jewel Tones */
  --color-jewel-emerald: #0F5132;
  --color-jewel-sapphire: #0D2F54;

  /* Typography / Ink */
  --color-text-primary: #F3E5AB;
  --color-text-secondary: #C5BA9D;
  --color-text-muted: #8E836A;

  /* Hairlines */
  --color-border-gold: #D4AF37;
  --color-border-subtle: rgba(212, 175, 55, 0.25);
}
```

## Border Radius Tokens

```css
:root {
  --radius-none: 0px; /* HARD ENFORCEMENT: 0px across all elements */
}
```

## Shadow & Elevation Tokens

```css
:root {
  --shadow-none: none;
  --shadow-deco-double: 0 0 0 1px #D4AF37, 0 0 0 4px #16161A, 0 0 0 5px #D4AF37;
  --shadow-gold-gleam: 0 0 15px rgba(212, 175, 55, 0.25);
}
```

## Spacing & Grid Tokens

```css
:root {
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
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
        deco: '0 0 0 1px #D4AF37, 0 0 0 4px #16161A, 0 0 0 5px #D4AF37',
        gleam: '0 0 15px rgba(212, 175, 55, 0.25)',
      },
      colors: {
        canvas: '#0E0E10',
        surface: '#16161A',
        gold: {
          DEFAULT: '#D4AF37',
          bright: '#F3E5AB',
          deep: '#A3702C',
        },
        ink: {
          primary: '#F3E5AB',
          secondary: '#C5BA9D',
          muted: '#8E836A',
        },
      },
      fontFamily: {
        serif: ['Bodoni Moda', 'Playfair Display', 'Cormorant Garamond', 'serif'],
        sans: ['Cinzel', 'Josefin Sans', 'sans-serif'],
      },
    },
  },
};
```

## Component Geometry Specs

- **Buttons:** Height 40px, `border-radius: 0px`, `border: 1px solid #D4AF37`, `font-family: 'Cinzel', sans-serif`, `letter-spacing: 0.12em`, `text-transform: uppercase`. Hover: background becomes gold `#D4AF37`, text becomes caviar `#0E0E10`.
- **Cards:** Background `#16161A`, `border: 1px solid #D4AF37`, `border-radius: 0px`, padding `24px`. Corner ornamentation via corner brackets.
- **Inputs:** Height 40px, `border-radius: 0px`, background `#0E0E10`, `border: 1px solid rgba(212, 175, 55, 0.4)`, gold text.
- **Tables:** Hairline gold dividers (`border-b: 1px solid rgba(212, 175, 55, 0.2)`), uppercase headers with generous letter spacing, centered symmetric metrics.
