---
name: style-quiet-luxury
description: Implementation rules for Quiet Luxury style. Warm alabaster and ecru palettes, immaculate serif headings with whisper-thin hairlines, zero border-radius, generous literary whitespace, and slow graceful cinematic easing.
---

# Style Pack: Quiet Luxury

A design language founded on discretion, bespoke craft, understatement, and expansive breathing room. Rather than clamoring for attention with loud accents or heavy borders, Quiet Luxury achieves authority through typographic perfection, tactile paper tones, and radical restraint.

## Core Principles

1. **Subtlety as the Ultimate Power Move:** Loud colors, aggressive dropshadows, and thick borders signify insecurity. Quiet Luxury uses quiet tonal shifts, whisper hairlines, and generous whitespace.
2. **Warm Tactile Canvas:** Reject sterile `#FFFFFF` and cold `#F3F4F6`. Surfaces are built on warm alabaster, linen, ecru, and aged bone (`#FBFBF9`, `#F5F2EB`, `#EBE7DF`).
3. **Immaculate Editorial Serifs:** High-contrast, elegant serif typefaces (Cormorant Garamond, Canela, Fraunces, Ogg) paired with a disciplined, quiet humanist sans.
4. **Whisper Hairlines & Tone Layering:** Dividers are 1px semi-transparent warm stone (`rgba(0,0,0,0.06)` or `#E8E6E1`). Elevation is communicated through subtle tonal planes or borders, NEVER through dark dropshadows.
5. **Zero Border Radius (`rounded-none`):** Cards, images, and interactive surfaces have crisp 0px corners. Sharp, tailored, architectural lines only.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use rounded corners (`rounded-md`, `rounded-lg`, `rounded-full`). Border-radius must be strictly `0px` (`rounded-none`).
- **NEVER** use dark or blurry drop shadows (`box-shadow: 0 4px 12px rgba(0,0,0,0.15)`). Shadows must be `none`.
- **NEVER** use high-saturation neon or primary colors (e.g. electric blue, bright red, hot pink). All accents are muted earth or mineral tones (champagne, warm espresso, olive bronze, muted brass).
- **NEVER** use heavy borders (`border: 2px` or `3px`). Borders are at most `1px solid rgba(0,0,0,0.08)`.
- **NEVER** crowd content into dense multi-row card grids. Whitespace is the primary asset; margins must be wide and unhurried.
- **NEVER** use bouncy, elastic, or frantic animations. Motion must be slow, fluid, and cinematic (400ms to 600ms).
- **NEVER** use badges with colored pills (`bg-green-100 text-green-800`). Labels are small-caps text with generous letter-spacing.
