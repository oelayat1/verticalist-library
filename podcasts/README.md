# Add podcast transcripts here

This folder is ready for podcast transcripts. No episodes have been added yet.

1. Copy [transcript-template.md.example](transcript-template.md.example) and save the new file in this folder as `YYYY-MM-DD-episode-title.md`.
2. Fill in the episode title, publication date, one-line summary, and optional original episode link. Paste the full transcript below `## Transcript`.
3. Keep existing speaker names and timestamps. Do not invent missing timestamps.
4. Regenerate the index and catalog by running `python3 scripts/rebuild_index.py` from the repository folder.
5. Commit the transcript, `INDEX.md`, and `library.json` together.

After those updates are published, the installed Claude skill can find the episode on its next run. Writers do not need to reinstall the skill when new transcripts are added.

The template and this guide are excluded from the searchable library.
