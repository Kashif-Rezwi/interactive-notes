#!/usr/bin/env python3
"""Learning OS HTML candidate verifier (ADR-0012).

Read-only, offline, deterministic verification tool for generated interactive
lesson HTML candidates. Validates mechanical constraints and syntax invariants
stipulated by the lesson standard (docs/01-product/lesson-standard.md) and
the quality QA checklist (library/rubrics/lesson-qa-checklist.md).

Usage:  python3 scripts/verify-candidate.py <path/to/candidate.html>
Exit:   0 = clean pass (informational notes allowed), 1 = at least one failure.
Needs:  Python 3.8+ standard library only. Zero dependencies, zero network access.
"""

import html.parser
import os
import re
import sys
from pathlib import Path

FAILURES = []
NOTES = []
METRICS = {}


def fail(msg: str) -> None:
    FAILURES.append(msg)


def note(msg: str) -> None:
    NOTES.append(msg)


class CandidateHTMLParser(html.parser.HTMLParser):
    """Custom parser to gather IDs, tags, attributes, and check tag balancing."""

    def __init__(self):
        super().__init__()
        self.ids = []
        self.tag_stack = []
        self.interactive_elements = {
            "canvas": 0,
            "button": 0,
            "input": 0,
            "select": 0,
            "details": 0,
            "script": 0,
            "style": 0,
            "textarea": 0,
        }
        self.textareas = []
        self.data_targets = []
        self.external_refs = []
        self.void_tags = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"
        }

    def handle_starttag(self, tag: str, attrs: list):
        attr_dict = dict(attrs)
        tag_lower = tag.lower()

        if tag_lower in self.interactive_elements:
            self.interactive_elements[tag_lower] += 1

        if tag_lower == "textarea":
            self.textareas.append(attr_dict.get("id", "unnamed"))

        if tag_lower not in self.void_tags:
            self.tag_stack.append(tag_lower)

        # 1. ID tracking
        if "id" in attr_dict:
            elem_id = attr_dict["id"].strip()
            if elem_id:
                self.ids.append(elem_id)

        # 2. Data wiring targets
        for k, v in attr_dict.items():
            if k.startswith("data-target") or k in ("data-gate-target", "data-ladder-target", "aria-controls"):
                if v:
                    self.data_targets.append((k, v.strip()))

        # 3. External references check
        for k in ("src", "href", "action", "data"):
            val = attr_dict.get(k, "")
            if val.startswith(("http://", "https://", "//", "ftp://")):
                self.external_refs.append((tag_lower, k, val))

    def handle_endtag(self, tag: str):
        tag_lower = tag.lower()
        if tag_lower in self.void_tags:
            return

        if self.tag_stack and self.tag_stack[-1] == tag_lower:
            self.tag_stack.pop()
        else:
            if tag_lower in self.tag_stack:
                while self.tag_stack and self.tag_stack[-1] != tag_lower:
                    unclosed = self.tag_stack.pop()
                    note(f"structure: auto-closed tag <{unclosed}> before closing </{tag_lower}>")
                if self.tag_stack:
                    self.tag_stack.pop()
            else:
                note(f"structure: closing tag </{tag_lower}> without matching open tag")


def check_provenance_header(content: str) -> None:
    """Verify governed provenance HTML comment exists at top of file."""
    first_chunk = content[:2000]
    prov_match = re.search(r"<!--\s*(?:candidate|artifact|run|source|provenance):.*?-->", first_chunk, re.DOTALL | re.IGNORECASE)
    if not prov_match and "candidate: CAN-" not in first_chunk:
        fail("provenance: candidate missing governed provenance HTML comment at start of file")
    else:
        note("provenance: governed provenance comment header found")


