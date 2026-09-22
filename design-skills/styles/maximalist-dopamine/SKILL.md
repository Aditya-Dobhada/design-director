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
