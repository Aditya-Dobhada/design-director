# Y2K / Frutiger Aero — Component Rules

Concrete specifications for core UI components.

## 1. Buttons

### Glossy Aqua Pill Button
- **Border Radius:** `9999px` (`rounded-full`).
- **Background:** Dual-tone vertical gloss gradient:
  ```css
  background: linear-gradient(180deg, #38D9FF 0%, #009FE3 50%, #0077C8 100%);
  ```
- **Top Specular Reflection:**
  ```css
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8), inset 0 -2px 0 rgba(0, 0, 0, 0.2), 0 4px 12px rgba(0, 159, 227, 0.4);
  ```
- **Text:** `#FFFFFF`, weight 700, with subtle text-shadow `0 1px 2px rgba(0, 50, 100, 0.5)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.6)`.
- **Padding:** 12px 28px.
- **Hover State:** Glow increases (`0 6px 20px rgba(0, 196, 255, 0.6)`), slight lift (`transform: translateY(-2px)`).
- **Active State:** Button depresses (`transform: translateY(1px)`), inner shadow deepens.

### Secondary Translucent Glass Button
- **Border Radius:** `9999px`.
- **Background:** `rgba(255, 255, 255, 0.6)`.
- **Backdrop Filter:** `blur(8px)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.9)`.
- **Color:** `#0078D7`.

## 2. Cards & Panels

- **Border Radius:** `16px` to `20px`.
- **Background:** `rgba(255, 255, 255, 0.75)`.
- **Backdrop Filter:** `blur(16px)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.85)`.
- **Shadow:**
  ```css
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 8px 32px rgba(0, 120, 215, 0.1);
  ```
- **Padding:** 28px to 36px.

## 3. Inputs & Forms

- **Border Radius:** `9999px` or `12px`.
- **Background:** `rgba(255, 255, 255, 0.9)`.
- **Border:** `1px solid rgba(0, 120, 215, 0.3)`.
- **Shadow:** `inset 0 2px 4px rgba(0, 0, 0, 0.06)`.
- **Focus State:** `outline: none; border-color: #00C4FF; box-shadow: 0 0 12px rgba(0, 196, 255, 0.5), inset 0 1px 2px rgba(0,0,0,0.05);`

## 4. Badges & Pills

- **Shape:** Rounded pill (`rounded-full`).
- **Background:** Gradient aqua/lime: `linear-gradient(180deg, #A8F000 0%, #76B900 100%)`.
- **Border:** `1px solid rgba(255, 255, 255, 0.7)`.
- **Text:** `#FFFFFF`, weight 700, 11px.
- **Shadow:** `0 2px 6px rgba(118, 185, 0, 0.3)`.
