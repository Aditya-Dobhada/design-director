# PRD: Design Director

**A design reasoning engine that turns product context into implementation-ready visual direction for AI coding agents.**

---

## 1. Problem Statement

AI coding agents produce technically valid, functionally correct UI that is visually indistinguishable from every other AI-generated product. This happens because coding agents collapse **design direction** and **implementation** into a single prompt-to-code step, defaulting to the statistical median of their training data — generic Tailwind SaaS aesthetics.

There is no layer that:
- Reasons about what a product *should feel like* based on its actual context (users, domain, competitors, constraints)
- Translates that feeling into a concrete, composable visual language
- Hands that language to a coding agent as a **contract** rather than a **vibe**
- Verifies after implementation that the contract was actually followed

This tool is not a frontend generator. It is a **design reasoning engine** whose output happens to be consumed by frontend coding agents (and, eventually, other downstream consumers like Figma plugins or brand guideline generators).

Since this system is built via agentic AI-driven development, it should be scoped in **build phases gated by validation checkpoints**, not calendar time. Each phase completes when its acceptance criteria pass, not when a deadline arrives.

---

## 2. Goals

1. Produce a structured **Design Brief** from product context (PRD, README, codebase, target audience, competitors).
2. Recommend multiple visual directions with honest tradeoffs, not a single forced answer.
3. Represent visual direction as **composable layers** (layout, typography, surface, color, imagery, motion) rather than a single monolithic "style."
4. Translate the chosen direction into an implementation-ready **Design Spec** that a coding agent can follow as hard constraints.
5. Audit implemented frontend code against the Design Spec and report deviations.
6. Support natural, iterative refinement ("more like Linear, less like a bank") without regenerating from scratch.

## 3. Non-Goals (v1)

- Generating pixel-accurate visual previews (images or full HTML mockups) before implementation.
- Supporting all ~50 design styles/families from the initial taxonomy.
- Building a general-purpose design tool, Figma integration, or standalone app. v1 is a coding-agent skill/CLI.
- Automatically fixing audit failures (v1 reports; it does not auto-remediate).

---

## 4. Users

- Developers using AI coding agents (Cursor, Claude Code, etc.) to build product frontends who want intentional, non-generic visual identity without hiring a designer.
- Small teams/solo founders who need a defensible design direction fast, with reasoning they can explain to stakeholders.

---

## 5. System Overview

```
PRD / SPEC / README / Codebase
              │
              ▼
       DESIGN DIRECTOR
   (extracts Design Brief)
              │
              ▼
   STYLE RECOMMENDATION
 (multiple directions + fit + tradeoffs)
              │
        User chooses / refines
              │
              ▼
      DESIGN SPEC (layered)
              │
              ▼
   STYLE-SPECIFIC SKILL PACKS
              │
              ▼
       FRONTEND AGENT
      (implements UI)
              │
              ▼
       DESIGN AUDIT
 (checks implementation vs spec)
```

---

## 6. Functional Requirements

### 6.1 `design-director` (analysis skill)

Reads available inputs: `PRD.md`, `SPEC.md`, `README.md`, existing frontend code, screenshots, stated target audience, product category, brand requirements, competitor references.

Outputs a **Design Brief** in structured YAML, including at minimum:
- Product type and audience
- Personality traits (e.g., trustworthy, playful, technical, premium)
- UX requirements (density, information load, workflow orientation)
- Brand positioning axes (playful↔serious, premium↔accessible, futuristic↔institutional)
- Visual constraints (accessibility needs, readability criticality, motion tolerance)

**Acceptance criteria:** Given a sample PRD, the director produces a Design Brief that a human reviewer agrees accurately reflects the product's context, without requiring the human to re-explain the product.

### 6.2 Style Recommendation

Given a Design Brief, recommend **2–4 candidate directions**, each with:
- Name/description of the direction
- Reasoning for why it fits
- Explicit tradeoffs/risks
- Qualitative fit rating only: **Strong fit / Good fit / Possible / Poor fit** (no numeric/percentage scores exposed to the user)

**Acceptance criteria:** Recommendations must differ meaningfully from each other (not cosmetic variants of the same direction), and each must include at least one honest tradeoff or risk.

### 6.3 Reference Library

A structured library (v1: ~20–30 entries) mapping well-known products/brands to decomposed design properties (mode, density, spacing, borders, shadows, typography, color, motion, personality) — not screenshots.

**Purpose:** When a user says "make it feel like Linear" or "less like a bank," the director maps this to concrete property adjustments instead of hallucinating.

**Acceptance criteria:** For at least 10 test reference terms, the director produces a consistent, concrete property mapping rather than a vague restatement.

### 6.4 Design Spec (Layered Composition)

Once a direction is chosen (or refined), the director outputs a **Design Spec** that decomposes the direction into independent layers, each with a single clear source of truth — no ambiguous percentage blending:

```yaml
layout: swiss-asymmetric-grid
typography: editorial-serif-headings + grotesk-body
surfaces: neo-brutalist-borders + hard-shadows
color: swiss-neutral + single-accent
motion: restrained
imagery: conceptual-sketch
```

**Acceptance criteria:** Every layer resolves to exactly one style-pack source; no layer is left as an unresolved blend/percentage.

### 6.5 Iterative Refinement

User can provide free-text critique (e.g., "too corporate," "more like Stripe"). The director updates the Design Spec layer-by-layer rather than regenerating the whole direction from scratch, and reports which layers changed and why.

**Acceptance criteria:** A refinement request changes only the relevant layers; unrelated layers remain stable across iterations.

