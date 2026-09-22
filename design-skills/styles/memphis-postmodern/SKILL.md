---
name: style-memphis-postmodern
description: Implementation rules for Memphis Postmodern style. 1980s Memphis Group geometric maximalism, Ettore Sottsass pattern collisions, contrasting squiggle/dot/stripe motifs, acid pastels mixed with primaries on white, and deliberately anti-functional playfulness.
---

# Style Pack: Memphis Postmodern

A visual language from the radical 1980s Memphis Group design movement led by Ettore Sottsass. Memphis rejected functionalism with geometric decoration for its own sake: squiggle lines, dot patterns, diagonal stripe fills, and intentional kitsch collisions between clashing pastels and primaries.

## Core Principles

1. **Color:** Contrasting primaries on white: Electric yellow `#FFE000`, coral `#FF6B6B`, cobalt `#003DE8`, teal `#00B4B4`, plus `#FFFFFF` background and `#000000` outlines. No gradients. No muted palettes. Colors appear as flat fills only.
2. **Patterns:** Squiggle lines, polka dots (12px circles on 24px grid), diagonal hatching (45° at 4px spacing), zigzag bands — applied as CSS `background-image` repeating patterns or inline SVGs. At least two distinct patterns per layout.
3. **Typography:** Display: `font-family: 'Boogaloo', 'Righteous', 'Fredoka One', sans-serif` at weight 400–700. Body: `'Space Grotesk'` or `'DM Sans'` for legibility. Large numbers and single letters as graphic elements (200px+). Never serif for display.
4. **Geometry:** Mixed `border-radius` within the same layout: 0px on some elements, 50% on others, 8px on others — intentional inconsistency. Shapes overlap and clip outside their containers. No visual hierarchy of uniform radii.
5. **Borders:** `border: 2px solid #000000` as a unifying element across all patterns and shapes. All pattern blocks enclosed in solid black outlines. No opacity-reduced borders.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use subtle, tonal, or restrained palettes. Memphis is deliberately chromatic excess — muted grays are a violation.
- **NEVER** use diffuse shadows or blur effects. Flat opaque graphic planes only.
- **NEVER** use austere negative space as a design device. Empty white areas must be filled with pattern motifs.
- **NEVER** use serious editorial serifs or formal grotesks. Typography must carry playful irreverence.
- **NEVER** use conventional container rectangles with default 8px radii. Shapes should be eccentric trapezoids, circles, or 0px sharp cuts.
- **NEVER** use smooth, professional animations. Motion is abrupt, pop-art mechanical, or totally absent.
- **NEVER** use dark backgrounds. Memphis lives on stark white or pale lemon with chromatic surface explosions.
