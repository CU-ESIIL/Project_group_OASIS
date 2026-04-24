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

2026-04-24

Prompt

User asked: "Can you update the style with this style guide? Also, the PDF button on the home page just takes us to the top of the page rather than to the PDF."

Files and folders inspected

* /Users/tuff/Downloads/ESIIL STYLE GUIDE.pdf
* docs/index.md
* docs/stylesheets/tokens.css
* docs/stylesheets/extra.css
* docs/assets/

Actions taken

* Mapped the ESIIL style guide palette, typography scale, and gradient button treatment into the site CSS tokens and custom styles.
* Updated the homepage Project brief PDF link from `#` to the existing PDF in `docs/assets/`.

Verification

* Rendered the one-page style guide PDF to an image for visual inspection because the PDF contains no extractable text.
* Confirmed the linked PDF asset exists.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.
* Searched the edited styles and homepage for stale legacy colors, negative letter spacing, and placeholder `#` links.
* Attempted `python3 -m mkdocs build --strict --clean`; it failed because local Python does not have the `mkdocs` module installed.

Open questions and follow-up

* Run a full MkDocs build after installing the dependencies in `requirements.txt`.

2026-04-24

Prompt

User asked: "Can we also swap out the logo with this image instead of the current one? Don't delete the current image, we may use it other places."

Files and folders inspected

* /Users/tuff/Downloads/Final_ESIIL%20Wordmark%20Color_0.png
* mkdocs.yml
* docs/overrides/partials/logo.html
* docs/assets/esiil_content/
* docs/stylesheets/extra.css

Actions taken

* Copied the new ESIIL wordmark into `docs/assets/esiil_content/esiil_wordmark_color.png`.
* Updated `mkdocs.yml` to use the new wordmark as the MkDocs header logo.
* Adjusted header logo sizing for the wider wordmark.
* Left the existing `docs/assets/esiil_content/esiil_oasis_logo.png` file untouched.

Verification

* Confirmed both the new wordmark and previous logo files exist.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.

Open questions and follow-up

* Preview the header after dependencies are installed to confirm the wordmark size feels right across desktop and mobile.

2026-04-24

Prompt

User asked: "Can we make the lower logo and project title into a home page logo that links back to the home page? The top banner logo can still link to OASIS."

Files and folders inspected

* docs/overrides/partials/logo.html
* mkdocs.yml
* docs/stylesheets/extra.css

Actions taken

* Added `docs/javascripts/home-brand-link.js` to make the primary sidebar brand area link to the site Home page.
* Registered the script in `mkdocs.yml`.
* Added a pointer cursor to the lower/sidebar brand title area.
* Preserved the top header logo link to `https://cu-esiil.github.io/home/`.

Verification

* Ran `node --check docs/javascripts/home-brand-link.js`.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.
* Confirmed the top logo partial still links to OASIS and the new sidebar script is registered in MkDocs.

Open questions and follow-up

* Preview after a MkDocs build to verify the sidebar brand click behavior in the rendered Material theme.

2026-04-24

Prompt

User clarified: "This logo is still linking to an outside repo instead of the home page. I want the home and the logo to link to home. The logo in the top bar can stay linked to the outside link."

Files and folders inspected

* docs/javascripts/home-brand-link.js

Actions taken

* Broadened the sidebar logo rewrite so every `a.md-logo` outside the top `.md-header` links to the site Home page.
* Preserved the top header logo's external OASIS link.

Verification

* Ran `node --check docs/javascripts/home-brand-link.js`.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.

Open questions and follow-up

* Preview the rendered sidebar after the next MkDocs build to confirm Material's lower logo markup is caught.

2026-04-24

Prompt

User asked: "That fixed the link but now I want to make a group logo so we don't have duplicates next to each other."

Files and folders inspected

* docs/javascripts/home-brand-link.js
* docs/stylesheets/extra.css
* docs/assets/esiil_content/
* mkdocs.yml

Actions taken

