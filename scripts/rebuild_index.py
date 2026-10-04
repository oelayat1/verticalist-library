#!/usr/bin/env python3
"""Rebuild the readable index and live catalog from essay/transcript Markdown metadata."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path

REPOSITORY = "oelayat1/verticalist-library"
RAW = "https://raw.githubusercontent.com/" + REPOSITORY + "/main/"
BLOB = "https://github.com/" + REPOSITORY + "/blob/main/"

def rebuild(root):
    sources = []
    ids = set()
    for folder, kind in (("essays", "essay"), ("podcasts", "podcast")):
        for path in sorted((root / folder).glob("*.md")):
            if path.name == "README.md":
                continue
            content = path.read_text(encoding="utf-8")
            lines = content.splitlines()
            if not lines or not lines[0].startswith("# "):
                raise ValueError(str(path) + ": missing title")
            meta = {}
            for line in lines[1:]:
                if line.startswith("## "):
                    break
                if ": " in line:
                    key, value = line.split(": ", 1)
                    meta[key] = value
            for field in ("Published", "Type", "Summary"):
                if not meta.get(field):
                    raise ValueError(str(path) + ": missing " + field)
            datetime.date.fromisoformat(meta["Published"])
            if meta["Type"] != kind:
                raise ValueError(str(path) + ": incorrect type")
            rel = path.relative_to(root).as_posix()
            source_id = path.stem
            if source_id in ids:
                raise ValueError("Duplicate ID: " + source_id)
            ids.add(source_id)
            sources.append({"id": source_id, "type": kind, "title": lines[0][2:],
                            "date": meta["Published"], "summary": meta["Summary"], "path": rel,
                            "url": meta.get("Source URL", BLOB + rel), "read_url": RAW + rel,
                            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                            "original_pdf": meta.get("Original PDF")})
    sources.sort(key=lambda source: (source["date"], source["id"]), reverse=True)
    updated = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    catalog = {"schema_version": 1, "library": "The Verticalist", "repository": REPOSITORY,
               "updated": updated, "sources": sources}
    (root / "library.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    essay_count = sum(s["type"] == "essay" for s in sources)
    podcast_count = sum(s["type"] == "podcast" for s in sources)
    md = "# The Verticalist — Content Index\n\n"
    md += "Updated: " + updated + ". Coverage: " + str(essay_count) + " essays and " + str(podcast_count) + " podcast transcripts.\n\n"
    md += "Dates are publication dates printed in the original sources. Descriptions help locate useful material; read the full source before proposing linked text for a draft.\n\n"
    for kind, heading in (("essay", "Essays"), ("podcast", "Podcast transcripts")):
        md += "## " + heading + "\n\n"
        subset = [s for s in sources if s["type"] == kind]
        if not subset:
            md += "No transcripts have been added yet.\n\n"
            continue
        md += "| Date | Source | One-line description |\n| --- | --- | --- |\n"
        for source in subset:
            title = source["title"].replace("|", "\\|")
            summary = source["summary"].replace("|", "\\|").replace("\n", " ")
            md += "| " + source["date"] + " | [" + title + "](" + source["url"] + ") | " + summary + " |\n"
        md += "\n"
    md += "## Source notes\n\n"
    md += "Essay text was extracted from the supplied PDF archive. Original wording and footnotes are retained; related-post lists after the essay are omitted where identifiable. PDF text can contain line-wrap and layout artifacts, and charts are not transcribed.\n\n"
    mismatches = [s for s in sources if s.get("original_pdf") and s["original_pdf"][:10] != s["date"]]
    if mismatches:
        md += "| Essay | Date printed in PDF | Date in original filename |\n| --- | --- | --- |\n"
        for source in mismatches:
            md += "| " + source["title"] + " | " + source["date"] + " | " + source["original_pdf"][:10] + " |\n"
        md += "\n"
    md += "The Dispatcher Problem was supplied as 2026-02-13-who-gets-to-eat.pdf. Market Sizing Part I and Part II are distinct essays dated 2025-01-08 and 2025-01-31.\n"
    (root / "INDEX.md").write_text(md, encoding="utf-8")
    print(str(essay_count) + " essays, " + str(podcast_count) + " transcripts indexed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    rebuild(parser.parse_args().root.resolve())
