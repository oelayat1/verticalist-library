#!/usr/bin/env python3
"""Read the current Verticalist catalog and selected sources; never send draft text."""
import argparse
import hashlib
import json
import sys
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = "https://raw.githubusercontent.com/oelayat1/verticalist-library/main/"
MAX_BYTES = 2_000_000

def fetch(url):
    if not url.startswith(ROOT):
        raise ValueError("Only this library's raw URLs are allowed")
    request = Request(url + "?fresh=" + str(time.time_ns()),
                      headers={"User-Agent": "Verticalist-Library/1.0", "Cache-Control": "no-cache"})
    with urlopen(request, timeout=30) as response:
        if not response.geturl().startswith(ROOT):
            raise ValueError("Unexpected redirect")
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("Source exceeds the supported size")
    return data

def catalog():
    data = json.loads(fetch(ROOT + "library.json"))
    if data.get("schema_version") != 1 or not isinstance(data.get("sources"), list):
        raise ValueError("Unsupported library catalog")
    seen = set()
    for source in data["sources"]:
        if not isinstance(source, dict):
            raise ValueError("Malformed source record")
        for key in ("id", "type", "title", "date", "summary", "path", "url", "read_url", "sha256"):
            if not isinstance(source.get(key), str) or not source[key]:
                raise ValueError("Incomplete source metadata")
        if source["id"] in seen:
            raise ValueError("Duplicate source ID")
        seen.add(source["id"])
        path = source["path"]
        if not path.startswith(("essays/", "podcasts/")) or not path.endswith(".md") or ".." in path.split("/"):
            raise ValueError("Unexpected source path")
        if source["read_url"] != ROOT + path:
            raise ValueError("Unexpected source read URL")
        link = urlparse(source["url"])
        if link.scheme != "https" or not link.netloc:
            raise ValueError("Invalid source hyperlink")
    return data

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--index", action="store_true")
    modes.add_argument("--source", nargs="+", metavar="SOURCE_ID")
    args = parser.parse_args()
    try:
        data = catalog()
        if args.index:
            print(json.dumps({"library": data["library"], "updated": data["updated"],
                              "sources": [{k: s[k] for k in ("id", "type", "title", "date", "summary", "url")}
                                          for s in data["sources"]]}, ensure_ascii=False, indent=2))
            return
        by_id = {s["id"]: s for s in data["sources"]}
        missing = [source_id for source_id in args.source if source_id not in by_id]
        if missing:
            raise ValueError("Unknown source IDs: " + ", ".join(missing))
        results = []
        for source_id in args.source:
            source = by_id[source_id]
            content = fetch(source["read_url"])
            if hashlib.sha256(content).hexdigest() != source["sha256"]:
                raise ValueError("Source changed since catalog generation; ask the maintainer to rebuild the index: " + source_id)
            results.append({"id": source_id, "title": source["title"], "date": source["date"],
                            "url": source["url"], "text": content.decode("utf-8")})
        print(json.dumps({"library_updated": data["updated"], "sources": results},
                         ensure_ascii=False, indent=2))
    except Exception as exc:
        print("Library unavailable: " + str(exc) + ". This is not a no-matches result.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
