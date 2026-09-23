---
name: style-neo-brutalism
description: Implementation rules for Neo-Brutalism style. Thick solid black borders (2-4px), hard offset box shadows (4-6px with zero blur), bold high-saturation color blocks, tactile physical button presses, and punchy display grotesks.
---

# Style Pack: Neo-Brutalism

A bold, high-contrast, tactile aesthetic rooted in raw web design, physical paper zines, and poster art. Neo-Brutalism rejects the sterile, homogenized SaaS aesthetic in favor of tangible borders, hyper-pigmented accents, and physical tactile feedback.

## Core Principles

1. **Borders:** `border: 3px solid #000000` on all interactive elements and cards. No `border-gray-*` or `border-opacity-*`. Buttons: `border: 3px solid #000000` always present — never borderless.
2. **Shadows:** `box-shadow: 4px 4px 0px #000000` on cards. `box-shadow: 6px 6px 0px #000000` on primary CTAs. Shadow offset must be solid black — zero blur radius. Active/pressed state: `box-shadow: 0px 0px 0px`, `transform: translate(4px, 4px)`.
3. **Color:** Maximum saturation background on the dominant element (e.g., `#FFDE03` yellow, `#FF3B30` red, `#00C853` green). Pure `#FFFFFF` or `#000000` secondary backgrounds. Single vibrant accent per composition, not multiple competing hues.
4. **Typography:** `font-family: 'Space Grotesk', 'Clash Display', system-ui` at weight 700–900 for headings. Body: `font-weight: 500` minimum. Uppercase `.tracking-wider` labels. No light or thin font weights.
5. **Geometry:** `border-radius: 0px` on cards and buttons. Inputs: `border-radius: 0px`, thick border. Pills only on tags (4px max). Never `rounded-full` on primary buttons.

## Mandatory Anti-Patterns (Explicit Negative Constraints)

- **NEVER** use soft, blurry drop shadows (`box-shadow: 0 4px 6px rgba(0,0,0,0.1)` or `filter: drop-shadow(...)` with blur). Blur radius must ALWAYS be `0px`.
- **NEVER** use faint or subtle borders (`border: 1px solid #e2e8f0`). Borders must be at least `2px solid #000000` (typically `3px` or `4px`).
- **NEVER** use washed-out pastel grays as the primary surface identity. Use high-contrast white, cream, or bold saturated backgrounds.
- **NEVER** use glassmorphism, backdrop-blur, or translucent frosted surfaces.
- **NEVER** use floating smooth gradient backgrounds (e.g. purple-to-blue SaaS radial gradients).
- **NEVER** use subtle, sluggish 300ms ease transitions. Transitions must be snappy (80-120ms) and mechanical.
- **NEVER** use timid 12px light-gray secondary text. Text must be stark, legible `#000000` or `#1F2937`.

---

## Neo-Brutalism — Design Tokens

Exact tokens for CSS variables and Tailwind configuration.

## Color Tokens

```css
:root {
  /* Outlines & Contrast Base */
  --color-border-main: #000000;
  --color-text-main: #000000;
  --color-text-sub: #1F2937;
  --color-surface-white: #FFFFFF;

  /* Saturated High-Energy Accents */
  --color-neo-yellow: #FFE600;
  --color-neo-pink: #FF69B4;
  --color-neo-green: #00F0A8;
  --color-neo-cyan: #00C4FF;
  --color-neo-orange: #FF5C00;
  --color-neo-purple: #A358DF;

  /* Canvas / Background Options */
  --color-bg-base: #FFFDF5; /* Warm off-white poster canvas */
  --color-bg-alt: #FFE600;  /* High-impact section canvas */
}
```

## Border Width & Radius Tokens

```css
:root {
  /* Border Widths: Heavy, structural, unapologetic */
  --border-width-default: 3px;
  --border-width-thick: 4px;
  --border-width-heavy: 5px;

  /* Radius: Sharp boxy OR playful chunky (never full pill) */
  --radius-sharp: 0px;       /* Classic brutalist */
  --radius-chunky: 6px;      /* Contemporary neo-brutalist standard */
  --radius-max: 8px;         /* Absolute maximum. rounded-full is FORBIDDEN on cards/containers */
}
```