### 6.6 Style Packs

Each supported style is a self-contained skill package including:
- Core principles
- Typography recommendations (preferred fonts + explicit fonts/approaches to avoid)
- Component rules (buttons, cards, inputs — concrete values: border widths, radius, shadow style)
- Layout guidance (preferred and anti-pattern layouts)
- Motion guidance (preferred and anti-pattern motion)

**v1 scope: 5 style packs**, chosen for maximum mutual distinctiveness and distance from generic AI-SaaS default:
1. Swiss / Editorial
2. Neo-Brutalism
3. Y2K / Frutiger Aero
4. Quiet Luxury
5. Cyberpunk

**Acceptance criteria:** Each style pack includes explicit **negative constraints** (anti-patterns), since these are more effective than positive descriptions at steering models away from default output.

### 6.7 Implementation Handoff

The Design Spec + relevant Style Pack(s) + product spec + tech stack are packaged into a single implementation contract handed to the frontend coding agent.

**Acceptance criteria (critical validation gate):** Given identical product specs, a coding agent's output *with* the Design Spec must be visibly and consistently distinguishable from its output *without* one, across all 5 v1 style packs. **This gate must pass before any further style packs or preview features are built.**

### 6.8 Design Audit

A post-implementation skill that inspects generated frontend code against the chosen Design Spec and reports adherence/deviation per layer (e.g., "14 cards use rounded corners; spec requires 0 radius").

**Acceptance criteria:** Audit correctly flags at least the deviations manually seeded into a test implementation (border-radius, shadow style, font substitution, spacing violations).

---

## 7. Non-Functional Requirements

- Delivered as a coding-agent skill repository (`SKILL.md`-based), not a hosted app, for v1.
- No numeric/percentage fit scores or blend ratios exposed in any user-facing output — qualitative language only.
- All style pack rules must be concrete/testable (specific values), not purely descriptive prose.
- Every skill (director, style packs, audit) must be independently testable in isolation before wiring the full pipeline together — build and validate bottom-up.

---

## 8. Repository Structure (v1)

```
design-skills/
│
├── director/
│   ├── SKILL.md
│   └── reference-library.yaml
│
├── styles/
│   ├── swiss-editorial/
│   ├── neo-brutalism/
│   ├── y2k-frutiger-aero/
│   ├── quiet-luxury/
│   └── cyberpunk/
│       ├── SKILL.md
│       ├── tokens.md
│       ├── typography.md
│       ├── layout.md
│       ├── components.md
│       └── motion.md
│
└── audit/
    └── SKILL.md
```

CLI/skill invocations:
```
/design analyze
/design recommend
/design choose <style>
/design refine "<free-text critique>"
/design implement
/design audit
```

---

## 9. Explicit Design Decisions

- **No visual preview generation in v1.** Image-based previews don't translate reliably into implementation; full HTML previews collapse the separation between direction and implementation. v1 ships a readable **Design Spec document** (typography specimens, color swatches, component rules in prose/HTML snippets) instead of a rendered preview.
- **No percentage-based style blending exposed to coding agents.** Composition is resolved into single-source-of-truth layers before handoff.
- **Negative constraints (anti-patterns) are mandatory** in every style pack, not optional.
- **Start with 5 deep style packs, not 50 shallow ones.** Depth over breadth until the handoff mechanism is proven.

---

## 10. Build Phases (dependency-gated, not time-gated)

Since development is agentic-AI-driven, phases proceed as fast as each gate can be validated — there is no assumption of multi-week durations. A phase does not start until the prior phase's acceptance criteria pass.

| Phase | Deliverable | Gate to proceed |
|---|---|---|
| **P1 — Core Reasoning** | `design-director` SKILL.md + reference library + 3 style packs (Swiss, Neo-Brutalism, Quiet Luxury) | Director produces an accurate Design Brief and a fully-resolved layered Design Spec on a real test PRD |
| **P2 — Handoff Validation (critical gate)** | Feed Design Spec + style pack into a real coding agent against a real product spec | Blind comparison shows output *with* spec is visibly distinct from output *without* spec, across all 3 packs. **Do not proceed to P3 until this passes** — if it fails, iterate on spec format/handoff, not on adding more styles |
| **P3 — Audit Loop** | `design-audit` skill | Audit correctly flags deviations seeded into a test implementation (radius, shadow, font, spacing) |
| **P4 — Expansion** | Remaining style packs (Y2K, Cyberpunk) + refinement loop (`/design refine`) | Refinement changes only targeted layers; new packs pass the same handoff gate as P2 |
| **P5 — Full Pipeline** | End-to-end `/design analyze → recommend → choose → implement → audit` on a fresh, unseen product spec | Full run completes without manual intervention and produces an implementation that passes audit |

---

## 11. Success Metrics

- **Primary:** In blind comparison, human reviewers can correctly match generated frontends to their intended style direction ≥80% of the time, and distinguish them from "default AI SaaS" output.
- **Secondary:** Audit skill precision/recall on seeded deviations ≥90%.
- **Secondary:** Refinement requests do not require full regeneration (layer-scoped diffs only).

---

## 12. Future / Out of Scope for v1

- Full 12-family style taxonomy (Retro, Futuristic, Cultural/Historical, Organic, Luxury, Experimental).
- Visual board/preview generation once a reliable image-to-token pipeline exists.
- Non-code downstream consumers (Figma plugins, brand guideline docs, design token exports to design tools).
- Auto-remediation of audit failures.
