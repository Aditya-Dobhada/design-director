---
name: style-japanese-wabi-sabi
description: Implementation rules for Japanese Wabi-Sabi style. Mingei folk craft philosophy, asymmetric imperfection as beauty, hand-drawn ink brushstroke accents, clay/charcoal/matcha natural palette, extreme silence and breathing room, and contemplative unhurried motion.
---

# Style Pack: Japanese Wabi-Sabi

A design philosophy drawn from the Japanese aesthetics of wabi (understated simplicity) and sabi (the beauty of age and imperfection). Inspired by Mingei folk craft, Zen temple gardens, shodō ink calligraphy, and the work of pottery masters like Shoji Hamada and Lucie Rie's Japanese influences. Nothing is symmetrical, polished, or mass-produced.

## Core Principles

1. **Color:** Rice paper `#F7F3EE`, bamboo cream `#EDE8DF`, charcoal `#1E1E1A`, sumi ink `#2A2420`. Matcha accent `#5C7A4E` or iron gray `#4A4A46`. No bright pigments. No pure `#FFFFFF` white — always warm off-white.
2. **Typography:** `font-family: 'Shippori Mincho', 'Hiragino Mincho Pro', Georgia, serif` for display (weight 400). Body: `Zen Kaku Gothic New` or `Noto Sans JP` at weight 300–400. Generous `line-height: 1.9–2.1`. Letter-spacing `0.02em` on body. Never condensed or heavy weights.
3. **Spacing (Ma):** Whitespace IS the primary design element. Minimum section padding 120px vertical. Content width max 640px for reading columns. Single focused element per screen viewport. Never compete for attention — silence communicates.
4. **Geometry:** Asymmetric layouts — deliberately uncentered. `border-radius: 2px–4px` on cards (near-sharp, not rounded). Ink-wash horizontal rules: `border-bottom: 1px solid rgba(30,30,26,0.15)`. No hard black borders.
5. **Texture/Pattern:** Subtle paper texture via CSS `background-image: url('noise.png')` at 3–5% opacity. No photographic backgrounds. Ink-wash brush motifs as SVG overlays at low opacity. No geometric patterns.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use synthetic neon or electric colors. The palette is entirely natural earth, ink, and plant pigment.
- **NEVER** use drop shadows or blur. Elevation is expressed through layered ink washes or tonal background shifts alone.
- **NEVER** use symmetric card grids with equal spacing. Asymmetry is mandatory — no two elements may have identical spatial relationships.
- **NEVER** use bold, heavy-weight geometric grotesks for headings. Calligraphic brush accents and quiet humanist serifs only.
- **NEVER** use sharp machined 0px corners on all elements. Organic imperfection allows slight irregularity; cards may have subtle hand-cut edges via SVG clip-path.
- **NEVER** use bouncy, energetic, or fast animations. Motion must be slow, contemplative, breath-paced.
- **NEVER** use high-saturation warm-white backgrounds (`#FFFFFF`). Rice paper (`#FAF7F0`), bamboo cream (`#EDE8D0`), or warm linen only.

---

## Japanese Wabi-Sabi — Design Tokens

## Color Tokens

```css
:root {
  /* Natural Canvas */
  --color-rice-paper: #FAF7F0;     /* Primary background */
  --color-bamboo-cream: #EDE8D0;   /* Panel background */
  --color-aged-linen: #DDD5BC;     /* Subtle surface distinction */

  /* Ink & Earth */
  --color-ink-stone: #2A2622;      /* Primary text — deep ink, never #000 */
  --color-ink-faded: #4A4240;      /* Secondary text */
  --color-ink-muted: #7D7268;      /* Muted / meta text */
  --color-clay: #A07E6A;           /* Fired clay accent */
  --color-terracotta: #9C5B3E;     /* Warm terracotta emphasis */

  /* Plant Pigments */
  --color-matcha: #5C6E4C;         /* Matcha green accent */
  --color-indigo-wash: #3D4E6D;    /* Natural indigo dye */
  --color-persimmon: #C8613E;      /* Kaki persimmon warm red */
}
```

## Border & Divider Tokens

```css
:root {
  /* Ink brushstroke dividers — single pixel warm-tone */
  --border-ink-wash: 1px solid rgba(42, 38, 34, 0.15);
  --border-ink-visible: 1px solid rgba(42, 38, 34, 0.40);

  /* No sharp mechanical borders */
  --radius-organic: 2px;   /* Slight hand-cut irregularity on some elements */
  --radius-none: 0px;      /* Default for most surfaces */
}
```

## Shadow Tokens

```css
:root {
  --shadow-none: none; /* Drop shadows: FORBIDDEN */
  /* Tonal elevation via background color shift only */
}
```

## Spacing (Ma — Meaningful Empty Space)

```css
:root {
  --space-ma-sm: 32px;
  --space-ma-md: 64px;
  --space-ma-lg: 96px;
  --space-ma-xl: 128px;
  --space-ma-2xl: 160px;  /* Hero margins at desktop */
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        DEFAULT: '0px', none: '0px', sm: '2px', md: '2px', lg: '2px', full: '2px',
      },
      boxShadow: {
        DEFAULT: 'none', none: 'none',
      },
      colors: {
        wabi: {
          rice: '#FAF7F0', bamboo: '#EDE8D0', linen: '#DDD5BC',
          ink: '#2A2622', clay: '#A07E6A', matcha: '#5C6E4C',
          indigo: '#3D4E6D', persimmon: '#C8613E',
        }
      }
    }
  }
}
```

---

## Japanese Wabi-Sabi — Typography

## Recommended Font Stacks

