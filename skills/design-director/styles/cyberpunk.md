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

---

## Cyberpunk — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

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

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px',
        none: '0px',
        sm: '0px',
        md: '0px',
        lg: '0px',
        full: '0px',
      },
      colors: {
        cyber: {
          void: '#060709',
          bg: '#0B0D13',
          surface: '#12151E',
          border: '#1E2536',
          cyan: '#00F0FF',
          amber: '#FFB800',
          magenta: '#FF0055',
          green: '#00FF66',
          phosphor: '#E8F4F8',
          dim: '#62728C',
        }
      },
      boxShadow: {
        'neon-cyan': '0 0 10px rgba(0, 240, 255, 0.4)',
        'neon-amber': '0 0 10px rgba(255, 184, 0, 0.4)',
        'neon-magenta': '0 0 10px rgba(255, 0, 85, 0.4)',
      }
    }
  }
}
```

---

## Cyberpunk — Typography

## Type System Principles

Cyberpunk typography feels like flight telemetry, hacker terminals, or tactical weapons HUDs. It heavily leverages technical monospaces, sharp display sans, uppercase metadata markers, and bracketed telemetry tags.

## Recommended Font Stacks

### Monospace / Telemetry Core
- `JetBrains Mono`
- `Share Tech Mono`
- `Space Mono`
- `Fira Code`
- `VT323` (for retro-arcade digital readouts)

### Technical Display Headings
- `Rajdhani` (Condensed, angular geometric sans)
- `Michroma`
- `Orbitron`
- `Chakra Petch`

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 48px - 72px | 700 / 800 Bold | +0.05em | 1.05 | UPPERCASE |
| **H1** | 36px - 44px | 700 Bold | +0.04em | 1.15 | UPPERCASE |
| **H2** | 24px - 30px | 600 SemiBold | +0.03em | 1.25 | UPPERCASE |
| **H3 / Telemetry** | 18px - 20px | 600 SemiBold | +0.05em | 1.30 | UPPERCASE |
| **Body (Default)** | 14px - 15px | 400 / 500 | 0.00em | 1.50 | Sentence case |
| **Data / Ticker** | 12px - 13px | 500 Medium | +0.08em | 1.35 | Monospace UPPER |
| **Status Prefix** | 11px - 12px | 700 Bold | +0.10em | 1.20 | `[PREFIX: VALUE]` |

## Typographic Rules

1. **System Tag Annotations:** Frame key headings with bracketed coordinates or hexadecimal hashes (e.g. `// SEC_01 :: CORE_MATRIX`, `[STATUS: NOMINAL]`).
2. **Tabular Numerals Everywhere:** Always use monospaced figures for timestamps, coordinates, metrics, and price tickers.
3. **Phosphor Glow Highlights:** Vital alerts can use subtle neon text shadows (`text-shadow: 0 0 8px rgba(0, 240, 255, 0.6)`).

## Anti-Patterns (Fonts to Avoid)
- **Serifs** (`Garamond`, `Georgia`): Destroys the futuristic hacker atmosphere.
- **Friendly / Organic Sans** (`Nunito`, `Comic`, `Comfortaa`): Completely inappropriate.
- **Low-contrast gray text on dark gray**: Phosphor text must be readable and luminous.

---

## Cyberpunk — Layout & Spatial Composition

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

---

## Cyberpunk — Component Rules

Concrete specifications for core UI components.

## 1. Buttons

### Primary Neon Cyan Action
- **Border Radius:** `0px` or chamfered (`clip-path: polygon(...)`).
- **Background:** `#00F0FF` (Cyan) or `#0B0D13` with neon cyan outline.
- **Border:** `1px solid #00F0FF`.
- **Shadow:** `box-shadow: 0 0 12px rgba(0, 240, 255, 0.4), inset 0 0 6px rgba(0, 240, 255, 0.2)`.
- **Text:** `#060709` (if cyan bg) or `#00F0FF` (if dark bg), uppercase, tracking +0.08em, weight 700.
- **Padding:** 10px 22px.
- **Hover State:** Glow expands (`0 0 20px rgba(0, 240, 255, 0.7)`), text flickers or shifts to solid white.
- **Active State:** Instant down press, border flashes hazard yellow (`#FFB800`).

### Tactical Hazard Button
- **Border:** `1px solid #FFB800`.
- **Background:** `rgba(255, 184, 0, 0.1)`.
- **Text:** `#FFB800`.
- **Glow:** `0 0 10px rgba(255, 184, 0, 0.3)`.

## 2. Cards & Telemetry Panels

- **Border Radius:** `0px` (`rounded-none`).
- **Background:** Deep Carbon `#12151E`.
- **Border:** `1px solid #1E2536`.
- **Top Header Bar:** Solid `#1A1F2C` header strip with active neon indicator dot and title in `JetBrains Mono`.
- **Corner Brackets:** Corner accents in `#00F0FF` or `#3F4B5E`.
- **Padding:** 20px to 28px.

## 3. Inputs & Terminal Prompts

- **Border Radius:** `0px`.
- **Background:** `#08090C`.
- **Border:** `1px solid #1E2536`.
- **Text:** `#00F0FF` or `#E8F4F8`, monospaced.
- **Prefix:** `> ` or `USR@TERMINAL:~$ ` in `#FFB800`.
- **Focus State:** `border-color: #00F0FF; box-shadow: 0 0 10px rgba(0, 240, 255, 0.4); outline: none;`

## 4. Status Badges & HUD Markers

- **Shape:** Chamfered or sharp rectangle.
- **Border:** `1px solid #00F0FF` or `#00FF66`.
- **Background:** `rgba(0, 240, 255, 0.1)`.
- **Prefix Dot:** `6px x 6px` glowing square with `animation: pulse 1.5s infinite`.
- **Text:** 11px uppercase monospace, `[ONLINE]`, `[ARMED]`, `[DISCONNECTED]`.

---

## Cyberpunk — Motion & Transitions

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
