# Japanese Wabi-Sabi — Motion

## Philosophy

Motion is like the slow opening of a shoji screen, the settling of a tea bowl onto a wooden surface, or ink spreading through washi paper. It is breath-paced, inevitable, and never rushed or exuberant.

## Tokens

```css
:root {
  --duration-wabi-breath: 400ms;
  --duration-wabi-settle: 600ms;
  --duration-wabi-unfurl: 900ms;

  --ease-wabi: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-wabi-slow: cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Transitions

1. **Button hover:** 350ms ease-out, background color shifts — no translate or scale.
2. **Section entrance:** Opacity 0 → 1, translateY(16px → 0), 600ms. Stagger sibling elements by 120ms.
3. **Ink divider reveal:** SVG stroke-dasharray draw-in over 900ms on scroll entry.

## Anti-Patterns
- No sub-200ms transitions.
- No spring physics or bouncing.
- No scale pop on hover (elements do not grow on hover).
