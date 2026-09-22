# Neo-Brutalism — Motion & Transitions

## Motion Philosophy

Neo-Brutalism embraces mechanical, physical, and snappy motion. Think of a physical keyboard switch, arcade buttons, or punch cards. Elements snap into place with quick, tactile responses rather than drifting lazily.

## Timing & Easing Curves

```css
:root {
  --duration-neo-fast: 80ms;
  --duration-neo-snap: 120ms;
  --duration-neo-pop: 160ms;

  --ease-neo-snap: cubic-bezier(0, 0, 0.2, 1);
  --ease-neo-linear: linear;
}
```

## Transition Specifications

1. **Button Active Click:**
   - Duration: `80ms`
   - Timing: `linear`
   - Transformation: `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000;`
2. **Hover Pop:**
   - Duration: `120ms`
   - Transformation: `transform: translate(-1px, -1px); box-shadow: 5px 5px 0px #000;`
3. **Card Expansion / Accordion:**
   - Snappy step-down without rubber band.

## Motion Anti-Patterns
- **No Soft Feathered Fades:** Elements shouldn't dissolve like mist. They toggle or snap.
- **No Long 400ms+ Easing:** Never make a user wait through a languid ease-in-out transition.
