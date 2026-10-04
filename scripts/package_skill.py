#!/usr/bin/env python3
"""Build a Claude-uploadable ZIP containing the skill folder."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
root = Path(__file__).resolve().parents[1]
source = root / "skills" / "verticalist-library"
destination = root / "downloads" / "verticalist-library-skill.zip"
destination.parent.mkdir(exist_ok=True)
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            archive.write(path, path.relative_to(source.parent))
print(destination)
