# Organic Natural — Motion

## Philosophy

Motion is breathing, tidal, and fluid — mimicking natural phenomena like the swaying of grass, the growth of vines, or water flowing over river stones. No abrupt stops, no mechanical snaps.

## Tokens

```css
:root {
  --duration-organic-breath: 350ms;
  --duration-organic-tide: 550ms;
  --duration-organic-growth: 800ms;

  --ease-organic: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-organic-in-out: cubic-bezier(0.45, 0, 0.55, 1);
}
```

## Transitions

1. **Button hover:** 350ms gentle color shift, 1px lift.
2. **Page element reveals:** Gentle unfurl — opacity 0 -> 1, translateY(12px -> 0), 550ms smooth deceleration.
3. **Botanical illustration stroke draw:** 1200ms SVG stroke-dashoffset transition on first viewport entry.

## Anti-Patterns
- No sub-150ms snap cuts.
- No bouncy cartoon springs.
- No linear robotic movements.
