"""
Design Audit Static Analysis Engine
Scans frontend source code against a target Design Spec and reports violations
across layout, typography, surfaces (borders, radius, shadows), color, and motion.
"""

import json
import os
import re
from pathlib import Path
from typing import Any


class DesignAuditor:
    def __init__(self, target_style: str, modifiers: list[str] | None = None):
        self.target_style = target_style.lower()
        self.modifiers = [m.lower() for m in (modifiers or [])]
        self.violations: list[dict[str, Any]] = []
        self._memphis_signals: dict[str, list] = {}  # per-file Corporate Memphis signal accumulator

    def audit_file(self, file_path: Path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            return

        for idx, line in enumerate(lines, 1):
            self._check_line(file_path, idx, line)
        # Post-file: evaluate accumulated Corporate Memphis signals
        self._check_corporate_memphis_drift(file_path)

    def _check_line(self, file_path: Path, line_no: int, line: str):
        # Skip pure comment lines (HTML <!-- ... --> or CSS /* / //) to avoid
        # false positives from inline design-contract documentation.
        stripped = line.strip()
        if (stripped.startswith('<!--') or stripped.startswith('//') or
                stripped.startswith('*') or stripped.startswith('/*')):
            return

        # 1. Border-Radius Violations
        sharp_radius_styles = [
            "swiss-editorial", "quiet-luxury", "bauhaus",
            "retro-americana", "japanese-wabi-sabi", "memphis-postmodern",
            "terminal-cli", "web-brutalism", "art-deco", "high-fashion-editorial"
        ]
        if self.target_style in sharp_radius_styles:
            # Spec requires 0px (rounded-none). Any rounded-md, rounded-lg, rounded-full, rounded-2xl is a violation (unless full is on an explicit circle medallion for bauhaus/memphis/art-deco).
            bad_radii = re.findall(r'\b(rounded-(?:md|lg|xl|2xl|3xl|full))\b', line)
            for br in bad_radii:
                # Allow rounded-full only if on a tiny circle medallion or icon
                if br == "rounded-full" and any(k in line for k in ["w-4", "h-4", "w-6", "h-6", "w-8", "h-8", "w-12", "h-12", "circle", "arch"]):
                    continue
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "surfaces",
                    "severity": "CRITICAL",
                    "type": "radius_violation",
                    "offending_code": br,
                    "message": f"Spec for '{self.target_style}' requires 0px radius (rounded-none). Found forbidden rounded utility '{br}'."
                })
            # CSS border-radius check
            css_radii = re.findall(r'border-radius\s*:\s*([^;]+);', line)
            for cr in css_radii:
                val = cr.strip()
                # Skip var(--...) references: they resolve to values declared in :root
                # (e.g. --radius: 0px). Flagging them is a false positive.
                if val.startswith('var('):
                    continue
                if val not in ["0", "0px", "none"] and not ("50%" in val and self.target_style in ["bauhaus", "memphis-postmodern", "art-deco"]):
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "CRITICAL",
                        "type": "radius_violation",
                        "offending_code": f"border-radius: {cr}",
                        "message": f"Spec for '{self.target_style}' requires 0px border-radius. Found '{val}'."
                    })

        elif self.target_style in ["space-age-optimism", "organic-natural", "y2k-frutiger-aero", "mid-century-modern"]:
            # These styles mandate organic or pod curves (minimum 16px to full pill). rounded-none is a violation on cards/buttons.
            if any(k in line for k in ["card", "panel", "btn", "button", "container"]):
                sharp_corners = re.findall(r'\b(rounded-none)\b', line)
                for sc in sharp_corners:
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "WARNING",
                        "type": "radius_violation",
                        "offending_code": sc,
                        "message": f"Spec for '{self.target_style}' mandates organic/capsule curves. Found '{sc}' on primary container."
                    })

        elif self.target_style in ["minimal-modern", "dark-minimal"]:
            # Spec requires restrained, crisp geometry (4-8px radius, e.g. rounded-md, rounded-lg).
            # Overly bubbly pill containers (rounded-full or rounded-3xl on containers) are forbidden.
            if any(k in line for k in ["card", "panel", "container", "section"]):
                bad_radii = re.findall(r'\b(rounded-full|rounded-3xl)\b', line)
                for br in bad_radii:
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "WARNING",
                        "type": "radius_violation",
                        "offending_code": br,
                        "message": f"{self.target_style} requires restrained geometry (4-8px). Found excessive container radius '{br}'."
                    })

        elif self.target_style in ["neo-brutalism", "maximalist-dopamine"]:
            # Spec requires 0px or chunky 4-8px max. rounded-full is banned on any element.
            bad_radii = re.findall(r'\b(rounded-full)\b', line)
            for br in bad_radii:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "surfaces",
                    "severity": "WARNING",
                    "type": "radius_violation",
                    "offending_code": br,
                    "message": f"{self.target_style} requires chunky geometry (0-8px). Found pill utility '{br}'."
                })

        # 2. Shadow Violations
        # Guard: skip CSS custom property *definitions* (e.g. --shadow-sm: ...) to avoid
        # false positives when shadow variable names contain 'shadow-sm/md/lg'.
        # Tailwind utility classes only appear in HTML class="..." or @apply statements,
        # never as property names preceded by '--'.
        is_css_var_definition = bool(re.search(r'--[\w-]*shadow', line))

        zero_blur_styles = [
            "swiss-editorial", "quiet-luxury",
            "bauhaus", "japanese-wabi-sabi", "memphis-postmodern", "retro-americana",
            "terminal-cli", "web-brutalism", "art-deco", "high-fashion-editorial"
            # cyberpunk and vaporwave are EXCLUDED: their specs define neon glow box-shadows (0 0 Npx rgba(cyan))
        ]
        if self.target_style in zero_blur_styles:
            if not is_css_var_definition:
                # Blur shadows (shadow-md, shadow-lg, shadow-xl) are forbidden as Tailwind utilities
                blurry_shadows = re.findall(r'(?<![\w-])(shadow-(?:sm|md|lg|xl|2xl))(?![\w-])', line)
                # Only flag if the match appears inside a class attribute or @apply, not a CSS property name
                blurry_shadows = [b for b in blurry_shadows if not re.search(r'--[\w-]*' + re.escape(b), line)]
                for bs in blurry_shadows:
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "CRITICAL",
                        "type": "shadow_violation",
                        "offending_code": bs,
                        "message": f"Spec for '{self.target_style}' forbids blurry drop shadows. Found '{bs}'."
                    })
            # CSS box-shadow check with blur
            css_shadows = re.findall(r'box-shadow\s*:\s*([^;]+);', line)
            for cs in css_shadows:
                # Skip var(--...) references — they resolve to values defined in :root
                if cs.strip().startswith('var('):
                    continue
                if "rgba" in cs or "px" in cs:
                    # Check if there is a blur radius (3rd length value > 0)
                    parts = cs.strip().split()
                    if len(parts) >= 3 and parts[2] not in ["0", "0px"]:
                        self.violations.append({
                            "file": str(file_path),
                            "line": line_no,
                            "layer": "surfaces",
                            "severity": "CRITICAL",
                            "type": "shadow_violation",
                            "offending_code": f"box-shadow: {cs}",
                            "message": f"Spec for '{self.target_style}' forbids diffuse blur in box-shadow. Found '{cs}'."
                        })

        elif self.target_style in ["neo-brutalism", "maximalist-dopamine"]:
            # Shadows must be hard offset (0 blur). Standard soft Tailwind utilities are forbidden.
            if not is_css_var_definition:
                blurry_shadows = re.findall(r'(?<![\w-])(shadow-(?:sm|md|lg|xl|2xl))(?![\w-])', line)
                blurry_shadows = [b for b in blurry_shadows if not re.search(r'--[\w-]*' + re.escape(b), line)]
                for bs in blurry_shadows:
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "CRITICAL",
                        "type": "shadow_violation",
                        "offending_code": bs,
                        "message": f"{self.target_style} requires hard solid offset shadows (e.g. 4px 4px 0px #000). Found standard blurry shadow."
                    })

        # 3. Border Width Violations
        if self.target_style in ["neo-brutalism", "retro-americana", "maximalist-dopamine"]:
            # These styles require heavy solid borders (2-4px). 1px timid gray borders are forbidden.
            timid_borders = re.findall(r'\b(border-(?:gray|slate|neutral|zinc)-(?:100|200|300))\b', line)
            for tb in timid_borders:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "surfaces",
                    "severity": "CRITICAL",
                    "type": "border_violation",
                    "offending_code": tb,
                    "message": f"{self.target_style} requires heavy solid ink borders (2-4px). Found faint border '{tb}'."
                })

        # 4. Color & Palette Violations
        if self.target_style in ["quiet-luxury", "japanese-wabi-sabi", "organic-natural", "retro-americana"]:
            # Cold gray backgrounds are forbidden in warm natural/earth/linen styles
            cold_grays = re.findall(r'\b(bg-(?:gray|slate|zinc)-(?:50|100|200))\b', line)
            for cg in cold_grays:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "color",
                    "severity": "WARNING",
                    "type": "color_violation",
                    "offending_code": cg,
                    "message": f"{self.target_style} requires warm canvas tones (linen, rice paper, cream, alabaster). Found cold generic gray '{cg}'."
                })
            # Neon or primary bright colors forbidden in quiet/natural styles
            if self.target_style in ["quiet-luxury", "japanese-wabi-sabi", "organic-natural"]:
                neon_accents = re.findall(r'\b((?:bg|text)-(?:blue|indigo|purple|pink|red)-(?:500|600))\b', line)
                for na in neon_accents:
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "color",
                        "severity": "CRITICAL",
                        "type": "color_violation",
                        "offending_code": na,
                        "message": f"{self.target_style} forbids saturated synthetic accents. Found loud accent '{na}'."
                    })

        elif self.target_style in ["cyberpunk", "terminal-cli", "dark-minimal"]:
            # Light mode classes are forbidden
            light_bgs = re.findall(r'\b(bg-(?:white|gray-50|slate-50|neutral-50|amber-50))\b', line)
            for lb in light_bgs:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "color",
                    "severity": "CRITICAL",
                    "type": "color_violation",
                    "offending_code": lb,
                    "message": f"{self.target_style} requires strict dark/obsidian canvas. Found light background '{lb}'."
                })

        elif self.target_style in ["space-age-optimism", "mid-century-modern"]:
            # Pitch dark backgrounds are forbidden — radiant warm white / cream / olive canvas.
            dark_bgs = re.findall(r'\b(bg-(?:black|zinc-950|gray-950|slate-950))\b', line)
            for db in dark_bgs:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "color",
                    "severity": "CRITICAL",
                    "type": "color_violation",
                    "offending_code": db,
                    "message": f"{self.target_style} requires radiant warm light canvas. Found pitch dark background."
                })

        # 5. Typography Substitutions
        if self.target_style in ["quiet-luxury", "swiss-editorial"]:
            # If the file contains headers, check if generic sans is applied where serif/display was mandated
            if "<h1" in line or "<h2" in line or "font-bold" in line:
                if "font-sans" in line and "font-serif" not in line and self.target_style == "quiet-luxury":
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "typography",
                        "severity": "WARNING",
                        "type": "font_substitution",
                        "offending_code": line.strip(),
                        "message": "Quiet Luxury mandates high-contrast editorial serif for primary headings. Found generic sans-serif."
                    })

        # 6. Surface Modifier Auditing
        if "backdrop-blur" in line or "backdrop-filter" in line:
            if self.target_style != "y2k-frutiger-aero" and "frosted-glass" not in self.modifiers:
                # Glassmorphism foundation legitimately uses backdrop-blur — skip flagging it
                if self.target_style not in ["glassmorphism"]:
                    if self.target_style in ["terminal-cli", "web-brutalism", "bauhaus", "swiss-editorial", "retro-americana"]:
                        self.violations.append({
                            "file": str(file_path),
                            "line": line_no,
                            "layer": "surfaces",
                            "severity": "CRITICAL",
                            "type": "unauthorized_modifier",
                            "offending_code": line.strip(),
                            "message": f"Frosted glass / backdrop-blur detected in '{self.target_style}' without declaring 'frosted-glass' modifier."
                        })

        # 7. Corporate Memphis / Alegria Drift Detection (cross-cutting, all styles)
        # Accumulate signal hits per file; severity emitted in _check_corporate_memphis_drift()
        self._memphis_signals.setdefault(str(file_path), [])
        if re.search(r'\b(bg-purple-500|bg-indigo-500|text-purple-600|#6366F1|#8B5CF6)\b', line):
            self._memphis_signals[str(file_path)].append(("purple_accent", line_no))
        if any(k in line for k in ["card", "panel", "container", "section"]):
            if re.search(r'\b(rounded-2xl|rounded-3xl)\b', line):
                self._memphis_signals[str(file_path)].append(("bubbly_container", line_no))
        if re.search(r'(?<![\\w-])(shadow-(?:md|lg|xl|2xl))(?![\\w-])', line):
            self._memphis_signals[str(file_path)].append(("ambient_shadow", line_no))
        if re.search(r'(<!--\s*illustration|blob|organic.shape|bg-blob)', line, re.IGNORECASE):
            self._memphis_signals[str(file_path)].append(("illustration_placeholder", line_no))

    def _check_corporate_memphis_drift(self, file_path: Path):
        """Emit violations if Corporate Memphis signal threshold is reached for a file."""
        signals = self._memphis_signals.get(str(file_path), [])
        signal_types = set(s[0] for s in signals)

        # Style-specific exemptions where elements are spec-mandated:
        # claymorphism: rounded-2xl/3xl (20-32px) is spec-mandated
        if self.target_style == "claymorphism":
            signal_types.discard("bubbly_container")
        # neumorphism: dual soft box-shadow is spec-mandated
        if self.target_style == "neumorphism":
            signal_types.discard("ambient_shadow")

        count = len(signal_types)
        if count >= 3:
            self.violations.append({
                "file": str(file_path),
                "line": 0,
                "layer": "color",
                "severity": "CRITICAL",
                "type": "corporate_memphis_drift",
                "offending_code": ", ".join(signal_types),
                "message": (
                    f"Corporate Memphis / Alegria anti-pattern detected ({count} signals: "
                    f"{', '.join(sorted(signal_types))}). "
                    "This is the AI-generated SaaS default, not an intentional visual direction. "
                    "Apply a foundation style contract via @design-director."
                )
            })
        elif count == 2:
            self.violations.append({
                "file": str(file_path),
                "line": 0,
                "layer": "color",
                "severity": "WARNING",
                "type": "corporate_memphis_drift",
                "offending_code": ", ".join(signal_types),
                "message": (
                    f"Possible Corporate Memphis drift ({count} signals: "
                    f"{', '.join(sorted(signal_types))}). "
                    "Verify the chosen foundation style is intentionally applied."
                )
            })

    def run_audit(self, target_dir: Path) -> dict[str, Any]:
        valid_extensions = [".html", ".jsx", ".tsx", ".vue", ".svelte", ".css"]
        files_scanned = 0
        
        if target_dir.is_file():
            self.audit_file(target_dir)
            files_scanned = 1
        else:
            for root, _, files in os.walk(target_dir):
                for f in files:
                    fp = Path(root) / f
                    if fp.suffix in valid_extensions:
                        self.audit_file(fp)
                        files_scanned += 1

        total_violations = len(self.violations)
        critical_count = sum(1 for v in self.violations if v["severity"] == "CRITICAL")
        warning_count = sum(1 for v in self.violations if v["severity"] == "WARNING")

        # Layer breakdown
        layer_summary: dict[str, int] = {}
        for v in self.violations:
            l = v["layer"]
            layer_summary[l] = layer_summary.get(l, 0) + 1

        # Qualitative adherence status (no artificial numeric score!)
        if critical_count == 0 and warning_count == 0:
            status = "PASSED: Full Spec Adherence"
        elif critical_count == 0:
            status = "PASSED WITH WARNINGS: Minor Stylistic Variances"
        elif critical_count <= 3:
            status = "FAILED: Moderate Spec Deviations"
        else:
            status = "FAILED: Severe Contract Breach"

        return {
            "target_style": self.target_style,
            "files_scanned": files_scanned,
            "status": status,
            "summary": {
                "total_violations": total_violations,
                "critical": critical_count,
                "warnings": warning_count,
                "by_layer": layer_summary
            },
            "violations": self.violations
        }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Design Audit Static Analysis Engine")
    parser.add_argument("style_id", help="Target design style ID (e.g. minimal-modern)")
    parser.add_argument("target", help="Target directory or file to audit")
    parser.add_argument("--modifiers", "-m", help="Comma-separated list of active modifiers (e.g. frosted-glass,subtle-grain)", default="")
    args = parser.parse_args()

    mods = [m.strip() for m in args.modifiers.split(",") if m.strip()]
    auditor = DesignAuditor(args.style_id, modifiers=mods)
    report = auditor.run_audit(Path(args.target))
    print(json.dumps(report, indent=2))
