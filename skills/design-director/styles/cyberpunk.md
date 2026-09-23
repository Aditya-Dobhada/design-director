---
name: style-cyberpunk
description: Implementation rules for Cyberpunk style. Obsidian black canvases, electric neon cyan/amber/magenta accents, monospace data telemetry, chamfered cut corners, HUD crosshairs, and scanline/glitch precision.
---

# Style Pack: Cyberpunk

A tactical, high-voltage visual system derived from military telemetry, hacker consoles, dystopian HUDs, and neon-lit megacities. Built for dense data displays, power users, and immersive technical workflows.

## Mandatory Anti-Patterns

- **NEVER** use light mode or white background panels. Light themes are strictly forbidden in Cyberpunk.
- **NEVER** use rounded pill buttons or soft bubble curves (`rounded-full`, `rounded-xl`). Corners must be sharp (`0px`) or chamfered/angled (`clip-path`).
- **NEVER** use pastel, low-contrast, or friendly corporate colors (e.g. soft teal, lavender, baby blue).
- **NEVER** use standard serif fonts or decorative script typefaces.
- **NEVER** use warm organic paper textures, hand-drawn linework, or cozy drop shadows.
- **NEVER** use bouncy, cheerful spring animations. Motion must be instantaneous, mechanical, or digitized.
- **NEVER** leave large swathes of uncalibrated whitespace without structural telemetry framing or grid lines.

---

## Color Tokens

```css
:root {
  /* Obsidian Base Canvas */
  --color-cyber-void: #060709;
  --color-cyber-bg: #0B0D13;
  --color-cyber-surface: #12151E;
  --color-cyber-surface-elevated: #1A1F2C;

  /* Neon High-Voltage Accents */
  --color-neon-cyan: #00F0FF;
  --color-neon-amber: #FFB800;
  --color-neon-magenta: #FF0055;
  --color-neon-green: #00FF66;

  /* HUD Lines & Dividers */
  --color-cyber-border: #1E2536;
  --color-cyber-border-active: #00F0FF;
  --color-cyber-grid: rgba(0, 240, 255, 0.06);

  /* Typography / Phosphor */
  --color-text-phosphor: #E8F4F8;
  --color-text-cyan: #00F0FF;
  --color-text-dim: #62728C;
  --color-text-muted: #3F4B5E;
}
```

## Border Radius & Chamfer Tokens

```css
:root {
  --radius-none: 0px; /* Sharp corners */
  /* Chamfer cut clip paths */
  --clip-chamfer-sm: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 8px 100%, 0 calc(100% - 8px));
  --clip-chamfer-btn: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 10px 100%, 0 calc(100% - 10px));
  --clip-notch-top: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%);
}
```

## Glow & Shadow Tokens

```css
:root {
  --glow-cyan-sm: 0 0 8px rgba(0, 240, 255, 0.4);
  --glow-cyan-lg: 0 0 20px rgba(0, 240, 255, 0.6), inset 0 0 10px rgba(0, 240, 255, 0.2);
  --glow-amber-sm: 0 0 8px rgba(255, 184, 0, 0.4);
  --glow-magenta-sm: 0 0 8px rgba(255, 0, 85, 0.4);
}
```

---

## Typography

### Recommended Font Stacks
- **Monospace / Telemetry Core:** `JetBrains Mono`, `Share Tech Mono`, `Space Mono`, or `Fira Code`
- **Technical Display Headings:** `Rajdhani`, `Michroma`, `Orbitron`, or `Chakra Petch`

### Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 48px - 72px | 700 / 800 Bold | +0.05em | 1.05 | UPPERCASE |
| **H1** | 36px - 44px | 700 Bold | +0.04em | 1.15 | UPPERCASE |
| **H2** | 24px - 30px | 600 SemiBold | +0.03em | 1.25 | UPPERCASE |
| **H3 / Telemetry** | 18px - 20px | 600 SemiBold | +0.05em | 1.30 | UPPERCASE |
| **Body (Default)** | 14px - 15px | 400 / 500 | 0.00em | 1.50 | Sentence case |
| **Data / Ticker** | 12px - 13px | 500 Medium | +0.08em | 1.35 | Monospace UPPER |
| **Status Prefix** | 11px - 12px | 700 Bold | +0.10em | 1.20 | `[PREFIX: VALUE]` |

