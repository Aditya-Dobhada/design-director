# Cyberpunk — Motion & Transitions

## Motion Philosophy

Motion is digitized, instantaneous, glitched, or precision-timed. Think of radar sweeps, flickering cathode-ray tubes, telemetry feeds, and lightning-fast terminal response times. Cheerful bounces are forbidden.

## Timing & Easing Curves

```css
:root {
  --duration-cyber-glitch: 60ms;
  --duration-cyber-snap: 100ms;
  --duration-cyber-telemetry: 180ms;

  --ease-cyber-instant: steps(3, end);
  --ease-cyber-snap: cubic-bezier(0, 0, 0.2, 1);
}
```

## Transition Specifications

1. **Button Hover & Activation:**
   - Duration: `80ms`
   - Timing: `linear`
   - Property: `box-shadow, border-color, background-color`
2. **Scanline / Pulse Loop:**
   - Subtle neon breathing glow: 2000ms infinite ease-in-out.
3. **Glitch / CRT Boot:**
   - Rapid 60ms opacity/transform jitter simulating signal noise on page mount.

## Motion Anti-Patterns
- **No Playful Springs:** No bouncing curves.
- **No Languid Sluggish Fades:** Avoid slow 500ms dissolves.
