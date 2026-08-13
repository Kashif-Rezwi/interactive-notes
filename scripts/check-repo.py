#!/usr/bin/env python3
"""Learning OS repository checker (ADR-0008).

Read-only, offline, deterministic hygiene checks over this governance
repository. The checker asserts conventions that are already written down;
it never introduces rules, never modifies files, and never executes or
scores learner artifacts (that remains human/agent and Stage 2 harness work).

Usage:  python3 scripts/check-repo.py
Exit:   0 = clean (notes allowed), 1 = at least one failure.
Needs:  Python 3.8+ standard library only. No network, no installs.
"""

import hashlib
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILURES = []
NOTES = []

LINK_RE = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")
HEX_RE = re.compile(r"\b[0-9a-f]{64}\b")
KEBAB_MD_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")
GENERATED_RE = re.compile(r"^[a-z0-9][a-z0-9-]*-v\d+\.[a-z0-9]+$")


def fail(msg):
    FAILURES.append(msg)


def note(msg):
    NOTES.append(msg)


def md_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def content_files():
    base = ROOT / "content"
    if not base.exists():
        return []
    return sorted(p for p in base.rglob("*") if p.is_file() and p.suffix != ".md")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


# --- 1. Links: every relative Markdown link resolves (ADR-0001 evidence rule)
def check_links():
    total = 0
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            if raw.startswith(("http://", "https://", "mailto:")):
                continue
            total += 1
            target = (f.parent / urllib.parse.unquote(raw)).resolve()
            if not target.exists():
                fail("links: %s -> %s does not resolve" % (rel(f), raw))
    return "%d relative links across %d markdown files" % (total, len(md_files()))


# --- 2. Hashes: provenance coverage + manifest accuracy (content-package convention)
def check_hashes():
    files = content_files()
    corpus = "\n".join(f.read_text(encoding="utf-8") for f in md_files())
    claimed = set(HEX_RE.findall(corpus))
    for f in files:
        if sha256(f) not in claimed:
            fail("hashes: %s has no provenance; its SHA-256 appears in no markdown record" % rel(f))
    checked = 0
    src_dir = ROOT / "records" / "sources"
    manifests = sorted(src_dir.glob("*.md")) if src_dir.exists() else []
    for m in manifests:
        if m.name == "README.md":
            continue
        text = m.read_text(encoding="utf-8")
        hashes = set(HEX_RE.findall(text))
        for raw in LINK_RE.findall(text):
            target = (m.parent / urllib.parse.unquote(raw)).resolve()
            inside_content = str(target).startswith(str(ROOT / "content"))
            if target.exists() and target.is_file() and inside_content and target.suffix != ".md":
                checked += 1
                if sha256(target) not in hashes:
                    fail("hashes: manifest %s links %s but does not declare its current SHA-256"
                         % (m.name, target.name))
    return "%d content files provenance-covered; %d manifest file links hash-verified" % (len(files), checked)


# --- 3. Weights: dimension weights sum to 100 and match the Total row (ADR-0007)
def check_weights():
    fw_path = ROOT / "docs" / "06-evaluation" / "evaluation-framework.md"
    fw = fw_path.read_text(encoding="utf-8")
    weights = [int(m) for m in re.findall(r"\n\| [^|]+ \| [^|]+ \| (\d+)% \|", fw)]
    if not weights:
        fail("weights: no dimension weights parsed from evaluation-framework.md")
        return "parse failure"
    total = sum(weights)
    if total != 100:
        fail("weights: dimension weights sum to %d, must be exactly 100 (weight-integrity rule)" % total)
    total_row = re.search(r"\*\*Total\*\* \|  \| \*\*(\d+)%\*\*", fw)
    if total_row and int(total_row.group(1)) != total:
        fail("weights: Total row claims %s%% but dimensions sum to %d" % (total_row.group(1), total))
    return "%d dimension weights sum to %d" % (len(weights), total)

# --- 4. Status vocabularies: controlled values per record type (ADR-0007)
RUN_STATES = {"Planned", "Generating", "Evaluating", "Reflecting", "Revising",
              "Validated", "Released", "Pilot complete", "Stopped", "Failed", "Blocked"}
