---
name: style-quiet-luxury
description: Implementation rules for Quiet Luxury style. Warm alabaster and ecru palettes, immaculate serif headings with whisper-thin hairlines, zero border-radius, generous literary whitespace, and slow graceful cinematic easing.
---

# Style Pack: Quiet Luxury

A design language founded on discretion, bespoke craft, understatement, and expansive breathing room. Rather than clamoring for attention with loud accents or heavy borders, Quiet Luxury achieves authority through typographic perfection, tactile paper tones, and radical restraint.

## Core Principles

1. **Typography:** `font-family: 'Cormorant Garamond', Georgia, serif` at `font-weight: 300–400` for all h1–h2. Body copy: `Suisse Int'l` or `Neue Haas Unica` at weight 300–400, 17–18px, 1.65 line-height. Never Inter, Helvetica, or Roboto for display headings.
2. **Color:** Canvas `#FBFBF9` (warm alabaster). Primary text `#1C1C1A`. Stone dividers `#E8E4DF`. Single deep-ink accent `#2C2C28`. No bright hues, no Tailwind color classes except `bg-neutral-*`, `text-neutral-*` (custom values only).
3. **Geometry:** `border-radius: 0px` on all containers, cards, and buttons. No `rounded-*` Tailwind class except `rounded-none`. No drop shadows — separation via 1px stone dividers `#E8E4DF`.
4. **Spacing:** Minimum 80px section padding. Grid gutters ≥ 40px. Never collapse to mobile gutters < 24px. Whitespace IS the design — never fill it.
5. **Motion:** Max 300ms ease transitions. `cubic-bezier(0.4, 0, 0.2, 1)` only. No bounce, spring, or keyframe animations. No parallax.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners (`rounded-md`, `rounded-lg`, `rounded-full`). Border-radius must be strictly `0px` (`rounded-none`).
- **NEVER** use dark or blurry drop shadows (`box-shadow: 0 4px 12px rgba(0,0,0,0.15)`). Shadows must be `none`.
- **NEVER** use high-saturation neon or primary colors (e.g. electric blue, bright red, hot pink). All accents are muted earth or mineral tones (champagne, warm espresso, olive bronze, muted brass).
- **NEVER** use heavy borders (`border: 2px` or `3px`). Borders are at most `1px solid rgba(0,0,0,0.08)`.
- **NEVER** crowd content into dense multi-row card grids. Whitespace is the primary asset; margins must be wide and unhurried.
- **NEVER** use bouncy, elastic, or frantic animations. Motion must be slow, fluid, and cinematic (400ms to 600ms).
- **NEVER** use badges with colored pills (`bg-green-100 text-green-800`). Labels are small-caps text with generous letter-spacing.
