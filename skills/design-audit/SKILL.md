---
name: design-audit
description: Post-implementation verification skill. Scans generated frontend code (HTML, JSX, TSX, Vue, Svelte, CSS) against a chosen design contract. Detects forbidden border-radius, blurry drop shadows, font substitutions, and illegal color classes, returning actionable remediation guidance.
---

# Design Audit

A verification skill that statically scans frontend source code against a target design style to guarantee that the `DESIGN_CONTRACT.md` was followed.

## Invocations

Run via CLI inside the project:
```bash
python3 skills/design-audit/audit_code.py <style_id> <target_directory_or_file>
```

Examples:
```bash
python3 skills/design-audit/audit_code.py quiet-luxury ./src
python3 skills/design-audit/audit_code.py neo-brutalism ./index.html
```

---

## What It Checks

1. **Surfaces & Radii:**
   - Sharp styles (Quiet Luxury, Swiss Editorial, Bauhaus, Cyberpunk): Flags any `rounded-md`, `rounded-lg`, `rounded-full`, or `border-radius > 0px`.
   - Brutalist styles (Neo-Brutalism, Maximalist): Flags pill utilities (`rounded-full`) on containers.
   - Organic & Space Age: Flags `rounded-none` where curved pods are required.
2. **Shadows & Depth:**
   - Zero-blur styles (Swiss Editorial, Quiet Luxury, Bauhaus, Wabi-Sabi, Memphis, Retro Americana): Flags blurry drop shadows (`shadow-sm`, `shadow-md`, `shadow-lg`, `box-shadow` with blur > 0).
   - Neo-Brutalism: Flags blurry shadows; mandates hard solid offset shadows (`4px 4px 0px #000`).
3. **Borders:**
   - Neo-Brutalism & Retro Americana: Flags faint 1px borders (`border-gray-200`); mandates 2–4px solid ink strokes.
4. **Color & Canvas:**
   - Quiet Luxury & Wabi-Sabi: Flags cold generic Tailwind grays (`bg-gray-100`, `text-slate-500`) and saturated neon accents.
   - Cyberpunk: Flags light backgrounds (`bg-white`, `bg-gray-50`).
   - Space Age Optimism: Flags pitch-black canvases; mandates warm optical white.
5. **Typography:**
   - Quiet Luxury: Flags generic sans-serif fallbacks on primary headings where high-contrast editorial serifs (`Cormorant Garamond`) are mandated.

---

## Audit Output Structure

The audit outputs a structured qualitative report:
- `PASSED: Full Spec Adherence`: 0 critical, 0 warnings
- `PASSED WITH WARNINGS`: 0 critical, minor stylistic variances
- `FAILED: Moderate Spec Deviations`: 1–3 critical deviations
- `FAILED: Severe Contract Breach`: >3 critical deviations

For each violation, the report provides the exact file path, line number, layer, offending code snippet, and remediation instruction.
