# Test Cases — design-director & design-audit

Small, copy-pasteable tests you can run yourself. Section A/C/D are deterministic
(CLI / Python — exact expected outputs verified on 2026-09-23). Section B tests the
conversational SKILL.md inside an AI coding agent (Claude Code, Cursor, Copilot),
so outputs vary in wording but must match the described behavior.

**Setup (once):** Python 3.10+ (standard library only — zero pip dependencies required).
All commands run from the repo root.

---

## A. design-audit — deterministic CLI tests

### A1. Clean code passes, seeded violations fail
```bash
python3 skills/design-audit/audit_code.py quiet-luxury   tests/fixtures/seeded_code/clean_quiet_luxury.html
python3 skills/design-audit/audit_code.py quiet-luxury   tests/fixtures/seeded_code/deviant_quiet_luxury.html
python3 skills/design-audit/audit_code.py bauhaus        tests/fixtures/seeded_code/deviant_bauhaus.html
python3 skills/design-audit/audit_code.py cyberpunk      tests/fixtures/seeded_code/deviant_cyberpunk.html
python3 skills/design-audit/audit_code.py neo-brutalism  tests/fixtures/seeded_code/deviant_neo_brutalism.html
```
**Expected** (JSON `status` field):
| File | Status |
|---|---|
| `clean_quiet_luxury.html` | `PASSED: Full Spec Adherence` (0 critical, 0 warnings) |
| `deviant_quiet_luxury.html` | `FAILED: Severe Contract Breach` (4 critical) |
| `deviant_bauhaus.html` | `FAILED: Moderate Spec Deviations` (3 critical) |
| `deviant_cyberpunk.html` | `FAILED: Moderate Spec Deviations` (1 critical: light bg) |
| `deviant_neo_brutalism.html` | `FAILED: Moderate Spec Deviations` (2 critical: pill radius, timid border) |

### A2. Every gallery preview passes its own style
```bash
for f in skills/design-director/gallery/*.html; do
  s=$(basename "$f" .html | tr '_' '-')
  [ "$s" = "baseline" ] && continue   # baseline is a deliberately generic demo, not a style
  python3 skills/design-audit/audit_code.py "$s" "$f" | python3 -c "import json,sys; r=json.load(sys.stdin); print(r['status'], '$f')"
done
```
**Expected:** 27× `PASSED: Full Spec Adherence`.

### A3. Cross-style audit discriminates
```bash
python3 skills/design-audit/audit_code.py quiet-luxury skills/design-director/gallery/neo_brutalism.html
```
**Expected:** `FAILED: Severe Contract Breach` (≥4 critical — hard offset shadows, chunky borders, loud palette).

### A4. Modifier whitelist
```bash
printf '<div class="backdrop-blur-xl bg-white/70 panel">Frosted</div>\n' > /tmp/glass.html
python3 skills/design-audit/audit_code.py swiss-editorial /tmp/glass.html
python3 skills/design-audit/audit_code.py swiss-editorial /tmp/glass.html --modifiers frosted-glass
```
**Expected:** first → `FAILED` (1 critical `unauthorized_modifier`); second → `PASSED: Full Spec Adherence`.

### A5. Unknown / typo'd style id is rejected
```bash
python3 skills/design-audit/audit_code.py quiet-luxury-TYPO tests/fixtures/seeded_code/clean_quiet_luxury.html; echo "exit=$?"
```
**Expected:** `error: Unknown style id 'quiet-luxury-TYPO'` + list of the 27 valid styles, `exit=2`. (Guards against a typo silently "passing" with zero rules.)

