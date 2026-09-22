# Retro Americana — Motion

## Philosophy

Motion mimics a mechanical world: projection reels, ticker tape, neon sign flickers, and hand-cranked carousels. It is deliberate and unhurried, never frictionless or digital-smooth.

## Tokens

```css
:root {
  --duration-retro-snap: 100ms;
  --duration-retro-reel: 280ms;
  --ease-retro: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-retro-stiff: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transitions

1. **Button press:** 100ms linear, mechanical translate down/right.
2. **Section reveal:** Slide in from left 24px → 0, opacity 0 → 1, 280ms ease-out.
3. **Neon flicker (optional badge):** 3-step opacity pulse: `0.9 → 1 → 0.85 → 1` over 600ms infinite.

## Anti-Patterns
- No bouncy springs.
- No silky 500ms iOS ease transitions.
- No parallax scrolling (breaks the static poster feel).
