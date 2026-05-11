---
layout: page
title: Directions
permalink: /instructions/
---

# Directions: 3-Day Science Sprint

Welcome! These guides help your team use this site as a live, visual record of your sprint. Each day has a different rhythm because the agenda gives teams different amounts of work time.

- **Day 1 →** [Form Your Summit Team](instructions/day1.md)
- **Day 2 →** [Build and Report Back](instructions/day2.md)
- **Day 3 →** [Synthesize and Share](instructions/day3.md)

The Home page is the editable blank template your team fills out during the Summit. The Example page is a completed model that shows how a filled-in project story can look. Edit Home, not Example.

For a completed model, see the [Example Project Page](example.md).

[📣 Edit the Home page](https://github.com/CU-ESIIL/Project_group_OASIS/edit/main/docs/index.md){ .md-button .md-button--primary }

## Summit Report Out workflow

Your team page is both your workspace and your final report-out page. During the Summit, use the edit buttons to update the sections for each day. On Day 3, use the **Summit Report Out** button to view the page in a clean Summit Report Out layout.

For the final report out, focus on:

- What question or challenge your team worked on
- What you built, tested, mapped, wrote, or designed
- What changed in your thinking
- What someone else could do next
- Images that make the work easier to understand

## Work rhythm

- **Day 1:** about 30 minutes of actual team work time. Focus on alignment, not results.
- **Day 2:** about 3.5 to 4 hours of total team work time. Build one useful thing.
- **Day 3:** about 4 to 4.5 hours of team time. Synthesize, polish, and report out.

## CRT cloud workflow

In this workflow, your work moves between three connected places:

- **JupyterLab** is the temporary active workspace where you run notebooks, edit files, and test ideas.
- **GitHub** is for code, Markdown, notebooks, small figures, collaboration, and the public site source.
- **Persistent storage** is for large data, intermediate outputs, model results, and files that must survive beyond the running container.

A simple rule: **work in JupyterLab, push code and text to GitHub, and save large data or outputs to persistent storage.**

Use the Cloud Triangle pages when you need to move work between those places:

1. [Connect instance to GitHub](instructions/link-to-github.md)
2. [Instance to/from GitHub](instructions/push-to-github.md)
3. [Instance to/from persistent storage](instructions/save-to-persistent-storage.md)

## Editing this project site

Most Summit participants should only edit Markdown files.

You can safely edit:

- the Home page content
- the People list on the Home page
- notes, figures, links, and team updates
- references in `references.bib`

You should avoid editing:

- HTML templates
- CSS files
- theme overrides
- site configuration

Those files control layout and styling. They are intentionally separated from the content so the team page is easier to edit without breaking the site.

## How to edit the Home page

Use this loop every time you update the editable Home page:

1. Open the Home page and click **Edit this page**, or open `docs/index.md` in GitHub.
2. Replace the blank template text directly in the Markdown.
3. Upload images and files to the matching folder under `docs/assets/`.
4. Reference images with relative paths, such as `assets/figures/main_result.png`.
5. Scroll to **Commit changes** in GitHub and commit before moving on.
6. Wait for GitHub Pages to rebuild, then refresh the public site.
7. If old text still appears, you edited the wrong file or the site has not rebuilt yet.

## Template instructions toggle

The sidebar has a small **Instructions on/off** toggle.

- Leave instructions on while editing during the workshop.
- Turn instructions off to preview the cleaner public-facing page.
- The setting is saved in your browser.

Write future editor instructions as Markdown notes, not as public paragraphs:

```markdown
!!! note "Day 2 task"
    Replace this note with short instructions for editors.
    Keep public-facing project text outside this note.
```

Instruction blocks with task guidance are hidden when instructions are turned off on the Home page.

## Where files go

| Put this here | Use it for |
|---|---|
| `docs/index.md` | Editable Home team page |
| `docs/example.md` | Completed model team page |
| `docs/assets/hero/` | Main banner or team identity image |
| `docs/assets/whiteboards/` | Whiteboard photos and brainstorm sketches |
| `docs/assets/explorations/` | Early plots, screenshots, rough maps, notebook screenshots |
| `docs/assets/figures/` | Polished figures and final visuals |
| `docs/assets/report-out/` | Report-out banners and image manifest files |
| `docs/assets/people/` | Optional team photos or profile images |
| `docs/assets/team/` | Team photos or headshots |
| `docs/assets/files/` | PDFs, briefs, slides, and downloadable materials |
| Innovation Summit learner files | Source profiles that can be linked from the People table |
| `docs/references.bib` | BibTeX references cited from Markdown |
| `code/` | Scripts, notebooks, and reusable analysis code |
| `documentation/` | Longer notes that should not clutter the public Home page |

## Copy-paste patterns

Image with caption:

```markdown
![Short alt text](assets/figures/example.png)
*Figure 1. One sentence explaining what this visual shows and why it matters.*
```

Data source:

```markdown
- **Dataset name:** one sentence on what it contains and why we need it. [Link](https://example.org)
```

People table row:

[Find learner files in the Innovation Summit 2026 repository](https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners)

```markdown
| [Jane Doe](https://github.com/CU-ESIIL/Innovation-Summit-2026/blob/main/docs/learners/jane-doe.md) | Learner / Example University | Fire spread visualization | GIS, Python, field context |
```

Edit the People table on `docs/index.md` directly. Add one row per person and keep each cell short enough to read quickly.

Citation:

```markdown
This sentence uses a source [@oasisProjectTemplate].
```

Add BibTeX entries to `docs/references.bib`, then cite them with `[@citationKey]` on `docs/index.md`. Keep the existing references marker on pages where the generated reference list should appear.
