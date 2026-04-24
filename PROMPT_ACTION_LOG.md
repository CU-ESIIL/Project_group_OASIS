Prompt Action Log

YYYY-MM-DD

Prompt

User asked: “[verbatim or close paraphrase]”

Files and folders inspected

* [file or folder]

Actions taken

* [action]

Verification

* [check performed]

Open questions and follow-up

* [item]

2026-04-23

Prompt

User asked: "Port the reusable technical and UX improvements from Working_group_OASIS into this repo while preserving all existing Project Group content and structure."

Files and folders inspected

* .github/workflows/
* docs/
* mkdocs.yml
* README.md
* ../Working_group_OASIS/

Actions taken

* Added the non-blocking site health generator and homepage integration.
* Updated MkDocs config for snippets, edit actions, and shared styling.
* Added AGENTS.md guidance and refreshed the README.
* Updated the Pages workflow to generate the health report before building.

Verification

* Ran `python3 scripts/site_health.py`.
* Confirmed `docs/_site_health.md` was generated.
* Attempted `python3 -m mkdocs build --strict --clean`.

Open questions and follow-up

* Install MkDocs dependencies locally if you want a full local build preview in this workspace.

2026-04-24

Prompt

User asked: "Revise Project_group_OASIS into a stronger reusable group template that guides teams toward evidence-backed synthesis, simplifies the sidebar navigation, updates related guidance, and validates the site."

Files and folders inspected

* docs/index.md
* mkdocs.yml
* README.md
* AGENTS.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/project_template.md
* TEMPLATE_GUIDE.md
* requirements.txt

Actions taken

* Tightened the homepage scaffold with claim-focused prompts, a quality check, artifact-linked captions, confidence language, limitations, reusable outputs, and next steps.
* Reworked Final Share Out into one-sentence takeaway, core insights, visuals, surprises/failures/limitations, reusable outputs, and next steps.
* Removed MkDocs Material `toc.integrate` so homepage headings do not populate the left sidebar.
* Updated participant and agent guidance to preserve the reusable scaffold and evidence-backed Final Share Out pattern.

Verification

* Attempted `python3 -m mkdocs build --strict --clean`; it failed because local Python does not have the `mkdocs` module installed.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.
* Checked homepage markdown image targets and raw-location link pattern with a local Python script.
* Searched edited files for key Final Share Out terms and confirmed `toc.integrate` is absent.

Open questions and follow-up

* Install the dependencies in `requirements.txt` to run a full local MkDocs build.