### Brush / Calligraphic Display (Japanese spirit)
- `Noto Serif JP` (Light/Regular for body, ExtraBold for shodō-inspired accents)
- `Zen Old Mincho` (elegant classic Japanese proportions)
- `Shippori Mincho` (refined ink-press feel)
- `BIZ UDMincho` (high-legibility Japanese serif)

### Body & Functional Text (Quiet Humanist)
- `Source Serif 4` (300/400 — quiet, literary)
- `EB Garamond` (400 — understated historic)
- `Lora` (400 — warm, readable)
- `Tenor Sans` (functional quiet sans)

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Brushstroke** | 48px - 64px | 300 Light or Calligraphic | -0.01em | 1.20 | Sentence case (never UPPERCASE) |
| **H1** | 32px - 40px | 400 Regular | -0.01em | 1.30 | Sentence case |
| **H2** | 22px - 28px | 400 Regular | 0.00em | 1.40 | Sentence case |
| **H3** | 16px - 20px | 400 / 500 | +0.01em | 1.50 | Sentence case |
| **Body** | 15px - 16px | 400 Regular | +0.02em | 1.75 | Sentence case |
| **Meta / Caption** | 12px - 13px | 400 Light | +0.04em | 1.60 | Sentence case or kanji-style initials |

## Rules

1. **No All-Caps:** Uppercase signals aggression and modernity. Wabi-Sabi typography is always sentence case.
2. **Wide Prose Measure:** Body text sits at 60–70ch measure with generous 1.75 line-height for meditative reading pace.
3. **Ink-Stone Text Color:** Always `#2A2622` — never pure black.

## Anti-Patterns
- **Bold heavy grotesks** (`Inter Black`, `Space Grotesk 800`): Destroys quiet.
- **Neon or saturated text colors**: The ink palette is always earth and pigment.
- **Technical monospace**: Wrong cultural register.

---

## Japanese Wabi-Sabi — Layout

## Composition Principles

1. **Ma (間) — Structural Empty Space:** Minimum desktop section padding is 96px vertical. Do not crowd. Empty space is a structural element.
2. **Deliberate Asymmetry:** Avoid equal-column symmetric grids. Offset text blocks, let images float with irregular margins. Two elements may share a row but their sizes differ by at least 30%.
3. **Ink Brushstroke Dividers:** Section breaks are marked by a single 1px warm-toned hairline (`rgba(42, 38, 34, 0.20)`) spanning partial width (e.g. 40% of viewport), never full-bleed.
4. **Scroll as Unrolling Scroll:** Content reveals as if unrolling a Japanese hanging scroll (kakejiku): top-to-bottom, one thoughtful block at a time.

## Layout Anti-Patterns
- **Dense side-by-side card matrices**: Destroy silence.
- **Full-bleed high-saturation section banners**: Replace with tonal ink-wash color shifts.
- **Sticky floating chat or action widgets**: Incompatible with contemplative silence.

---

## Japanese Wabi-Sabi — Component Rules

## 1. Buttons

### Primary — Ink Brushstroke
- **Background:** Ink Stone `#2A2622`
- **Color:** Rice Paper `#FAF7F0`
- **Border:** none (the solid ink block is the border)
- **Border Radius:** `0px` or `2px`
- **Shadow:** none
- **Font:** 13px Humanist Serif or Quiet Sans, weight 400, tracking +0.06em, sentence case
- **Padding:** 12px 28px
- **Hover:** Background shifts to Clay `#A07E6A` — slow, 350ms ease-out
- **Active:** Opacity drops to 0.85

### Secondary — Ink Outline
- **Background:** Transparent
- **Border:** `1px solid rgba(42, 38, 34, 0.50)`
- **Color:** `#2A2622`
- **Border Radius:** `0px`
- **Hover:** Border darkens to full `#2A2622`, subtle rice paper tint fills background

## 2. Cards

- **Background:** Bamboo Cream `#EDE8D0` or Rice Paper `#FAF7F0`
- **Border:** `1px solid rgba(42, 38, 34, 0.12)`
- **Border Radius:** `0px` or `2px`
- **Shadow:** none
- **Padding:** 40px to 56px (generous, breathing)
- **Internal Divider:** Single hairline `border-t border-[rgba(42,38,34,0.12)]`

## 3. Inputs

- **Border:** Bottom border only: `border-b border-[rgba(42,38,34,0.30)]`
- **Background:** Transparent
- **Border Radius:** `0px`
- **Font:** 15px humanist serif, ink stone color
- **Focus:** Bottom border deepens to `#2A2622`, no glow rings
- **Placeholder:** Light clay tone `#A07E6A` italic

## 4. Labels & Meta Tags

- **Style:** Text-only, no background box. Small 12px Quiet Sans, ink muted `#7D7268`, tracking +0.06em.
- **Separator:** Thin dot `·` or en-dash `—` between metadata items.
- **NEVER use colored pill badges:** Alien to wabi-sabi vocabulary.

---

## Japanese Wabi-Sabi — Motion

## Philosophy

Motion is like the slow opening of a shoji screen, the settling of a tea bowl onto a wooden surface, or ink spreading through washi paper. It is breath-paced, inevitable, and never rushed or exuberant.

## Tokens

```css
:root {
  --duration-wabi-breath: 400ms;
  --duration-wabi-settle: 600ms;
  --duration-wabi-unfurl: 900ms;

  --ease-wabi: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-wabi-slow: cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Transitions

1. **Button hover:** 350ms ease-out, background color shifts — no translate or scale.
2. **Section entrance:** Opacity 0 → 1, translateY(16px → 0), 600ms. Stagger sibling elements by 120ms.
3. **Ink divider reveal:** SVG stroke-dasharray draw-in over 900ms on scroll entry.

## Anti-Patterns
- No sub-200ms transitions.
- No spring physics or bouncing.
- No scale pop on hover (elements do not grow on hover).
