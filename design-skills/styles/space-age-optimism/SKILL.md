---
name: style-space-age-optimism
description: Implementation rules for Space Age Optimism style. 1960s NASA/Eero Saarinen futurism, warm white and orange-chrome palette, tulip-pod organic geometry, atomic age moiré patterns, optimistic technological aspiration without darkness or aggression.
---

# Style Pack: Space Age Optimism

A visual language celebrating the luminous technological optimism of the 1960s: NASA mission graphics, Eero Saarinen's Tulip Chair, Olivetti Valentina, TWA terminal, and Braun product design. Curved forms, warm-white surfaces, chrome accents, and a persistent belief that the future is beautiful.

## Core Principles

1. **Canvas:** Warm optical white `#FAFAF8` body background. Never dark canvas — this is radiant, daylit design. Section alternates: warm white `#FAFAF8` and soft warm gray `#F0EDE8`.
2. **Color:** Dominant white base with single Mission Orange accent `#E8521A` (or NASA blue `#1B4FBF`). Chrome metallic: `#C0C0C0` / `#A8A8A8` for borders and structural lines. No neon. No pastels.
3. **Geometry (Pods):** Primary containers: `border-radius: 24px–40px`. Buttons: `border-radius: 48px` (capsule). Icon containers: `border-radius: 50%`. No sharp corners on interactive surfaces. Hard-edged geometric shapes only as decorative background elements.
4. **Typography:** `font-family: 'Euclid Circular', 'DM Sans', 'Neue Haas Grotesk', sans-serif` — clean geometric humanist sans. Weight 400–600 for body, 700–800 for display. No slab serifs, no condensed display fonts, no italics.
5. **Motion:** Smooth `cubic-bezier(0.25, 0.46, 0.45, 0.94)` at 250–350ms. Hover: lift with `transform: translateY(-2px)` and `box-shadow: 0 8px 24px rgba(0,0,0,0.12)`. No hard mechanical clicks. No bounce.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use dark or obsidian backgrounds. Space Age Optimism is radiant, luminous, and warm-white.
- **NEVER** use multiple accent colors. The contrast of ONE vivid accent against white is the entire visual power move.
- **NEVER** use heavy black brutalist borders (`3px solid #000`). Boundaries are fine chrome lines or no lines at all.
- **NEVER** use grunge, halftone, or analog texture. This aesthetic is precision-molded, clean, and futuristic.
- **NEVER** use sharp angular 0px corners on primary containers. Organic curves are essential — minimum 16px radius on cards.
- **NEVER** use neon fluorescent colors. The palette is warm-spectrum, natural material–inspired.
- **NEVER** use condensed aggressive display type. Type is wide, geometric, optimistic, and spacious.