* Added `docs/assets/esiil_content/group_logo.svg` as a reusable group-logo placeholder using ESIIL colors.
* Updated the non-header brand script so lower/sidebar logos link to Home and use the group-logo image.
* Kept the top banner logo configured as the ESIIL wordmark.
* Added sidebar-specific sizing for the group logo.

Verification

* Ran `node --check docs/javascripts/home-brand-link.js`.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.

Open questions and follow-up

* Preview the rendered sidebar and adjust the group-logo size if the Material theme spacing differs across viewports.

2026-04-24

Prompt

User asked: "We have 4 possible specialty tracks. I need to add a new category of stuff in the side bar for specialty tracks with a unique link. The four tracks are LLM, Digital twins, Earth embeddings, and causal inference. Here is the link to the LLM lesson https://cu-esiil.github.io/LLM_lesson_exemplar/ and here is one for the embeddings lesson https://center-for-effective-global-action-cega.github.io/MOSAIKS-Training-Manual/en/index.html The other two need a markdown placeholder file. Also, still have the double logo problem. We want the bottom logo to be different."

Files and folders inspected

* mkdocs.yml
* docs/javascripts/home-brand-link.js
* docs/stylesheets/extra.css
* docs/assets/esiil_content/

Actions taken

* Added a Specialty Tracks section to the sidebar navigation.
* Linked LLM and Earth Embeddings to their external lesson sites.
* Added placeholder pages for Digital Twins and Causal Inference.
* Strengthened the sidebar logo replacement so the lower logo visually uses the group-logo asset via CSS as well as JS.

Verification

* Ran `node --check docs/javascripts/home-brand-link.js`.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.
* Confirmed the new nav labels, external URLs, placeholder pages, and group-logo CSS references are present.

Open questions and follow-up

* Replace the Digital Twins and Causal Inference placeholder pages with final lesson links or materials when available.

2026-04-24

Prompt

User asked: "I don't need this project title here, we have it above and to the right, we don't need it here, just a larger logo."

Files and folders inspected

* docs/stylesheets/extra.css
* docs/javascripts/home-brand-link.js

Actions taken

* Hid the repeated sidebar project title next to the group logo.
* Increased the sidebar group logo size and brand-area height.

Verification

* Ran `node --check docs/javascripts/home-brand-link.js`.
* Ran `python3 scripts/site_health.py`; it generated `docs/_site_health.md` with 6 existing template warnings.

Open questions and follow-up

* Preview the rendered sidebar and tune logo size if needed for narrow screens.

2026-04-24

Prompt

User asked: "Make Project_group_OASIS edit-driven and fix sidebar logo."

Files and folders inspected

* docs/index.md
* mkdocs.yml
* docs/overrides/partials/logo.html
* docs/stylesheets/extra.css
* docs/javascripts/home-brand-link.js
* scripts/site_health.py
* docs/assets/

Actions taken

* Reworked the homepage into an editing guide with a GitHub web-edit workflow, file map, copy-paste Markdown patterns, day-by-day checklists, and direct replacement instructions.
* Created structured asset folders for hero images, whiteboards, explorations, final figures, team images, and downloadable files.
* Copied existing placeholder assets into the new folder structure and updated homepage references.
* Updated MkDocs metadata to use the real Project_group_OASIS site URL and a non-placeholder site name.
* Removed the sidebar logo JavaScript workaround and group-logo asset.
* Hid Material's duplicate primary-sidebar title block with a narrow `.md-sidebar--primary .md-nav__title` selector while preserving the top OASIS logo link and normal Home nav link.
* Updated the site health script to check required asset folders and avoid flagging intentional instructional language as stale placeholders.
* Added `scripts/template_regression_check.py` for lightweight template regressions.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Attempted direct `python3 -m pip install -r requirements.txt`; system Python refused because it is externally managed.
* Created a temporary virtual environment in `/tmp`, installed requirements after allowing network access, and ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the rendered site to confirm the narrow sidebar branding selector matches the deployed Material markup.
