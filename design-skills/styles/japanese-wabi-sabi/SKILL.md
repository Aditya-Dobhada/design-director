---
name: style-japanese-wabi-sabi
description: Implementation rules for Japanese Wabi-Sabi style. Mingei folk craft philosophy, asymmetric imperfection as beauty, hand-drawn ink brushstroke accents, clay/charcoal/matcha natural palette, extreme silence and breathing room, and contemplative unhurried motion.
---

# Style Pack: Japanese Wabi-Sabi

A design philosophy drawn from the Japanese aesthetics of wabi (understated simplicity) and sabi (the beauty of age and imperfection). Inspired by Mingei folk craft, Zen temple gardens, shodō ink calligraphy, and the work of pottery masters like Shoji Hamada and Lucie Rie's Japanese influences. Nothing is symmetrical, polished, or mass-produced.

## Core Principles

1. **Color:** Rice paper `#F7F3EE`, bamboo cream `#EDE8DF`, charcoal `#1E1E1A`, sumi ink `#2A2420`. Matcha accent `#5C7A4E` or iron gray `#4A4A46`. No bright pigments. No pure `#FFFFFF` white — always warm off-white.
2. **Typography:** `font-family: 'Shippori Mincho', 'Hiragino Mincho Pro', Georgia, serif` for display (weight 400). Body: `Zen Kaku Gothic New` or `Noto Sans JP` at weight 300–400. Generous `line-height: 1.9–2.1`. Letter-spacing `0.02em` on body. Never condensed or heavy weights.
3. **Spacing (Ma):** Whitespace IS the primary design element. Minimum section padding 120px vertical. Content width max 640px for reading columns. Single focused element per screen viewport. Never compete for attention — silence communicates.
4. **Geometry:** Asymmetric layouts — deliberately uncentered. `border-radius: 2px–4px` on cards (near-sharp, not rounded). Ink-wash horizontal rules: `border-bottom: 1px solid rgba(30,30,26,0.15)`. No hard black borders.
5. **Texture/Pattern:** Subtle paper texture via CSS `background-image: url('noise.png')` at 3–5% opacity. No photographic backgrounds. Ink-wash brush motifs as SVG overlays at low opacity. No geometric patterns.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use synthetic neon or electric colors. The palette is entirely natural earth, ink, and plant pigment.
- **NEVER** use drop shadows or blur. Elevation is expressed through layered ink washes or tonal background shifts alone.
- **NEVER** use symmetric card grids with equal spacing. Asymmetry is mandatory — no two elements may have identical spatial relationships.
- **NEVER** use bold, heavy-weight geometric grotesks for headings. Calligraphic brush accents and quiet humanist serifs only.
- **NEVER** use sharp machined 0px corners on all elements. Organic imperfection allows slight irregularity; cards may have subtle hand-cut edges via SVG clip-path.
- **NEVER** use bouncy, energetic, or fast animations. Motion must be slow, contemplative, breath-paced.
- **NEVER** use high-saturation warm-white backgrounds (`#FFFFFF`). Rice paper (`#FAF7F0`), bamboo cream (`#EDE8D0`), or warm linen only.
