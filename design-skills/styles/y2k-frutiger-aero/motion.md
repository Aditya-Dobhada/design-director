# Y2K / Frutiger Aero — Motion & Transitions

## Motion Philosophy

Motion is liquid, buoyant, and lively. Elements feel as though they are floating in clear water or gently hovering above an airy glass surface. Gentle spring physics and glowing pulses bring the interface to life.

## Timing & Easing Curves

```css
:root {
  --duration-aero-quick: 180ms;
  --duration-aero-fluid: 280ms;
  --duration-aero-float: 400ms;

  /* Buoyant spring ease with gentle bounce */
  --ease-aero-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-aero-fluid: cubic-bezier(0.25, 0.8, 0.25, 1);
}
```

## Transition Specifications

1. **Button Hover & Lift:**
   - Duration: `240ms`
   - Timing: `var(--ease-aero-spring)`
   - Properties: `transform: translateY(-2px) scale(1.02); box-shadow: ...`
2. **Modal / Tooltip Floating Bloom:**
   - Smooth scale-up from 0.95 -> 1.0 with gentle spring over 300ms.
3. **Glass Shimmer Animation:**
   - Specular highlight gradient sweeping diagonally across cards on hover.

## Motion Anti-Patterns
- **No Abrupt Cuts:** Everything must transition smoothly.
- **No Rigid Machine Clunks:** Avoid stiff linear zero-easing movements.
