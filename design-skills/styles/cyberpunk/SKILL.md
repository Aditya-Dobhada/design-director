---
name: style-cyberpunk
description: Implementation rules for Cyberpunk style. Obsidian black canvases, electric neon cyan/amber/magenta accents, monospace data telemetry, chamfered cut corners, HUD crosshairs, and scanline/glitch precision.
---

# Style Pack: Cyberpunk

A tactical, high-voltage visual system derived from military telemetry, hacker consoles, dystopian HUDs, and neon-lit megacities. Built for dense data displays, power users, and immersive technical workflows.

## Core Principles

1. **Canvas:** Body background `#080A0E` (obsidian). Card surfaces `#0F1117`. Never any `bg-white`, `bg-gray-50`, or light canvas — this is 100% dark mode.
2. **Color:** Single neon accent: `#39FF14` (acid green), `#00F5FF` (electric cyan), or `#FF0090` (magenta). Accent used for borders, active states, and glow only — never as a fill background. Secondary text: `#A0A8B0`. Never warm hues (amber, orange) except error states.
3. **Typography:** `font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace` for all data readouts, metrics, and terminal text. UI labels: `IBM Plex Mono` or `Space Mono`. Proportional sans only for body prose. Never Helvetica or Inter.
4. **Borders:** `1px solid rgba(57,255,20,0.25)` (accent-translucent) on card edges. HUD brackets: CSS `::before`/`::after` corner marks, 8px long, 1px thick, accent color. No solid black borders.
5. **Glow:** Accent glow: `box-shadow: 0 0 8px rgba(57,255,20,0.4), 0 0 24px rgba(57,255,20,0.15)` on focused/active interactive elements. Never on static text or decorative elements.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use light mode or white background panels. Light themes are strictly forbidden in Cyberpunk.
- **NEVER** use rounded pill buttons or soft bubble curves (`rounded-full`, `rounded-xl`). Corners must be sharp (`0px`) or chamfered/angled (`clip-path`).
- **NEVER** use pastel, low-contrast, or friendly corporate colors (e.g. soft teal, lavender, baby blue).
- **NEVER** use standard serif fonts or decorative script typefaces.
- **NEVER** use warm organic paper textures, hand-drawn linework, or cozy drop shadows.
- **NEVER** use bouncy, cheerful spring animations. Motion must be instantaneous, mechanical, or digitized.
- **NEVER** leave large swathes of uncalibrated whitespace without structural telemetry framing or grid lines.
