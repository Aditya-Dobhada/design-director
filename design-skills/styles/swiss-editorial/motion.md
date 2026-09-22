# Swiss / Editorial — Motion & Transitions

## Motion Philosophy

Motion is utilitarian, immediate, and restrained. It serves strictly to confirm state transitions and orient the eye across architectural shifts. Never use playful bounces, rubber-banding, or dramatic zooms.

## Timing & Easing Curves

```css
:root {
  /* Durations */
  --duration-instant: 80ms;
  --duration-snappy: 140ms;
  --duration-standard: 200ms;

  /* Easings */
  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-linear: cubic-bezier(0, 0, 1, 1);
}
```

## Transition Specifications

1. **Hover Transitions (Buttons & Links):**
   - Property: `background-color`, `color`, `border-color`
   - Duration: `140ms`
   - Timing Function: `cubic-bezier(0.16, 1, 0.3, 1)`
2. **Page & Section Shifts:**
   - Subtle vertical fade: opacity 0 -> 1, transform translateY(6px -> 0px)
   - Duration: `200ms`
3. **Disclosure / Accordion:**
   - Height transition with zero overshoot. Snappy 180ms ease-out.

## Motion Anti-Patterns
- **No Spring / Bouncy Physics:** `cubic-bezier(0.34, 1.56, 0.64, 1)` is strictly forbidden.
- **No Floating Hover Elevators:** Do not translate cards upwards with `translateY(-6px)` and expanding blur shadows.
- **No Parallax Backgrounds:** Static, architectural stability only.
