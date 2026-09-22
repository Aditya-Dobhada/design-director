# Space Age Optimism — Motion

## Philosophy

Motion is smooth, confident, and slightly slower than the modern web default — like a Space Age mechanism opening precisely. No snap-cuts, no bounces. Deliberate, elegant, purposeful kinetics.

## Tokens

```css
:root {
  --duration-space-quick: 200ms;
  --duration-space-standard: 350ms;
  --duration-space-slow: 500ms;
  --ease-space: cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Classic ease-out */
  --ease-space-in-out: cubic-bezier(0.45, 0, 0.55, 1);
}
```

## Transitions

1. **Button hover lift:** 200ms `ease-out`, `translateY(-2px)`, shadow glow expands.
2. **Card reveal on scroll:** Scale `0.97 → 1.0`, opacity `0 → 1`, 350ms.
3. **Navigation capsule active indicator:** 200ms sliding underline or background fill.

## Anti-Patterns
- No spring bounces or rubber-band effects.
- No sub-100ms snap transitions.
- No glitch or flicker effects (that's Cyberpunk).
