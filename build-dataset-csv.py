#!/usr/bin/env python3
"""Build resources.csv from the markdown inventory. Run from the repo root."""

import csv
import os
import re

SOURCES = {"README.md": "text", "SPEECH.md": "speech", "MODELS.md": "model"}
TAGS = ["open", "on request", "paywalled", "paper only", "paper-only", "gated", "commercial"]
COLUMNS = ["id", "name", "type", "category", "access", "description", "url", "file"]


def plain(text):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text).strip()


def parse(filename, kind):
    entries, section, entry = [], "", None

    for raw in open(filename, encoding="utf-8"):
        line = raw.rstrip("\n")

        if line.startswith("## "):
            section = line[3:].strip()
        elif line.startswith("### "):
            if entry:
                entries.append(entry)
            heading = line[4:].strip()
            link = re.match(r"\[([^\]]+)\]\(([^)]+)\)", heading)
            entry = {
                "name": link.group(1) if link else plain(heading),
                "url": link.group(2) if link else "",
                "type": kind,
                "category": section,
                "access": "",
                "tags": set(),
                "description": "",
                "file": filename,
            }
        elif entry:
            if line.startswith("- ") and not entry["description"]:
                entry["description"] = plain(line[2:])
            if not entry["url"]:
                # Headings that are plain text keep their links in the body.
                # Take the first one so no row ships without a URL.
                found = re.search(r"\]\((https?://[^)]+)\)", line)
                if found:
                    entry["url"] = found.group(1)
            for tag in TAGS:
                if f"**[{tag}]**" in line:
                    found_tag = "paper only" if tag == "paper-only" else tag
                    entry["tags"].add(found_tag)

    if entry:
        entries.append(entry)
    return entries


def main():
    rows = []
    for filename, kind in SOURCES.items():
        if not os.path.exists(filename):
            print(f"  ! {filename} not found")
            continue
        found = parse(filename, kind)
        print(f"  {filename}: {len(found)}")
        rows += found

    for number, row in enumerate(rows, 1):
        row["id"] = number
        tags = row.pop("tags")
        # A heading that groups several items can carry several different
        # access tags; picking the first would be arbitrary, so say so.
        if len(tags) == 1:
            row["access"] = tags.pop()
        elif len(tags) > 1:
            row["access"] = "varies (grouped entry)"
        else:
            row["access"] = "not tagged"

    with open("resources.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["access"]] = counts.get(row["access"], 0) + 1

    print(f"\nresources.csv: {len(rows)} rows")
    for access in sorted(counts, key=lambda a: -counts[a]):
        print(f"  {counts[access]:>4}  {access}")
    print("\nCheck these against the README badges before committing.")


if __name__ == "__main__":
    main()
