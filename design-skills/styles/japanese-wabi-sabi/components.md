# Japanese Wabi-Sabi — Component Rules

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
