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

2026-05-01

Prompt

User asked to add a new `Norms` tab under the AI for Sustainability section with a Markdown primer on group discussions about AI-use norms.

Files and folders inspected

* mkdocs.yml
* docs/ai-for-sustainability/

Actions taken

* Added `docs/ai-for-sustainability/norms.md` as a plain-language discussion primer for setting group norms around AI use.
* Added the new page to the AI for Sustainability navigation as `Norms`.

Verification

* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; failed because `docs/index.md` already contains raw HTML iframe markup from prior homepage work, unrelated to this Norms page change.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-05-04

Prompt

User provided two Norms images and asked to add the simple norms image to the Norms page and add the norms decision panel to both the Norms page and the directions for adding norms to the website.

Files and folders inspected

* docs/ai-for-sustainability/norms.md
* docs/instructions/day1.md
* docs/assets/hero/

Actions taken

* Replaced `docs/assets/hero/norms.png` with the provided Gradients of Agreement image for the Norms page.
* Added `docs/assets/hero/norms-panel.png` from the provided Summit Team Norms panel.
* Added the norms panel image and a short worksheet sentence to the Norms page.
* Added the norms panel image and a link to the Team Norms activity in the Day 1 norms directions.

Verification

* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built Norms page and Day 1 directions reference `norms.png` and `norms-panel.png`.
* Confirmed the built site includes `/ai-for-sustainability/norms/` and the Norms nav link.

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

2026-04-24

Prompt

User asked: "Add header logo to Project_group_OASIS and remove text clutter."

Files and folders inspected

* mkdocs.yml
* docs/overrides/partials/logo.html
* docs/assets/
* docs/assets/esiil_content/
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Added `docs/assets/oasis_logo.png` by reusing the existing ESIIL wordmark asset.
* Updated `mkdocs.yml` to use `theme.logo: assets/oasis_logo.png`.
* Set `site_name` to a blank string value to prevent header title text clutter.
* Set `extra.homepage` to `https://cu-esiil.github.io/Project_group_OASIS/` so the logo links to the Project_group_OASIS homepage.
* Removed the custom `docs/overrides/partials/logo.html` override so Material handles the logo link normally.
* Added a small `.md-header__title { display: none; }` CSS rule for header spacing.
* Updated the template regression check to verify the standard Material logo configuration.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Inspected rendered `site/index.html` and confirmed the header logo uses `assets/oasis_logo.png` and links to `https://cu-esiil.github.io/Project_group_OASIS/`.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the deployed header to confirm the logo dimensions feel right with the blank site title.

2026-04-24

Prompt

User clarified: "You understand we just want a logo for the group at the top of the side bar. We are not modifying the top bar or anything else. We got this error: Config value 'theme': The path set in custom_dir ... docs/overrides does not exist."

Files and folders inspected

* mkdocs.yml
* docs/stylesheets/extra.css
* scripts/template_regression_check.py
* docs/assets/

Actions taken

* Removed the stale `custom_dir: docs/overrides` setting from `mkdocs.yml` so GitHub Actions no longer fails when the untracked overrides folder is absent.
* Changed the sidebar branding CSS from hiding the whole sidebar title block to showing the sidebar logo while hiding only the adjacent title text.
* Updated the template regression check to verify that `custom_dir` is not configured and that the sidebar logo area remains visible.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Inspected rendered `site/index.html` and confirmed the sidebar logo markup is present.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the deployed sidebar to confirm the logo size is right.

2026-04-24

Prompt

User clarified: "You are working on the wrong thing... we want both [the top header logo and title] back. The thing we're talking about is the white space below that where we had a logo that we got rid of... we wanted to keep the group logo."

Files and folders inspected

* mkdocs.yml
* docs/stylesheets/extra.css
* docs/assets/esiil_content/
* scripts/template_regression_check.py

Actions taken

* Restored `site_name: "OASIS Project Group Template"` so the top blue header shows both the ESIIL logo and the title text again.
* Removed the header-title hiding rule.
* Re-added `docs/assets/esiil_content/group_logo.svg`.
* Updated the sidebar title area so it stays visible, hides only the sidebar text, and displays the group logo in the white sidebar brand space.
* Kept `custom_dir` removed so GitHub Actions does not fail on a missing `docs/overrides` folder.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Inspected rendered `site/index.html` and confirmed the header title text is present again.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the deployed sidebar to confirm the group logo size and placement match the desired old scene.

2026-04-24

Prompt

User reported: "You made space for the logo and fixed the header, but there is no logo in the white space."

Files and folders inspected

* docs/stylesheets/extra.css
* docs/assets/esiil_content/group_logo.svg
* scripts/template_regression_check.py

Actions taken

* Changed the sidebar group logo rendering to use `.md-sidebar--primary .md-nav__title::before`.
* Hid Material's sidebar logo anchor in that same area so the group mark does not depend on the header-logo image element.
* Updated the regression check to require the sidebar pseudo-element logo rule.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Confirmed the built CSS contains the `group_logo.svg` pseudo-element rule.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Refresh the deployed page after GitHub Pages rebuilds to confirm the group logo appears in the white sidebar brand space.

2026-04-24

Prompt

User asked: "The logo is there now but it has too much white space around it. Can we reduce the height of the block that the logo is in so everything moves up toward the header? Also, can we call 'home' something more descriptive and alluring like display page or public facing or front page... the front of house."

Files and folders inspected

* mkdocs.yml
* docs/stylesheets/extra.css
* scripts/site_health.py
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md

Actions taken

* Reduced the sidebar group-logo block height and padding.
* Reduced the group-logo pseudo-element from `10rem` by `8rem` to `7rem` by `5.25rem`.
* Renamed the main nav item from `Home` to `Public Front Page`.
* Updated instruction pages and the site health nav check to use `Public Front Page`.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Confirmed the built HTML contains `Public Front Page` and built CSS contains the smaller sidebar group-logo dimensions.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the deployed sidebar; if the logo feels too small after rebuild, bump only the pseudo-element size without increasing the block height.

2026-04-24

Prompt

User asked: "That made the white space smaller but the logo got smaller as well. I think you can make the white space even smaller, but you need to then make the logo fill the space. While we're editing, can you also move the specialty tracks above the manuals in the side bar menu? We also don't need the RStudio Proxy Workaround anymore."

Files and folders inspected

* mkdocs.yml
* docs/stylesheets/extra.css
* scripts/site_health.py

Actions taken

* Reduced the sidebar group-logo block height to `3.9rem` with no vertical padding.
* Increased the group-logo pseudo-element to `8.8rem` by `6.4rem` and nudged it upward with negative top margin so it fills the compact block.
* Moved Specialty Tracks above Manuals in the sidebar navigation.
* Removed the RStudio Proxy Workaround link from Manuals.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Confirmed built HTML places Specialty Tracks before Manuals and no longer includes the RStudio nav item.
* Confirmed built CSS contains the updated compact group-logo dimensions.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the deployed sidebar to confirm the larger logo does not overlap the Public Front Page nav label.

2026-04-24

Prompt

User asked: "Make the logo twice that big within the same space so it really fills the space. Also, can you make the group titles in the side bar our branded green? This is 'instructions' 'specialty tracks' 'manuals' etc."

Files and folders inspected

* docs/stylesheets/extra.css

Actions taken

* Doubled the sidebar group-logo pseudo-element size from `8.8rem` by `6.4rem` to `17.6rem` by `12.8rem` while keeping the same compact block height.
* Colored top-level sidebar group labels with the branded green token.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed.
* Confirmed built CSS contains the doubled logo dimensions and branded green sidebar-label rules.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the sidebar; this intentionally overfills the compact block, so tune the negative margin if it overlaps the first nav link.

