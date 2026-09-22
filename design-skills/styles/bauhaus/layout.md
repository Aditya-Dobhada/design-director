# Bauhaus — Layout

## Composition Rules

1. **Strict Modular Grid:** All layout derives from an 8px baseline grid. Column and row gutters are multiples of 8. No free-floating arbitrary values.
2. **Solid Color Plane Sections:** Sections are delineated by solid color plane changes — white → black, white → red, black → yellow — not by hairlines or whitespace alone.
3. **Geometric Accent Integration:** Bauhaus circles (50% border-radius, solid primary color) are deployed as section markers, numbered list bullets, and accent spots. They do not exceed the established size scale.
4. **Sidebar + Main Column Structure:** A structural left sidebar (black or primary color block) anchors the primary navigation; a white main column holds content.

## Layout Anti-Patterns
- **Free-floating asymmetric layouts without mathematical basis**: Every element must sit on the grid.
- **Decorative whitespace without structural purpose**: Space is used deliberately, not as aesthetics.
- **Soft corner rounding on any rectangular container**: 0px only.
