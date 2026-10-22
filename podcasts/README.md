# Verticals podcast transcripts

This folder contains 29 full transcripts covering archive episodes 20–48. [Browse the summaries and dates](../INDEX.md#podcast-transcripts).

Each transcript includes a one-line summary, featured participants, the published episode-page link, and the supplied speaker labels and timestamps. Text is preserved as supplied; automated transcription errors and ambiguous speaker labels may remain. Consult the episode recording when an exact quotation or speaker attribution matters.

Publication dates refer to the linked published episode pages, not recording dates or Drive upload dates. Stable filenames use the archive numbering from the supplied Drive folders, which may differ from other published numbering. In particular, Deepak Chhugani's transcript is filed under archive episode 21 even though its source filename says Episode 20.

## Add another transcript

1. Copy [transcript-template.md.example](transcript-template.md.example) and save the new file in this folder as `YYYY-MM-DD-episode-title.md`.
2. Fill in the episode title, publication date, one-line summary, and optional original episode link. Paste the full transcript below `## Transcript`.
3. Keep existing speaker names and timestamps. Do not invent missing timestamps.
4. Regenerate the index and catalog by running `python3 scripts/rebuild_index.py` from the repository folder.
5. Commit the transcript, `INDEX.md`, and `library.json` together.

After those updates are published, the installed Claude skill can find the episode on its next run. Writers do not need to reinstall the skill when new transcripts are added.

The template and this guide are excluded from the searchable library.
