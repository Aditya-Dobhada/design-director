---
name: style-maximalist-dopamine
description: Implementation rules for Maximalist Dopamine style. High-stimulation visual density, colliding saturated neon palettes, sticker-bomb badges, chaotic typography scale shifts, layered pattern noise, and unapologetic anti-minimalism.
---

# Style Pack: Maximalist Dopamine

A design language rooted in hyper-sensory digital culture, early 2000s net art, sticker-bombed skateboards, and contemporary dopamine-driven aesthetics. It violently rejects the quiet beige and sterile gray conventions of corporate SaaS in favor of intense visual joy, chromatic collision, and expressive density.

## Core Principles

1. **Color:** Candy neon multi-palette: Yellow `#FFDE03`, Magenta `#FF0090`, Cyan `#00E5FF`, Lime `#AAFF00`. Used simultaneously as competing fills. Background is either pure black `#000000` or pure white `#FFFFFF`. 3+ colors active per viewport.
2. **Shadows:** Multi-layer offset shadows on all primary elements: `box-shadow: 4px 4px 0px #FF0090, 8px 8px 0px #00E5FF`. Each shadow a different accent color. No blurred shadows — solid offset only. Shadow colors rotate across cards.
3. **Typography:** `font-family: 'Boogaloo', 'Fredoka One', 'Luckiest Guy', sans-serif` for display at 900 weight where available. Stacked, oversized text at 80px–160px on hero sections. Body: `'Space Grotesk'` weight 500. All-caps `.uppercase` on primary labels and CTAs.
4. **Geometry:** Layered border on cards: `border: 3px solid #000000`, then multi-color offset shadow. `border-radius: 0px` on main cards (sticker-like flatness). `border-radius: 50%` on badge elements. Rotation: `transform: rotate(-2deg)` to `rotate(3deg)` on sticker elements.
5. **Density:** Pack the viewport. Every section has competing visual weight. No empty whitespace — fill with color, pattern, or sticker elements. Navigation: bold, thick, full-bleed color bar.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use muted, tasteful corporate grays or minimalist beige canvases. The aesthetic requires high-stimulation pigment.
- **NEVER** leave wide expanses of empty, austere negative space without graphic interest, stickers, or pattern fills.
- **NEVER** use timid 1px light gray borders (`#E5E7EB`). Borders are bold (2px–4px black, neon, or double-stroked).
- **NEVER** use calm, sleepy 600ms transitions. Motion is instant, jittery, or spring-popping (80ms–150ms).
- **NEVER** use a single restrained accent color. Maximalism requires a minimum of three colliding saturated hues.
- **NEVER** use delicate, whisper-thin typography (weights under 400). Display type must be loud, heavy, and punchy.
- **NEVER** use generic flat design cards without borders, badges, or hard offset shadows.

---

## Maximalist Dopamine — Design Tokens

## Color Tokens

```css
:root {
  /* High-Voltage Candy & Neon Palette */
  --color-dopamine-yellow: #FFF500;
  --color-dopamine-magenta: #FF007F;
  --color-dopamine-cyan: #00E5FF;
  --color-dopamine-lime: #00FF66;
  --color-dopamine-purple: #7A00FF;
  --color-dopamine-orange: #FF5E00;

  /* High-Contrast Bases */
  --color-canvas-black: #0D0D11;
  --color-canvas-candy-pink: #FFE5F1;
  --color-canvas-electric-cream: #FFFFE0;
  --color-ink-black: #000000;
  --color-ink-white: #FFFFFF;

  /* Card Surfaces */
  --color-card-surface-1: #FFF500;
  --color-card-surface-2: #FF007F;
  --color-card-surface-3: #00E5FF;
  --color-card-surface-white: #FFFFFF;
}
```

## Border & Offset Tokens

