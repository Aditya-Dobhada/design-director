# Neo-Brutalism — Component Rules

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