2026-04-24

Prompt

User asked: "Render a new group image that fills the sidebar space, says project group, and has minimalist on-brand flair. Add a button for https://what-uses-more.com, move people near the top of the front page, make the front page read like a polished example narrative, move editing instructions to the instructions pages, and make dark mode actually work."

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/assets/esiil_content/group_logo.svg
* docs/stylesheets/extra.css
* docs/stylesheets/tokens.css
* mkdocs.yml
* scripts/template_regression_check.py

Actions taken

* Replaced the sidebar group logo SVG with a larger minimalist Project Group mark using ESIIL colors, subtle gradient, and light texture.
* Reworked the Public Front Page into a polished fire-speed working example with people near the top, process sections in narrative order, polished results, citations, and the health report.
* Added a front-page link/button target for https://what-uses-more.com.
* Moved operational editing guidance, file placement, and copy-paste patterns into the Instructions page.
* Updated dark-mode palette settings and CSS variables so dark mode changes page background, text, links, tables, surfaces, and footer styling.
* Updated the template regression check to match the new split between public-facing front page and editing instructions.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with only the upstream Material for MkDocs 2.0 warning.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview dark mode and the oversized sidebar logo in the browser after deployment; spacing may need one visual tuning pass on narrow screens.

2026-04-24

Prompt

User asked: "Add a new sidebar category after Instructions but before Specialty Tracks called AI for Sustainability, with pages for Defining AI, Defining Sustainability, and What Does It Cost. The cost page should include the What Uses More calculator in an iframe."

Files and folders inspected

* mkdocs.yml
* docs/
* scripts/template_regression_check.py
* scripts/site_health.py

Actions taken

* Added an AI for Sustainability sidebar section between Instructions and Specialty Tracks.
* Created `docs/ai-for-sustainability/defining-ai.md`.
* Created `docs/ai-for-sustainability/defining-sustainability.md`.
* Created `docs/ai-for-sustainability/what-does-it-cost.md` with an embedded What Uses More calculator iframe and a fallback button link.
* Updated the site health navigation list and template regression check to protect the new nav section and pages.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `git diff --check`; passed.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning and expected git-revision-date warnings for newly added files.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Confirm after deploy that `https://what-uses-more.com` allows iframe embedding in GitHub Pages. If it blocks embedding, keep the button link as the working fallback.

2026-04-24

Prompt

User asked: "Improve the Project Group OASIS site so it is a clean, intuitive, forkable template. Keep the project/group name persistent in the header, make the main title ESIIL blue, refactor people into per-person files and cards, move buttons into context, remove Featured Outputs, add BibTeX citations, and set/reflect MIT license."

Files and folders inspected

* mkdocs.yml
* docs/index.md
* docs/instructions.md
* docs/instructions/day3.md
* docs/stylesheets/extra.css
* hooks.py
* README.md
* TEMPLATE_GUIDE.md
* AGENTS.md
* LICENSE
* scripts/site_health.py
* scripts/template_regression_check.py

Actions taken

* Kept the Material header title visible and added CSS to hide the dynamic section title so the project/group name stays persistent while scrolling.
* Styled page H1 headings with the ESIIL brand blue, with an accessible dark-mode alternate.
* Replaced the People table with snippet-included per-person Markdown files in `docs/people/`, rendered as cards on the front page.
* Removed the top-level button cluster and Featured Outputs section.
* Moved buttons into context: data notes in methods, code in methods, PDF in polished results, and compute-cost comparison near next steps.
* Added `docs/references.bib` and a lightweight MkDocs hook that converts `[@citationKey]` citations into page-local references at `{{ references }}`.
* Updated participant and template guidance to explain per-person files, BibTeX citations, contextual buttons, and MIT licensing.
* Updated the footer copyright line to include MIT License.
* Expanded regression and health checks to protect the new people, citation, navigation, header, and license-related behavior.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `git diff --check`; passed.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning and expected git-revision-date warnings for new people files.
* Confirmed the built homepage contains people cards, rendered references, no Featured Outputs section, and persistent-header CSS.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the rendered people cards in a browser after deploy and adjust card copy/spacing if the real team entries run much longer than the examples.

2026-04-24

Prompt

User asked: "Implement Day Directions, Landmark Stickers, and Markdown-Safe Editing for Project Group OASIS. Add a parking-garage-style landmark system with sticker assets, rewrite the Day 1/2/3 instructions with lettered tasks and anchor links, keep participant editing Markdown-only, add People profile templates, move buttons into context, verify MIT license/citation workflow, and run quality checks."

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/people/
* docs/data.md
* docs/stylesheets/extra.css
* docs/stylesheets/tokens.css
* mkdocs.yml
* scripts/site_health.py
* scripts/template_regression_check.py

Actions taken

* Added seven square landmark sticker PNG assets in `docs/assets/stickers/`.
* Added `scripts/generate_stickers.py` so the sticker assets can be regenerated from repo-native code.
* Reworked `docs/index.md` around the required landmark sections: People, Project Question, Specialty Tracks and Strategy, Data Exploration, Methods and Code, Results, and Polished Outputs.
* Added the required "How to use this page" legend text and sticker images on each editable section heading.
* Replaced participant-facing homepage HTML with Markdown headings, images, links, snippet includes, and Markdown attributes.
* Replaced Day 1, Day 2, and Day 3 instruction pages with the requested lettered task directions and fixed the section links to real `docs/index.md` anchors.
* Updated People profiles to plain Markdown, added `docs/people/template.md`, and added `docs/people/README.md`.
* Updated data guidance to point to the ESIIL Data Library instead of a placeholder-only data page.
* Added sticker and day-color CSS while keeping ESIIL brand colors aligned with the requested values.
* Updated site health and regression checks to protect the sticker assets, landmark sections, People template, and Markdown-safe front page.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `git diff --check`; passed after restoring generated build output.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning and expected git-revision-date warnings for new uncommitted People pages.
* Confirmed the built homepage includes sticker image assets and the expected section anchors.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the rendered homepage and day pages in a browser to tune sticker size or spacing if the landmark icons feel too large or too subtle in presentation mode.

2026-04-24

Prompt

User provided a new project group logo image and clarified it should replace the logo at the top of the sidebar, not the header.

Files and folders inspected

* docs/stylesheets/extra.css
* docs/assets/esiil_content/
* mkdocs.yml
* scripts/template_regression_check.py

Actions taken

* Added the provided PNG as `docs/assets/esiil_content/event_group_logo.png`.
* Updated the sidebar branding CSS to use `event_group_logo.png`.
* Left the header logo configuration unchanged at `assets/oasis_logo.png`.
* Left the prior `group_logo.svg` asset in place for possible future use.
* Updated the template regression check to protect the new sidebar-logo asset reference.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `git diff --check`; passed.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning and expected git-revision-date warnings for new uncommitted People pages.
* Confirmed built CSS references `event_group_logo.png` while the built header still references `assets/oasis_logo.png`.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* Preview the sidebar after deployment to confirm the new square logo crops and scales the way you want in the existing sidebar logo block.

2026-04-24

Prompt

User reported that the sticker attempt made the page look broken: tiny button-like sticker artifacts, odd paragraph text, and poor overall page quality on the live Project Group OASIS site.

Files and folders inspected

* Live site at https://cu-esiil.github.io/Project_group_OASIS/
* docs/index.md
* docs/people/
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Removed sticker image Markdown from homepage section headings.
* Kept normal Markdown headings with stable anchors for People, Project Question, Specialty Tracks and Strategy, Data Exploration, Methods and Code, Results, and Polished Outputs.
* Replaced direct image-heading stickers with CSS-generated landmark badges so participants do not edit image attributes or layout syntax.
* Converted included People profile files from oversized heading structures to smaller Markdown snippets that render more cleanly inside the homepage.
* Updated the regression check so future edits do not put sticker image syntax back into front-page headings.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `git diff --check`; passed.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built homepage headings render as plain `<h2>` anchors and built CSS supplies the visual landmark badges.
* Restored generated `site/` build output so the working tree contains source changes only.

