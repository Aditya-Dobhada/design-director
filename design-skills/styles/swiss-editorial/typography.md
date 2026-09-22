# Swiss / Editorial — Typography

## Type System Principles

The typography system relies on stark contrasts in size, weight, and classification. It pairs an authoritative editorial serif or stark grotesque display with an objective, highly legible body neo-grotesk.

## Recommended Font Stacks

### Option A: Editorial Broadside (Serif Headings + Neo-Grotesk Body)
- **Headings (Display / H1 / H2):** `Playfair Display`, `Newsreader`, `Instrument Serif`, `Cormorant Garamond`, or `Bodoni MT`, serif
- **Body & Functional (H3 / Body / Code / Badges):** `Inter`, `Neue Haas Grotesk`, `Helvetica Neue`, `Arial`, sans-serif
- **Metadata / Accents:** `JetBrains Mono`, `Space Mono`, monospace

### Option B: Pure Neo-Grotesk (Purist International Style)
- **Headings & Body:** `Inter`, `Helvetica Neue`, `Neue Haas Grotesk`, `Geist Sans`, sans-serif
- **Execution:** Extreme scale ratios (Display: 56px Bold / Body: 14px Regular), tight negative tracking on display titles, generous line-height on text.

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 56px - 72px | 700 / Bold or 400 Italic Serif | -0.03em | 1.05 | Sentence case |
| **H1** | 40px - 48px | 600 / SemiBold | -0.025em | 1.15 | Sentence case |
| **H2** | 28px - 32px | 600 / SemiBold | -0.02em | 1.25 | Sentence case |
| **H3 / Section** | 20px - 22px | 500 / Medium | -0.01em | 1.35 | Sentence case |
| **Body (Default)** | 15px - 16px | 400 / Regular | 0.00em | 1.55 | Sentence case |
| **Small / Meta** | 12px - 13px | 500 / Medium | +0.04em | 1.40 | Uppercase or Sentence |
| **Eyebrow / Overline**| 11px - 12px | 600 / SemiBold | +0.10em | 1.20 | UPPERCASE |

## Typographic Rules

1. **Left Alignment Only:** Center-aligned body text and multi-line headings are forbidden. Left-align copy with intentional, clean ragging.
2. **Tabular Numerals:** Use `font-variant-numeric: tabular-nums` for all pricing, statistics, data tables, and metrics.
3. **Subtle Metadata Footers:** Mark metadata, timestamps, and categories with uppercase small type and generous letter-spacing.
4. **No Artificial Bolding:** Do not use bold weight (700) on long paragraphs. Use weight shifts strictly for semantic anchors.

## Anti-Patterns (Fonts to Avoid)
- **Comic Sans, Papyrus, Pacifico** (obviously)
- **Rounded Sans** (`Quicksand`, `Comfortaa`, `Nunito`): Destroys the disciplined architectural feel.
- **Overly generic geometric sans** (`Poppins`, `Montserrat`): Read as generic template landing pages.
