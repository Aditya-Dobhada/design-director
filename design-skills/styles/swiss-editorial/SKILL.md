---
name: style-swiss-editorial
description: Implementation rules for Swiss / Editorial style. Asymmetric grids, rigorous typography hierarchy, high-contrast monochrome with single deliberate accent, zero-or-hairline borders, and zero-blur elevation.
---

# Style Pack: Swiss / Editorial

A visual language grounded in the International Typographic Style (Swiss Style) and contemporary high-end editorial broadsheets. Built on mathematical precision, asymmetric column grids, deliberate scale contrast, and total absence of decorative fluff.

## Core Principles

1. **Typography:** `font-family: 'Suisse Int\'l', 'Neue Haas Unica', Helvetica, sans-serif` for all body/UI. Editorial display: `Suisse Works` (serif) or `Playfair Display` at weight 700–900. Scale: 11px caption → 14px body → 22px section → 48px display. Never mix more than 2 type families.
2. **Color:** Canvas `#FFFFFF` or `#F8F8F6`. Primary `#0A0A0A`. Single accent (one of: vermilion `#E63946`, electric blue `#0052CC`, or warm amber `#F4A261`). No gradients. No Tailwind `bg-gray-*` — use custom CSS values.
3. **Geometry:** `border-radius: 0px` universally. Hairlines: `1px solid #0A0A0A` or `0.5px solid rgba(0,0,0,0.2)`. No box-shadow blur > 0px. Grid: strict 12-column, 8px baseline.
4. **Layout:** At least one asymmetric text offset per page section. Column text at 60–70% width max. Large typographic numbers as graphic elements (420px+ at breakpoints).
5. **Motion:** 150–200ms linear or ease-out transitions. No easing bounce. Page transitions: instant or 100ms fade — never slide.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use pill-shaped buttons (`rounded-full`, `border-radius: 9999px`). Radius must be 0px (`rounded-none`) or maximum 2px (`rounded-sm`).
- **NEVER** use diffuse, blurred box-shadows (`box-shadow: 0 10px 25px rgba(...)` or Tailwind `shadow-lg`, `shadow-xl`). Elevation is conveyed through 1px border lines or solid 1px/2px hard offset lines.
- **NEVER** use rainbow or multi-hue accent colors. Pick exactly ONE accent color and use it strictly for primary actions and active states.
- **NEVER** use floating gradient orbs, blurred mesh backdrops, or decorative background blobs.
- **NEVER** use icon-only decorative chips, pastel badge pills, or cartoonish illustrations.
- **NEVER** center-align long blocks of prose or primary hero copy. Align to left margins with deliberate typographic rag.
- **NEVER** use generic low-contrast gray text (`#9CA3AF`). Secondary text must remain crisp and readable (e.g., `#525252` on light, `#A3A3A3` on dark).
