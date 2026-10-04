# The Verticalist Library

A living collection of essays and podcast transcripts for writers looking for relevant examples, evidence, frameworks, and counterarguments.

[Browse the index](INDEX.md) · [Download the Claude skill](https://raw.githubusercontent.com/oelayat1/verticalist-library/main/downloads/verticalist-library-skill.zip)

## Use it in Claude

1. Download the skill ZIP above.
2. In Claude, open Customize → Skills and upload the ZIP as a custom skill.
3. Share a draft, outline, or topic and ask: **“Use the Verticalist library to suggest useful additions to this draft. Give me copy-ready wording with hyperlinks.”**

The skill reads the current catalog whenever it runs, then fetches relevant sources. It provides an insertion point, copy-ready linked text, and a short explanation of why it helps. It can return “No strong matches.”

Claude needs code execution with network access to raw.githubusercontent.com, or a working web-fetch tool. Organization settings may restrict this. If remote access is unavailable, add the repository files through Claude's GitHub integration and sync before use; the skill will identify that material as a snapshot.

Adding content to this repository does not require reinstalling the skill. If the skill instructions or bundled helper change, download and upload a new ZIP.

## What is included

The initial library contains 28 essays extracted from the supplied PDFs. The index uses the publication dates and titles printed in those PDFs. Podcast transcripts will be added later.

The searchable files preserve extracted essay text and footnotes, with identifiable post-discussion and related-post footers removed. They may contain PDF layout artifacts. Figures and chart data have not been separately transcribed.

## Update the library

Put each essay in `essays/` and each transcript in `podcasts/` as a Markdown file with a stable, descriptive filename.

For podcasts, start with the [transcript template and instructions](podcasts/README.md).

Begin each source with:

```markdown
# Source title

Published: 2026-10-03
Type: essay
Summary: One sentence describing what the source contributes.

## Essay text

Full source text…
```

For podcasts, use `Type: podcast` and `## Transcript`; retain speaker labels and timestamps when available. An optional `Source URL: https://…` can point the writer to the original article or episode. If omitted, the source hyperlink points to the readable repository file.

After adding or editing sources, regenerate both catalogs:

```bash
python3 scripts/rebuild_index.py
```

Commit the source files, `INDEX.md`, and `library.json` together. The Claude helper checks each fetched source against the catalog, so regenerate the catalogs whenever a source changes.

The skill source lives in `skills/verticalist-library/`. To rebuild the downloadable ZIP after changing it:

```bash
python3 scripts/package_skill.py
```

## Reuse

Source material belongs to its respective authors. Making this repository public does not grant a blanket republication license. The library helps writers find, attribute, link to, and accurately discuss useful material.
