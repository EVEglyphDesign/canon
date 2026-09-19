#!/usr/bin/env python3
"""
canon/harness/build.py — one canon, many surfaces.

Reads canon/CANON.md and writes a generated adapter for each AI surface named
in canon/harness/surfaces.yml. Run it from the host repository root:

    python3 canon/harness/build.py            # write the adapters
    python3 canon/harness/build.py --check    # verify none has drifted (CI)
    python3 canon/harness/build.py --list     # show surfaces and sizes

Why this exists
---------------
A canon copied by hand into four files is four canons within a month. The
account holder edits CANON.md and nothing else; every surface file is derived,
carries the source hash in its header, and is regenerated rather than edited.
--check makes that mechanical: a commit where an adapter no longer matches its
source fails.

This script has no knowledge of any particular canon's content. It slices by
heading, so it works in any host repository whose canon follows the CANON.md
heading shape.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit(
        "PyYAML is required.\n"
        "  pip install pyyaml        (or: pip install pyyaml --break-system-packages)"
    )

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")

# The harness works in two layouts and must resolve both:
#
#   dropped into a host repo   <host>/canon/harness/  -> ROOT = <host>, canon = "canon"
#   inside the canon repo      <canon>/harness/       -> ROOT = <canon>, canon = "."
#
# CANON_REL is substituted into every generated link as {canon}, so a surface
# file points at the right place in either layout without being edited.
HARNESS_DIR = Path(__file__).resolve().parent
CANON_DIR = HARNESS_DIR.parent
ROOT = CANON_DIR.parent if CANON_DIR.name == "canon" else CANON_DIR
CANON_REL = "canon" if CANON_DIR.name == "canon" else "."

SOURCE = CANON_DIR / "CANON.md"
MANIFEST = HARNESS_DIR / "surfaces.yml"


def subst(text: str) -> str:
    """Resolve {canon} to the canon directory as seen from the host repo root."""
    return text.replace("{canon}/", "" if CANON_REL == "." else CANON_REL + "/") \
               .replace("{canon}", CANON_REL)


LINK = re.compile(r"\[([^\]]+)\]\((?!https?://|#|mailto:)([^)]+)\)")


def delink(text: str) -> str:
    """Flatten repository-relative links to their label.

    A surface pasted into a Perplexity Space or a ChatGPT Project cannot
    resolve `./OBSERVATIONS.md`. A dead link reads as a broken instruction, so
    the label is kept in backticks and the target dropped.
    """
    return LINK.sub(lambda m: f"`{m.group(2).lstrip('./')}`"
                    if m.group(1).strip("`") == m.group(2).strip("`").lstrip("./")
                    else f"{m.group(1)} (`{m.group(2).lstrip('./')}`)", text)


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------


@dataclass
class Block:
    """One heading and everything under it, children included."""

    level: int
    title: str
    lines: list[str] = field(default_factory=list)
    children: list["Block"] = field(default_factory=list)

    def render(self, shift: int = 0) -> str:
        """Render this block and its children, optionally shifting heading depth."""
        out = ["#" * max(1, self.level + shift) + " " + self.title, ""]
        out.extend(self.lines)
        for child in self.children:
            out.append(child.render(shift))
        return "\n".join(out).rstrip() + "\n"

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()


def parse(text: str) -> tuple[list[str], list[Block]]:
    """Split markdown into (preamble_lines, top_level_blocks)."""
    preamble: list[str] = []
    roots: list[Block] = []
    stack: list[Block] = []

    for raw in text.splitlines():
        m = HEADING.match(raw)
        if not m:
            (stack[-1].lines if stack else preamble).append(raw)
            continue

        level = len(m.group(1))
        block = Block(level=level, title=m.group(2))

        while stack and stack[-1].level >= level:
            stack.pop()
        if stack:
            stack[-1].children.append(block)
        else:
            roots.append(block)
        stack.append(block)

    return preamble, roots


def select(roots: list[Block], patterns: list[str]) -> list[Block]:
    """Return blocks whose title matches each pattern, in the manifest's order.

    A pattern that matches nothing is an error, not a silent omission — a
    renamed heading must break the build, otherwise a surface quietly loses a
    section and nobody finds out until a client reads it.
    """
    all_blocks = [b for root in roots for b in root.walk()]
    picked: list[Block] = []

    for pat in patterns:
        rx = re.compile(pat)
        hits = [b for b in all_blocks if rx.search(b.title)]
        if not hits:
            titles = "\n  ".join(b.title for b in all_blocks)
            raise SystemExit(
                f"FAIL: surfaces.yml selector {pat!r} matched no heading in "
                f"{SOURCE}.\nHeadings present:\n  {titles}"
            )
        for h in hits:
            if h not in picked:
                picked.append(h)

    # Drop any block already contained in a broader selected ancestor, so a
    # manifest that names both '§1' and '§1.2' does not emit §1.2 twice.
    contained = {id(d) for b in picked for d in b.walk() if d is not b}
    return [b for b in picked if id(b) not in contained]


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def frontmatter(spec: dict) -> str:
    fm = spec.get("frontmatter")
    if not fm:
        return ""
    body = yaml.safe_dump(dict(fm), sort_keys=False, allow_unicode=True,
                          default_flow_style=False, width=100)
    return "---\n" + body + "---\n\n"


def build_one(spec: dict, roots: list[Block], source_sha: str,
              provenance_tpl: str, built: str) -> str:
    blocks = select(roots, spec["sections"])

    # Normalise heading depth: the shallowest selected block becomes an H2, so
    # the generated file has exactly one H1 (its own title).
    shallowest = min(b.level for b in blocks)
    shift = 2 - shallowest

    parts: list[str] = []
    parts.append(frontmatter(spec))
    parts.append(subst(provenance_tpl).format(source_sha=source_sha, built=built).rstrip() + "\n")
    parts.append("")
    parts.append(f"# {spec['title']}")
    parts.append("")
    if spec.get("lead"):
        parts.append(subst(spec["lead"]).rstrip())
        parts.append("")
        parts.append("---")
        parts.append("")
    for b in blocks:
        parts.append(b.render(shift).rstrip())
        parts.append("")
    if spec.get("tail"):
        parts.append("---")
        parts.append("")
        parts.append(subst(spec["tail"]).rstrip())
        parts.append("")

    text = "\n".join(p for p in parts if p is not None)
    if spec.get("delink"):
        text = delink(text)
    text = re.sub(r"\n{4,}", "\n\n\n", text).rstrip() + "\n"
    return text


def check_budget(name: str, spec: dict, text: str) -> list[str]:
    warnings: list[str] = []
    n = len(text)
    hard = spec.get("hard_budget")
    soft = spec.get("budget")
    if hard and n > hard:
        raise SystemExit(
            f"FAIL: {name} ({spec['path']}) is {n} chars, over its hard budget "
            f"of {hard}. Either trim the sections it selects or raise the "
            f"budget deliberately in surfaces.yml."
        )
    if soft and n > soft:
        warnings.append(
            f"WARN: {name} ({spec['path']}) is {n} chars, over its soft budget "
            f"of {soft}. This file is read on every turn; every character is "
            f"paid for repeatedly."
        )
    return warnings


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="verify every adapter matches its source; write nothing")
    ap.add_argument("--list", action="store_true",
                    help="list surfaces, paths and rendered sizes")
    args = ap.parse_args()

    if not SOURCE.exists():
        return err(f"FAIL: {SOURCE} not found. Run this from the host repository root.")
    if not MANIFEST.exists():
        return err(f"FAIL: {MANIFEST} not found.")

    raw = SOURCE.read_text(encoding="utf-8")
    source_sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    provenance_tpl = manifest.get("defaults", {}).get("provenance", "")
    _, roots = parse(raw)

    built = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    rendered: dict[str, tuple[dict, str]] = {}
    warnings: list[str] = []
    for name, spec in manifest["surfaces"].items():
        if not spec.get("enabled", True):
            continue
        spec = dict(spec, path=subst(spec["path"]))
        text = build_one(spec, roots, source_sha, provenance_tpl, built)
        warnings.extend(check_budget(name, spec, text))
        rendered[name] = (spec, text)

    if args.list:
        print(f"source: {subst('{canon}/CANON.md')}  sha256 {source_sha[:16]}…  {len(raw)} chars\n")
        for name, (spec, text) in rendered.items():
            print(f"  {name:<14} {spec['path']:<42} {len(text):>7} chars")
        for w in warnings:
            print("\n" + w)
        return 0

    if args.check:
        drifted: list[str] = []
        for name, (spec, text) in rendered.items():
            target = ROOT / spec["path"]
            if not target.exists():
                drifted.append(f"  {spec['path']} — missing")
                continue
            # The built-at line changes every run; compare everything else.
            if strip_built(target.read_text(encoding="utf-8")) != strip_built(text):
                drifted.append(f"  {spec['path']} — differs from source")
        for w in warnings:
            print(w, file=sys.stderr)
        if drifted:
            print(f"FAIL: generated surfaces have drifted from {subst('{canon}/CANON.md')}:",
                  file=sys.stderr)
            print("\n".join(drifted), file=sys.stderr)
            print(f"\nRun `python3 {subst('{canon}/harness/build.py')}` and commit the result.",
                  file=sys.stderr)
            return 1
        print(f"OK: {len(rendered)} surfaces match {subst('{canon}/CANON.md')} "
              f"(sha256 {source_sha[:16]}…)")
        return 0

    for name, (spec, text) in rendered.items():
        target = ROOT / spec["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        if existing is not None and strip_built(existing) == strip_built(text):
            print(f"  unchanged  {spec['path']}")
            continue
        target.write_text(text, encoding="utf-8")
        print(f"  {'updated  ' if existing else 'created  '} {spec['path']} "
              f"({len(text)} chars)")

    for w in warnings:
        print("\n" + w)
    print(f"\nsource: {subst('{canon}/CANON.md')}  sha256 {source_sha[:16]}…")
    return 0


def strip_built(text: str) -> str:
    return re.sub(r"^\s*Built at: .*$", "", text, flags=re.MULTILINE)


def err(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
