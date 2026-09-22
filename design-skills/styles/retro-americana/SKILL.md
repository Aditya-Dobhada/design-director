---
name: style-retro-americana
description: Implementation rules for Retro Americana style. Mid-century roadside vernacular, Saul Bass poster geometry, warm amber/vermilion/cream palettes, slab serif and condensed display type, halftone textures, and tactile print-register imperfection.
---

# Style Pack: Retro Americana

A visual language drawn from 1950s–1970s American commercial vernacular: roadside diner signage, Saul Bass film titles, Federal era travel posters, Route 66 motel neon, and Depression-era WPA prints. It is warm, confident, saturated with nostalgia, and structurally bold.

## Core Principles

1. **Color:** Vermilion `#CC3311`, neon amber `#FFB300`, parchment `#F5E6C8`, carbon `#1A1208`, cream `#FFF8E7`. No digital-clean colors. All values reference vintage ink press printing — slight warmth, slight desaturation.
2. **Typography:** Display: `font-family: 'Alfa Slab One', 'Playfair Display Black', serif` at weight 900. Headline: `'Oswald', 'Barlow Condensed'` at weight 700, uppercase. Body: `'Source Serif Pro', 'Lora'` at weight 400. No sans-serif display headings — always slab or condensed serif for headers.
3. **Borders:** `border: 3px solid #1A1208` on cards and containers. `border: 2px solid #CC3311` as decorative rule between sections. No `border-gray-*` — all borders are ink-dark or vermilion. No box-shadow blur — only `box-shadow: 3px 3px 0px #1A1208` offset.
4. **Geometry:** `border-radius: 0px` on cards, containers, and form inputs. Buttons: `border-radius: 4px` max. Stamp badges: `border-radius: 50%` only. Never rounded-lg or rounded-xl on primary containers.
5. **Texture:** SVG halftone dot pattern at 8% opacity on primary background sections. Worn paper grain on hero areas via CSS `filter: contrast(1.05) brightness(0.98)`. No photographic textures from stock.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use cold, flat grays or pure white backgrounds (`#FFFFFF`, `#F3F4F6`). Canvas must be warm: cream (`#F9F0DC`), aged linen (`#EDE5CB`), or warm off-white (`#FBF7EF`).
- **NEVER** use neon or electric colors (cyan, magenta, electric blue). The palette is entirely warm-spectrum incandescent.
- **NEVER** use geometric sans without personality (no plain `Inter`, `Helvetica Neue`). Typography must have historical weight: slabs or condensed display grotesks.
- **NEVER** use blurred translucent frosted glass or modern `backdrop-blur`. This is a physical print world.
- **NEVER** use zero-radius flat digital cards. Cards have 3px solid ink borders and subtle paper texture.
- **NEVER** use smooth, frictionless spring animations. Motion is slow, deliberate, projector-reel mechanical.
- **NEVER** use generic icon sets (Heroicons, Feather). Iconography is bold silhouette vector cut-outs or WPA-style illustration marks.