Open questions and follow-up

* After deployment, inspect the live page visually and tune badge size or remove badges entirely if the page still feels too busy.

2026-04-24

Prompt

User reported that stickers were working better but People panels were not. User also asked for direction pages to use matching sticker files and better day/sticker color coding.

Files and folders inspected

* docs/index.md
* docs/people/
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Converted People profile snippets into Markdown blockquote panels and styled those panels as cards.
* Added separators between included People profiles so each profile renders as its own panel.
* Updated homepage section badges to use the shared `docs/assets/stickers/*.png` files via CSS background images.
* Added the same sticker image files to Day 1, Day 2, and Day 3 tasks with the `task-sticker` class.
* Improved direction-page color coding by styling task headings with day colors.
* Fixed Markdown spacing in day pages so lists render as lists instead of paragraph text.
* Updated regression checks to require shared sticker assets in day pages and CSS-backed homepage landmark badges.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built direction pages render sticker images from `assets/stickers/` and lists render as real `<ul>` elements.
* Confirmed built homepage renders People profiles as separate blockquote panels.

Open questions and follow-up

* Preview in browser after deployment to confirm the blockquote-card styling is visually strong enough for the People section.

2026-04-24

Prompt

User asked to implement the approved content cleanup plan: replace broken People panels with a simple Markdown list linking to existing Innovation Summit learner profile files, replace the Defining AI and Defining Sustainability pages with supplied Markdown-safe content, add citations, and make the main content title blue while preserving white header text.

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/ai-for-sustainability/defining-ai.md
* docs/ai-for-sustainability/defining-sustainability.md
* docs/people/
* docs/stylesheets/extra.css
* docs/references.bib
* scripts/template_regression_check.py

Actions taken

* Replaced local People profile snippet includes on the homepage with a plain Markdown learner-link list.
* Updated People editing guidance to point participants to the Innovation Summit 2026 learner files.
* Replaced the Defining AI and Defining Sustainability pages with Markdown-safe concept content and image/file replacement instructions.
* Added BibTeX entries for the AI and sustainability references cited from those pages.
* Fixed the later homepage `h1` style so public page titles use ESIIL Primary Blue while header text remains white.
* Updated the regression check to protect the external learner-link People pattern instead of the old local snippet pattern.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-24

Prompt

User noticed that the whiteboard image was no longer visible on the front page and asked to add it back.

Files and folders inspected

* docs/index.md
* docs/assets/whiteboards/

Actions taken

* Added the existing `assets/whiteboards/day1_whiteboard.jpg` image back to the Project Question section on the public front page.
* Added a replacement caption prompt that asks groups to say what the whiteboard shows, what decision it supported, and what question remains open.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-27

Prompt

User asked to restore a polished People gallery while keeping participant editing Markdown-only. The gallery should preserve D1-A/D1-C sticker navigation, render people as responsive cards, use learner profile links, avoid participant-facing HTML, and handle missing fields gracefully.

Files and folders inspected

* docs/index.md
* docs/_data/people.yml
* docs/people/
* docs/stylesheets/extra.css
* hooks.py
* scripts/site_health.py
* scripts/template_regression_check.py

Actions taken

* Added `docs/_data/people.yml` as the plain-text source for People gallery cards.
* Added generated People gallery rendering in `hooks.py` using the `{{ people_gallery }}` marker.
* Updated the front page People section to keep D1-A/D1-C sticker anchors while rendering the gallery below the editing guidance.
* Added centralized responsive People card styling with initials fallback avatars and dark-mode support.
* Updated People documentation and copy-paste instructions for learner links and optional profile images.
* Added people-gallery checks to site health and regression validation.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built homepage contains `people-gallery` cards and preserved `edit-D1-A` / `edit-D1-C` anchors.

2026-04-24

Prompt

User reported that neither logo link worked as intended. They clarified that the header logo should link to OASIS, while the sidebar event logo should link to the local front page.

Files inspected

* mkdocs.yml
* docs/stylesheets/extra.css
* scripts/template_regression_check.py
* Material for MkDocs `partials/header.html` and `partials/nav.html`
* built sidebar/header HTML in `/tmp/project_oasis_site_check/index.html`

Actions taken

* Set `extra.homepage` to the OASIS homepage so the header logo links to OASIS.
* Added `docs/overrides/partials/nav.html` so the sidebar logo uses `nav.homepage.url` and links to the local Project Group front page.
* Registered `docs/overrides` as the Material custom override directory.
* Updated the regression check to protect the split-link behavior.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built header logo href is `https://cu-esiil.github.io/home/`.
* Confirmed built sidebar logo href is `.` on the front page, which resolves to the Project Group homepage.

2026-04-27

Prompt

User requested a bidirectional task sticker navigation system. Each task sticker should appear once on the public front page and once in the matching directions page, with explicit `edit-Dx-Y` and `guide-Dx-Y` anchors and links in both directions.

Files and folders inspected

* docs/index.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/assets/stickers/tasks/
* docs/stylesheets/extra.css
* scripts/site_health.py
* scripts/template_regression_check.py
* mkdocs.yml

Actions taken

* Added explicit `edit-Dx-Y` anchors to front-page sticker locations.
* Added explicit `guide-Dx-Y` anchors to the matching directions tasks.
* Converted task stickers into bidirectional links between the public front page and day directions.
* Removed duplicate front-page placements for D3-C and D3-E so every task sticker appears exactly twice.
* Added `docs/stickers.md` as the central task sticker registry.
* Added `scripts/check_stickers.py` to validate sticker anchors, links, image paths, and ID casing.
* Integrated sticker validation into the generated Site Health report.
* Updated regression checks to run the sticker validation.
* Added scroll/focus/hover styling for linked task stickers.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning and a git-revision warning for the new uncommitted `stickers.md` file.
* Confirmed built front-page stickers link to directions anchors, including D1-A and D3-F.
* Confirmed built directions stickers link back to front-page anchors, including D1-A and D3-F.

2026-04-24

Prompt

User asked for the ESIIL event logo at the top of the sidebar to link back to the front page.

Files and folders inspected

* docs/stylesheets/extra.css
* scripts/template_regression_check.py
* mkdocs.yml
* built sidebar HTML in `/tmp/project_oasis_site_check/index.html`

Actions taken

* Moved the sidebar event logo from a non-clickable CSS pseudo-element onto Material's existing sidebar logo anchor.
* Hid the default logo image inside that anchor while using `event_group_logo.png` as the clickable background image.
* Added focus styling for keyboard accessibility.
* Updated the regression check to require the logo to render on the existing Material logo link.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built sidebar still contains Material's homepage logo anchor and the CSS now draws `event_group_logo.png` on that link.

2026-04-24

Prompt

User asked to move the Day 1, Day 2, and Day 3 instruction banner images before the page titles.

Files inspected

* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md

Actions taken

* Moved each day hero image above its H1 title.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-24

Prompt

User supplied hero images for the Day 1, Day 2, and Day 3 instruction pages.

Files and folders inspected

* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/assets/hero/
* /Users/tuff/Downloads/day 1.png
* /Users/tuff/Downloads/day 2.png
* /Users/tuff/Downloads/day 3.png

Actions taken

