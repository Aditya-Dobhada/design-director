# Neo-Brutalism — Layout & Spatial Composition

## Grid & Composition Rules

1. **Card Stacking & Physical Layers:**
   - Elements are framed as distinct physical cards on a cream or saturated canvas.
   - Cards can have subtle overlapping offsets or rotated sticker badges (`transform: rotate(-2deg)` or `rotate(3deg)`).
2. **Clear Spatial Separation:**
   - Cards are separated by explicit margins (20px to 32px), allowing their 4px solid black offset shadows to stand out against the background without colliding into each other.
3. **Chunky Section Banners:**
   - Full-width ticker banners or scrolling marquee strips with 3px top and bottom black borders, filled with high-voltage yellow (`#FFE600`) or lime (`#00F0A8`).
4. **Header Navigation:**
   - Framed within a distinct border container: `border: 3px solid #000; box-shadow: 4px 4px 0px #000; border-radius: 6px;` or spanning full width with a crisp 3px bottom rule.

## Layout Anti-Patterns
- **Borderless Floating Lists:** Floating content without borders looks unfinished in Neo-Brutalism.
- **Glassmorphic Floating Bars:** Blurred backdrop headers are strictly forbidden.
- **Micro-Padded Forms:** Forms with crammed 4px paddings destroy the chunky poster aesthetic.
