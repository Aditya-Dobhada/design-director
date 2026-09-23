---
name: style-bauhaus
description: Implementation rules for Bauhaus style. Rigorous constructivist geometry, Gropius-era form-follows-function discipline, primary red/yellow/blue on black and white, Herbert Bayer Universal typeface aesthetic, modular grid precision, and zero ornament.
---

# Style Pack: Bauhaus

A visual language from the German Bauhaus school (1919–1933): Walter Gropius, László Moholy-Nagy, Herbert Bayer, and Oskar Schlemmer. Form strictly follows function. Every element exists because it serves a purpose. Ornamentation is crime. Color is primary and structural. Typography is a functional system, not decoration.

## Core Principles

1. **Color:** Primary triad only: Red `#CC0000`, Yellow `#FFD700`, Blue `#0033CC`, on `#FFFFFF` white canvas and `#000000` black. No pastels, no tints, no gradients. Color applied as flat fills — never gradients or opacity layers.
2. **Typography:** `font-family: 'IBM Plex Sans', 'Neue Haas Grotesk', Helvetica, sans-serif` at weight 700–900 for display. Body weight 400. Scale locked to 8px baseline grid: 12 / 16 / 24 / 32 / 48 / 64px. Herbert Bayer universal letterforms as decorative elements where applicable.
3. **Geometry:** `border-radius: 0px` universally. Geometric primitives only: circles (`border-radius: 50%`), squares, triangles (CSS clip-path). No freeform organic shapes. Composition built from overlapping geometric blocks.
4. **Grid:** 8px base unit. All spacing and sizing multiples of 8. 12-column grid with 24px gutters. Asymmetric column splits (e.g., 3/9, 4/8) for visual tension.
5. **Borders/Dividers:** Structural `border: 2px solid #000000` to define zones. No decorative borders. No shadows. Separation through solid black lines, not softened edges.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use tonal muted colors or pastels. Only pure primary red, yellow, blue, black, white, and structural gray.
- **NEVER** use ornamental serifs, calligraphic fonts, or display typefaces with personality. Typography is geometric, functional, systematic.
- **NEVER** use drop shadows or blur effects. Depth is expressed through contrasting solid color planes.
- **NEVER** use rounded containers. All geometry is pure circles (for medallion accents), squares, or triangles — no intermediate radii on rectangular containers (0px only).
- **NEVER** use decorative patterns or halftone textures. Surface is pure flat color.
- **NEVER** use more than three accent colors simultaneously. The primary triad is complete — do not augment it.
- **NEVER** use animation for decoration. Motion, if used, is strictly functional: state transitions only.

---

## Bauhaus — Design Tokens

## Color Tokens

```css
:root {
  /* Bauhaus Structural Canvas */
  --color-bauhaus-white: #FFFFFF;
  --color-bauhaus-black: #0A0A0A;    /* Near-black, functional */
  --color-bauhaus-gray: #E8E8E8;     /* Structural neutral */
  --color-bauhaus-gray-mid: #B0B0B0;

  /* The Primary Triad — ONLY these three accent colors */
  --color-bauhaus-red: #D62B2B;
  --color-bauhaus-yellow: #F5C800;
  --color-bauhaus-blue: #1B4FBD;

  /* Typography */
  --color-text-primary: #0A0A0A;
  --color-text-secondary: #3A3A3A;
  --color-text-muted: #707070;
  --color-text-on-dark: #FFFFFF;
  --color-text-on-primary: #FFFFFF;   /* For red/blue backgrounds */
  --color-text-on-yellow: #0A0A0A;   /* Black on yellow */
}
```

## Geometric Accent Tokens

```css
:root {
  /* Bauhaus circle accent size scales */
  --circle-sm: 16px;   /* Bullet / indicator */
  --circle-md: 48px;   /* Section accent */
  --circle-lg: 120px;  /* Hero accent medallion */
}
```

## Border & Structure Tokens

```css
:root {
  --border-structural: 2px solid #0A0A0A;
  --border-light: 1px solid #E8E8E8;
  --radius-none: 0px;          /* All rectangular elements */
  --radius-circle: 50%;        /* Bauhaus circle medallions */
  /* Any other radius value is FORBIDDEN */
}
```

## Shadow Tokens

```css
:root {
  --shadow-none: none; /* Drop shadows: FORBIDDEN */
  /* Depth = contrasting color planes only */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px', none: '0px', sm: '0px', md: '0px',
        lg: '0px', xl: '0px', full: '9999px', // full only for circles
      },
      boxShadow: { DEFAULT: 'none', none: 'none' },
      colors: {
        bauhaus: {
          black: '#0A0A0A', white: '#FFFFFF', gray: '#E8E8E8',
          red: '#D62B2B', yellow: '#F5C800', blue: '#1B4FBD',
        }
      }
    }
  }
}
```

---

## Bauhaus — Typography

## Recommended Font Stacks

