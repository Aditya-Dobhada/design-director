# HARD IMPLEMENTATION DESIGN CONTRACT
**Target Style:** QUIET-LUXURY
**Tech Stack:** Tailwind CSS + React
**Execution Mode:** STRICT CONTRACT (Not a vibe. Zero tolerance for generic AI defaults.)

---

## 1. Resolved Design Spec Layers
- **Layout Source:** `quiet-luxury/layout.md`
- **Typography Source:** `quiet-luxury/typography.md`
- **Surfaces & Shadows:** `cyberpunk/tokens.md`
- **Color Palette:** `obsidian-monochrome-with-violet-accent`
- **Motion & Transitions:** `swiss-editorial/motion.md`
- **Component Geometry:** `quiet-luxury/components.md`

---

## 2. Hard Anti-Patterns (BANNED CLASSES & PATTERNS)
The coding agent MUST NOT output any of the following patterns. Doing so triggers an immediate post-implementation audit rejection:

- **NEVER** use rounded corners (`rounded-md`, `rounded-lg`, `rounded-full`). Border-radius must be strictly `0px` (`rounded-none`).
- **NEVER** use dark or blurry drop shadows (`box-shadow: 0 4px 12px rgba(0,0,0,0.15)`). Shadows must be `none`.
- **NEVER** use high-saturation neon or primary colors (e.g. electric blue, bright red, hot pink). All accents are muted earth or mineral tones (champagne, warm espresso, olive bronze, muted brass).
- **NEVER** use heavy borders (`border: 2px` or `3px`). Borders are at most `1px solid rgba(0,0,0,0.08)`.
- **NEVER** crowd content into dense multi-row card grids. Whitespace is the primary asset; margins must be wide and unhurried.
- **NEVER** use bouncy, elastic, or frantic animations. Motion must be slow, fluid, and cinematic (400ms to 600ms).
- **NEVER** use badges with colored pills (`bg-green-100 text-green-800`). Labels are small-caps text with generous letter-spacing.

---

## 3. Product Specification & Requirements
# Product Requirements Document: Aurelia Private Wealth

## 1. Overview
Aurelia is a private wealth management portal for ultra-high-net-worth families, estate managers, and boutique wealth advisory firms overseeing portfolios exceeding $25M.

## 2. Target Audience
- Principals of family offices
- Private wealth advisors and trust officers
- Discerning clients accustomed to luxury private banking (e.g. Lombard Odier, Pictet)

## 3. Product Character & Personality
- Understated elegance, supreme discretion, quiet authority.
- Avoid loud crypto hype, flashing stock tickers, or generic commercial banking aesthetics.
- Reading experience should feel like an impeccably crafted leather-bound financial ledger or architectural monograph.

## 4. Key Workflows
- Quarterly wealth balance allocation reviews
- Trust distributions and multi-generational asset holdings
- Curated private equity deal briefs
- Direct confidential messaging with senior managing partners

## 5. Visual Constraints
- Extremely legible typography for large financial figures and asset allocations.
- Calming, distraction-free environment.
- Restrained motion: zero playful springs or flashy animations.

---

## 4. Contract Verification Notice
Upon code generation, the post-implementation `design-audit` will statically scan all `.html`, `.jsx`, `.tsx`, and `.css` files.
Deviations in border-radius, shadow blur, font substitutions, or color values will be flagged as audit failures.
