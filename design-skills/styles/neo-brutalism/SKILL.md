---
name: style-neo-brutalism
description: Implementation rules for Neo-Brutalism style. Thick solid black borders (2-4px), hard offset box shadows (4-6px with zero blur), bold high-saturation color blocks, tactile physical button presses, and punchy display grotesks.
---

# Style Pack: Neo-Brutalism

A bold, high-contrast, tactile aesthetic rooted in raw web design, physical paper zines, and poster art. Neo-Brutalism rejects the sterile, homogenized SaaS aesthetic in favor of tangible borders, hyper-pigmented accents, and physical tactile feedback.

## Core Principles

1. **Physicality & Hard Geometry:** Elements feel like cut paper cards pinned to a board. Every interactive element has weight, hard outlines, and tangible press depths.
2. **Hard Offset Shadows (Zero Blur):** Shadows are solid black offsets (`3px 3px 0px #000`, `4px 4px 0px #000`, or `5px 5px 0px #000`). Blur is strictly 0px.
3. **Heavy Black Outlines:** Every container, card, button, and input is bordered in solid black (`2px` to `4px` solid `#000000`). No faint `#E5E7EB` border lines.
4. **Hyper-Saturated Accent Palette:** Raw, unapologetic primary and secondary colors: Canary Yellow (`#FFE600`), Electric Lime (`#00F0A8`), Hot Pink (`#FF69B4`), Vivid Cyan (`#00C4FF`), and Alert Orange (`#FF5C00`).
5. **Bold, Punchy Typography:** Heavy display grotesks, punchy geometric sans, or heavyweight monospaces that command attention.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use soft, blurry drop shadows (`box-shadow: 0 4px 6px rgba(0,0,0,0.1)` or `filter: drop-shadow(...)` with blur). Blur radius must ALWAYS be `0px`.
- **NEVER** use faint or subtle borders (`border: 1px solid #e2e8f0`). Borders must be at least `2px solid #000000` (typically `3px` or `4px`).
- **NEVER** use washed-out pastel grays as the primary surface identity. Use high-contrast white, cream, or bold saturated backgrounds.
- **NEVER** use glassmorphism, backdrop-blur, or translucent frosted surfaces.
- **NEVER** use floating smooth gradient backgrounds (e.g. purple-to-blue SaaS radial gradients).
- **NEVER** use subtle, sluggish 300ms ease transitions. Transitions must be snappy (80-120ms) and mechanical.
- **NEVER** use timid 12px light-gray secondary text. Text must be stark, legible `#000000` or `#1F2937`.