### Primary Geometric Functional Sans (Herbert Bayer Universal spirit)
- `Inter` (used at strict weights only: 400/500/700 — no 300 or 900)
- `Geist Sans` (clean, geometric, minimal stroke variation)
- `DM Sans` (humanist geometric)
- `Source Sans 3` (400/600)
- `Neue Haas Grotesk` / `Helvetica Neue` (300/400/700 only)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display** | 52px - 72px | 700 Bold | +0.00em | 1.05 | lowercase preferred (Bayer Universal) |
| **H1** | 36px - 48px | 700 Bold | 0.00em | 1.15 | lowercase or Sentence |
| **H2** | 24px - 32px | 700 Bold | 0.00em | 1.25 | lowercase or Sentence |
| **H3** | 18px - 22px | 500/600 | 0.00em | 1.35 | Sentence |
| **Body** | 15px - 16px | 400 Regular | 0.00em | 1.50 | Sentence |
| **Function Label** | 12px - 13px | 600/700 | +0.06em | 1.25 | lowercase |

## Rules

1. **Lowercase Priority:** Herbert Bayer's Universal typeface was lowercase-first. Use lowercase for primary headings to honor this philosophy.
2. **Only Two Weights in Use:** 400 Regular and 700 Bold. No in-between weights create noise.
3. **Color Typography:** Primary headings or key data values can be rendered in Bauhaus Red, Yellow, or Blue for structural emphasis.

## Anti-Patterns
- **Serif typefaces**: Ornamental by definition — forbidden.
- **Script or calligraphic fonts**: Alien to Bauhaus.
- **Tracking extremes** (+0.10em or -0.03em): Type is neutral and unmanipulated.

---

## Bauhaus — Layout

## Composition Rules

1. **Strict Modular Grid:** All layout derives from an 8px baseline grid. Column and row gutters are multiples of 8. No free-floating arbitrary values.
2. **Solid Color Plane Sections:** Sections are delineated by solid color plane changes — white → black, white → red, black → yellow — not by hairlines or whitespace alone.
3. **Geometric Accent Integration:** Bauhaus circles (50% border-radius, solid primary color) are deployed as section markers, numbered list bullets, and accent spots. They do not exceed the established size scale.
4. **Sidebar + Main Column Structure:** A structural left sidebar (black or primary color block) anchors the primary navigation; a white main column holds content.

## Layout Anti-Patterns
- **Free-floating asymmetric layouts without mathematical basis**: Every element must sit on the grid.
- **Decorative whitespace without structural purpose**: Space is used deliberately, not as aesthetics.
- **Soft corner rounding on any rectangular container**: 0px only.

---

## Bauhaus — Component Rules

## 1. Buttons

### Primary
- **Background:** Bauhaus Blue `#1B4FBD` or Red `#D62B2B`
- **Color:** `#FFFFFF`
- **Border:** `none`
- **Border Radius:** `0px`
- **Shadow:** `none`
- **Font:** 14px Geometric Sans, weight 700, tracking 0.00em, lowercase
- **Padding:** 12px 24px
- **Hover:** Background shifts to complementary primary (blue → red, red → blue), instant 80ms

### Secondary — Structural Outline
- **Background:** White `#FFFFFF`
- **Border:** `2px solid #0A0A0A`
- **Border Radius:** `0px`
- **Color:** `#0A0A0A`
- **Hover:** Background fills to black, color inverts to white

## 2. Cards

- **Background:** `#FFFFFF` or `#E8E8E8`
- **Border:** `2px solid #0A0A0A` or none
- **Border Radius:** `0px`
- **Shadow:** `none`
- **Padding:** 32px
- **Left Accent Bar:** 4px solid Red, Yellow, or Blue — exactly one

## 3. Inputs

- **Border:** `2px solid #0A0A0A`
- **Border Radius:** `0px`
- **Background:** `#FFFFFF`
- **Focus:** Border shifts to Bauhaus Blue `#1B4FBD`; no glow ring
- **Font:** 15px Geometric Sans, weight 400

## 4. Status Indicators

- **Shape:** Solid filled circle (8px or 12px, `border-radius: 50%`) in primary color
- **Red circle:** Error / alert
- **Yellow circle:** Warning / pending
- **Blue circle:** Active / in progress
- **Black circle:** Complete

---

## Bauhaus — Motion

## Philosophy

Motion is strictly functional. It communicates state change, not delight. If an animation can be removed without information loss, it must be removed.

## Tokens

```css
:root {
  --duration-bauhaus-instant: 80ms;
  --duration-bauhaus-standard: 160ms;
  --ease-bauhaus: cubic-bezier(0, 0, 0.2, 1);
  --ease-bauhaus-linear: linear;
}
```

## Transitions

1. **Button color swap:** 80ms linear — fast, functional.
2. **Navigation active state:** 160ms border-bottom draw or background fill.
3. **Content panel swap:** 160ms opacity 1 → 0 → 1 (cross-dissolve on state change).

## Anti-Patterns
- No spring animations.
- No decorative kinetics (parallax, floating, hover lifts).
- Anything exceeding 200ms must justify its duration with functional necessity.
