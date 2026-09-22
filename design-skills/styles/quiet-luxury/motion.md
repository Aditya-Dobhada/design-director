# Quiet Luxury — Motion & Transitions

## Motion Philosophy

Motion is cinematic, unhurried, and poised. Transitions feel like turn-of-the-century film cuts or pages turning in a cloth-bound book. Zero bouncy springs, zero abrupt jarring cuts.

## Timing & Easing Curves

```css
:root {
  --duration-luxury-fast: 250ms;
  --duration-luxury-standard: 400ms;
  --duration-luxury-slow: 600ms;

  /* Custom cubic bezier for smooth, graceful deceleration */
  --ease-luxury: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-luxury-in-out: cubic-bezier(0.65, 0, 0.35, 1);
}
```

## Transition Specifications

1. **Button & Link Hover:**
   - Duration: `350ms`
   - Timing: `var(--ease-luxury)`
   - Property: `background-color, color, border-color`
2. **Page Section Reveals:**
   - Smooth subtle fade: opacity 0 -> 1, translateY(12px -> 0px) over 600ms.
3. **Image / Card Tonal Shift:**
   - Smooth subtle opacity or filter transition over 500ms.

## Motion Anti-Patterns
- **No Spring / Rubber-band Physics:** Strict prohibition against spring overshoots.
- **No Frantic Short Durations:** Durations under 150ms feel rushed and nervous.
