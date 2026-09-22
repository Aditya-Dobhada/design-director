# Maximalist Dopamine — Motion

## Philosophy

Motion is jittery, bouncy, and hyper-caffeinated. Elements pop, wiggle, and snap with high visual kinetic reward. Like an arcade cabinet or pinball machine hitting a bonus multiplier.

## Tokens

```css
:root {
  --duration-dopamine-pop: 90ms;
  --duration-dopamine-bounce: 160ms;
  --duration-dopamine-wiggle: 250ms;

  --ease-dopamine-pop: cubic-bezier(0.34, 1.56, 0.64, 1); /* Hyper-spring */
  --ease-dopamine-snap: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transitions

1. **Button Pop on Hover:** `transform: translate(-2px, -2px) scale(1.03)` with `var(--ease-dopamine-pop)` over 120ms.
2. **Sticker Wiggle:** Subtle continuous rotation oscillation (`-2deg -> 2deg`) on hovered tags.
3. **Card Press:** Rapid 80ms down-press with zero-shadow collision.

## Anti-Patterns
- No languid 500ms+ dissolves.
- No calm, restrained, whisper transitions.
- Motion must deliver immediate, tactile feedback.
