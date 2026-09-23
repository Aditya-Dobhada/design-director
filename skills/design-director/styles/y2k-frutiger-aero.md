---
name: style-y2k-frutiger-aero
description: Implementation rules for Y2K / Frutiger Aero style. Glossy skeuomorphic glass reflections, vibrant aqua/sky/lime palettes, pill-radius buttons, translucent frosted backdrops, and optimistic technological futurism.
---

# Style Pack: Y2K / Frutiger Aero

A design language celebrating the vibrant, optimistic futurism of the mid-2000s to early 2010s. Characterized by glossy glass reflections, crystal-clear water and sky motifs, lush greens, translucent acrylic layers, and skeuomorphic tactile depth.

## Core Principles

1. **Color:** Sky gradient: `linear-gradient(180deg, #87CEEB 0%, #E0F4FF 100%)`. Aqua accent `#00CFDC`. Gloss overlay: `rgba(255,255,255,0.35)` on all primary surfaces. Warm white base `#FAFEFF`. No dark canvases. No desaturated palettes.
2. **Surfaces:** Gloss cards: `background: rgba(255,255,255,0.45)`, `backdrop-filter: blur(12px)`, `border: 1px solid rgba(255,255,255,0.6)`, `box-shadow: 0 8px 32px rgba(0,207,220,0.15)`. The glass effect is mandatory on all card components.
3. **Typography:** `font-family: 'Nunito', 'Varela Round', 'Rounded Mplus 1c', sans-serif` — rounded geometric humanist. Weight 400–700. Avoid sharp grotesque fonts (no Helvetica Neue or Inter). Display size 48px+, tightly letter-spaced `letter-spacing: -0.01em`.
4. **Geometry:** `border-radius: 16px–24px` on cards. `border-radius: 48px–9999px` on buttons (pill shape). `border-radius: 50%` on avatars and icon containers. Zero sharp corners on interactive surfaces.
5. **Motion:** Springy `cubic-bezier(0.34, 1.56, 0.64, 1)` at 300–400ms. Hover: scale up `transform: scale(1.03)` with glow shadow. Button click: scale down `transform: scale(0.97)`. Micro-animations on icons: 200ms bounce.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use 0px sharp corners (`rounded-none`). All cards and buttons must feature soft or pill rounding (minimum `8px`, ideally `12px` to `full`).
- **NEVER** use flat, borderless flat-design cards. Cards must feature specular top borders or gloss gradient reflections.
- **NEVER** use gloomy, desaturated dark-mode obsidian as the main identity. Aero is light, airy, sky-tinted, and translucent.
- **NEVER** use heavy 3px solid black brutalist borders. Borders must be translucent white specular lines (`rgba(255,255,255,0.7)`) or soft cyan/blue strokes.
- **NEVER** use harsh monospace or gothic serif typefaces. Typography is clean, humanist, rounded, or tech-sans.
- **NEVER** use zero-elevation flat design without depth cues. Depth is an essential pillar of Frutiger Aero.

---

