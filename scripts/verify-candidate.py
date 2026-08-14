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
        }
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

    gate_matches = len(re.findall(r'class=["\'][^"\']*(?:gate|predict|prediction)[^"\']*["\']', content, re.IGNORECASE))
    ladder_matches = len(re.findall(r'class=["\'][^"\']*(?:ladder|step-ladder|faded)[^"\']*["\']', content, re.IGNORECASE))

    METRICS["prediction_gates"] = gate_matches
    METRICS["faded_ladders"] = ladder_matches

    if METRICS["canvases"] == 0 and METRICS["inputs"] == 0 and METRICS["buttons"] == 0:
        fail("interactivity: zero canvas, input, or button elements found; lesson appears non-interactive")


def verify_file(filepath: Path) -> int:
    if not filepath.exists() or not filepath.is_file():
        print(f"[FAIL] Candidate file not found: {filepath}")
        return 1

    content = filepath.read_text(encoding="utf-8")
    METRICS["file_bytes"] = len(content.encode("utf-8"))
    METRICS["file_lines"] = len(content.splitlines())

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

    # Print Report
    print(f"=== Verification Report: {filepath.name} ===")
    print(f"Size: {METRICS['file_bytes']:,} bytes | Lines: {METRICS['file_lines']:,} | Unique IDs: {METRICS.get('unique_ids', 0)}")
    print(f"Elements: {METRICS['canvases']} canvases, {METRICS['buttons']} buttons, {METRICS['inputs']} inputs, {METRICS['scripts']} scripts")
    print(f"Structures: ~{METRICS.get('glossary_terms', 0)} glossary entries, {METRICS.get('prediction_gates', 0)} gates, {METRICS.get('faded_ladders', 0)} ladders")
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
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/verify-candidate.py <path/to/candidate.html>")
        return 1

    target = Path(sys.argv[1]).resolve()
    return verify_file(target)


if __name__ == "__main__":
    sys.exit(main())