def check_standard_colophon(content: str) -> None:
    """Verify standard colophon closes the artifact without external banners."""
    colophon_match = re.search(r'<footer[^>]*class=["\'][^"\']*colophon[^"\']*["\']', content, re.IGNORECASE)
    has_honesty_text = any(phrase in content for phrase in [
        "AI-generated, so mistakes can sneak in",
        "AI-assisted",
        "Interactive Notes",
        "Learning OS"
    ])
    if not colophon_match or not has_honesty_text:
        fail("colophon: standard colophon (<footer class=\"colophon\">) / AI-honesty statement not found in document")
    else:
        note("colophon: standard colophon presence verified")


def check_external_dependencies(content: str, parser: CandidateHTMLParser) -> None:
    """Verify zero external resource requests (scripts, styles, fonts, CDN)."""
    for tag, attr, url in parser.external_refs:
        # Ignore external markdown/citation links in anchor tags
        if tag == "a" and attr == "href":
            continue
        fail(f"zero-dependency: external URL detected in <{tag} {attr}=\"{url}\">")

    # Check CSS @import and url()
    css_imports = re.findall(r"@import\s+['\"](https?://[^'\"]+)['\"]", content, re.IGNORECASE)
    css_urls = re.findall(r"url\s*\(\s*['\"]?(https?://[^'\")]+)['\"]?\s*\)", content, re.IGNORECASE)
    for u in css_imports + css_urls:
        fail(f"zero-dependency: external CSS reference detected: {u}")


def check_duplicate_ids(parser: CandidateHTMLParser) -> None:
    """Verify all element IDs in HTML are globally unique."""
    seen = set()
    duplicates = set()
    for elem_id in parser.ids:
        if elem_id in seen:
            duplicates.add(elem_id)
        seen.add(elem_id)

    if duplicates:
        for dup in sorted(duplicates):
            fail(f"dom-integrity: duplicate element ID found: #{dup}")
    else:
        METRICS["unique_ids"] = len(seen)


def check_data_wiring(parser: CandidateHTMLParser) -> None:
    """Verify data-target / aria-controls target IDs actually exist in DOM."""
    id_set = set(parser.ids)
    missing_targets = set()
    for attr, target in parser.data_targets:
        for tid in target.split():
            tid = tid.lstrip("#")
            if tid and tid not in id_set:
                missing_targets.add((attr, tid))

    if missing_targets:
        for attr, tid in sorted(missing_targets):
            fail(f"wiring: {attr}=\"{tid}\" targets nonexistent ID #{tid}")


def check_glossary_structure(content: str) -> None:
    """Verify glossary presence and measure its richness."""
    has_glossary_section = bool(re.search(r'<section[^>]*id=["\']glossary["\']', content, re.IGNORECASE))
    gitem_count = len(re.findall(r'class=["\'][^"\']*gitem[^"\']*["\']', content, re.IGNORECASE))
    dt_count = len(re.findall(r'<dt\b', content, re.IGNORECASE))
    data_terms = len(re.findall(r'\{\s*(?:term|name)\s*:\s*["\']', content, re.IGNORECASE))
    
    total_terms = max(gitem_count, dt_count, data_terms)
    if not has_glossary_section and total_terms == 0:
        fail("glossary: no glossary section or glossary data structures detected")
    else:
        METRICS["glossary_terms"] = total_terms
        note(f"glossary: detected ~{total_terms} terms")


def check_interactive_density(parser: CandidateHTMLParser, content: str) -> None:
    """Record interactive elements count and verify minimum interactive density."""
    METRICS["canvases"] = parser.interactive_elements["canvas"]
    METRICS["buttons"] = parser.interactive_elements["button"]
    METRICS["inputs"] = parser.interactive_elements["input"]
    METRICS["scripts"] = parser.interactive_elements["script"]
    METRICS["textareas"] = parser.interactive_elements["textarea"]

    gate_matches = len(re.findall(r'class=["\'][^"\']*(?:gate|predict|prediction)[^"\']*["\']', content, re.IGNORECASE))
    ladder_matches = len(re.findall(r'class=["\'][^"\']*(?:ladder|step-ladder|faded)[^"\']*["\']', content, re.IGNORECASE))

    METRICS["prediction_gates"] = gate_matches
    METRICS["faded_ladders"] = ladder_matches

    if METRICS["canvases"] == 0 and METRICS["inputs"] == 0 and METRICS["buttons"] == 0:
        fail("interactivity: zero canvas, input, or button elements found; lesson appears non-interactive")