* Copied the supplied Day 1 image to `docs/assets/hero/day-1-hero.png`.
* Copied the supplied Day 2 image to `docs/assets/hero/day-2-hero.png`.
* Copied the supplied Day 3 image to `docs/assets/hero/day-3-hero.png`.
* Added each image directly below the matching instruction page title.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-24

Prompt

User supplied hero banner images for the AI and Sustainability pages.

Files and folders inspected

* docs/ai-for-sustainability/defining-ai.md
* docs/ai-for-sustainability/defining-sustainability.md
* docs/assets/hero/
* /Users/tuff/Downloads/ai hero.png
* /Users/tuff/Downloads/sustain.png

Actions taken

* Copied the supplied AI image to `docs/assets/hero/ai-hero.png`.
* Copied the supplied sustainability image to `docs/assets/hero/sustainability-hero.png`.
* Replaced the top image-placeholder text on both concept pages with Markdown hero banner images.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-24

Prompt

User disliked the existing abstract section stickers and asked to replace them with coordinated task stickers like the supplied mockup. They wanted Day 1 direction headers in the Day 1 color, each task beside its sticker, and the same stickers on the front page where the corresponding work belongs.

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stylesheets/extra.css
* docs/assets/stickers/
* scripts/template_regression_check.py

Actions taken

* Added shared SVG task sticker assets under `docs/assets/stickers/tasks/` for Day 1, Day 2, and Day 3 tasks.
* Updated Day 1, Day 2, and Day 3 instruction pages to use the task-specific sticker files instead of abstract section icon files.
* Added the same task sticker files to the matching front-page sections so directions and homepage landmarks line up.
* Removed CSS-injected homepage section badges so the visible homepage stickers now come from the same Markdown image paths as the directions.
* Tuned task sticker styling and day color styling so Day 2 task headings use the Day 2 color.
* Updated regression checks for the shared task-sticker system.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built homepage and Day 1/2/3 pages reference the shared `assets/stickers/tasks/*.svg` files.

2026-04-24

Prompt

User supplied a new hero image for the front page and asked for it to replace the current hero image.

Files and folders inspected

* docs/index.md
* docs/assets/hero/
* /Users/tuff/Downloads/image.png

Actions taken

* Copied the supplied PNG into `docs/assets/hero/hero.png`.
* Updated the front page hero image reference from `assets/hero/hero.jpg` to `assets/hero/hero.png`.
* Updated the image alt text to describe the fire spread progression scene.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-04-27

Prompt

User asked for instruction page visual cleanup so the right-side table of contents on Day 1, Day 2, and Day 3 instruction pages matches each day color without putting styling into participant-editable Markdown.

Files and folders inspected

* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stylesheets/tokens.css
* docs/stylesheets/extra.css
* hooks.py
* scripts/template_regression_check.py

Actions taken

* Added day metadata to the Day 1, Day 2, and Day 3 instruction pages.
* Added shared day color tokens that reuse the ESIIL blue, light blue, and green palette.
* Added a hook-generated hidden day marker so styling is driven by page metadata rather than hand-authored layout HTML.
* Colored the right-side table of contents for each instruction day, including stronger active/hover colors in the same day color family.
* Added regression checks to protect the day metadata, hook, tokens, and TOC color rules.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built Day 1, Day 2, and Day 3 pages include the expected `oasis-day-marker` values.

2026-04-27

Prompt

User asked to add an Edit Mode / Public Mode toggle to the public front page so workshop guidance remains available by default, while Public Mode hides scaffolding and shows a polished fire-spread example narrative.

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/stylesheets/extra.css
* docs/javascripts/
* hooks.py
* mkdocs.yml
* scripts/template_regression_check.py

Actions taken

* Added front-page metadata and hook-generated marker support for the Edit/Public mode toggle.
* Added `docs/javascripts/mode-toggle.js` to create the toggle, persist the setting in local storage, and mark scaffold admonitions.
* Registered the JavaScript asset and enabled Material-style collapsible admonitions.
* Reworked the public front page so visible text reads as a polished fire-spread example while editor instructions live in collapsible Markdown guidance blocks.
* Added centralized CSS for the toggle and Public Mode hiding behavior.
* Documented how future editors should write guidance blocks in Markdown.
* Updated regression checks to protect the toggle, scaffolding pattern, and public-mode marker.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built homepage includes the public-mode marker, collapsible scaffold blocks, People gallery, registered mode-toggle script, and D1-A bidirectional sticker links.

2026-04-27

Prompt

User asked to update `docs/instructions/link-to-github.md` so the main workflow uses GitHub web authentication through `startup/github_web_auth.ipynb`, HTTPS cloning from the JupyterLab Git sidebar, and timeout re-authentication. SSH should remain only as a backup.

Files and folders inspected

* docs/instructions/link-to-github.md
* docs/instructions/push-to-github.md
* docs/stylesheets/extra.css
* docs/assets/cyverse_basics/

Actions taken

* Rewrote the Link JupyterLab to GitHub page around GitHub web authentication and the `startup/github_web_auth.ipynb` notebook.
* Added a full-width launch button pointing to the requested CyVerse `/launch` URL and opening in a new tab.
* Documented running the first cell, copying the one-time code, approving GitHub device login, and running the second cell to configure Git credentials.
* Added first-commit name/email guidance, top-folder clone guidance, HTTPS clone-link instructions, push/pull expectations, and re-authentication steps for expired credentials.
* Moved SSH into a short backup/advanced option section.
* Updated the Git widget page intro so it points to GitHub web authentication instead of SSH.
* Added centralized launch-button styling in `docs/stylesheets/extra.css`.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built Link JupyterLab to GitHub page includes the `/launch` button, `github_web_auth.ipynb`, HTTPS clone guidance, timeout recovery, and SSH backup section.

2026-04-27

Prompt

User asked to unify the GitHub authentication page, Git widget push/pull page, and persistent storage/gocmd page as a coherent CRT Cloud Triangle workflow. The pages should explain JupyterLab as the temporary active workspace, GitHub as the place for code/text/small files, and persistent storage as the place for large data and durable outputs.

Files and folders inspected

* mkdocs.yml
* docs/instructions.md
* docs/instructions/link-to-github.md
* docs/instructions/push-to-github.md
* docs/instructions/save-to-persistent-storage.md
* scripts/site_health.py
* scripts/template_regression_check.py

Actions taken

* Renamed the sidebar section to `Cloud Triangle` with three action-oriented instance links.
* Added a CRT cloud workflow overview to `docs/instructions.md`.
* Added shared Cloud Triangle mental-model text, cross-links, and a What should I use table to the GitHub auth, Git widget, and persistent storage pages.
* Kept the GitHub auth page centered on HTTPS web authentication through `startup/github_web_auth.ipynb`.
* Reworked the Git widget page to clarify pull/stage/commit/push, coordination, conflicts, credential timeout, and large-file boundaries.
* Reworked the persistent storage page to keep non-interactive `gocmd` setup and transfer commands while explaining when to use persistent storage instead of GitHub.
* Updated site health and regression checks for the Cloud Triangle navigation.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built instruction overview and all three Cloud Triangle pages contain the new nav labels, cross-links, and GitHub vs persistent storage distinction.

2026-04-27

Prompt

User asked to move the Show template guidance toggle out of the main page and into the left sidebar as a compact global utility. The toggle should default on, persist its state, and hide clearly marked scaffold guidance without requiring participants to edit HTML, JS, CSS, or custom classes.

Files and folders inspected

* docs/overrides/partials/nav.html
* docs/javascripts/mode-toggle.js
* docs/stylesheets/extra.css
* docs/index.md
* docs/instructions.md
* scripts/template_regression_check.py

Actions taken

