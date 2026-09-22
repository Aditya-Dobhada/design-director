---
name: style-swiss-editorial
description: Implementation rules for Swiss / Editorial style. Asymmetric grids, rigorous typography hierarchy, high-contrast monochrome with single deliberate accent, zero-or-hairline borders, and zero-blur elevation.
---

# Style Pack: Swiss / Editorial

A visual language grounded in the International Typographic Style (Swiss Style) and contemporary high-end editorial broadsheets. Built on mathematical precision, asymmetric column grids, deliberate scale contrast, and total absence of decorative fluff.

## Core Principles

1. **Information Architecture is the Design:** Structure and typography do 95% of the visual work. Do not use decorative cards or colored backgrounds to create hierarchy where typography and spatial proportion can do it better.
2. **Extreme Typographic Contrast:** Combine large display scales (36px to 64px+) with compact, highly legible body text (14px to 16px). Pair an authoritative editorial serif or stark neo-grotesk with a disciplined body grotesk.
3. **Asymmetric Grid Alignment:** Avoid centered, symmetrical card grids. Use asymmetric column splits (e.g. 5-column / 7-column, 4-column / 8-column) with visible structural alignments.
4. **Ruthless Monochromatic Foundation:** 90% of the surface area is pure white/paper and pure black/ink. Exactly ONE intentional accent color (e.g. Swiss Red `#E30613`, International Klein Blue `#002FA7`, or Forest Noir `#143829`) is permitted for interactive focal points.
5. **Architectural Hairlines:** Dividers and card borders are either 0px (separated by whitespace alone) or strict 1px solid hairlines (`#000000` or `#E5E5E5`). No blurry box shadows.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use pill-shaped buttons (`rounded-full`, `border-radius: 9999px`). Radius must be 0px (`rounded-none`) or maximum 2px (`rounded-sm`).
- **NEVER** use diffuse, blurred box-shadows (`box-shadow: 0 10px 25px rgba(...)` or Tailwind `shadow-lg`, `shadow-xl`). Elevation is conveyed through 1px border lines or solid 1px/2px hard offset lines.
- **NEVER** use rainbow or multi-hue accent colors. Pick exactly ONE accent color and use it strictly for primary actions and active states.
- **NEVER** use floating gradient orbs, blurred mesh backdrops, or decorative background blobs.
- **NEVER** use icon-only decorative chips, pastel badge pills, or cartoonish illustrations.
- **NEVER** center-align long blocks of prose or primary hero copy. Align to left margins with deliberate typographic rag.
- **NEVER** use generic low-contrast gray text (`#9CA3AF`). Secondary text must remain crisp and readable (e.g., `#525252` on light, `#A3A3A3` on dark).
