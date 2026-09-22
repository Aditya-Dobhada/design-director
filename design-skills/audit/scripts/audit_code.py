"""
Design Audit Static Analysis Engine
Scans frontend source code against a target Design Spec and reports violations
across layout, typography, surfaces (borders, radius, shadows), color, and motion.
"""

import sys
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

class DesignAuditor:
    def __init__(self, target_style: str):
        self.target_style = target_style.lower()
        self.violations: List[Dict[str, Any]] = []

    def audit_file(self, file_path: Path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            return

        for idx, line in enumerate(lines, 1):
            self._check_line(file_path, idx, line)

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
            "retro-americana", "japanese-wabi-sabi", "memphis-postmodern"
        ]
        if self.target_style in sharp_radius_styles:
            # Spec requires 0px (rounded-none). Any rounded-md, rounded-lg, rounded-full, rounded-2xl is a violation (unless full is on an explicit circle medallion for bauhaus/memphis).
            bad_radii = re.findall(r'\b(rounded-(?:md|lg|xl|2xl|3xl|full))\b', line)
            for br in bad_radii:
                # Allow rounded-full only if on a tiny circle medallion or icon
                if br == "rounded-full" and any(k in line for k in ["w-4", "h-4", "w-6", "h-6", "w-8", "h-8", "w-12", "h-12", "circle"]):
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
                if val not in ["0", "0px", "none"] and not ("50%" in val and self.target_style in ["bauhaus", "memphis-postmodern"]):
                    self.violations.append({
                        "file": str(file_path),
                        "line": line_no,
                        "layer": "surfaces",
                        "severity": "CRITICAL",
                        "type": "radius_violation",
                        "offending_code": f"border-radius: {cr}",
                        "message": f"Spec for '{self.target_style}' requires 0px border-radius. Found '{val}'."
                    })

        elif self.target_style in ["space-age-optimism", "organic-natural", "y2k-frutiger-aero"]:
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
            "bauhaus", "japanese-wabi-sabi", "memphis-postmodern", "retro-americana"
            # cyberpunk is EXCLUDED: its spec defines neon glow box-shadows (0 0 Npx rgba(cyan)) as correct idiom
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

        elif self.target_style in ["cyberpunk"]:
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
                    "message": f"Cyberpunk requires 100% dark mode / obsidian canvas. Found light background '{lb}'."
                })

        elif self.target_style in ["space-age-optimism"]:
            # Pitch dark backgrounds forbidden — space age is radiant warm white
            dark_bgs = re.findall(r'\b(bg-(?:black|zinc-950|gray-950|slate-950))\b', line)
            for db in dark_bgs:
                self.violations.append({
                    "file": str(file_path),
                    "line": line_no,
                    "layer": "color",
                    "severity": "CRITICAL",
                    "type": "color_violation",
                    "offending_code": db,
                    "message": "Space Age Optimism requires radiant warm white / chrome canvas. Found dark background."
                })
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
                    "message": f"Cyberpunk requires 100% dark mode / obsidian canvas. Found light background '{lb}'."
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

    def run_audit(self, target_dir: Path) -> Dict[str, Any]:
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
        layer_summary: Dict[str, int] = {}
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
    if len(sys.argv) < 3:
        print("Usage: python audit_code.py <style_id> <target_directory_or_file>")
        sys.exit(1)

    style = sys.argv[1]
    target = Path(sys.argv[2])
    auditor = DesignAuditor(style)
    report = auditor.run_audit(target)
    print(json.dumps(report, indent=2))