## Shadow & Depth Tokens

```css
:root {
  /* Hard Offset Shadows - BLUR IS STRICTLY ZERO */
  --shadow-neo-sm: 2px 2px 0px #000000;
  --shadow-neo-md: 4px 4px 0px #000000;
  --shadow-neo-lg: 6px 6px 0px #000000;
  --shadow-neo-xl: 8px 8px 0px #000000;
  --shadow-neo-active: 0px 0px 0px #000000; /* When button is pressed */
}
```

## Spacing & Metrics

```css
:root {
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
}
```

## Tailwind Config Mapping

```js
module.exports = {
  theme: {
    extend: {
      borderWidth: {
        DEFAULT: '3px',
        2: '2px',
        3: '3px',
        4: '4px',
        5: '5px',
      },
      borderRadius: {
        DEFAULT: '0px',
        none: '0px',
        sm: '4px',
        md: '6px',
        lg: '8px',
        full: '8px', // Prevent rounded-full from creating circles/pills on cards
      },
      boxShadow: {
        DEFAULT: '4px 4px 0px #000000',
        sm: '2px 2px 0px #000000',
        md: '4px 4px 0px #000000',
        lg: '6px 6px 0px #000000',
        xl: '8px 8px 0px #000000',
        none: '0 0 #0000',
      },
      colors: {
        neo: {
          border: '#000000',
          yellow: '#FFE600',
          pink: '#FF69B4',
          green: '#00F0A8',
          cyan: '#00C4FF',
          orange: '#FF5C00',
          purple: '#A358DF',
          cream: '#FFFDF5',
        }
      }
    }
  }
}
```

---

## Neo-Brutalism — Typography

## Type System Principles

Neo-Brutalism relies on bold, expressive, character-heavy typography that doesn't apologize for taking up space. It uses heavy display weights, monospace contrast, and deliberate uppercase statements.

## Recommended Font Stacks

### Primary Display Grotesks
- `Space Grotesk`
- `Syne`
- `Archivo Black` / `Archivo`
- `Lexend Mega`
- `Clash Display`
- `Plus Jakarta Sans` (Heavy weights: 800-900)

### Body & Data Type
- `Inter` (500/600 weight)
- `Space Mono` / `JetBrains Mono`
- `DM Sans`

## Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 56px - 80px | 800 / 900 Heavy | -0.03em | 1.05 | Title or UPPERCASE |
| **H1** | 40px - 52px | 800 Heavy | -0.025em | 1.15 | Title case |
| **H2** | 28px - 36px | 700 Bold | -0.02em | 1.20 | Title case |
| **H3** | 20px - 24px | 700 Bold | -0.01em | 1.30 | Title case |
| **Body (Default)** | 16px - 17px | 500 / Medium | 0.00em | 1.50 | Sentence case |
| **Badge / Label** | 12px - 14px | 700 Bold | +0.05em | 1.20 | UPPERCASE |
| **Code / Ticker** | 13px - 14px | 600 SemiBold | 0.00em | 1.35 | Monospace |

## Typographic Rules

1. **High Contrast Weight Hierarchy:** Headings are thick and punchy (700-900 weight). Body text is minimum 500 weight for crisp contrast against solid borders.
2. **Uppercase Badges:** Category pills, status indicators, and micro-tags are UPPERCASE with letter-spacing +0.05em and a 2px-3px solid border.
3. **Black Text Dominance:** Text is almost always `#000000`. Do not use soft gray text for readability-critical information.

## Anti-Patterns (Fonts to Avoid)
- **Delicate Editorial Serifs** (`Cormorant Garamond`, `Didot`): Too fragile for heavy black ink.
- **Timid, Light Sans** (`Inter Light 300`, `Helvetica Light 200`): Disappears against 3px black borders.
- **Script / Calligraphy fonts**: Clashes completely with the raw graphic poster ethos.

---

## Neo-Brutalism — Layout & Spatial Composition

