# Reference Anti-Patterns: Corporate Memphis / Alegria

> **Status: NOT a selectable foundation style.** This file is a design-audit reference document.  
> It exists so the `design-audit` engine can detect and flag output that has drifted toward this pattern, and so the `design-director` can explicitly warn against it when recommending styles.

---

## What It Is

**Corporate Memphis** (also called **Alegria**, after the original Meta/Facebook illustration language) is a visual style characterized by:

- Flat, geometric human figures with exaggerated limb proportions (noodle arms, oversized heads, tiny feet)
- A predictable SaaS color palette: soft purple (`#6366F1` / `#8B5CF6`), pastel teal, coral, and warm yellow
- Rounded sans-serif typography — almost always Inter, Nunito, or DM Sans at medium weight
- `rounded-xl` to `rounded-3xl` border-radius on all cards, buttons, and containers
- `shadow-md` / `shadow-lg` ambient drop shadows on cards
- Gradient hero blobs or organic SVG shapes used decoratively, not functionally
- Generic "happy team collaboration" or "productivity" illustration scenes

It became the statistical default of AI-generated UI because these patterns appear at very high frequency in SaaS marketing sites in the training data. It is not a deliberate design choice — it is what happens when no design choice is made.

---

## Why It Is an Anti-Pattern Here

The Design Director taxonomy keeps **Visual Signature** (what it looks like) separate from **Ideal Domain** (where it fits). Corporate Memphis conflates both: it *looks* like "general SaaS" and is *used* for "general SaaS," which makes it self-reinforcing and indistinct. It communicates no specific brand personality, no craft, and no consideration of the actual product's users or context.

It is the typographic equivalent of stock photography: technically inoffensive, unmemorable by design.

---

## Audit Detection Rules

The `audit_code.py` engine flags Corporate Memphis drift when **two or more** of the following signals appear together in the same output:

| Signal | Pattern |
|---|---|
| Generic purple accent | `bg-purple-500`, `bg-indigo-500`, `text-purple-600`, `#6366F1`, `#8B5CF6` as primary/only accent |
| Bubbly containers | `rounded-2xl`, `rounded-3xl` on `card`, `panel`, `container`, `section` elements |
| Soft ambient shadows on everything | `shadow-md`, `shadow-lg` applied broadly (4+ occurrences in same file) |
| Illustration placeholder comment | `<!-- illustration -->`, `[illustration here]`, SVG with `fill="#6366F1"` and `viewBox` suggesting human figures |
| Generic font stack | `font-family: 'Inter'` or `font-family: 'DM Sans'` with no custom typographic rule, paired with `font-weight: 400` on headings |
| Gradient blob decoration | `radial-gradient` used decoratively without functional purpose, `blob`, `bg-blob`, `organic-shape` class names |

### Severity

- **2 signals co-present:** WARNING — "Possible Corporate Memphis drift detected."
- **3+ signals co-present:** CRITICAL — "Output matches Corporate Memphis / Alegria anti-pattern. This is the AI-generated SaaS default, not an intentional visual direction. Apply a foundation style contract."

---

## Remediation

When Corporate Memphis drift is detected:

1. **Run `@design-director`** — let the diagnostic interview assign an actual foundation style.
2. **Remove the generic purple accent.** Replace with a single intentional accent color from the chosen foundation's token spec.
3. **Reduce border-radius.** Most foundation styles cap at `8px`–`16px` on primary containers. Only Claymorphism intentionally uses `rounded-2xl`+.
4. **Replace ambient shadows.** Most foundations either use zero-blur hard offset shadows (Neo-Brutalism), hairline borders only (Swiss/Quiet Luxury), or contextual translucent panels (Glassmorphism). `shadow-md` on every card is not a design decision.
5. **Remove decorative illustration placeholders.** The imagery layer is specified in the foundation style's `DESIGN_CONTRACT.md`. Use that.

---

## Related Foundations That Are NOT Corporate Memphis

These styles can look superficially similar but have disciplined, specific rules that distinguish them:

| Foundation | Key Differentiator |
|---|---|
| `minimal-modern` | Zinc palette only, 6–8px radius max, no gradient blobs, no decorative illustrations |
| `space-age-optimism` | NASA orange accent (specific hex), molded pod radius (24–40px), warm optical white, moiré decorative system |
| `claymorphism` | Pastel fills are *functional* (element color) not decorative, heavy rounding is *specific* (20–32px per spec), layered inner shadow required |
| `organic-natural` | Earth pigment palette only, no pastels, no purple |

---

*This document is consumed by `audit_code.py` for drift detection and by `design-director/SKILL.md` for explicit anti-pattern warnings.*
