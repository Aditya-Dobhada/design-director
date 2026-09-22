---
name: style-neo-brutalism
description: Implementation rules for Neo-Brutalism style. Thick solid black borders (2-4px), hard offset box shadows (4-6px with zero blur), bold high-saturation color blocks, tactile physical button presses, and punchy display grotesks.
---

# Style Pack: Neo-Brutalism

A bold, high-contrast, tactile aesthetic rooted in raw web design, physical paper zines, and poster art. Neo-Brutalism rejects the sterile, homogenized SaaS aesthetic in favor of tangible borders, hyper-pigmented accents, and physical tactile feedback.

## Core Principles

1. **Borders:** `border: 3px solid #000000` on all interactive elements and cards. No `border-gray-*` or `border-opacity-*`. Buttons: `border: 3px solid #000000` always present — never borderless.
2. **Shadows:** `box-shadow: 4px 4px 0px #000000` on cards. `box-shadow: 6px 6px 0px #000000` on primary CTAs. Shadow offset must be solid black — zero blur radius. Active/pressed state: `box-shadow: 0px 0px 0px`, `transform: translate(4px, 4px)`.
3. **Color:** Maximum saturation background on the dominant element (e.g., `#FFDE03` yellow, `#FF3B30` red, `#00C853` green). Pure `#FFFFFF` or `#000000` secondary backgrounds. Single vibrant accent per composition, not multiple competing hues.
4. **Typography:** `font-family: 'Space Grotesk', 'Clash Display', system-ui` at weight 700–900 for headings. Body: `font-weight: 500` minimum. Uppercase `.tracking-wider` labels. No light or thin font weights.
5. **Geometry:** `border-radius: 0px` on cards and buttons. Inputs: `border-radius: 0px`, thick border. Pills only on tags (4px max). Never `rounded-full` on primary buttons.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use soft, blurry drop shadows (`box-shadow: 0 4px 6px rgba(0,0,0,0.1)` or `filter: drop-shadow(...)` with blur). Blur radius must ALWAYS be `0px`.
- **NEVER** use faint or subtle borders (`border: 1px solid #e2e8f0`). Borders must be at least `2px solid #000000` (typically `3px` or `4px`).
- **NEVER** use washed-out pastel grays as the primary surface identity. Use high-contrast white, cream, or bold saturated backgrounds.
- **NEVER** use glassmorphism, backdrop-blur, or translucent frosted surfaces.
- **NEVER** use floating smooth gradient backgrounds (e.g. purple-to-blue SaaS radial gradients).
- **NEVER** use subtle, sluggish 300ms ease transitions. Transitions must be snappy (80-120ms) and mechanical.
- **NEVER** use timid 12px light-gray secondary text. Text must be stark, legible `#000000` or `#1F2937`.