### A6. Corporate Memphis trap (the money test)
```bash
mkdir -p /tmp/mock-frontend && cat > /tmp/mock-frontend/bad.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<body class="bg-gray-50 text-slate-900 font-sans">
  <!-- illustration: friendly blob characters waving -->
  <header class="bg-white shadow-md px-6 py-4"><h1 class="font-sans font-bold text-3xl">Aurelia</h1></header>
  <main class="p-6">
    <section class="card bg-white rounded-2xl shadow-lg p-8 border border-gray-200">
      <button class="bg-blue-600 text-white rounded-lg px-4 py-2 shadow-sm">Get Started</button>
      <div class="bg-purple-500 rounded-3xl p-4 mt-4">Upgrade now</div>
    </section>
  </main>
</body>
</html>
EOF
python3 skills/design-audit/audit_code.py quiet-luxury /tmp/mock-frontend/bad.html
```
**Expected:** `FAILED: Severe Contract Breach`, ~11 violations with exact line numbers across
`color` / `surfaces` / `typography`, plus a `corporate_memphis_drift` CRITICAL naming all
4 signals (`ambient_shadow, bubbly_container, illustration_placeholder, purple_accent`).

### A7. Audit your own project
```bash
python3 skills/design-audit/audit_code.py <style_id> ./src            # directory walk (.html .jsx .tsx .vue .svelte .css)
python3 skills/design-audit/audit_code.py <style_id> ./index.html     # single file
```
**Expected:** JSON report — `status`, `summary.by_layer`, and per-violation `file`/`line`/`offending_code`/`message` with a remediation instruction.

---

## B. design-director — conversational tests inside an AI agent

Install both skills into your agent first (see README → Install & Publish), then run
these in a scratch project.

### B1. Rich context → no interview, direct recommendations
Copy `tests/fixtures/prds/fintech-wealth.md` into an empty project as `PRD.md`, then prompt:
```text
Use the design-director skill: analyze my PRD and recommend a visual direction.
```
**Expected behavior:**
- Skips the interview (context is rich) — SKILL.md Phase 2 gate.
- Presents 2–3 directions, each with an in-chat visual micro-spec (inline SVG strip + swatch token line: display font, canvas/surface/accent hexes, radius rule), a portable project-relative link to `skills/design-director/gallery/<style>.html` (or `.agents/skills/design-director/gallery/<style>.html`), and an honest trade-off. Never emits absolute `file:///` URLs.
- Recommendations should be in the quiet-luxury / art-deco / swiss-editorial neighborhood (matches the deterministic engine, C1).
- Must NOT propose generic defaults (`Inter` + `rounded-lg` + `bg-blue-600`).

### B2. Thin context → interview gate fires
In an empty project prompt:
```text
@design-director I want a website for my startup.
```
**Expected:** asks **at most 3** targeted questions (information density, brand character, visual constraints) *before* recommending — never more than 3, never zero-and-guess when context is this thin.

### B3. Critique & refinement
Continue from B1:
```text
More like Linear. And add a frosted-glass surface with snappy motion.
```
**Expected:** shifts surfaces/color/motion toward `dark-minimal` (obsidian canvas, hairline borders, single muted accent), applies `frosted-glass` + `micro-snappy` modifiers, and states which layers changed vs. stayed stable.

### B4. Contract handoff
```text
Confirmed — generate the design contract.
```
**Expected:** a `DESIGN_CONTRACT.md` appears in the project root containing: target style + token variables (CSS vars / Tailwind mapping), active modifiers with audit whitelists, component geometry rules, and a `NEVER`-style anti-pattern section. The agent should have loaded **only** the one chosen `styles/<style_id>.md` file from the skill directory (token economy rule).
Optionally, the agent offers to generate ONE tailored single-file preview (e.g. `preview_<style_id>.html`) reflecting the project's actual domain, active modifiers, and custom palette (strictly opt-in, never unprompted at candidate stage).


### B5. Full loop: director → build → audit
After B4, in the same project:
```text
Build a single-page landing hero (index.html, Tailwind CDN) that strictly follows DESIGN_CONTRACT.md.
```
Then verify with the audit skill:
```bash
python3 <path-to>/skills/design-audit/audit_code.py quiet-luxury ./index.html
```
**Expected:** `PASSED: Full Spec Adherence`, or a failed report whose violations are real and actionable (fix them and re-audit until green). This is the end-to-end contract the whole framework exists for.