### Typographic Rules
1. **System Tag Annotations:** Frame key headings with bracketed coordinates or hexadecimal hashes (`// SEC_01 :: CORE_MATRIX`, `[STATUS: NOMINAL]`).
2. **Tabular Numerals Everywhere:** Always use monospaced figures for timestamps, coordinates, metrics, and price tickers.
3. **Phosphor Glow Highlights:** Critical alerts can use subtle neon text shadows (`text-shadow: 0 0 8px rgba(0, 240, 255, 0.6)`).
4. **Banned Fonts:** Serifs (`Garamond`, `Georgia`), friendly rounded sans (`Nunito`, `Comfortaa`), and low-contrast dim text on dark backgrounds.

---

## Layout & Spatial Composition

1. **Tactical Modular Grid:**
   - Multi-panel interface with visible division lines and technical framing.
   - High information density: dashboards, telemetry strips, and terminal outputs.
2. **HUD Registration Framing:**
   - Cards and screen corners feature registration brackets using CSS `::before` / `::after` with 2px borders on corners.
3. **Corner Chamfers & Diagonal Cuts:**
   - Panels and cards cut at 45-degree angles on corners using CSS polygon clip-paths.
4. **Scanlines & Grid Overlay:**
   ```css
   background-image: linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
                     linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
   background-size: 24px 24px;
   ```
5. **Layout Anti-Patterns:**
   - No light theme interfaces. No centered SaaS hero layouts with soft pill buttons. No uncalibrated empty whitespace lacking structural framing.

---

## Component Rules

### 1. Buttons
- **Primary Neon Cyan Action:**
  - Border Radius: `0px` or chamfered (`clip-path: polygon(...)`)
  - Background: `#00F0FF` (Cyan) or `#0B0D13` with neon cyan outline | Border: `1px solid #00F0FF`
  - Shadow: `box-shadow: 0 0 12px rgba(0, 240, 255, 0.4), inset 0 0 6px rgba(0, 240, 255, 0.2)`
  - Text: `#060709` (if cyan bg) or `#00F0FF` (if dark bg), uppercase, tracking +0.08em, weight 700 | Padding: 10px 22px
  - Hover: Glow expands (`0 0 20px rgba(0, 240, 255, 0.7)`), text flickers or shifts to solid white
  - Active: Instant down press, border flashes hazard yellow (`#FFB800`)
- **Tactical Hazard Button:**
  - Border: `1px solid #FFB800` | Background: `rgba(255, 184, 0, 0.1)` | Text: `#FFB800` | Glow: `0 0 10px rgba(255, 184, 0, 0.3)`

### 2. Cards & Telemetry Panels
- Border Radius: `0px` (`rounded-none`) | Background: Deep Carbon `#12151E` | Border: `1px solid #1E2536`
- Top Header Bar: Solid `#1A1F2C` header strip with active neon indicator dot and title in `JetBrains Mono`
- Corner Brackets: Corner accents in `#00F0FF` or `#3F4B5E` | Padding: 20px to 28px

### 3. Inputs & Terminal Prompts
- Border Radius: `0px` | Background: `#08090C` | Border: `1px solid #1E2536` | Text: `#00F0FF` or `#E8F4F8`, monospaced
- Prefix: `> ` or `USR@TERMINAL:~$ ` in `#FFB800`
- Focus: `border-color: #00F0FF; box-shadow: 0 0 10px rgba(0, 240, 255, 0.4); outline: none;`

### 4. Status Badges & HUD Markers
- Shape: Chamfered or sharp rectangle | Border: `1px solid #00F0FF` or `#00FF66` | Background: `rgba(0, 240, 255, 0.1)`
- Prefix Dot: `6px x 6px` glowing square with pulse animation | Text: 11px uppercase monospace (`[ONLINE]`, `[ARMED]`)

---

## Motion & Transitions

```css
:root {
  --duration-cyber-glitch: 60ms;
  --duration-cyber-snap: 100ms;
  --duration-cyber-telemetry: 180ms;
  --ease-cyber-instant: steps(3, end);
  --ease-cyber-snap: cubic-bezier(0, 0, 0.2, 1);
}
```

- **Button Activation:** 80ms, linear, `box-shadow, border-color, background-color`.
- **Pulse Loop:** Neon breathing glow: 2000ms infinite ease-in-out.
- **Glitch / CRT Boot:** Rapid 60ms opacity/transform jitter simulating signal noise on page mount.
- **Motion Anti-Patterns:** No playful bouncing springs, no slow 500ms sluggish dissolves.
