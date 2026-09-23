---
name: style-retro-americana
description: Implementation rules for Retro Americana style. Mid-century roadside vernacular, Saul Bass poster geometry, warm amber/vermilion/cream palettes, slab serif and condensed display type, halftone textures, and tactile print-register imperfection.
---

# Style Pack: Retro Americana

A visual language drawn from mid-century American commercial vernacular: roadside diner signage, Saul Bass film titles, travel posters, and print letterpress. It is warm, confident, saturated with nostalgia, and structurally bold.

## Mandatory Anti-Patterns

- **NEVER** use cold, flat grays or pure white backgrounds (`#FFFFFF`, `#F3F4F6`). Canvas must be warm: cream (`#F9F0DC`), aged linen (`#EDE5CB`), or warm off-white (`#FBF7EF`).
- **NEVER** use neon or electric colors (cyan, magenta, electric blue). The palette is entirely warm-spectrum incandescent.
- **NEVER** use geometric sans without personality (no plain `Inter`, `Helvetica Neue`). Typography must have historical weight: slabs or condensed display grotesks.
- **NEVER** use blurred translucent frosted glass or modern `backdrop-blur`. This is a physical print world.
- **NEVER** use zero-radius flat digital cards. Cards have 3px solid ink borders and subtle paper texture.
- **NEVER** use smooth, frictionless spring animations. Motion is slow, deliberate, projector-reel mechanical.
- **NEVER** use generic icon sets (Heroicons, Feather). Iconography is bold silhouette vector cut-outs or WPA-style illustration marks.

---

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
  --border-ink-sm: 2px solid #1C1410;
  --border-ink-md: 3px solid #1C1410;
  --border-ink-lg: 5px solid #1C1410;

  --texture-halftone: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Ccircle cx='1' cy='1' r='0.8' fill='rgba(28,20,16,0.06)'/%3E%3C/svg%3E");
  --texture-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
}
```

## Shadow & Radius Tokens

```css
:root {
  --shadow-ink-press: 3px 3px 0px #1C1410;
  --shadow-ink-heavy: 5px 5px 0px #1C1410;
  --shadow-none: none;
  --radius-none: 0px;     /* Cards, containers, inputs */
  --radius-tab: 4px 4px 0px 0px;  /* Tab tops only */
}
```

---

## Typography

### Recommended Font Stacks
- **Display / Hero (Slab Serifs):** `Alfa Slab One`, `Zilla Slab` (700/800 Black), `Rockwell`, or `Patua One`
- **Condensed Display Sans:** `Barlow Condensed` (700/800), `Oswald` (600/700), or `Bebas Neue`
- **Body & Supporting:** `Source Serif 4`, `Bitter` (400/500), or `Zilla Slab` (400)

### Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Poster** | 60px - 80px | 900 Black Slab | -0.01em | 0.95 | UPPERCASE / Title |
| **H1** | 40px - 52px | 700/800 Condensed or Slab | -0.01em | 1.10 | UPPERCASE / Title |
| **H2** | 28px - 36px | 700 Condensed | 0.00em | 1.15 | Title case |
| **H3** | 20px - 24px | 600 Slab | +0.02em | 1.25 | Title case |
| **Body** | 15px - 16px | 400 Slab or Serif | 0.00em | 1.60 | Sentence case |
| **Label / Callout** | 12px - 13px | 700 Condensed | +0.08em | 1.20 | UPPERCASE |

### Typographic Rules
1. **All-Caps Poster Headers:** Primary display typography in full uppercase with tight tracking for billboard density.
2. **Warm Ink Text Color:** Primary text is always deep carbon ink (`#1C1410`), never pure `#000000`.
3. **Overline Category Tags:** Short uppercase slab or condensed tags preceding article or product blocks.
4. **Banned Fonts:** Plain sans body (`Inter`, `Roboto`), light/thin weights (100–300), and futuristic display fonts (`Orbitron`).

---

## Layout & Spatial Composition

1. **Saul Bass Geometric Sectioning:** Divide pages with bold solid-color geometric blocks (full-bleed vermilion banners, cream panels, teal section markers) rather than thin digital lines.
2. **Asymmetric Poster Grid:** 2-3 column asymmetric compositions with oversized display type anchoring one quadrant.
3. **Full-Bleed Ink Banner Headers:** Solid ink (`#1C1410`) section headers with inverted cream-on-ink type.
4. **Badge & Stamp Overlays:** Circular badge stamps or angled sticker elements (`transform: rotate(-12deg)`) over card corners.
5. **Layout Anti-Patterns:** No symmetric centered SaaS columns, no borderless floating cards, and no infinite scroll lacking section markers.

---

## Component Rules

### 1. Buttons
- **Primary Ink Press:**
  - Background: Vermilion `#C8391E` or Ink `#1C1410` | Text: Cream `#F9F0DC` | Border: `3px solid #1C1410`
  - Border Radius: `0px` | Shadow: `3px 3px 0px #1C1410` | Padding: 11px 24px
  - Font: 14px Condensed Bold, uppercase, tracking +0.06em
  - Hover: `transform: translate(-1px, -1px); box-shadow: 4px 4px 0px #1C1410;`
  - Active: `transform: translate(3px, 3px); box-shadow: 0px 0px 0px;`
- **Secondary Stamp Outline:**
  - Background: Transparent | Text: `#1C1410` | Border: `3px solid #1C1410` | Shadow: `3px 3px 0px #1C1410`
  - Hover: Inverts to ink background with cream text.

### 2. Cards
- Background: Cream `#F9F0DC` or Linen `#EDE5CB` | Border: `3px solid #1C1410`
- Border Radius: `0px` | Shadow: `3px 3px 0px #1C1410` | Padding: 24px
- Optional halftone overlay: `background-image: var(--texture-halftone);`
- Optional rotated stamp badge: `transform: rotate(-12deg)` on corner.

### 3. Inputs
- Border: `3px solid #1C1410` or bottom-border `border-b-3 border-ink`
- Border Radius: `0px` | Background: `#F9F0DC` | Font: Slab serif, 15px
- Focus: Border shifts to vermilion `#C8391E`.

### 4. Badges & Tags
- Shape: 0px or slight 2px radius | Border: `2px solid #1C1410` | Shadow: `2px 2px 0px #1C1410`
- Background: Amber `#E8A126` or Vermilion `#C8391E` | Text: `#1C1410` or `#F9F0DC`
- Font: 11px Condensed Bold UPPERCASE, tracking +0.08em

---

## Motion & Transitions

```css
:root {
  --duration-retro-snap: 100ms;
  --duration-retro-reel: 280ms;
  --ease-retro: cubic-bezier(0.4, 0, 0.2, 1);
}
```

- **Button Press:** 100ms linear, mechanical translate down/right.
- **Section Reveal:** Slide in from left 24px → 0, opacity 0 → 1, 280ms ease-out.
- **Motion Anti-Patterns:** No bouncy springs, no silky 500ms smooth iOS ease transitions, and no parallax scrolling.
