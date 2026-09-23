---
name: design-audit
description: Post-implementation verification skill. Scans generated frontend code (HTML, JSX, TSX, Vue, Svelte, CSS) against a chosen design contract. Detects forbidden border-radius, blurry drop shadows, font substitutions, and illegal color classes, returning actionable remediation guidance.
---

# Design Audit

A verification skill that statically scans frontend source code against a target design style to guarantee that the `DESIGN_CONTRACT.md` was followed.

## Invocations

Run via CLI inside the project:
```bash
python3 skills/design-audit/audit_code.py <style_id> <target_directory_or_file> [--modifiers <mod1,mod2>]
```

Examples:
```bash
python3 skills/design-audit/audit_code.py quiet-luxury ./src
python3 skills/design-audit/audit_code.py terminal-cli ./src
python3 skills/design-audit/audit_code.py dark-minimal ./src --modifiers frosted-glass,subtle-grain
python3 skills/design-audit/audit_code.py neo-brutalism ./index.html
```

Unknown or misspelled `style_id` values are rejected with exit code 2 and the list of the 27 valid styles — a typo can never silently "pass" an audit.

---

## What It Checks

1. **Surfaces & Radii:**
   - **Sharp styles (0px / `rounded-none` required):** `swiss-editorial`, `quiet-luxury`, `bauhaus`, `retro-americana`, `japanese-wabi-sabi`, `memphis-postmodern`, `terminal-cli`, `web-brutalism`, `art-deco`, `high-fashion-editorial`. Flags any `rounded-md`, `rounded-lg`, `rounded-full`, or `border-radius > 0px`.
   - **Organic & Pod styles:** `space-age-optimism`, `organic-natural`, `y2k-frutiger-aero`, `mid-century-modern`. Flags `rounded-none` where curved pods (16–24px) are required.
   - **Restrained Minimal styles:** `minimal-modern`, `dark-minimal`. Flags excessive container pill utilities (`rounded-full`, `rounded-3xl` on cards); mandates 4–8px bounded radii.
   - **Brutalist styles:** `neo-brutalism`, `maximalist-dopamine`. Flags pill utilities (`rounded-full`) on containers; requires chunky 0–8px geometry.
2. **Shadows & Depth:**
   - **Zero-blur styles:** `swiss-editorial`, `quiet-luxury`, `bauhaus`, `japanese-wabi-sabi`, `memphis-postmodern`, `retro-americana`, `terminal-cli`, `web-brutalism`, `art-deco`, `high-fashion-editorial`. Flags blurry drop shadows (`shadow-sm`, `shadow-md`, `shadow-lg`, or `box-shadow` with blur > 0).
   - **Neo-Brutalism & Maximalism:** Flags blurry shadows; mandates hard solid offset shadows (e.g. `4px 4px 0px #000`).
3. **Borders:**
   - `neo-brutalism`, `retro-americana`, `maximalist-dopamine`: Flags faint 1px borders (`border-gray-200`); mandates 2–4px solid ink strokes.
4. **Color & Canvas:**
   - **Quiet Luxury, Wabi-Sabi, Organic Natural:** Flags cold generic Tailwind grays (`bg-gray-100`, `text-slate-500`) and saturated neon accents.
   - **Strict Dark Canvas (`cyberpunk`, `terminal-cli`, `dark-minimal`):** Flags light backgrounds (`bg-white`, `bg-gray-50`, `bg-slate-50`).
   - **Radiant Light Canvas (`space-age-optimism`, `mid-century-modern`):** Flags pitch-black canvases (`bg-black`, `bg-zinc-950`).
5. **Modifiers Whitelist:**
   - Flags unauthorized `backdrop-blur` or glassmorphism classes in sharp/brutalist styles unless the `frosted-glass` modifier is explicitly declared.
6. **Typography:**
   - Flags generic sans-serif fallbacks on primary headings where high-contrast editorial serifs or monospace fonts are mandated.

---

## Audit Output Structure

The audit outputs a structured qualitative report:
- `PASSED: Full Spec Adherence`: 0 critical, 0 warnings
- `PASSED WITH WARNINGS`: 0 critical, minor stylistic variances
- `FAILED: Moderate Spec Deviations`: 1–3 critical deviations
- `FAILED: Severe Contract Breach`: >3 critical deviations
- `ERROR: No files scanned`: nonexistent path, empty target, or unreadable files (CLI exits 2; see `skipped_files` for reasons) — never a silent pass

For each violation, the report provides the exact file path, line number, layer, offending code snippet, and remediation instruction.
