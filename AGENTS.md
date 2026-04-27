AGENTS.md

This repository is a template for ESIIL Project Groups.

Guidelines for agents:

* Treat this repository as the source of truth.
* Treat the website as a rendered view of repository state.
* Make small, focused edits. Avoid rewriting entire files.
* Do not change navigation or structure unless explicitly instructed.
* Preserve existing project content and historical context.
* Prefer improving shared systems over one-off fixes.
* Keep documentation and site content in sync.
* Do not introduce complex HTML into markdown pages. Keep participant-facing content Markdown-first, and hide layout or reusable behavior in CSS, hooks, includes, or templates.
* Keep everything editable by non-experts in GitHub.
* Do not add blocking tests for template completeness. Use the site health report for user-facing warnings instead.
* When adding new features, ensure they do not increase user complexity.
* Preserve the homepage as a polished, public-facing, replaceable example, not a long editing manual.
* Keep instructions, file maps, and editing workflows in the instructions pages rather than cluttering the front page.
* Keep final results structured around claims, evidence, confidence, limitations, reusable outputs, and next steps.
* Preserve per-person profile files in `docs/people/` so contributors can edit independently, and keep `docs/_data/people.yml` as an index of profile paths only.
* Preserve BibTeX citation flow through `docs/references.bib` and `[@citationKey]` references.
* Preserve artifact-first editing patterns: image placeholders, raw file replacement links, and clear captions that explain what claim each artifact supports.
* Do not replace scaffold language with project-specific conclusions unless the user explicitly asks for a finished group report.
* After meaningful changes, append an entry to PROMPT_ACTION_LOG.md.