def check_forbidden_inputs(parser: CandidateHTMLParser, is_strict: bool) -> None:
    """Check for forbidden open textarea inputs in assessment/check units (standard §1.4)."""
    if parser.textareas:
        msg = f"modality: {len(parser.textareas)} <textarea> element(s) detected ({', '.join(parser.textareas)}); open text fields forbidden in checks; use diagnostic MCQs, interactive visual widgets, or bounded numeric inputs (standard §1.4)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")


def check_slider_architecture(content: str, is_strict: bool) -> None:
    """Verify range inputs are wrapped in atomic .slider-control with tabular .slider-val (standard §10.6)."""
    has_range_input = bool(re.search(r'<input[^>]*type=["\']range["\']', content, re.IGNORECASE))
    if not has_range_input:
        return

    has_slider_control = ".slider-control" in content
    has_tabular_nums = "tabular-nums" in content
    has_ctrl_grid = ".ctrl-grid" in content

    if not has_slider_control or not has_tabular_nums:
        msg = "slider-layout: range inputs found without atomic .slider-control encapsulation and font-variant-numeric: tabular-nums (standard §10.6)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")
    else:
        note("slider-layout: atomic .slider-control and tabular numeric styling verified")


def check_option_stack_architecture(content: str, is_strict: bool) -> None:
    """Verify radio/checkbox option groups use vertical .option-stack and .option-item (standard §10.7)."""
    has_radio_predict = bool(re.search(r'class=["\'][^"\']*predict[^"\']*["\'][^>]*>.*?<input[^>]*type=["\']radio["\']', content, re.DOTALL | re.IGNORECASE))
    if not has_radio_predict:
        return

    has_option_stack = ".option-stack" in content
    has_option_item = ".option-item" in content

    if not has_option_stack or not has_option_item:
        msg = "option-layout: radio/checkbox options in .predict or .check missing .option-stack and .option-item vertical card wrappers (standard §10.7)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")
    else:
        note("option-layout: vertical .option-stack and .option-item verified")


def check_formula_completeness(content: str) -> None:
    """Verify presence of .formula blocks with annotated .symkey symbol keys (standard §1.1)."""
    formula_count = len(re.findall(r'class=["\'][^"\']*formula[^"\']*["\']', content, re.IGNORECASE))
    symkey_count = len(re.findall(r'class=["\'][^"\']*symkey[^"\']*["\']', content, re.IGNORECASE))
    METRICS["formulas"] = formula_count
    METRICS["symkeys"] = symkey_count

    if formula_count == 0:
        note("formula: zero .formula blocks detected (standard §1.1 requires keyed formulas for math/quantitative concepts)")
    else:
        note(f"formula: detected {formula_count} .formula blocks with {symkey_count} symbol keys")


def check_callout_density(content: str, is_strict: bool) -> None:
    """Verify callout discipline: at most 1 .callout block per unit section (standard §10.8)."""
    unit_sections = re.findall(r'<section[^>]*class=["\'][^"\']*unit[^"\']*["\'][^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    over_limit = []
    for idx, sec in enumerate(unit_sections, start=1):
        callout_count = len(re.findall(r'class=["\'][^"\']*callout[^"\']*["\']', sec, re.IGNORECASE))
        if callout_count > 1:
            id_match = re.search(r'id=["\']([^"\']+)["\']', sec[:100])
            sec_id = id_match.group(1) if id_match else f"unit-{idx}"
            over_limit.append((sec_id, callout_count))

    if over_limit:
        msg = f"callout-density: {len(over_limit)} unit(s) exceed limit of 1 .callout per unit ({', '.join(f'#{u}: {c}' for u, c in over_limit)}); integrate misconceptions directly into prose or MCQ feedback (standard §10.8)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")
    else:
        note("callout-density: callout discipline verified (<= 1 per unit)")


