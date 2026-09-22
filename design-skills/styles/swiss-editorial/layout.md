# Swiss / Editorial — Layout & Spatial Composition

## Grid & Structural Foundation

1. **Modular 12-Column Asymmetric Grid:**
   - Instead of symmetrical 3-column or 4-column card matrices, divide layouts asymmetrically:
     - 4 cols (Sidebar / Overview / Index) + 8 cols (Primary Content / Editorial Stream)
     - 5 cols (Hero Statement / Thesis) + 7 cols (Supporting Evidence / Metric Matrix)
2. **Explicit Structural Lines:**
   - Section breaks are marked by crisp 1px horizontal hairlines spanning full viewport width or grid bounds (`border-t border-black` or `border-neutral-200`).
   - Vertical column boundaries can have visible 1px hairline dividers between content blocks.
3. **Generous White & Paper Space:**
   - Margins: 32px (mobile), 64px to 96px (desktop).
   - Generous breathing space between major editorial blocks (64px to 120px) creates gravitas and focus.
4. **Number-Indexed Sections:**
   - Prefix major sections or lists with tabular numeral indices (`01 /`, `02 /`, `[03]`) in small monospace or small-caps.

## Anti-Pattern Layouts
- **Centered SaaS Feature Cards:** The classic "3 identical rounded cards in a row with purple icons in soft circles" is strictly prohibited.
- **Card-Soup UI:** Do not wrap every piece of content in its own bordered, elevated box. Let typography and rule-lines structure the content.
- **Floating Pill Navbars:** Floating detached navigation pills with blurred backdrops are prohibited. Navigation must be a top-pinned, sharp-edged bar or minimalist architectural header line.