```css
:root {
  --border-dopamine-black: 3px solid #000000;
  --border-dopamine-heavy: 4px solid #000000;
  --border-dopamine-neon: 3px solid #00FF66;

  /* Colored Hard Offset Shadows (zero blur) */
  --shadow-dopamine-black: 5px 5px 0px #000000;
  --shadow-dopamine-magenta: 5px 5px 0px #FF007F;
  --shadow-dopamine-cyan: 5px 5px 0px #00E5FF;
  --shadow-dopamine-yellow: 5px 5px 0px #FFF500;
  --shadow-dopamine-double: 4px 4px 0px #FF007F, 8px 8px 0px #000000;
}
```

## Border Radius Tokens

```css
:root {
  --radius-chunky: 8px;
  --radius-pill: 9999px;
  --radius-sharp: 0px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderWidth: {
        DEFAULT: '3px',
        3: '3px',
        4: '4px',
      },
      boxShadow: {
        'dopamine-black': '5px 5px 0px #000000',
        'dopamine-magenta': '5px 5px 0px #FF007F',
        'dopamine-cyan': '5px 5px 0px #00E5FF',
        'dopamine-double': '4px 4px 0px #FF007F, 8px 8px 0px #000000',
      },
      colors: {
        dopamine: {
          yellow: '#FFF500', magenta: '#FF007F', cyan: '#00E5FF',
          lime: '#00FF66', purple: '#7A00FF', orange: '#FF5E00',
          candy: '#FFE5F1',
        }
      }
    }
  }
}
```

---

## Maximalist Dopamine — Typography

## Type System Principles

Typography is an act of defiance. It stacks heavy display grotesks next to condensed poster types and chaotic monospace stickers. Headings scream, numbers pop with intense contrast, and text layers overlap.

## Recommended Font Stacks

### Heavy Display Headings
- `Clash Display` (700 Bold / Variable)
- `Syne` (800 ExtraBold)
- `Archivo Black`
- `Cabinet Grotesk` (800/900)
- `Righteous`
- `Rubik Mono One`

### Body & Supporting Type
- `Space Grotesk` (600/700)
- `Plus Jakarta Sans` (600/700)
- `JetBrains Mono` (for sticker codes, tickers, badges)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Scream** | 64px - 96px | 800/900 Heavy | -0.03em | 0.95 | UPPERCASE / Title |
| **H1** | 44px - 56px | 800 Heavy | -0.02em | 1.05 | Title / UPPERCASE |
| **H2** | 30px - 38px | 700 Bold | -0.01em | 1.15 | Title case |
| **H3** | 22px - 26px | 700 Bold | 0.00em | 1.25 | Title case |
| **Body** | 16px - 17px | 600 SemiBold | 0.00em | 1.45 | Sentence case |
| **Sticker / Tag** | 12px - 14px | 800 ExtraBold | +0.06em | 1.10 | UPPERCASE |

## Typographic Rules

1. **Heavy Body Weights:** Minimum body weight is 500/600. Delicate thin typography gets drowned out by saturated color planes.
2. **Text Highlighting:** Key phrases inside headings are highlighted with contrasting color background chips (e.g. black text on neon lime block).
3. **Rotated Inline Badges:** Tiny rotated tags (e.g. `NEW!`, `HOT`, `100%`) positioned above or next to headings.

## Anti-Patterns
- **Delicate formal serifs**: Incompatible with dopamine chaos.
- **Timid gray body copy**: Body copy must be crisp black or crisp white.
- **Understated letter-spacing**: Never whisper.

---

## Maximalist Dopamine — Layout

## Composition Rules

1. **Sticker-Bomb Overlaps:** Elements do not neatly stay inside grid boxes. Badges, pill tags, and secondary cards overlap adjacent card boundaries by 10px–24px.
2. **Scrolling Marquee Ribbons:** Full-bleed marquee banners with 3px black borders filled with high-voltage neon yellow or magenta, repeating uppercase ticker text.
3. **Colliding Color Sectioning:** Rather than separating sections with subtle whitespace, alternate full-bleed saturated colors: Acid Yellow section → Hot Magenta section → Deep Black section.
4. **Rotated Card Grids:** Subtle rotation on cards (`transform: rotate(-1.5deg)` or `rotate(1deg)`) creates a chaotic, pinned-poster energy.

