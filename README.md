# Project Group Template

This repository is a template for ESIIL Project Groups.

The website is built from the docs/ folder using MkDocs.

## Preview locally

pip install mkdocs-material
mkdocs serve

## Build site

mkdocs build --strict --clean

## Site Health

The site generates a non-blocking health report during the build.

The report appears at the bottom of the homepage and flags common issues such as missing files, placeholder links, or incomplete template fields.

Warnings do not prevent the site from publishing.

## Editing Pages

Use the edit icon on the website to open the corresponding markdown file in GitHub edit mode.

## Team Profiles

Each person has their own file in `docs/people/`. Edit one profile at a time and include only a profile link or public contact route, not email and GitHub together.

## Citations

Add BibTeX entries to `docs/references.bib`, then cite them in Markdown with `[@citationKey]`. The site build renders the References section automatically.

## Completing the Final Share Out

Use the homepage Final Share Out as a synthesis checklist, not an activity log. Add 3-5 specific insights, link each one to a figure, notebook, PDF, dashboard, data product, or other artifact, and mark confidence as High, Medium, or Low with a short reason.

Strong entries state what changed, why it matters, what evidence supports it, what remains uncertain, and what another group can reuse. Keep the text short enough to present in a 2-minute walkthrough.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.

## License

This template is released under the MIT License.
