#!/usr/bin/env python3
"""
Build resources.csv from the markdown inventory.

The markdown files stay the single source of truth; this regenerates the
machine-readable table that the Hugging Face dataset viewer displays.

Run from the repo root:   python3 build_dataset_csv.py
Then check the printed counts against the README badges before committing.
"""

import csv
import os
import re

FILES = {
    "README.md": "text",
    "SPEECH.md": "speech",
    "MODELS.md": "model",
}

ACCESS_TAGS = ["open", "on request", "paywalled", "paper only", "paper-only", "gated"]


def strip_links(s: str) -> str:
    """[label](url) -> label"""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).strip()


def parse(filename: str, kind: str):
    entries = []
    section = ""
    cur = None

    with open(filename, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")

            if line.startswith("## "):
                section = line[3:].strip()
                continue

            if line.startswith("### "):
                if cur:
                    entries.append(cur)
                heading = line[4:].strip()
                m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", heading)
                cur = {
                    "name": m.group(1) if m else heading,
                    "url": m.group(2) if m else "",
                    "resource_type": kind,
                    "category": section,
                    "access": "",
                    "description": "",
                    "source_file": filename,
                }
                continue

            if cur is None:
                continue

            if line.startswith("- ") and not cur["description"]:
                cur["description"] = strip_links(line[2:])

            if not cur["access"]:
                for tag in ACCESS_TAGS:
                    if f"**[{tag}]**" in line:
                        cur["access"] = "paper only" if tag == "paper-only" else tag
                        break

    if cur:
        entries.append(cur)
    return entries


def main():
    rows = []
    for filename, kind in FILES.items():
        if not os.path.exists(filename):
            print(f"  ! {filename} not found — skipped")
            continue
        found = parse(filename, kind)
        print(f"  {filename}: {len(found)} entries")
        rows.extend(found)

    # Headings with no access tag are group headings (e.g. "Classic ASR systems
    # (papers)") whose sub-items have different access levels. Label them so the
    # exported table is self-explanatory instead of showing a blank cell.
    for r in rows:
        if not r["access"]:
            r["access"] = "varies (grouped entry, see source)"

    for i, r in enumerate(rows, 1):
        r["id"] = i

    fields = ["id", "name", "resource_type", "category", "access", "description", "url", "source_file"]
    with open("resources.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"\nwrote resources.csv — {len(rows)} rows")

    counts = {}
    for r in rows:
        key = r["access"] or "(no access tag)"
        counts[key] = counts.get(key, 0) + 1
    print("access breakdown:")
    for k in sorted(counts, key=lambda x: -counts[x]):
        print(f"  {counts[k]:>4}  {k}")
    print("\nCHECK: do these totals match the README badges? If not, fix the README,")
    print("not the CSV — the markdown is the source of truth.")


if __name__ == "__main__":
    main()
