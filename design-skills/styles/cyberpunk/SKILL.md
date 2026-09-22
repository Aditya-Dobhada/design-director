---
name: style-cyberpunk
description: Implementation rules for Cyberpunk style. Obsidian black canvases, electric neon cyan/amber/magenta accents, monospace data telemetry, chamfered cut corners, HUD crosshairs, and scanline/glitch precision.
---

# Style Pack: Cyberpunk

A tactical, high-voltage visual system derived from military telemetry, hacker consoles, dystopian HUDs, and neon-lit megacities. Built for dense data displays, power users, and immersive technical workflows.

## Core Principles

1. **Obsidian Void Canvas:** 100% dark mode. Deep carbon, midnight obsidian, and pitch-black backgrounds (`#08090C`, `#0E1017`) create a backdrop where neon accents burn with intense luminescence.
2. **High-Voltage Triad Accents:** Electric Neon Cyan (`#00F0FF`), Tactical Hazard Yellow/Amber (`#FFB800`), and Acid Neon Magenta (`#FF0055`).
3. **Chamfered & Clipped Geometry:** Diagonal 45-degree cut corners (`clip-path: polygon(...)`), angled tabs, and notched card headers replace generic rectangular boxes.
4. **Data Telemetry & Monospace Dominance:** Technical monospaced typography, tabular numbers, bracketed system prefixes (`[SYS_INIT]`, `// TELEMETRY_ACTIVE`), and coordinate stamps.
5. **HUD Overlays & Framing:** Fine crosshair marks (`+`), corner registration brackets (`┌ ┐`), and subtle scanline grid overlays.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use light mode or white background panels. Light themes are strictly forbidden in Cyberpunk.
- **NEVER** use rounded pill buttons or soft bubble curves (`rounded-full`, `rounded-xl`). Corners must be sharp (`0px`) or chamfered/angled (`clip-path`).
- **NEVER** use pastel, low-contrast, or friendly corporate colors (e.g. soft teal, lavender, baby blue).
- **NEVER** use standard serif fonts or decorative script typefaces.
- **NEVER** use warm organic paper textures, hand-drawn linework, or cozy drop shadows.
- **NEVER** use bouncy, cheerful spring animations. Motion must be instantaneous, mechanical, or digitized.
- **NEVER** leave large swathes of uncalibrated whitespace without structural telemetry framing or grid lines.
