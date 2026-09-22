# Swiss / Editorial — Component Rules

Concrete specifications for core UI components. All values are strict and testable.

## 1. Buttons

### Primary Button
- **Shape:** Sharp rectangle (`border-radius: 0px` or `2px`). No pills.
- **Background:** Solid Black (`#111111`) or Accent (`#E30613`).
- **Text:** White (`#FFFFFF`), 14px, weight 500, letter-spacing +0.02em.
- **Padding:** 10px 20px (Desktop), 8px 16px (Compact).
- **Border:** 1px solid `#111111` or `#E30613`.
- **Hover State:** Background shifts to `#2A2A2A` or accent hover (`#BF0410`). No bounce, no scale pop.
- **Active State:** Instant 1px press down or inverse color flip.

### Secondary / Outline Button
- **Shape:** Sharp rectangle (`border-radius: 0px` or `2px`).
- **Background:** Transparent or Pure White (`#FFFFFF`).
- **Text:** Solid Black (`#111111`), 14px, weight 500.
- **Border:** 1px solid `#111111`.
- **Hover State:** Background inverts to `#111111`, text becomes `#FFFFFF`.

### Text / Underline Action
- **Shape:** Inline text with 1px solid underline.
- **Hover State:** Underline thickens to 2px or transitions color to accent.

## 2. Cards & Containers

- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#E5E5E5` or `#111111`. Never 2px soft pastel.
- **Shadow:** None (`box-shadow: none`). Alternatively, hard 2px solid black shadow (`box-shadow: 2px 2px 0px #111111`) if high contrast is needed.
- **Padding:** 24px to 32px.
- **Internal Dividers:** 1px hairline horizontal divider between card header and body.

## 3. Inputs & Forms

- **Border Radius:** 0px (`rounded-none`).
- **Border:** 1px solid `#CCCCCC` or bottom-border only (`border-b border-black`).
- **Background:** `#FFFFFF` or `#F8F8F6`.
- **Focus State:** 1px solid `#111111` outline, or bottom-border becomes 2px solid `#111111`. No diffuse blue/purple focus ring glow.
- **Placeholder:** Text muted `#737373`, italicized serif or neutral sans.

## 4. Badges & Status Chips

- **Shape:** Sharp rectangular tags (`border-radius: 0px`).
- **Border:** 1px solid `#111111` or `#E5E5E5`.
- **Background:** `#F2F2F0` or `#FFFFFF`.
- **Typography:** 11px uppercase, medium weight, letter-spacing +0.06em.
- **Anti-Pattern:** Never use rounded pill badges with soft colored backgrounds (`bg-blue-100 text-blue-700 rounded-full`).

## 5. Tables & Data Display

- **Borders:** Crisp horizontal 1px lines (`#E5E5E5`). No vertical column borders.
- **Headers:** 12px uppercase, tracking +0.05em, text muted `#4A4A4A`.
- **Numbers:** Tabular figures, right-aligned.
