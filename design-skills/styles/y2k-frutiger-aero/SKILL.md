---
name: style-y2k-frutiger-aero
description: Implementation rules for Y2K / Frutiger Aero style. Glossy skeuomorphic glass reflections, vibrant aqua/sky/lime palettes, pill-radius buttons, translucent frosted backdrops, and optimistic technological futurism.
---

# Style Pack: Y2K / Frutiger Aero

A design language celebrating the vibrant, optimistic futurism of the mid-2000s to early 2010s. Characterized by glossy glass reflections, crystal-clear water and sky motifs, lush greens, translucent acrylic layers, and skeuomorphic tactile depth.

## Core Principles

1. **Luminous Skeuomorphic Depth & Glass:** Surfaces feature glossy highlight reflections on their top hemisphere, subtle inner borders, and soft glowing dropshadows.
2. **Techno-Organic Palette:** Clear sky cyan (`#00C4FF`), Aero blue (`#0078D7`), vivid lime green (`#76B900`), and clean white translucency.
3. **Pill & Rounded Organic Geometry:** Buttons and badges use generous border radii (`rounded-full`, 12px to 24px) that feel like polished river stones or glass capsules.
4. **Frosted Acrylic / Aero Glass:** Backgrounds and cards use translucent layers with backdrop blur (`backdrop-filter: blur(12px)`), paired with crisp 1px white specular border highlights.
5. **Optimistic, Buoyant Motion:** Transitions feel fluid, aquatic, and lively with gentle spring physics.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use 0px sharp corners (`rounded-none`). All cards and buttons must feature soft or pill rounding (minimum `8px`, ideally `12px` to `full`).
- **NEVER** use flat, borderless flat-design cards. Cards must feature specular top borders or gloss gradient reflections.
- **NEVER** use gloomy, desaturated dark-mode obsidian as the main identity. Aero is light, airy, sky-tinted, and translucent.
- **NEVER** use heavy 3px solid black brutalist borders. Borders must be translucent white specular lines (`rgba(255,255,255,0.7)`) or soft cyan/blue strokes.
- **NEVER** use harsh monospace or gothic serif typefaces. Typography is clean, humanist, rounded, or tech-sans.
- **NEVER** use zero-elevation flat design without depth cues. Depth is an essential pillar of Frutiger Aero.
