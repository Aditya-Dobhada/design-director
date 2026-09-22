---
name: style-organic-natural
description: Implementation rules for Organic Natural style. Biophilic design philosophy, botanical illustration aesthetic, seed-pod and mycelium-network geometry, clay/moss/sap/bark earth palette, hand-drawn SVG mark accents, and fluid unhurried motion that breathes.
---

# Style Pack: Organic Natural

A design philosophy grounded in the biophilic turn in contemporary design — organizations like Patagonia, Aesop, and Le Labo applied to digital interfaces. Surfaces feel like handmade paper, glazed ceramic, and pressed botanical specimens. The geometry is imperfect, alive, and continuous rather than mechanical and gridded.

## Core Principles

1. **Color:** Earth palette: clay `#C4714F`, moss `#5C7A4E`, sap green `#3D5C2E`, bone white `#F5F0E8`, warm linen `#EDE6D6`, deep charcoal `#2A2622`. No bright saturated hues. Never neon. Palette max 4 colors per composition.
2. **Geometry:** `border-radius: 16px–32px` (river-stone curves) on cards. `border-radius: 48px–9999px` on pills and tags. Organic blob shapes as background SVG fills. No sharp corners on primary content containers.
3. **Typography:** `font-family: 'Lora', 'Fraunces', 'Libre Baskerville', serif` for headings at weight 400–600. Body: `font-family: 'DM Sans', 'Plus Jakarta Sans', sans-serif` at weight 300–400. Slightly warm `line-height: 1.7–1.8`.
4. **Surfaces:** Off-white linen cards `#EDE6D6` with `box-shadow: 0 2px 12px rgba(42,38,34,0.08)` (soft, warm-tinted shadow). No cold blue-gray shadows. Card borders: none or `1px solid rgba(196,113,79,0.2)` (clay-translucent).
5. **Motion:** `cubic-bezier(0.34, 1.56, 0.64, 1)` (gentle organic spring) at 350–450ms. Hover: warm shadow lift `box-shadow: 0 8px 32px rgba(42,38,34,0.16)`. No linear/mechanical easing. No hard clicks.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use neon or electric colors. Every pigment must be traceable to a natural material (clay, bark, leaf, sap, stone, mineral).
- **NEVER** use sharp 0px rectangular containers for primary content surfaces. Use organic blob clip-paths, large radii (24px–60px), or continuous flowing shapes.
- **NEVER** use mechanical, grid-locked symmetrical layouts. Content should feel grown, not engineered.
- **NEVER** use heavy drop shadows or offset box shadows. Depth is expressed through layered paper tones or subtle material casting shadow (2-4px warm, very-low-opacity).
- **NEVER** use geometric grotesks (Inter, Neue Haas, Helvetica). Typography must be humanist, literary, or handwritten-adjacent.
- **NEVER** use fast, snappy animations. Motion is slow, breathing, and tidal.
- **NEVER** use cold whites (`#FFFFFF`). Warm bone white (`#F5F1E8`) or raw linen are required.
