#!/usr/bin/env python3
"""
CLI entry point for Design Director
Supports:
  design analyze [prd_file]
  design recommend [brief_file]
  design choose <style_id>
  design refine "<free-text critique>"
  design implement [spec_file] [product_spec_file]
  design audit <style_id> <target_path>
"""

import sys
import os
import json
import yaml
from pathlib import Path

# Add project root and director to sys.path
BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "design-skills" / "director"))
sys.path.insert(0, str(BASE_DIR / "design-skills" / "audit" / "scripts"))

from director_engine import (
    extract_design_brief,
    recommend_styles,
    create_design_spec,
    refine_spec,
    generate_implementation_contract,
    find_reference
)
from audit_code import DesignAuditor

STATE_FILE = BASE_DIR / ".design_state.json"

def save_state(key: str, data: any):
    state = {}
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except Exception:
            state = {}
    state[key] = data
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def load_state(key: str, default=None):
    if not STATE_FILE.exists():
        return default
    try:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
            return state.get(key, default)
    except Exception:
        return default

def cmd_analyze(args):
    prd_path = Path(args[0]) if args else (BASE_DIR / "PRD.md")
    if not prd_path.exists():
        print(f"Error: PRD file not found at {prd_path}", file=sys.stderr)
        sys.exit(1)
    with open(prd_path, "r", encoding="utf-8") as f:
        text = f.read()
    brief = extract_design_brief(text)
    save_state("current_brief", brief)
    print("### DESIGN BRIEF EXTRACTED")
    print(yaml.dump(brief, sort_keys=False))

def cmd_recommend(args):
    brief = load_state("current_brief")
    if not brief:
        # Try reading PRD.md directly
        prd_path = BASE_DIR / "PRD.md"
        if prd_path.exists():
            with open(prd_path, "r", encoding="utf-8") as f:
                brief = extract_design_brief(f.read())
        else:
            print("Error: No Design Brief found. Run '/design analyze' first.", file=sys.stderr)
            sys.exit(1)
    recs = recommend_styles(brief)
    save_state("current_recommendations", recs)
    print("### RECOMMENDED DESIGN DIRECTIONS\n")
    for r in recs:
        print(f"#### {r['name']} (`{r['style_id']}`)")
        print(f"- **Fit Rating:** {r['fit_rating']}")
        print(f"- **Reasoning:** {r['reasoning']}")
        print("- **Tradeoffs & Risks:**")
        for t in r["tradeoffs"]:
            print(f"  - {t}")
        print()

def cmd_choose(args):
    if not args:
        print("Usage: /design choose <style_id> (e.g. quiet-luxury, swiss-editorial, neo-brutalism, cyberpunk, y2k-frutiger-aero)")
        sys.exit(1)
    style_id = args[0].strip().lower()
    spec = create_design_spec(style_id)
    save_state("current_spec", spec)
    print(f"### DESIGN SPEC INITIALIZED: `{style_id}`\n")
    print(yaml.dump(spec, sort_keys=False))

def cmd_refine(args):
    if not args:
        print("Usage: /design refine \"<critique>\" (e.g. 'more like Linear, less like a bank')")
        sys.exit(1)
    critique = " ".join(args)
    spec = load_state("current_spec")
    if not spec:
        # Default to swiss-editorial if no spec was explicitly chosen yet
        spec = create_design_spec("swiss-editorial")

    refinement = refine_spec(spec, critique)
    updated_spec = refinement["updated_spec"]
    diff = refinement["diff_report"]
    save_state("current_spec", updated_spec)

    print("### DESIGN SPEC REFINEMENT REPORT\n")
    print(f"**Critique Received:** \"{diff['critique_received']}\"\n")
    print(f"**Layers Updated:** {diff['layers_changed_count']}")
    for c in diff["changes"]:
        print(f"- **{c['layer']}**: {c['reason']} (`{c['old']}` -> `{c['new']}`)")
    print(f"\n**Stable Layers Preserved:** {diff['layers_preserved_count']} ({', '.join(diff['stable_layers'])})")
    print("\n#### Current Resolved Spec:")
    print(yaml.dump(updated_spec, sort_keys=False))

def cmd_implement(args):
    spec = load_state("current_spec")
    if not spec:
        print("Error: No Design Spec found. Run '/design choose <style>' first.", file=sys.stderr)
        sys.exit(1)
    
    product_spec = "Implement the core application views matching product requirements."
    if args and Path(args[0]).exists():
        with open(args[0], "r", encoding="utf-8") as f:
            product_spec = f.read()
    elif (BASE_DIR / "PRD.md").exists():
        with open(BASE_DIR / "PRD.md", "r", encoding="utf-8") as f:
            product_spec = f.read()

    contract = generate_implementation_contract(spec, product_spec)
    contract_file = BASE_DIR / "DESIGN_CONTRACT.md"
    with open(contract_file, "w", encoding="utf-8") as f:
        f.write(contract)
    print(f"Implementation contract successfully written to: {contract_file}")
    print("\n--- CONTRACT PREVIEW ---\n")
    print(contract[:1000] + "\n...[truncated]...")

def cmd_audit(args):
    if not args:
        print("Usage: /design audit <style_id> [target_path]")
        sys.exit(1)
    style_id = args[0]
    target_path = Path(args[1]) if len(args) > 1 else BASE_DIR
    auditor = DesignAuditor(style_id)
    report = auditor.run_audit(target_path)
    print(json.dumps(report, indent=2))

def main():
    if len(sys.argv) < 2:
        print("Usage: design <command> [args...]")
        print("Commands: analyze, recommend, choose, refine, implement, audit")
        sys.exit(1)

    cmd = sys.argv[1].lower().replace("/design", "").replace("design:", "").strip()
    if cmd.startswith("/"):
        cmd = cmd[1:]
    args = sys.argv[2:]

    dispatch = {
        "analyze": cmd_analyze,
        "recommend": cmd_recommend,
        "choose": cmd_choose,
        "refine": cmd_refine,
        "implement": cmd_implement,
        "audit": cmd_audit
    }

    if cmd in dispatch:
        dispatch[cmd](args)
    else:
        print(f"Unknown command: '{cmd}'. Available: {list(dispatch.keys())}")
        sys.exit(1)

if __name__ == "__main__":
    main()
