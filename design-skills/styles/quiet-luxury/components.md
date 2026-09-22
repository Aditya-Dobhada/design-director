# Quiet Luxury — Component Rules

Concrete specifications for core UI components.

## 1. Buttons & Interactive Links

### Primary Action
- **Border Radius:** `0px` (`rounded-none`).
- **Background:** Deep Espresso (`#1C1A17`) or Warm Charcoal (`#2C2926`).
- **Color:** Warm Alabaster (`#FBFBF9`).
- **Font:** 13px - 14px, weight 500, letter-spacing +0.06em, uppercase or sentence case.
- **Padding:** 14px 28px.
- **Border:** 1px solid `#1C1A17`.
- **Hover State:** Background shifts gently to `#383430` over 350ms. No scale, no shadow expansion.

### Underline Editorial Link
- **Shape:** Text element with an offset bottom hairline border (`border-b border-[#1C1A17] pb-1`).
- **Hover State:** Underline expands or deepens in tone; subtle rightward arrow translation (2px).

## 2. Cards & Panels

- **Border Radius:** `0px` (`rounded-none`).
- **Border:** 1px solid `#E4E0D6` or none (demarcated solely by subtle tonal shift from `#FBFBF9` to `#F5F2EB`).
- **Shadow:** None (`box-shadow: none`).
- **Padding:** 36px to 48px.
- **Typography Inside Card:** Editorial serif card title, followed by generous leading body text.

## 3. Inputs & Forms

- **Border Radius:** `0px` (`rounded-none`).
- **Border:** Bottom-border only (`border-b 1px solid #C8B89C` or `#D6D2C8`), background transparent.
- **Background:** Transparent.
- **Padding:** 12px 0px.
- **Focus State:** Bottom border deepens to `#1C1A17` over 300ms. No glowing rings.
- **Placeholder:** 14px, warm stone `#8C867A`, italicized serif or quiet sans.

## 4. Status Indicators & Metadata

- **Shape:** Text-only metadata with letter-spacing +0.12em.
- **Prefix:** Delicate typographic bullet (`•`) or small Roman numeral (`I.`, `II.`).
- **Anti-Pattern:** Never use colored pill badges with rounded borders.