## Y2K / Frutiger Aero — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Sky, Water & Aero Accents */
  --color-aero-cyan: #00C4FF;
  --color-aero-blue: #0078D7;
  --color-aero-sky: #E8F4FD;
  --color-aero-lime: #76B900;
  --color-aero-aqua: #00D2BA;

  /* Gloss & Glass Surfaces */
  --color-glass-base: rgba(255, 255, 255, 0.72);
  --color-glass-surface: rgba(255, 255, 255, 0.85);
  --color-glass-border: rgba(255, 255, 255, 0.8);
  --color-glass-border-subtle: rgba(0, 120, 215, 0.18);

  /* Typography */
  --color-text-primary: #0F2744;
  --color-text-secondary: #3B577D;
  --color-text-muted: #6B88B0;
  --color-text-white: #FFFFFF;
}
```

## Border Radius Tokens

```css
:root {
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-pill: 9999px; /* Core Frutiger Aero element */
}
```

## Shadow & Gloss Depth Tokens

```css
:root {
  /* Dual-layer depth: inner specular highlight + soft cyan drop glow */
  --shadow-aero-card: 
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    0 4px 16px rgba(0, 120, 215, 0.12),
    0 1px 3px rgba(0, 0, 0, 0.05);

  --shadow-aero-button: 
    inset 0 1px 0 rgba(255, 255, 255, 0.8),
    inset 0 -2px 0 rgba(0, 0, 0, 0.15),
    0 4px 12px rgba(0, 196, 255, 0.35);

  --shadow-aero-glow: 0 0 16px rgba(0, 196, 255, 0.5);
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        'aero': '14px',
        'aero-pill': '9999px',
      },
      boxShadow: {
        'aero-card': 'inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 4px 16px rgba(0, 120, 215, 0.12)',
        'aero-btn': 'inset 0 1px 0 rgba(255, 255, 255, 0.8), inset 0 -2px 0 rgba(0, 0, 0, 0.15), 0 4px 12px rgba(0, 196, 255, 0.35)',
      },
      colors: {
        aero: {
          cyan: '#00C4FF',
          blue: '#0078D7',
          sky: '#E8F4FD',
          lime: '#76B900',
          aqua: '#00D2BA',
          text: '#0F2744',
          subtext: '#3B577D',
        }
      }
    }
  }
}
```

---

## Y2K / Frutiger Aero — Typography

## Type System Principles

Frutiger Aero typography is approachable, forward-looking, clear, and humanist. It uses smooth geometric or rounded sans typefaces that feel clean and optimistic.

## Recommended Font Stacks

### Primary Font Stacks
- `Trebuchet MS` / `Segoe UI` (Iconic 2000s Aero foundation)
- `Comfortaa` / `Quicksand` (For playful, bubbly rounded headings)
- `Exo 2` / `Ubuntu` / `Nunito`
- `Arial Rounded MT Bold`

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 52px - 68px | 700 / 800 | -0.01em | 1.10 | Title case |
| **H1** | 36px - 44px | 700 Bold | -0.01em | 1.20 | Title case |
| **H2** | 26px - 32px | 600 SemiBold | 0.00em | 1.25 | Title case |
| **H3** | 20px - 22px | 600 SemiBold | 0.00em | 1.35 | Title case |
| **Body (Default)** | 15px - 16px | 400 / 500 | 0.00em | 1.50 | Sentence case |
| **Badge / Pill** | 12px - 13px | 700 Bold | +0.02em | 1.20 | Sentence / Title |

## Typographic Rules

1. **Subtle Drop Shadows on Large Text:** Hero headings on glossy backgrounds can have a soft, crisp drop shadow (`text-shadow: 0 1px 2px rgba(255,255,255,0.8)` or dark drop shadow on colored pills).
2. **Deep Navy Ink:** Body copy uses deep ocean blue (`#0F2744`) rather than flat gray.
3. **Rounded Letterforms:** Favour rounded terminals and open apertures.

## Anti-Patterns (Fonts to Avoid)
- **Monospace and Terminal fonts**: Clash with the aquatic/naturalistic ethos.
- **Harsh Angular Grotesks** (`Space Grotesk`, `Archivo Black`): Too brutalist.
- **Traditional Serifs** (`Times New Roman`, `Baskerville`): Feel antique rather than technological.

---

## Y2K / Frutiger Aero — Layout & Spatial Composition

## Grid & Composition Rules

1. **Layered Frosted Acrylic Cards:**
   - Content sits inside soft, translucent glass panels (`backdrop-filter: blur(12px); background: rgba(255,255,255,0.75)`).
2. **Sky and Horizon Backgrounds:**
   - Backgrounds use luminous linear or radial gradients evoking open sky, tropical water, or green hills (`linear-gradient(180deg, #E6F6FF 0%, #FFFFFF 60%, #E8F9EE 100%)`).
3. **Pill Floating Navigation:**
   - Floating navigation bar with `border-radius: 9999px`, frosted glass background, specular top highlight, and subtle blue/cyan shadow glow.
4. **Organic Flow & Spacing:**
   - Moderate density with rounded container corners (14px to 24px).

