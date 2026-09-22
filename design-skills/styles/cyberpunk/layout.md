# Cyberpunk — Layout & Spatial Composition

## Grid & Composition Rules

1. **Tactical Modular Grid:**
   - Multi-panel interface with visible division lines and technical framing.
   - High information density: dashboards, telemetry strips, and terminal outputs.
2. **HUD Registration Framing:**
   - Cards and screen corners feature registration brackets:
     ```
     ┌────────────────────────┐
     │ [SYS: ACTIVE]          │
     └────────────────────────┘
     ```
   - Rendered using CSS pseudo-elements (`::before` / `::after`) with 2px borders on corners.
3. **Corner Chamfers & Diagonal Cuts:**
   - Panels and cards cut at 45-degree angles on top-right or bottom-left corners.
4. **Scanlines & Grid Overlay:**
   - Subtle background repeating linear gradient simulating CRT scanlines or radar grids:
     ```css
     background-image: linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
                       linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
     background-size: 24px 24px;
     ```

## Layout Anti-Patterns
- **Light Theme Interfaces:** Any white canvas is a critical violation.
- **Centered SaaS Hero Layouts:** Avoid center-aligned generic hero headings with round pill buttons.
- **Empty Vague Whitespace:** Whitespace without structural grid marks feels like a blank canvas rather than an operational console.