* Added the real checkbox toggle to the primary sidebar nav override, above the navigation list.
* Updated `mode-toggle.js` to bind to the sidebar toggle instead of injecting a toggle into the main article body.
* Changed local storage to use the `oasis-template-guidance` key with `show`/`hide` values.
* Updated CSS so the sidebar toggle is compact and hides when a page has no marked template guidance.
* Kept hiding scoped to scaffold-style admonitions marked by the script from titles such as `D1-`, `D2-`, `D3-`, `How to edit`, and `Show template guidance`.
* Updated front-page and instruction wording so the toggle is described as a sidebar control.
* Updated regression checks to require sidebar placement and prevent main-body toggle injection.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built HTML places the toggle in the sidebar before the nav list and still includes Cloud Triangle navigation, the People gallery, and D1-A bidirectional sticker links.

2026-04-27

Prompt

User asked for small visual tweaks after the sidebar guidance toggle: move the toggle under Instructions before AI for Sustainability, shorten the label, color-match Day 2/Day 3 instruction headers, make the fixed header show only the public page title, and align animated buttons with the ESIIL style guide.

Files and folders inspected

* docs/overrides/partials/nav.html
* docs/javascripts/mode-toggle.js
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Moved the template guidance toggle into the nav list immediately after the Instructions section and before AI for Sustainability.
* Shortened the visible label to `Guidance on`, with JavaScript updating it to `Guidance off` when disabled.
* Added explicit Day 1, Day 2, and Day 3 H1 colors using the existing day color tokens.
* Updated the shared JavaScript to set the fixed header title from the visible page H1 while keeping the dynamic section topic hidden.
* Consolidated site button styling so `.md-button` and launch buttons use ESIIL-style gradients, compact padding, rounded corners, and subtle hover movement.
* Updated regression checks for the new toggle placement, dynamic label, H1 color tokens, and header-title behavior.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built HTML places the toggle after Instructions and before AI for Sustainability, includes compact `Guidance on` text, keeps Cloud Triangle navigation, and includes the updated button/header JavaScript assets.

2026-04-27

Prompt

User asked to fix the sidebar toggle so all public-front-page template instruction boxes hide when the toggle is off, expand by default when on, and use `Instructions on` / `Instructions off` instead of guidance language.

Files and folders inspected

* docs/index.md
* docs/instructions.md
* docs/javascripts/mode-toggle.js
* docs/overrides/partials/nav.html
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Renamed the visible sidebar toggle label to `Instructions on` / `Instructions off` and updated its accessible label.
* Converted front-page template notes to expanded Markdown admonitions so instructions are open by default when enabled.
* Updated the toggle script to mark both expanded admonitions and collapsible details as `.template-instructions-block`.
* Added class-based CSS hiding with `.hide-template-instructions .template-instructions-block` while preserving the older guidance class for compatibility.
* Updated participant instructions and regression checks to describe the instructions toggle and expanded instruction-note convention.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed built HTML includes the sidebar toggle with `Instructions on`, the accessible `Show or hide template instructions` label, expanded front-page instruction admonitions, and the class-based instruction hiding JavaScript/CSS.

2026-04-27

Prompt

User provided `Example Public Front Page Fire Project.pdf` as updated homepage text.

Files and folders inspected

* /Users/tuff/Downloads/Example Public Front Page Fire Project.pdf
* docs/index.md
* docs/references.bib

Actions taken

* Extracted the PDF text and adapted it into the existing public front page structure.
* Updated the homepage title and narrative to use the Fire Polygon Velocity Project example.
* Replaced the older fire-speed example text with the supplied polygon-velocity overview, scientific gap, project question, approach, findings, interpretation, limitations, and next steps.
* Preserved the reusable template systems: instruction blocks, task stickers, people gallery marker, contextual buttons, citations, and site health block.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `/tmp/project_oasis_mkdocs_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built homepage includes `Fire Polygon Velocity Project`, the polygon-velocity project question, the updated findings, and the `Instructions on` sidebar toggle.
2026-04-29

Prompt

User asked to rewrite `docs/ai-for-sustainability/defining-sustainability.md` and `docs/ai-for-sustainability/defining-ai.md` so they read like thoughtful conversation starters rather than textbook definitions or AI summaries.

Files and folders inspected

* docs/ai-for-sustainability/defining-sustainability.md
* docs/ai-for-sustainability/defining-ai.md

Actions taken

* Replaced the Defining Sustainability page with essay-style Markdown focused on constraints, scale, thresholds, tradeoffs, and judgment.
* Replaced the Defining AI page with essay-style Markdown focused on representation, data limits, infrastructure costs, uncertainty, and the relationship between AI and sustainability.
* Removed old image-placeholder, gallery, and reference-scaffold content from those two pages.

Verification

* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Checked both rewritten pages for em dashes, old image placeholders, gallery macros, and reference hooks; none found.
* Installed MkDocs requirements into `/tmp/project_oasis_mkdocs_pkgs` after the local MkDocs command was unavailable.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-05-01

Prompt

User asked to make the main page edit link open in a new tab so authors can move back and forth between the rendered site and GitHub edits.

Files and folders inspected

* docs/javascripts/mode-toggle.js
* docs/overrides/partials/nav.html
* mkdocs.yml

Actions taken

* Updated the centralized site JavaScript to add `target="_blank"` to MkDocs Material edit links.
* Preserved safe `rel` attributes by adding `noopener` and `noreferrer` while keeping the edit relation.
* Applied the behavior after page initialization and MkDocs instant-navigation content replacement.

Verification

* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning and one expected revision-date warning for the new Norms page.
* Confirmed the built JavaScript contains the new edit-link new-tab behavior.
* Ran `python3 scripts/template_regression_check.py`; it still fails because `docs/index.md` contains the existing raw HTML CubeDynamics iframe wrapper, unrelated to this edit-link change.

2026-05-01

Prompt

User asked to change the GitHub repository link label in the header from `Project_group_OASIS` to `link to repo`.

Files and folders inspected

* mkdocs.yml
* docs/overrides/

Actions taken

* Updated `repo_name` in `mkdocs.yml` to `link to repo`.
* Left `repo_url` unchanged so the header link still points to the Project_group_OASIS GitHub repository.

Verification

* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built homepage header source link still points to the GitHub repository and displays `link to repo`.

2026-05-01

Prompt

User asked to remove the Storage sidebar item called `Add your profile` and simplify the homepage People section into an easy-to-fill Markdown table.

Files and folders inspected

* mkdocs.yml
* docs/index.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/people/README.md
* scripts/template_regression_check.py

Actions taken

* Removed `Add your profile` from the Storage navigation in `mkdocs.yml`.
* Replaced the generated People gallery marker on `docs/index.md` with a simple Markdown table.
* Updated People editing instructions to tell groups to add one table row per person and link names to existing learner files when possible.
* Updated the template regression check to expect the simpler People table instead of the older generated gallery marker.

Verification

* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built homepage renders the simplified People table rows and no longer contains the generated people gallery marker.
* Confirmed `Add your profile` no longer appears in the built homepage/sidebar output checked.
* Ran `python3 scripts/template_regression_check.py`; it still fails because `docs/index.md` contains the existing raw HTML CubeDynamics iframe wrapper, unrelated to the People table or Storage nav changes.

2026-05-01

Prompt

User asked to move the Present mode button to the bottom of the right sidebar.

Files and folders inspected

* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css
* docs/overrides/partials/nav.html
* scripts/template_regression_check.py

Actions taken

* Updated the presentation-mode script so the Present control attaches to the secondary/right sidebar when that sidebar exists.
* Kept the content-area placement as a fallback for layouts without a right sidebar.
* Added sidebar-specific styling so the button sits at the bottom of the right table-of-contents panel.
* Updated the template regression check to protect the sidebar placement.

Verification

* Ran `node --check docs/javascripts/presentation-mode.js`; passed.

2026-05-10

Prompt

User asked to capitalize Summit throughout the website.

Files inspected

* docs/index.md
* docs/instructions.md
* docs/example.md
* docs/instructions/day1.md
* docs/instructions/day3.md
* docs/ai-for-sustainability/norms.md
* docs/data.md

Actions taken

* Updated participant-facing prose and alt text so standalone lowercase “summit” reads “Summit.”
* Left the `innovation-summit-2025` URL unchanged because it is part of a link target.

Verification

* Ran `rg -n "\\bsummit\\b" docs mkdocs.yml`; the only remaining match is the `innovation-summit-2025` URL in `docs/data.md`.

2026-05-11

Prompt

User asked to fix presenter mode ordering so “Why this matters” appears in the Day 2 report-out group before data sources, matching its position on the Home page.

Files inspected

* docs/index.md
* docs/javascripts/presentation-mode.js

Actions taken

* Changed the `Why this matters` heading marker from `.oasis-report-out-day3` to `.oasis-report-out-day2`.

Verification

* Confirmed Day 2 report-out sections now include Product, Question, Why this matters, Data sources, and Methods in page order.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.

2026-05-11

Prompt

User asked to add a Cite & Reuse section at the bottom of the Home page modeled on last year's Innovation Summit citation example.

Files inspected

* docs/index.md

Actions taken

* Added a bottom `Cite & Reuse` section to the Home page.
* Included a template citation for Project Group OASIS and a CC-BY-4.0 license note with a link to the Data page.

Verification

* Confirmed the section was added after `What's next?` and is not marked as a report-out section.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Used a local browser check of `/instructions/day1/` at 1440 by 1000 and confirmed the Present button and hint render fully at the bottom of the right sidebar.
* Ran `python3 scripts/template_regression_check.py`; it still fails because `docs/index.md` contains the existing raw HTML CubeDynamics iframe wrapper, unrelated to the Present button placement.

