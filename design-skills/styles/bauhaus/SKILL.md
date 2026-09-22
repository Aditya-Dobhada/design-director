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
