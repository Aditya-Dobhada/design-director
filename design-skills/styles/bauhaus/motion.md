# Bauhaus — Motion

## Philosophy

Motion is strictly functional. It communicates state change, not delight. If an animation can be removed without information loss, it must be removed.

## Tokens

```css
:root {
  --duration-bauhaus-instant: 80ms;
  --duration-bauhaus-standard: 160ms;
  --ease-bauhaus: cubic-bezier(0, 0, 0.2, 1);
  --ease-bauhaus-linear: linear;
}
```

## Transitions

1. **Button color swap:** 80ms linear — fast, functional.
2. **Navigation active state:** 160ms border-bottom draw or background fill.
3. **Content panel swap:** 160ms opacity 1 → 0 → 1 (cross-dissolve on state change).

## Anti-Patterns
- No spring animations.
- No decorative kinetics (parallax, floating, hover lifts).
- Anything exceeding 200ms must justify its duration with functional necessity.