2026-05-01

Prompt

User asked to move the Instructions on/off button from the left sidebar to the right sidebar, just above the Present button.

Files and folders inspected

* docs/overrides/partials/nav.html
* docs/javascripts/mode-toggle.js
* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css
* scripts/template_regression_check.py

Actions taken

* Removed the static Instructions toggle from the left sidebar navigation override.
* Updated the mode toggle script to create the Instructions on/off control in the right sidebar only on pages with template instructions.
* Added a shared right-sidebar utility container so the Instructions toggle sits directly above the Present button.
* Updated sidebar styling so the stacked controls remain at the bottom of the right sidebar.
* Updated the template regression check to expect the Instructions toggle in the right sidebar behavior rather than the left navigation override.

Verification

* Ran `node --check docs/javascripts/mode-toggle.js`; passed.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed for 19 task sticker pairs.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built assets include the right-sidebar utility container, the JavaScript-created Instructions toggle, and the Present toolbar sharing that container.
* Ran `python3 scripts/template_regression_check.py`; it still fails because `docs/index.md` contains the existing raw HTML CubeDynamics iframe wrapper, unrelated to the sidebar control placement.

2026-05-01

Prompt

User provided PDF prompts asking for targeted sidebar UI fixes and a clean separation between the editable Home template and the completed Example page.

Files and folders inspected

* docs/index.md
* docs/example.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stylesheets/extra.css
* docs/javascripts/presentation-mode.js
* scripts/check_stickers.py
* scripts/template_regression_check.py
* scripts/site_health.py
* mkdocs.yml

Actions taken

* Kept the top-level navigation split as Home and Example.
* Replaced the Home page with a sparse editable worksheet that keeps the Instructions toggle, hides guidance in note blocks, removes example narrative prose, and adds Day 2 and Day 3 report-out sections.
* Added a completed Example page with public-facing project-report prose, figures, interpretation, limits, outputs, and next steps.
* Retired the sticker/button navigation workflow from Home and the day-by-day instruction pages.
* Updated Day 1, Day 2, and Day 3 instructions to point groups to Home as the working page and Example as the reference page.
* Added detailed Day 2 and Day 3 report-out guidance to the instructions.
* Updated Present mode so the Present button only appears on Home and presentation mode isolates the two report-out sections.
* Applied sidebar fixes for primary nav spacing and weight, right table-of-contents padding, and stray sidebar utility marker removal.
* Updated local regression checks for the retired sticker workflow, Home/Example split, report-out sections, and sidebar fixes.

Verification

* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
* Ran `python3 scripts/site_health.py`; generated `docs/_site_health.md` with 0 warnings.
* Ran `python3 scripts/check_stickers.py`; passed with the retired sticker workflow check.
* Ran `python3 scripts/template_regression_check.py`; passed.
* Ran `PYTHONPATH=/tmp/project_oasis_mkdocs_pkgs python3 -m mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.

2026-05-08

Prompt

User asked to replace the Home page hero with a blue placeholder image that says "replace me with your own image," add figure guidance for swapping the hero, and update the LLM specialty track sidebar link.

Files inspected

* docs/index.md
* docs/assets/hero/hero.png
* mkdocs.yml

Actions taken

* Replaced `docs/assets/hero/hero.png` with a blue placeholder PNG reading "REPLACE ME WITH YOUR OWN IMAGE."
* Added a short hero-image caption and an instruction note on Home with a link to the GitHub hero image folder.
* Updated the LLM specialty track link to `https://cu-esiil.github.io/LLM_lesson_exemplar/cyverse/`.

Verification

* Ran `python3 scripts/site_health.py`; it reported one pre-existing Orientation nav warning, so `docs/_site_health.md` was restored to avoid committing unrelated generated noise.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User clarified there is not time for D1-E or D1-F on Day 1 and asked to move that work to Day 2 activities.

Files inspected

* docs/index.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/stickers.md
* docs/assets/stickers/tasks/

Actions taken

* Removed the Day 1 project-question task from the Day 1 directions and finish line.
* Updated the Home Project Question instruction block so drafting and refining the question is a Day 2 task.
* Updated Day 2 D2-A to draft and refine the question.
* Updated Day 2 D2-D to include capturing notes, links, decisions, and rough steps that did not fit on Day 1.
* Updated the task label registry and retired sticker asset labels so D1-E and D1-F are marked as moved to Day 2, D2-A covers drafting/refining the question, and D2-D covers build plus notes.

Verification

* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `python3 scripts/site_health.py`; it reported the existing Orientation nav warning, so `docs/_site_health.md` was restored to avoid committing unrelated generated noise.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to turn off the Instructions sidebar item without deleting the instructions so they can be turned back on later.

Files inspected

* mkdocs.yml

Actions taken

* Commented out the top-level Instructions navigation block in `mkdocs.yml`.
* Added the Day 1, Day 2, and Day 3 instruction pages to `not_in_nav` so the files remain available but do not appear in the sidebar.
* Left a comment in `mkdocs.yml` explaining that the block can be uncommented to show Instructions again.

Verification

* Ran `python3 scripts/site_health.py`; it reported the expected hidden Instructions nav item plus the existing Orientation nav warning, so `docs/_site_health.md` was restored to avoid committing generated warning noise.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built Home page no longer has the Instructions/Day 1/Day 2/Day 3 sidebar nav entries.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to add the Norms page hero image to the Team Norms section of the Home page and rename the Product Direction section to "Define, Explore, Data, and Methods."

Files inspected

* docs/index.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stickers.md

Actions taken

* Added `assets/hero/norms.png` to the Team Norms and Decision Making section on Home.
* Renamed the visible Product Direction heading on Home to "Define, Explore, Data, and Methods" while keeping the existing `#product-direction` anchor for compatibility.
* Updated Day 1, Day 2, Day 3, and the task label registry to use the new section name where they point to that Home section.