---

## C. director_engine.py — programmatic pipeline

### C1. PRD → brief → recommendations
```bash
python3 - <<'EOF'
import sys; sys.path.insert(0, 'skills/design-director')
from director_engine import extract_design_brief, recommend_styles
for f in ["fintech-wealth", "dev-telemetry-cli", "indie-creators-store"]:
    b = extract_design_brief(open(f'tests/fixtures/prds/{f}.md').read())
    print(f"{f:22} -> {b['product_type']:35}", [r['style_id'] for r in recommend_styles(b)])
EOF
```
**Expected (verified):**
```text
fintech-wealth         -> FinTech / Wealth Management       ['quiet-luxury', 'art-deco', 'swiss-editorial']
dev-telemetry-cli      -> Developer Tool / Platform         ['command-center', 'dark-minimal', 'terminal-cli']
indie-creators-store   -> Creator Marketplace / Community   ['minimal-modern', 'organic-natural', 'neo-brutalism']
```

### C2. Refinement mapping ("more like Linear")
```bash
python3 - <<'EOF'
import sys; sys.path.insert(0, 'skills/design-director')
from director_engine import create_design_spec, refine_spec
spec = create_design_spec("quiet-luxury")
out = refine_spec(spec, "more like Linear")["updated_spec"]["layers"]
print({k: out[k] for k in ("surfaces", "color", "motion")})
EOF
```
**Expected:** surfaces/color/motion now point at `styles/dark-minimal.md` (reference-library driven, no percentage blending).

### C3. Domain routing has no substring false positives
```bash
python3 - <<'EOF'
import sys; sys.path.insert(0, 'skills/design-director')
from director_engine import extract_design_brief
for t in ["Build me a website for my startup.",
          "A dashboard to create invoices and track revenue per account.",
          "A firewall appliance that helps prevent intrusions.",
          "Software for modern agriculture cooperatives."]:
    print(f"{t[:52]:54} -> {extract_design_brief(t)['product_type']}")
EOF
```
**Expected:** all four → `Web Application` (neutral fallback). Before the word-boundary fix these misrouted via `st·art·up`, `·cre·ate`, `re·venue`, `agri·culture`.

---

## D. Repository test suites

```bash
npm run test:unit          # 39 tests: briefs, specs, contracts, routing, audit precision/recall, regressions
npm run test:e2e:pipeline  # 37 tests: unseen PRDs end-to-end + gallery audits
npm run test:e2e:browser   # Playwright computed-style DOM audit (needs: npx playwright install chromium)
```
**Expected:** unit + pipeline fully green anywhere Python 3.10+ exists. The browser suite
additionally needs a Chromium download — skip it in network-restricted sandboxes.

---

## Known limitations (by design, worth knowing when you test)

1. **The auditor matches class/CSS patterns, not computed values.** Code using arbitrary
   hex values (`bg-[#FBFBF9]`) or CSS-variable indirection is invisible to palette rules —
   e.g. `clean_quiet_luxury.html` audited as `cyberpunk` passes, because its light canvas is
   a hex literal, not `bg-white`. The Playwright suite covers computed styles for the gallery.
2. **"building" is semantically ambiguous** in domain routing: "building an internal
   dashboard" routes to Architecture & Spatial Design when no earlier bucket matches.
3. **The interview gate is prompt-level** (SKILL.md Phase 2). `director_engine.py` itself
   always returns a brief, falling back to neutral `Web Application` — that fallback is the
   deterministic-pipeline behavior, not the conversational one.
4. **Corporate Memphis signals are hand-duplicated** between `audit_code.py` and
   `skills/design-director/styles/reference-anti-patterns.md` (see NOTE comment in the source) — keep them in sync
   if you edit either.
