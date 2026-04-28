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

Each person has their own Markdown profile file in `docs/people/`. The homepage People gallery reads those files at build time. Use `docs/_data/people.yml` only as an index of profile paths, for example `profile: people/your-name.md`; do not duplicate profile text in YAML.

## Citations

Add BibTeX entries to `docs/references.bib`, then cite them in Markdown with `[@citationKey]`. The site build renders the References section automatically.

## Completing the Results and Polished Outputs

Use the homepage **Results** and **Polished Outputs** sections as a synthesis checklist, not an activity log. Add specific insights, link each one to a figure, notebook, PDF, dashboard, data product, or other artifact, and mark confidence as High, Medium, or Low with a short reason.

Strong entries state what changed, why it matters, what evidence supports it, what remains uncertain, and what another group can reuse. Keep the text short enough to present in a 2-minute walkthrough.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.

## License

This template is released under the MIT License.
