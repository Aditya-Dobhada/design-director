---
name: style-neo-brutalism
description: Implementation rules for Neo-Brutalism style. Thick solid black borders (2-4px), hard offset box shadows (4-6px with zero blur), bold high-saturation color blocks, tactile physical button presses, and punchy display grotesks.
---

# Style Pack: Neo-Brutalism

A bold, high-contrast, tactile aesthetic rooted in raw web design, physical paper zines, and poster art. Neo-Brutalism rejects the sterile, homogenized SaaS aesthetic in favor of tangible borders, hyper-pigmented accents, and physical tactile feedback.

## Mandatory Anti-Patterns

- **NEVER** use soft, blurry drop shadows (`box-shadow: 0 4px 6px rgba(0,0,0,0.1)` or `filter: drop-shadow(...)` with blur). Blur radius must ALWAYS be `0px`.
- **NEVER** use faint or subtle borders (`border: 1px solid #e2e8f0`). Borders must be at least `2px solid #000000` (typically `3px` or `4px`).
- **NEVER** use washed-out pastel grays as the primary surface identity. Use high-contrast white, cream, or bold saturated backgrounds.
- **NEVER** use glassmorphism, backdrop-blur, or translucent frosted surfaces.
- **NEVER** use floating smooth gradient backgrounds (e.g. purple-to-blue SaaS radial gradients).
- **NEVER** use subtle, sluggish 300ms ease transitions. Transitions must be snappy (80-120ms) and mechanical.
- **NEVER** use timid 12px light-gray secondary text. Text must be stark, legible `#000000` or `#1F2937`.

---

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

---

## Typography

### Recommended Font Stacks
- **Primary Display Grotesks:** `Space Grotesk`, `Syne`, `Archivo Black`, `Clash Display`, `Lexend Mega`, or `Plus Jakarta Sans` (weights 800-900)
- **Body & Data Type:** `Inter` (500/600 weight), `DM Sans`, `Space Mono`, or `JetBrains Mono`

### Scale & Metrics

| Level | Size | Weight | Tracking | Line Height | Case |
|---|---|---|---|---|---|
| **Display / Hero** | 56px - 80px | 800 / 900 Heavy | -0.03em | 1.05 | Title or UPPERCASE |
| **H1** | 40px - 52px | 800 Heavy | -0.025em | 1.15 | Title case |
| **H2** | 28px - 36px | 700 Bold | -0.02em | 1.20 | Title case |
| **H3** | 20px - 24px | 700 Bold | -0.01em | 1.30 | Title case |
| **Body (Default)** | 16px - 17px | 500 / Medium | 0.00em | 1.50 | Sentence case |
| **Badge / Label** | 12px - 14px | 700 Bold | +0.05em | 1.20 | UPPERCASE |
| **Code / Ticker** | 13px - 14px | 600 SemiBold | 0.00em | 1.35 | Monospace |

### Typographic Rules
1. **Weight Hierarchy:** Headings are thick and punchy (700-900). Body text is minimum 500 weight for crisp contrast against solid borders.
2. **Uppercase Badges:** Category tags and micro-labels are UPPERCASE with tracking +0.05em and a 2px-3px solid border.
3. **Black Text Dominance:** Text is almost always `#000000` or `#1F2937`. Never use soft washed-out gray text.
4. **Banned Fonts:** Delicate serifs (`Cormorant Garamond`, `Didot`), timid light sans (`Inter Light 300`), and script/calligraphy fonts.

---

## Layout & Spatial Composition

1. **Card Stacking & Physical Layers:**
   - Elements are framed as distinct physical cards on a cream (`#FFFDF5`) or saturated canvas.
   - Cards can feature subtle overlapping offsets or rotated sticker badges (`transform: rotate(-2deg)`).
2. **Clear Spatial Separation:**
   - Separate cards by explicit margins (20px to 32px), allowing their 4px solid black offset shadows to stand out without collision.
3. **Chunky Section Banners:**
   - Full-width ticker strips with 3px top and bottom black borders, filled with high-voltage yellow (`#FFE600`) or lime (`#00F0A8`).
4. **Layout Anti-Patterns:**
   - No borderless floating lists.
   - No glassmorphic floating bars or blurred headers.
   - No cramped micro-paddings; maintain bold, generous framing.

---

## Component Rules

### 1. Buttons
- **Primary Tactile Button:**
  - Border: `3px solid #000000` | Radius: `0px` or `4px` to `6px`
  - Background: Saturated Accent (Yellow `#FFE600`, Pink `#FF69B4`, Lime `#00F0A8`) | Text: `#000000`, 15-16px, weight 700/800
  - Shadow: `box-shadow: 4px 4px 0px #000000` | Padding: 12px 24px
  - Hover: `transform: translate(-1px, -1px); box-shadow: 5px 5px 0px #000000;`
  - Active / Press: `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000000;` (Simulates physical key switch depression).
- **Secondary Button:**
  - Border: `3px solid #000000` | Radius: `4px` to `6px` | Background: `#FFFFFF` | Text: `#000000`
  - Shadow: `box-shadow: 4px 4px 0px #000000`
  - Active: `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000000;`

### 2. Cards & Panels
- Border: `3px solid #000000` | Radius: `0px` or `6px` (never full pill)
- Background: `#FFFFFF` or pale pastel (`#FFFDF5`)
- Shadow: `box-shadow: 4px 4px 0px #000000` (or `6px 6px 0px #000000` for hero cards)
- Padding: 24px to 32px
- Header Badge: Top corner badge with `2px solid #000; background: #FFE600; padding: 4px 8px; font-weight: 700;`

### 3. Inputs & Forms
- Border: `3px solid #000000` | Radius: `4px` to `6px` | Background: `#FFFFFF`
- Shadow: `box-shadow: 3px 3px 0px #000000` | Padding: 12px 16px
- Focus: `outline: none; box-shadow: 5px 5px 0px #000000; border-color: #000000; background-color: #FFFFF8;`

### 4. Badges & Tags
- Border: `2px solid #000000` | Radius: `4px` | Shadow: `2px 2px 0px #000000`
- Background: High-voltage accent (`#FFE600`, `#00F0A8`, `#FF69B4`) | Padding: 3px 8px
- Typography: 11px - 12px, weight 800, uppercase, tracking +0.05em

### 5. Checkboxes & Toggles
- Checkbox: `20px x 20px`, `border: 3px solid #000000`, `border-radius: 4px`. Checked: fills `#FFE600` with heavy black checkmark `✓`.

---

## Motion & Transitions

```css
:root {
  --duration-neo-fast: 80ms;
  --duration-neo-snap: 120ms;
  --duration-neo-pop: 160ms;
  --ease-neo-snap: cubic-bezier(0, 0, 0.2, 1);
  --ease-neo-linear: linear;
}
```

- **Button Active Click:** Duration `80ms`, `linear`, `transform: translate(4px, 4px); box-shadow: 0px 0px 0px #000;`.
- **Hover Pop:** Duration `120ms`, `transform: translate(-1px, -1px); box-shadow: 5px 5px 0px #000;`.
- **Card Expansion:** Snappy step-down without rubber-band bounce.
- **Motion Anti-Patterns:** No soft feathered fades, no long 400ms+ easing curves. Elements snap and toggle.