## Grid & Composition Rules

1. **Card Stacking & Physical Layers:**
   - Elements are framed as distinct physical cards on a cream or saturated canvas.
   - Cards can have subtle overlapping offsets or rotated sticker badges (`transform: rotate(-2deg)` or `rotate(3deg)`).
2. **Clear Spatial Separation:**
   - Cards are separated by explicit margins (20px to 32px), allowing their 4px solid black offset shadows to stand out against the background without colliding into each other.
3. **Chunky Section Banners:**
   - Full-width ticker banners or scrolling marquee strips with 3px top and bottom black borders, filled with high-voltage yellow (`#FFE600`) or lime (`#00F0A8`).
4. **Header Navigation:**
   - Framed within a distinct border container: `border: 3px solid #000; box-shadow: 4px 4px 0px #000; border-radius: 6px;` or spanning full width with a crisp 3px bottom rule.

## Layout Anti-Patterns
- **Borderless Floating Lists:** Floating content without borders looks unfinished in Neo-Brutalism.
- **Glassmorphic Floating Bars:** Blurred backdrop headers are strictly forbidden.
- **Micro-Padded Forms:** Forms with crammed 4px paddings destroy the chunky poster aesthetic.

---

## Neo-Brutalism — Component Rules

Concrete specifications for core UI components.

## 1. Buttons

### Primary Tactile Button
- **Border:** `3px solid #000000`
- **Border Radius:** `0px` or `4px` to `6px`
- **Background:** Saturated Accent (e.g. Yellow `#FFE600`, Pink `#FF69B4`, or Lime `#00F0A8`)
- **Color:** `#000000`
- **Font:** 15px - 16px, weight 700 / 800, uppercase or title case
- **Shadow:** `box-shadow: 4px 4px 0px #000000`
- **Padding:** 12px 24px
- **Hover State:** Translate up/left: `transform: translate(-1px, -1px); box-shadow: 5px 5px 0px #000000;`
- **Active / Press State:** Translate down/right: `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000000;` (Simulates physical key switch depression).

### Secondary Button
- **Border:** `3px solid #000000`
- **Border Radius:** `4px` to `6px`
- **Background:** `#FFFFFF`
- **Color:** `#000000`
- **Shadow:** `box-shadow: 4px 4px 0px #000000`
- **Hover State:** Background flips to soft yellow or cyan; shadow increases to 5px.
- **Active State:** `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000000;`

## 2. Cards & Panels

- **Border:** `3px solid #000000`
- **Border Radius:** `0px` or `6px` (never full pill)
- **Background:** `#FFFFFF` or pale pastel (`#FFFDF5`)
- **Shadow:** `box-shadow: 4px 4px 0px #000000` (or `6px 6px 0px #000000` for hero cards)
- **Padding:** 24px to 32px
- **Header Badge:** Top corner badge with `2px solid #000; background: #FFE600; padding: 4px 8px; font-weight: 700;`

## 3. Inputs & Form Fields

- **Border:** `3px solid #000000`
- **Border Radius:** `4px` to `6px`
- **Background:** `#FFFFFF`
- **Shadow:** `box-shadow: 3px 3px 0px #000000`
- **Color:** `#000000`
- **Padding:** 12px 16px
- **Focus State:** `outline: none; box-shadow: 5px 5px 0px #000000; border-color: #000000; background-color: #FFFFF8;`

## 4. Badges & Tags

- **Border:** `2px solid #000000`
- **Border Radius:** `4px`
- **Shadow:** `2px 2px 0px #000000`
- **Background:** High-voltage accent (`#FFE600`, `#00F0A8`, `#FF69B4`)
- **Typography:** 11px - 12px, weight 800, uppercase, tracking +0.05em
- **Padding:** 3px 8px

## 5. Checkboxes & Toggles

- **Checkbox:** `20px x 20px`, `border: 3px solid #000000`, `border-radius: 4px`, checked state fills with `#FFE600` and displays heavy black checkmark `✓`.

---

## Neo-Brutalism — Motion & Transitions

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