Verification

* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Confirmed the built Home page includes the Norms image and the renamed section.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User reported conflicts that needed to be resolved.

Files inspected

* mkdocs.yml
* docs/instructions/push-to-github.md
* docs/orientation/art_gallery.md

Actions taken

* Confirmed Git did not report any unmerged files.
* Removed literal conflict-marker text from the Push to GitHub instructions example so repository conflict scans do not flag the documentation as conflicted.
* Converted the `docs/orientation/art_gallery.md` Setext heading underline to an ATX heading so it does not look like a conflict divider in text searches.

Verification

* Ran a source conflict-marker scan; no unresolved conflict markers remain in source files.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked for a narrow fix to report-out mode and megaphone logic only.

Files inspected

* docs/index.md
* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css

Actions taken

* Added explicit `.oasis-report-out-section` markers to the Home page sections that belong in end-of-day report-out mode.
* Kept megaphones only on edit buttons for those marked report-out sections.
* Removed megaphones from editable-but-not-report-out buttons.
* Updated the Home page guidance text to explain that green buttons indicate editable content and megaphones indicate end-of-day report-out content.
* Updated presentation mode JavaScript to reveal only explicitly marked report-out sections instead of hard-coded People and report-out blocks.
* Updated presentation mode CSS to hide green buttons during report-out mode.

Verification

* Confirmed `docs/index.md` has exactly 8 `.oasis-report-out-section` markers for the requested report-out sections.
* Confirmed megaphone edit buttons only appear for those marked report-out sections.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
* Ran a modified-file trailing-whitespace check; passed.
* Attempted `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; it hung during MkDocs file discovery at the `mkdocs-jupyter` files event, before rendering pages.

2026-05-08

Prompt

User clarified that the Gradients of Agreement image should be on the Home page, not the directions or Norms page.

Files inspected

* docs/index.md
* docs/instructions/day1.md

Actions taken

* Moved the side-by-side Gradients of Agreement and norms worksheet image pair into the Home page Team Norms instruction box.
* Restored the Day 1 directions page to show only the norms worksheet image.
* Kept the image pair inside the Home page instruction box so it hides when instructions are off.

Verification

* Confirmed the Gradients of Agreement image appears in `docs/index.md` inside the Team Norms instruction box.
* Confirmed `docs/instructions/day1.md` no longer includes the side-by-side Gradients image pair.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to put the Gradients of Agreement image in the directions with a hover animation like the name cards.

Files inspected

* docs/instructions/day1.md
* docs/stylesheets/extra.css

Actions taken

* Added the Gradients of Agreement image to the Day 1 team norms directions.
* Placed the Gradients image and the norms worksheet side by side in the same Markdown-table pattern used for the name cards.
* Reused the existing global image hover/lift styling so the new directions images animate consistently with the name cards.

Verification

* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User reported that not all Home page directions were hiding when instructions were turned off and asked to move the "How to use this page" directions above the title.

Files inspected

* docs/index.md
* docs/javascripts/mode-toggle.js
* docs/stylesheets/extra.css

Actions taken

* Moved the "How to use this page during the summit" instruction box above the Home page title.
* Updated the instruction-toggle detection pattern so "How to use this page," "Day 1 directions," and similar direction labels are marked as hideable instruction blocks.
* Moved hero-image replacement guidance into its instruction box so it hides with instructions.
* Removed duplicate Method and Code instruction boxes that had drifted into the public content area.
* Updated shifted Home page edit-button line anchors.

Verification

* Confirmed the Home page has the "How to use this page" instruction box above the title.
* Confirmed the old standalone "Replace this hero image" guidance is no longer outside the hero instruction box.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to add side-by-side images of the in-person name cards to the directions for getting to know the group.

Files inspected

* docs/index.md
* docs/instructions/day1.md

Actions taken

* Added the two provided name-card screenshots as site assets in `docs/assets/team/`.
* Added a side-by-side Markdown table of the name-card prompt and follow-up-note images to the Day 1 introduce-yourselves directions.
* Added the same side-by-side visual inside the Home page People instruction box so it appears with instructions rather than as public team content.

Verification

* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User clarified that the Day 2 morning and afternoon divide should be a directions divide, not public content headings.

Files inspected

* docs/index.md

Actions taken

* Removed public-facing Morning Focus and Afternoon Focus headings from the Home page.
* Moved Day 2 morning guidance into the Define, Explore, Data, and Methods and Project Question instruction boxes.
* Moved Day 2 afternoon guidance into the Data Exploration and Method and Code instruction boxes.
* Kept the public-facing content flowing through each category without exposing schedule labels as content structure.
* Updated shifted edit-button line anchors.

Verification

* Confirmed `docs/index.md` no longer has public headings for Morning Focus or Afternoon Focus.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to add a Day 1 directions box under the Home page title.

Files inspected

* docs/index.md

Actions taken

* Added a Day 1 directions instruction box immediately under the Home page title.
* Added a 📣 edit button inside that Day 1 directions box.
* Updated shifted Home page edit-button line anchors after inserting the new box.

Verification

* Confirmed the Day 1 directions box appears under the Home page title with a 📣 edit button.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User said the previous Home page scaffold lost the interplay between instruction boxes and public-facing Markdown content.

Files inspected

* docs/index.md

Actions taken

* Reworked the Home page from Define, Explore, Data, and Methods through the end so instruction boxes explain the meta task and the content below each box is clean public-facing scaffold text.
* Added instruction boxes with 📣 edit buttons for Team Photo, Findings at a glance, Visuals that tell the story, and What's next.
* Removed megaphone markers from public headings so the megaphones live in edit buttons instead.
* Updated edit-button line anchors after restructuring the sections.

Verification

* Confirmed no public headings in `docs/index.md` contain the 📣 marker.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to reshape the Home page sections before report-out, especially Data Exploration, Method and Code, and Results.

Files inspected

* docs/index.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/stickers.md

Actions taken

* Replaced the Data Exploration instruction with "Snapshot showing initial data patterns" and added a 2-4 item data-source list scaffold.
* Renamed the Home page Methods section to "Method and Code" while preserving the existing `#methods-and-code` anchor.
* Added Method and Code scaffolds for methods/technologies, challenges identified, visuals, and short- and long-term next steps.
* Reworked Results into a synthesis-focused section with Team Photo, Findings at a glance, Visuals that tell the story, and What's next subsections.
* Updated Day 2 directions, Day 3 references, and the task label registry to match the revised Home page structure.

Verification

* Confirmed the old "Use this section after Day 1" Data Exploration copy is gone from Home and directions.
* Confirmed Home, Day 2, Day 3, and the task label registry use the revised "Method and Code" label where relevant.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User clarified that the Define, Explore, Data, and Methods section should be a Day 2 task split between morning and afternoon, with a whiteboard/notes visual placeholder.

Files inspected

* docs/index.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/stickers.md
* docs/assets/whiteboards/

Actions taken

* Changed the Define, Explore, Data, and Methods instruction label on Home to "Day 2 Task."
* Reworked the Home section into Morning Focus for questions, hypotheses, and context, plus Afternoon Focus for datasets and analyses.
* Added a new Day 2 morning whiteboard/notes placeholder image at `docs/assets/whiteboards/day2_morning_whiteboard.svg`.
* Updated Day 1 directions so product direction is no longer listed as a Day 1 finish-line item.
* Updated Day 2 directions and task labels to match the morning/afternoon workflow.

Verification

* Confirmed no remaining "Day 1 and Day 2 task" labels or Day 1 product-direction finish-line language in Home, directions, or stickers.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to add a megaphone emoji next to each edit button and remove the Specialty Tracks section from the Home page.

