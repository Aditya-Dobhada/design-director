# Cyberpunk — Typography

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
