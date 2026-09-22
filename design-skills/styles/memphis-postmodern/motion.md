# Memphis Postmodern — Motion

## Philosophy

Motion is either absent (pure static graphic) or abrupt pop-art mechanical. No smoothing, no easing curves that feel sophisticated. Pattern switches and color hops are instantaneous.

## Tokens

```css
:root {
  --duration-memphis-pop: 80ms;
  --ease-memphis: steps(1, end); /* Binary state switches */
  --ease-memphis-bounce: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transitions

1. **Hover color swap:** Instantaneous `steps(1)` — no cross-fade.
2. **Pattern fill reveal:** 80ms `ease-out` opacity.
3. **Card pop-in on mount:** Scale `0.95 → 1.0` over 100ms.

## Anti-Patterns
- No silky smooth 300ms transitions.
- No spring physics.
- No parallax or scroll-linked effects.