def check_slider_encapsulation_per_element(content: str, is_strict: bool) -> None:
    """Verify per-element §10.6: every range input sits inside a .slider-track wrapper.

    Presence-only checks (class names exist somewhere) cannot detect partially
    conformant artifacts; this counts range inputs vs .slider-track wrappers
    (standard §10.6: every slider MUST be structurally encapsulated).
    Added 2026-09-04 after RUN-20260904-0001 found 15 of 22 range inputs in the
    legacy `.ctrl` layout in the otherwise-clean CAN-2026-0008 (v9) reference.
    """
    range_inputs = re.findall(r'<input[^>]*type=["\']range["\']', content, re.IGNORECASE)
    if not range_inputs:
        return
    tracks = re.findall(r'<div[^>]*class=["\'][^"\']*slider-track[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL | re.IGNORECASE)
    wrapped = sum(1 for t in tracks if re.search(r'<input[^>]*type=["\']range["\']', t, re.IGNORECASE))
    total = len(range_inputs)
    if wrapped != total:
        msg = f"slider-encapsulation: {total - wrapped} of {total} range input(s) are NOT wrapped in .slider-track inside .slider-control (standard §10.6 requires per-element encapsulation)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")
    else:
        note(f"slider-encapsulation: all {total} range inputs verified inside .slider-track wrappers (per-element)")


def _strip_print_blocks(css: str) -> str:
    """Remove @media print blocks (balanced-brace aware) from a stylesheet string."""
    out = []
    i = 0
    lowered = css.lower()
    while True:
        j = lowered.find("@media print", i)
        if j == -1:
            out.append(css[i:])
            break
        out.append(css[i:j])
        k = css.find("{", j)
        if k == -1:
            out.append(css[j:])
            break
        depth = 1
        p = k + 1
        while p < len(css) and depth > 0:
            if css[p] == "{":
                depth += 1
            elif css[p] == "}":
                depth -= 1
            p += 1
        i = p
    return "".join(out)


def check_body_font_floor(content: str, is_strict: bool) -> None:
    """Verify §10.1: every body font-size declaration on screen (including width
    media queries) is >= 16px. Print stylesheets are exempt: §10.1 governs the
    learner-facing screen rendering path ("at all breakpoints" = screen widths);
    print fallbacks conventionally reduce size for paper.

    Base-rule-only checks miss small-screen overrides; this scans all
    `body{...font-size:...px}` declarations outside @media print blocks.
    Added 2026-09-04 after RUN-20260904-0001 found a `@media (max-width:640px)
    {body{font-size:15.5px}}` override in the CAN-2026-0008 (v9) reference.
    """
    screen_css = _strip_print_blocks(content)
    declarations = re.findall(r'body\s*\{[^}]*font-size\s*:\s*([\d.]+)px', screen_css, re.IGNORECASE)
    violations = [d for d in declarations if float(d) < 16.0]
    if violations:
        msg = f"font-floor: body font-size below the 16px floor in {len(violations)} declaration(s) ({', '.join(violations + ['px'])} — standard §10.1 applies at ALL breakpoints, media queries included)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")
    else:
        note(f"font-floor: all {len(declarations)} body font-size declaration(s) >= 16px")