## Layout Anti-Patterns
- **Clean symmetrical card grids with uniform spacing**: Too boring and sterile.
- **Vast empty white spaces without visual markers**: Space must be visually activated.
- **Single-color monochromatic templates**: Anti-maximalist.

---

## Maximalist Dopamine — Component Rules

## 1. Buttons

### Primary — Dopamine Pop
- **Background:** Acid Yellow `#FFF500` or Hot Magenta `#FF007F`
- **Color:** `#000000`
- **Border:** `3px solid #000000`
- **Border Radius:** `8px` or `9999px`
- **Shadow:** `5px 5px 0px #000000` (or colored offset shadow: `5px 5px 0px #00E5FF`)
- **Font:** 15px - 16px Heavy Display, uppercase, weight 800
- **Padding:** 14px 28px
- **Hover:** Pop up: `transform: translate(-2px, -2px); box-shadow: 7px 7px 0px #000000;`
- **Active:** Down-press: `transform: translate(5px, 5px); box-shadow: 0px 0px 0px #000000;`

### Secondary — Multi-Shadow Button
- **Background:** White `#FFFFFF`
- **Border:** `3px solid #000000`
- **Shadow:** `4px 4px 0px #FF007F, 8px 8px 0px #000000`
- **Hover:** Shadow flips colors (Cyan + Magenta).

## 2. Cards

- **Background:** Saturated color block (Neon Yellow, Electric Candy Pink, or White)
- **Border:** `3px solid #000000`
- **Border Radius:** `8px`
- **Shadow:** `5px 5px 0px #000000` (or double offset shadow)
- **Padding:** 28px to 36px
- **Corner Sticker:** Rotated badge pinned to top-right corner with `2px solid #000` and contrasting fill.

## 3. Inputs

- **Border:** `3px solid #000000`
- **Border Radius:** `8px`
- **Background:** `#FFFFFF`
- **Shadow:** `4px 4px 0px #000000`
- **Padding:** 14px 18px
- **Focus:** `box-shadow: 6px 6px 0px #00E5FF; border-color: #000000; outline: none;`

## 4. Sticker Badges

- **Shape:** Pill or faceted 4px rectangle
- **Border:** `2px solid #000000`
- **Background:** Neon Lime `#00FF66` or Magenta `#FF007F`
- **Color:** `#000000` or `#FFFFFF`
- **Transform:** `transform: rotate(-3deg)`
- **Shadow:** `2px 2px 0px #000000`
- **Font:** 11px - 12px, weight 900, UPPERCASE

---

## Maximalist Dopamine — Motion

## Philosophy

Motion is jittery, bouncy, and hyper-caffeinated. Elements pop, wiggle, and snap with high visual kinetic reward. Like an arcade cabinet or pinball machine hitting a bonus multiplier.

## Tokens

```css
:root {
  --duration-dopamine-pop: 90ms;
  --duration-dopamine-bounce: 160ms;
  --duration-dopamine-wiggle: 250ms;

  --ease-dopamine-pop: cubic-bezier(0.34, 1.56, 0.64, 1); /* Hyper-spring */
  --ease-dopamine-snap: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transitions

1. **Button Pop on Hover:** `transform: translate(-2px, -2px) scale(1.03)` with `var(--ease-dopamine-pop)` over 120ms.
2. **Sticker Wiggle:** Subtle continuous rotation oscillation (`-2deg -> 2deg`) on hovered tags.
3. **Card Press:** Rapid 80ms down-press with zero-shadow collision.

## Anti-Patterns
- No languid 500ms+ dissolves.
- No calm, restrained, whisper transitions.
- Motion must deliver immediate, tactile feedback.
