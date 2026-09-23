---
name: style-y2k-frutiger-aero
description: Implementation rules for Y2K / Frutiger Aero style. Glossy skeuomorphic glass reflections, vibrant aqua/sky/lime palettes, pill-radius buttons, translucent frosted backdrops, and optimistic technological futurism.
---

# Style Pack: Y2K / Frutiger Aero

A design language celebrating the vibrant, optimistic futurism of the mid-2000s to early 2010s. Characterized by glossy glass reflections, crystal-clear water and sky motifs, lush greens, translucent acrylic layers, and skeuomorphic tactile depth.

## Mandatory Anti-Patterns

- **NEVER** use 0px sharp corners (`rounded-none`). All cards and buttons must feature soft or pill rounding (minimum `8px`, ideally `12px` to `full`).
- **NEVER** use flat, borderless flat-design cards. Cards must feature specular top borders or gloss gradient reflections.
- **NEVER** use gloomy, desaturated dark-mode obsidian as the main identity. Aero is light, airy, sky-tinted, and translucent.
- **NEVER** use heavy 3px solid black brutalist borders. Borders must be translucent white specular lines (`rgba(255,255,255,0.7)`) or soft cyan/blue strokes.
- **NEVER** use harsh monospace or gothic serif typefaces. Typography is clean, humanist, rounded, or tech-sans.
- **NEVER** use zero-elevation flat design without depth cues. Depth is an essential pillar of Frutiger Aero.

---

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

---

## Typography

### Recommended Font Stacks
- **Primary Font Stacks:** `Segoe UI`, `Trebuchet MS`, `Nunito`, `Ubuntu`, or `Exo 2`
- **Playful / Rounded Headings:** `Comfortaa`, `Quicksand`, or `Arial Rounded MT Bold`

### Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 52px - 68px | 700 / 800 | -0.01em | 1.10 | Title case |
| **H1** | 36px - 44px | 700 Bold | -0.01em | 1.20 | Title case |
| **H2** | 26px - 32px | 600 SemiBold | 0.00em | 1.25 | Title case |
| **H3** | 20px - 22px | 600 SemiBold | 0.00em | 1.35 | Title case |
| **Body (Default)** | 15px - 16px | 400 / 500 | 0.00em | 1.50 | Sentence case |
| **Badge / Pill** | 12px - 13px | 700 Bold | +0.02em | 1.20 | Sentence / Title |

### Typographic Rules
1. **Drop Shadows on Large Text:** Hero headings on glossy backgrounds can feature subtle specular text shadows (`text-shadow: 0 1px 2px rgba(255,255,255,0.8)`).
2. **Deep Navy Ink:** Body copy uses deep ocean blue (`#0F2744`) rather than flat gray.
3. **Rounded Letterforms:** Favor rounded terminals and open apertures.
4. **Banned Fonts:** Monospaces, harsh angular grotesks (`Space Grotesk`, `Archivo Black`), and traditional antique serifs (`Times New Roman`).

---

## Layout & Spatial Composition

1. **Layered Frosted Acrylic Cards:**
   - Content sits inside soft, translucent glass panels (`backdrop-filter: blur(12px); background: rgba(255,255,255,0.75)`).
2. **Sky and Horizon Backgrounds:**
   - Backgrounds use luminous linear or radial gradients evoking open sky or water (`linear-gradient(180deg, #E6F6FF 0%, #FFFFFF 60%, #E8F9EE 100%)`).
3. **Pill Floating Navigation:**
   - Floating navigation bar with `border-radius: 9999px`, frosted glass background, specular top highlight, and subtle blue/cyan shadow glow.
4. **Layout Anti-Patterns:**
   - No stark 0px black wireframe grids. No dark obsidian canvases. No flat monotone boxes lacking depth or specular highlights.

---

## Component Rules

### 1. Buttons
- **Glossy Aqua Pill Button:**
  - Border Radius: `9999px` (`rounded-full`)
  - Background: `linear-gradient(180deg, #38D9FF 0%, #009FE3 50%, #0077C8 100%)`
  - Shadow: `inset 0 1px 0 rgba(255, 255, 255, 0.8), inset 0 -2px 0 rgba(0, 0, 0, 0.2), 0 4px 12px rgba(0, 159, 227, 0.4)`
  - Text: `#FFFFFF`, weight 700, text-shadow `0 1px 2px rgba(0, 50, 100, 0.5)`
  - Border: `1px solid rgba(255, 255, 255, 0.6)` | Padding: 12px 28px
  - Hover: `transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 196, 255, 0.6);`
  - Active: `transform: translateY(1px);`
- **Secondary Translucent Glass Button:**
  - Border Radius: `9999px` | Background: `rgba(255, 255, 255, 0.6)`
  - Backdrop Filter: `blur(8px)` | Border: `1px solid rgba(255, 255, 255, 0.9)` | Text: `#0078D7`

### 2. Cards & Panels
- Border Radius: `16px` to `20px` | Background: `rgba(255, 255, 255, 0.75)`
- Backdrop Filter: `blur(16px)` | Border: `1px solid rgba(255, 255, 255, 0.85)`
- Shadow: `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 8px 32px rgba(0, 120, 215, 0.1);`
- Padding: 28px to 36px

### 3. Inputs & Forms
- Border Radius: `9999px` or `12px` | Background: `rgba(255, 255, 255, 0.9)`
- Border: `1px solid rgba(0, 120, 215, 0.3)` | Shadow: `inset 0 2px 4px rgba(0, 0, 0, 0.06)`
- Focus: `outline: none; border-color: #00C4FF; box-shadow: 0 0 12px rgba(0, 196, 255, 0.5);`

### 4. Badges & Pills
- Shape: Rounded pill (`rounded-full`) | Background: `linear-gradient(180deg, #A8F000 0%, #76B900 100%)`
- Border: `1px solid rgba(255, 255, 255, 0.7)` | Text: `#FFFFFF`, weight 700, 11px
- Shadow: `0 2px 6px rgba(118, 185, 0, 0.3)`

---

## Motion & Transitions

```css
:root {
  --duration-aero-quick: 180ms;
  --duration-aero-fluid: 280ms;
  --duration-aero-float: 400ms;
  --ease-aero-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-aero-fluid: cubic-bezier(0.25, 0.8, 0.25, 1);
}
```

- **Button Hover & Lift:** Duration 240ms, `var(--ease-aero-spring)`, `transform: translateY(-2px) scale(1.02)`.
- **Modal / Floating Bloom:** Scale-up 0.95 -> 1.0 with gentle spring over 300ms.
- **Glass Shimmer Animation:** Specular highlight gradient sweeping diagonally across cards on hover.
- **Motion Anti-Patterns:** No abrupt jarring cuts, no stiff linear zero-easing mechanical movements.
