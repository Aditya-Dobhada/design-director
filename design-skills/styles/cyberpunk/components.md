# Cyberpunk — Component Rules

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
