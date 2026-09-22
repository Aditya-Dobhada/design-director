---
name: design-audit
description: Post-implementation verification skill that audits generated frontend code (HTML, JSX, TSX, Vue, Svelte, CSS) against a chosen Design Spec. Scans for border-radius violations, blurry drop shadows, font substitutions, border-width mismatches, and color palette leaks, reporting structured layer-by-layer deviations.
---

# Design Audit

A verification engine that inspects generated frontend code against the chosen Design Spec and reports adherence or deviation per layer. It guarantees that the contract agreed upon during `/design choose` was actually respected by the coding agent.

## Invocations

```bash
/design audit
# or via CLI:
python design-skills/audit/scripts/audit_code.py <style_id> <path_to_code>
```

---

## 1. Audit Checkpoints

The audit statically parses class names, inline styles, CSS rules, and HTML elements across all source files:

1. **Surfaces (Border-Radius & Corners):**
   - Flags forbidden rounding (e.g. `rounded-lg`, `rounded-full`, `border-radius: 8px`) in styles requiring sharp 0px geometry (Swiss Editorial, Quiet Luxury, Cyberpunk).
   - Flags pill utilities (`rounded-full`) on containers in Neo-Brutalism.
2. **Surfaces (Shadows & Depth):**
   - Flags blurry drop shadows (`shadow-md`, `shadow-lg`, `box-shadow` with blur radius > 0) in Swiss Editorial, Quiet Luxury, and Neo-Brutalism.
   - Verifies hard solid offset shadows (`4px 4px 0px #000`) for Neo-Brutalism.
3. **Surfaces (Border Weights):**
   - Flags faint gray borders (`border-gray-200`) in Neo-Brutalism where 2-4px solid black borders are mandatory.
4. **Color & Palette:**
   - Flags cold generic Tailwind grays (`bg-gray-100`, `text-slate-500`) in Quiet Luxury where warm alabaster and espresso ink are mandated.
   - Flags bright primary/neon accents in Quiet Luxury.
   - Flags light-mode backgrounds (`bg-white`) in Cyberpunk.
5. **Typography:**
   - Flags generic sans-serif fallbacks on primary headings in styles that mandate editorial serifs or monospaced telemetry.

---

## 2. Structured Audit Report Format

The audit produces a qualitative adherence verdict and detailed layer-by-layer breakdown:

```markdown
# DESIGN AUDIT REPORT
**Target Style:** QUIET-LUXURY
**Status:** FAILED: Moderate Spec Deviations
**Files Scanned:** 4

## Summary
- **Total Deviations:** 3
- **Critical Violations:** 2
- **Warnings:** 1
- **Layer Breakdown:**
  - Surfaces: 2 violations
  - Typography: 1 violation

## Detected Violations
1. `src/components/WealthCard.tsx` (Line 14)
   - **Layer:** Surfaces
   - **Severity:** CRITICAL
   - **Type:** Radius Violation
   - **Offending Code:** `rounded-xl`
   - **Issue:** Quiet Luxury spec mandates 0px radius (`rounded-none`). Found `rounded-xl`.

2. `src/components/WealthCard.tsx` (Line 22)
   - **Layer:** Surfaces
   - **Severity:** CRITICAL
   - **Type:** Shadow Violation
   - **Offending Code:** `shadow-lg`
   - **Issue:** Quiet Luxury forbids blurry drop shadows. Elevation is conveyed via tone and hairline borders.

3. `src/components/HeroHeading.tsx` (Line 8)
   - **Layer:** Typography
   - **Severity:** WARNING
   - **Type:** Font Substitution
   - **Offending Code:** `font-sans font-bold`
   - **Issue:** Quiet Luxury mandates editorial serif for primary headings.
```
