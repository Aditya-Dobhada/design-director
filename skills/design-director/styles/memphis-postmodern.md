---
name: style-memphis-postmodern
description: Implementation rules for Memphis Postmodern style. 1980s Memphis Group geometric maximalism, Ettore Sottsass pattern collisions, contrasting squiggle/dot/stripe motifs, acid pastels mixed with primaries on white, and deliberately anti-functional playfulness.
---

# Style Pack: Memphis Postmodern

A visual language from the radical 1980s Memphis Group design movement led by Ettore Sottsass. Memphis rejected functionalism with geometric decoration for its own sake: squiggle lines, dot patterns, diagonal stripe fills, and intentional kitsch collisions between clashing pastels and primaries.

## Core Principles

1. **Color:** Contrasting primaries on white: Electric yellow `#FFE000`, coral `#FF6B6B`, cobalt `#003DE8`, teal `#00B4B4`, plus `#FFFFFF` background and `#000000` outlines. No gradients. No muted palettes. Colors appear as flat fills only.
2. **Patterns:** Squiggle lines, polka dots (12px circles on 24px grid), diagonal hatching (45° at 4px spacing), zigzag bands — applied as CSS `background-image` repeating patterns or inline SVGs. At least two distinct patterns per layout.
3. **Typography:** Display: `font-family: 'Boogaloo', 'Righteous', 'Fredoka One', sans-serif` at weight 400–700. Body: `'Space Grotesk'` or `'DM Sans'` for legibility. Large numbers and single letters as graphic elements (200px+). Never serif for display.
4. **Geometry:** Mixed `border-radius` within the same layout: 0px on some elements, 50% on others, 8px on others — intentional inconsistency. Shapes overlap and clip outside their containers. No visual hierarchy of uniform radii.
5. **Borders:** `border: 2px solid #000000` as a unifying element across all patterns and shapes. All pattern blocks enclosed in solid black outlines. No opacity-reduced borders.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use subtle, tonal, or restrained palettes. Memphis is deliberately chromatic excess — muted grays are a violation.
- **NEVER** use diffuse shadows or blur effects. Flat opaque graphic planes only.
- **NEVER** use austere negative space as a design device. Empty white areas must be filled with pattern motifs.
- **NEVER** use serious editorial serifs or formal grotesks. Typography must carry playful irreverence.
- **NEVER** use conventional container rectangles with default 8px radii. Shapes should be eccentric trapezoids, circles, or 0px sharp cuts.
- **NEVER** use smooth, professional animations. Motion is abrupt, pop-art mechanical, or totally absent.
- **NEVER** use dark backgrounds. Memphis lives on stark white or pale lemon with chromatic surface explosions.

---

## Memphis Postmodern — Design Tokens

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

---

## Memphis Postmodern — Typography

## Recommended Font Stacks

### Display (Playful Geometric / Rounded)
- `Nunito` (900 Black)
- `Fredoka One`
- `Boogaloo`
- `Righteous`
- `Titan One`
- `Lilita One`

### Body (Clean Geometric Sans)
- `Nunito Sans` (600 / 700)
- `DM Sans` (500)
- `Poppins` (500 / 600)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display** | 56px - 72px | 900 Black | -0.02em | 1.00 | UPPERCASE or Title |
| **H1** | 40px - 48px | 800/900 | -0.01em | 1.10 | Title case |
| **H2** | 28px - 34px | 700/800 | 0.00em | 1.20 | Title case |
| **H3** | 20px - 24px | 700 | 0.00em | 1.30 | Title case |
| **Body** | 15px - 16px | 500/600 | 0.00em | 1.50 | Sentence |
| **Badge** | 12px - 13px | 800 | +0.04em | 1.20 | UPPERCASE |

## Rules
1. **High Weight Everywhere:** Minimum body weight is 500. Thin or light type disappears against patterned surfaces.
2. **Chromatic Text Accents:** Headings can be rendered in electric blue, coral, or yellow — contrasting with black body text.

## Anti-Patterns
- **Formal serif fonts** (`Cormorant`, `Garamond`): Memphis is plastic and toylike, not literary.
- **Technical monospace**: Does not fit the playful postmodern spirit.

---

## Memphis Postmodern — Layout

## Composition Rules

1. **Pattern-Filled Panels:** Section backgrounds are filled with polka dots, hatch lines, or checkerboard patterns at 20-30% opacity — not left as white voids.
2. **Eccentric Shape Containers:** Cards can be trapezoids, rhomboids, or asymmetrically cut with CSS `clip-path`. Standard rectangles are acceptable but must have bold outlines and pattern fills.
3. **Circular Medallion Accents:** Floating circles with pattern fills or solid colors positioned as decorative overlapping layers on hero sections.
4. **Asymmetric Overlapping Stacks:** Elements overlap by design. A yellow circle can intrude 30% into an adjacent blue panel.

## Layout Anti-Patterns
- **Orderly aligned card grids with equal gutter spacing**: Too rational for Memphis philosophy.
- **Full-bleed dark dark backgrounds**: Memphis is always light and chromatic.
- **Negative space as a refined device**: Unfilled areas always receive pattern treatment.

---

## Memphis Postmodern — Component Rules

## 1. Buttons

### Primary — Memphis Pop
- **Background:** Electric Blue `#1565C0` or Coral `#FF6B6B`
- **Color:** `#FFFFFF`
- **Border:** `3px solid #000000`
- **Border Radius:** `0px` (or circle if icon-only)
- **Shadow:** `none` (flat planes)
- **Font:** 14px Rounded Bold, uppercase, tracking +0.04em
- **Padding:** 12px 24px
- **Hover:** Background shifts to contrasting Memphis color (e.g. coral → yellow)
- **Active:** Instant color swap, no translate

### Secondary — Outline Pop
- **Background:** Pattern fill (polka dots in hovered accent color)
- **Border:** `3px solid #000000`
- **Color:** `#000000`
- **Hover:** Fill switches from pattern to solid color

## 2. Cards

- **Background:** White or Memphis Lemon `#FFF9C4`
- **Border:** `3px solid #000000`
- **Border Radius:** `0px`
- **Shadow:** `none`
- **Padding:** 24px
- **Optional pattern sidebar accent:** Left 4px border in coral or electric blue; or left 8px panel with dot pattern fill

## 3. Inputs

- **Border:** `3px solid #000000`
- **Border Radius:** `0px`
- **Background:** White
- **Focus State:** Border changes to electric blue `#1565C0`, left accent panel appears with polka dot fill

## 4. Badges

- **Background:** Solid primary (yellow, coral, teal, lime)
- **Border:** `2px solid #000000`
- **Border Radius:** `0px` or `50%` for round medallion badges
- **Font:** 11px Rounded Bold, UPPERCASE
- **Shadow:** `none`

---

## Memphis Postmodern — Motion

## Philosophy

Motion is either absent (pure static graphic) or abrupt pop-art mechanical. No smoothing, no easing curves that feel sophisticated. Pattern switches and color hops are instantaneous.

## Tokens

```css
:root {
  --duration-memphis-pop: 80ms;
  --ease-memphis: steps(1, end); /* Binary state switches */
  --ease-memphis-bounce: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transitions

1. **Hover color swap:** Instantaneous `steps(1)` — no cross-fade.
2. **Pattern fill reveal:** 80ms `ease-out` opacity.
3. **Card pop-in on mount:** Scale `0.95 → 1.0` over 100ms.

## Anti-Patterns
- No silky smooth 300ms transitions.
- No spring physics.
- No parallax or scroll-linked effects.