VOCAB = {
    "records/runs": ("Status", RUN_STATES),
    "records/concepts": ("Status", {"Draft", "Reviewed", "Superseded"}),
    "records/plans": ("Status", {"Draft", "Reviewed", "Superseded"}),
    "records/specifications": ("Status", {"Draft", "Approved", "Superseded"}),
    "records/memory": ("Status|Confidence", {"Tentative", "Supported", "Established", "Disputed", "Retired"}),
    "records/sources": ("Status", {"Draft", "Recorded", "Superseded", "Retired"}),
}
# ADR-0007 section 5 declared equivalences: pre-2026-08-13 records keep their
# historical values (append-only). This list is the machine-readable form of
# that declaration and grows only through an ADR-level equivalence.
GRANDFATHERED = {
    "records/runs/run-20260804-0002-linear-algebra-cross-model.md",
    "records/runs/run-20260810-0001-linear-algebra-foundations-v4.md",
    "records/specifications/xs-2026-0001-linear-algebra-foundations-v2.md",
    "records/specifications/xs-2026-0002-linear-algebra-foundations-v4.md",
}


def check_status_vocabularies():
    checked = 0
    for subdir, (field, allowed) in sorted(VOCAB.items()):
        base = ROOT / subdir
        if not base.exists():
            continue
        for f in sorted(base.glob("*.md")):
            if f.name == "README.md":
                continue
            key = rel(f)
            if key in GRANDFATHERED:
                note("status: %s keeps its pre-ADR-0007 historical value (declared equivalence)" % f.name)
                continue
            text = f.read_text(encoding="utf-8")
            m = re.search(r"^\*\*(?:%s):\*\*\s*(.+?)\s*(?:<br>|$)" % field, text, re.M)
            if not m:
                fail("status: %s has no **%s:** header field" % (key, field.replace("|", ":** / **")))
                continue
            value = m.group(1).strip()
            checked += 1
            if value not in allowed:
                fail("status: %s uses %r, not in the controlled vocabulary %s (ADR-0007)"
                     % (key, value, sorted(allowed)))
    return "%d records carry controlled status values" % checked


# --- 5. README metadata: inheritance declarations present (documentation standard)
def check_readme_metadata():
    targets = [ROOT / "docs" / "README.md"]
    targets += sorted(p for p in ROOT.glob("docs/*/README.md") if p.parent.name[0].isdigit())
    for f in targets:
        text = f.read_text(encoding="utf-8")
        for field in ("**Status:**", "**Owner:**", "**Review by:**", "**Applies to:**"):
            if field not in text:
                fail("metadata: %s is missing %s" % (rel(f), field))
    return "%d docs READMEs declare Status/Owner/Review-by/Applies-to" % len(targets)


# --- 6. Filenames: kebab-case records; <note-slug>-v<N> generated artifacts
def check_filenames():
    records = ROOT / "records"
    rec_count = 0
    if records.exists():
        for p in records.rglob("*.md"):
            if p.name == "README.md":
                continue
            rec_count += 1
            if not KEBAB_MD_RE.match(p.name):
                fail("filenames: %s is not lowercase kebab-case (naming conventions)" % rel(p))
    gen_count = 0
    for p in content_files():
        if p.parent.name == "generated":
            gen_count += 1
            if not GENERATED_RE.match(p.name):
                fail("filenames: %s does not match <note-slug>-v<N>.<ext>" % rel(p))
    return "%d record files kebab-case; %d generated artifacts versioned" % (rec_count, gen_count)


# --- 7. ADR index: every numbered ADR file is indexed (ADR strategy)
def check_adr_index():
    adr_dir = ROOT / "docs" / "adr"
    index = (adr_dir / "README.md").read_text(encoding="utf-8")
    count = 0
    for p in sorted(adr_dir.glob("[0-9]*.md")):
        adr_id = "ADR-%s" % p.name.split("-")[0]
        count += 1
        if "| %s |" % adr_id not in index:
            fail("adr-index: %s is missing from docs/adr/README.md" % adr_id)
    return "%d ADR files all indexed" % count


def main():
    checks = [
        ("links", check_links),
        ("hashes", check_hashes),
        ("weights", check_weights),
        ("status vocabularies", check_status_vocabularies),
        ("README metadata", check_readme_metadata),
        ("filename conventions", check_filenames),
        ("ADR index", check_adr_index),
    ]
    for name, fn in checks:
        before = len(FAILURES)
        detail = fn()
        print("[%s] %s: %s" % ("PASS" if len(FAILURES) == before else "FAIL", name, detail))
    for n in NOTES:
        print("[NOTE] %s" % n)
    for f in FAILURES:
        print("[FAIL] %s" % f)
    print("\nSummary: %d checks, %d failure(s), %d note(s)" % (len(checks), len(FAILURES), len(NOTES)))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())