Files inspected

* docs/index.md
* docs/instructions.md
* docs/instructions/day1.md
* docs/instructions/day2.md
* docs/instructions/day3.md
* docs/project_template.md
* docs/stickers.md
* mkdocs.yml

Actions taken

* Added a 📣 marker to participant-facing edit links and edit buttons.
* Removed the Specialty Tracks and Strategy section from the Home page.
* Kept the Specialty Tracks sidebar navigation intact after the user clarified that only the Home page section should be removed.
* Updated Day 2 and the task label registry so D2-B points to the remaining Home sections instead of the removed Specialty Tracks section.

Verification

* Confirmed no participant-facing edit links remain without the 📣 marker.
* Confirmed the Home page, directions, and stickers registry no longer point to the removed Specialty Tracks and Strategy section.
* Ran `python3 scripts/check_stickers.py`; passed.
* Ran `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_site_check`; passed with the standard Material for MkDocs 2.0 warning.
* Ran `git diff --check`; passed.

2026-05-08

Prompt

User asked to update the completed example page so it matches the current homepage/template structure while preserving and improving the fictitious fire polygon velocity project.

Files inspected

* docs/index.md
* docs/example.md
* docs/assets/hero/hero.jpg
* docs/assets/figures/fire_hull.png
* docs/assets/figures/hull_panels.png
* docs/assets/figures/main_result.png
* docs/assets/Seven ways to measure fire polygon velocity-4.pdf

Actions taken

* Rebuilt `docs/example.md` around the current Home page section order and report-out section markers.
* Restored the completed example hero image to `assets/hero/hero.jpg` instead of the generic Home placeholder.
* Updated the People table to match the Home page columns: Name, Affiliation, Contact, Github.
* Folded the old example sections into the current structure: Team Norms, Our product(s), Our question(s), Why this matters, Data sources, Methods/technologies, Results, Team Photo, Findings, Visuals, What's next, and Cite & Reuse.
* Added concise fire polygon velocity content from the project brief, including the seven metric comparison framework.

Verification

* Tried `mkdocs build`; unavailable because `mkdocs` is not installed globally.
* Tried `python3 -m mkdocs build`; unavailable because the active Python does not have the MkDocs module.
* Tried `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_example_check`; the build started, reached "Building documentation", then timed out after 90 seconds without completing.

2026-05-08

Prompt

User asked to make Summit Report Out mode literal and section-driven so the Home worksheet is the single source of truth for report-out content.

Files inspected

* docs/index.md
* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css

Actions taken

* Replaced the top Home guidance with clearer green-button and megaphone language.
* Marked the eight worksheet report-out sections with visible 📣 labels and the existing `.oasis-report-out-section` class.
* Moved megaphones to the end of only the green edit buttons for report-out sections.
* Kept non-report-out edit buttons without megaphones.
* Replaced the duplicate Day 2 and Day 3 report-out fill-in forms with short guidance explaining that Summit Report Out presents the megaphone worksheet sections.
* Updated presentation-mode JavaScript so the Home hero image can be explicitly included in report-out mode with `.oasis-report-out-hero`.

Verification

* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
* Confirmed duplicate report-out form prompts and gallery includes no longer appear in `docs/index.md`.
* Tried `mkdocs build`; unavailable because `mkdocs` is not installed globally.
* Tried `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_report_out_check`; the build started, reached "Building documentation", then timed out after 90 seconds without completing.

2026-05-08

Prompt

User reported merge conflicts preventing GitHub push.

Files inspected

* docs/index.md
* PROMPT_ACTION_LOG.md

Actions taken

* Resolved conflict markers in `docs/index.md`.
* Kept the section-driven Summit Report Out workflow, staff breakout-room note, Day 2 whiteboard visual, and two-image team norms guidance.
* Marked `docs/index.md` as resolved in Git.
* Restored generated `site/` files that had been deleted by the earlier local MkDocs build attempt.

Verification

* Confirmed `git status --short` no longer reports unmerged files.
* Confirmed no conflict markers remain under `docs/`, `mkdocs.yml`, or `PROMPT_ACTION_LOG.md`.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.

2026-05-09

Prompt

User asked to add a footer like the one in the LLM lesson exemplar site.

Files inspected

* mkdocs.yml
* docs/overrides/partials/nav.html
* docs/stylesheets/extra.css
* https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/docs/overrides/main.html
* https://github.com/CU-ESIIL/LLM_lesson_exemplar/blob/main/docs/stylesheets/extra.css

Actions taken

* Added `docs/overrides/main.html` with the ESIIL footer pattern from the LLM lesson exemplar.
* Added institutional logo assets under `docs/assets/images/logos/`.
* Replaced the default Material footer styling with the custom `.site-footer` layout, logo row, light/dark styling, and mobile adjustments.
* Hid the new footer in Summit Report Out mode so presentation view remains clean.

Verification

* Confirmed the four logo files are valid PNGs.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
* Tried `/tmp/project_oasis_mkdocs_check_venv/bin/mkdocs build --strict --clean --site-dir /tmp/project_oasis_footer_check`; could not run because that local MkDocs executable no longer exists.

2026-05-09

Prompt

User asked to hide the Digital Twins and Causal Inference sidebar links for now, ensure all note and tip boxes turn off with Instructions off, and check Home edit-button line links.

Files inspected

* mkdocs.yml
* docs/index.md
* docs/javascripts/mode-toggle.js

Actions taken

* Commented out the Digital Twins and Causal Inference sidebar links without deleting them.
* Updated the instructions toggle so pages with `public_mode_toggle: true` mark every admonition and details block as template guidance.
* Updated Home edit-button GitHub line anchors to point closer to the current editable Markdown lines.

Verification

* Confirmed Digital Twins and Causal Inference are commented out in `mkdocs.yml`.
* Confirmed Home edit buttons now point to current line anchors.
* Ran `node --check docs/javascripts/mode-toggle.js`; passed.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.

2026-05-09

Prompt

User asked to confirm and adjust Summit Report Out mode so it shows the title and People first, then Day 2 report-out content from Day 2 megaphone sections, then Day 3 report-out content from Day 3 megaphone sections.

Files inspected

* docs/index.md
* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css

Actions taken

* Marked the People section as report-out context without adding a megaphone.
* Split megaphone report-out sections into explicit Day 2 and Day 3 classes.
* Updated Summit Report Out mode to show title, People, a Day 2 Report Out divider, Day 2 megaphone sections, a Day 3 Report Out divider, and Day 3 megaphone sections.
* Kept report-out content sourced directly from the existing Home page sections rather than duplicating or rewriting the content.
* Removed the Home hero from report-out mode so title and People appear first.
* Added cleanup so inserted Day 2 and Day 3 dividers disappear when leaving report-out mode.

Verification

* Confirmed the only report-out content sections are the megaphone-marked sections in `docs/index.md`.
* Ran `node --check docs/javascripts/presentation-mode.js`; passed.

2026-05-09

Prompt

User clarified that subheadings inside Methods do not have megaphones and that Challenges, Visuals, and Next Steps should not appear in report-out mode.

Files inspected

* docs/index.md
* docs/javascripts/presentation-mode.js
* docs/stylesheets/extra.css

Actions taken

* Updated report-out mode so unmarked `h3` subsections inside a megaphone section are hidden from Summit Report Out.
* Added CSS for `.oasis-report-out-hidden` so those hidden subsection blocks stay out of presentation mode.
* Kept the top-level Methods section in Day 2 report-out mode because it has the megaphone.

Verification

* Ran `node --check docs/javascripts/presentation-mode.js`; passed.
