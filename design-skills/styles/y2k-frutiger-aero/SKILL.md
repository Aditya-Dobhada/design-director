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