def check_jargon_and_glossary_resolution(content: str, parser: CandidateHTMLParser, is_strict: bool) -> None:
    """Verify zero deferred jargon cop-outs and confirm all .gterm targets exist (standard §1.4)."""
    deferral_patterns = [
        r"words belong to a later course",
        r"promise for a later course",
        r"a later course makes this precise"
    ]
    found_deferrals = []
    for pat in deferral_patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        if matches:
            found_deferrals.extend(matches)

    if found_deferrals:
        msg = f"jargon: {len(found_deferrals)} deferred domain term cop-out(s) detected ({', '.join(set(found_deferrals))}); domain terms must be defined immediately or omitted from main path (standard §1.4)"
        if is_strict:
            fail(msg)
        else:
            note(f"[LEGACY] {msg}")

    # Check that in-text gterms resolve
    gterm_targets = re.findall(r'data-term=["\']([^"\']+)["\']', content)
    id_set = set(parser.ids)
    missing_gterms = [t for t in set(gterm_targets) if t not in id_set]
    if missing_gterms:
        fail(f"glossary: data-term targets nonexistent glossary element: {', '.join(missing_gterms)}")


def verify_file(filepath: Path, force_strict: bool = False) -> int:
    if not filepath.exists() or not filepath.is_file():
        print(f"[FAIL] Candidate file not found: {filepath}")
        return 1

    content = filepath.read_text(encoding="utf-8")
    METRICS["file_bytes"] = len(content.encode("utf-8"))
    METRICS["file_lines"] = len(content.splitlines())

    # Detect if candidate was generated under prompt @0.6.0+ or forced strict
    is_v6 = "@0.6.0" in content or "prm-generator-lesson-standard@0.6" in content
    is_strict = force_strict or is_v6

    parser = CandidateHTMLParser()
    try:
        parser.feed(content)
        parser.close()
    except Exception as e:
        fail(f"html-parse: malformed HTML structure: {e}")

    # Run check suite
    check_provenance_header(content)
    check_standard_colophon(content)
    check_external_dependencies(content, parser)
    check_duplicate_ids(parser)
    check_data_wiring(parser)
    check_glossary_structure(content)
    check_interactive_density(parser, content)
    check_forbidden_inputs(parser, is_strict)
    check_slider_architecture(content, is_strict)
    check_slider_encapsulation_per_element(content, is_strict)
    check_body_font_floor(content, is_strict)
    check_option_stack_architecture(content, is_strict)
    check_formula_completeness(content)
    check_callout_density(content, is_strict)
    check_jargon_and_glossary_resolution(content, parser, is_strict)

    # Print Report
    mode_str = "STRICT (v0.6.0 contract)" if is_strict else "COMPATIBILITY (legacy)"
    print(f"=== Verification Report: {filepath.name} [{mode_str}] ===")
    print(f"Size: {METRICS['file_bytes']:,} bytes | Lines: {METRICS['file_lines']:,} | Unique IDs: {METRICS.get('unique_ids', 0)}")
    print(f"Elements: {METRICS['canvases']} canvases, {METRICS['buttons']} buttons, {METRICS['inputs']} inputs, {METRICS.get('textareas', 0)} textareas, {METRICS['scripts']} scripts")
    print(f"Structures: ~{METRICS.get('glossary_terms', 0)} glossary entries, {METRICS.get('prediction_gates', 0)} gates, {METRICS.get('faded_ladders', 0)} ladders, {METRICS.get('formulas', 0)} formulas")
    print("-" * 50)

    for n in NOTES:
        print(f"[NOTE] {n}")

    for f in FAILURES:
        print(f"[FAIL] {f}")

    if FAILURES:
        print(f"\nResult: FAILED ({len(FAILURES)} failure(s), {len(NOTES)} note(s))")
        return 1
    else:
        print(f"\nResult: PASSED (0 failures, {len(NOTES)} note(s))")
        return 0


def main():
    args = [a for a in sys.argv[1:] if a != "--strict"]
    force_strict = "--strict" in sys.argv[1:]

    if not args:
        print("Usage: python3 scripts/verify-candidate.py [--strict] <path/to/candidate.html>")
        return 1

    target = Path(args[0]).resolve()
    return verify_file(target, force_strict=force_strict)


if __name__ == "__main__":
    sys.exit(main())