## Layout Anti-Patterns
- **Stark 0px Grid Wireframes:** Harsh, sharp grids with black outlines completely violate the aesthetic.
- **Pure Dark-Mode Obsidian Screens:** Aero must remain luminous, airy, and sky-inspired.
- **Flat Monotone White SaaS Cards:** Flat white boxes without reflections or specular highlights read as boring generic SaaS.

---

## Y2K / Frutiger Aero — Component Rules

Concrete specifications for core UI components.

## 1. Buttons

### Glossy Aqua Pill Button
- **Border Radius:** `9999px` (`rounded-full`).
- **Background:** Dual-tone vertical gloss gradient:
  ```css
  background: linear-gradient(180deg, #38D9FF 0%, #009FE3 50%, #0077C8 100%);
  ```
- **Top Specular Reflection:**
  ```css
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8), inset 0 -2px 0 rgba(0, 0, 0, 0.2), 0 4px 12px rgba(0, 159, 227, 0.4);
  ```
- **Text:** `#FFFFFF`, weight 700, with subtle text-shadow `0 1px 2px rgba(0, 50, 100, 0.5)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.6)`.
- **Padding:** 12px 28px.
- **Hover State:** Glow increases (`0 6px 20px rgba(0, 196, 255, 0.6)`), slight lift (`transform: translateY(-2px)`).
- **Active State:** Button depresses (`transform: translateY(1px)`), inner shadow deepens.

### Secondary Translucent Glass Button
- **Border Radius:** `9999px`.
- **Background:** `rgba(255, 255, 255, 0.6)`.
- **Backdrop Filter:** `blur(8px)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.9)`.
- **Color:** `#0078D7`.

## 2. Cards & Panels

- **Border Radius:** `16px` to `20px`.
- **Background:** `rgba(255, 255, 255, 0.75)`.
- **Backdrop Filter:** `blur(16px)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.85)`.
- **Shadow:**
  ```css
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 8px 32px rgba(0, 120, 215, 0.1);
  ```
- **Padding:** 28px to 36px.

## 3. Inputs & Forms

- **Border Radius:** `9999px` or `12px`.
- **Background:** `rgba(255, 255, 255, 0.9)`.
- **Border:** `1px solid rgba(0, 120, 215, 0.3)`.
- **Shadow:** `inset 0 2px 4px rgba(0, 0, 0, 0.06)`.
- **Focus State:** `outline: none; border-color: #00C4FF; box-shadow: 0 0 12px rgba(0, 196, 255, 0.5), inset 0 1px 2px rgba(0,0,0,0.05);`

## 4. Badges & Pills

- **Shape:** Rounded pill (`rounded-full`).
- **Background:** Gradient aqua/lime: `linear-gradient(180deg, #A8F000 0%, #76B900 100%)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.7)`.
- **Text:** `#FFFFFF`, weight 700, 11px.
- **Shadow:** `0 2px 6px rgba(118, 185, 0, 0.3)`.

---

## Y2K / Frutiger Aero — Motion & Transitions

## Motion Philosophy

Motion is liquid, buoyant, and lively. Elements feel as though they are floating in clear water or gently hovering above an airy glass surface. Gentle spring physics and glowing pulses bring the interface to life.

## Timing & Easing Curves

```css
:root {
  --duration-aero-quick: 180ms;
  --duration-aero-fluid: 280ms;
  --duration-aero-float: 400ms;

  /* Buoyant spring ease with gentle bounce */
  --ease-aero-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-aero-fluid: cubic-bezier(0.25, 0.8, 0.25, 1);
}
```

## Transition Specifications

1. **Button Hover & Lift:**
   - Duration: `240ms`
   - Timing: `var(--ease-aero-spring)`
   - Properties: `transform: translateY(-2px) scale(1.02); box-shadow: ...`
2. **Modal / Tooltip Floating Bloom:**
   - Smooth scale-up from 0.95 -> 1.0 with gentle spring over 300ms.
3. **Glass Shimmer Animation:**
   - Specular highlight gradient sweeping diagonally across cards on hover.

## Motion Anti-Patterns
- **No Abrupt Cuts:** Everything must transition smoothly.
- **No Rigid Machine Clunks:** Avoid stiff linear zero-easing movements.
