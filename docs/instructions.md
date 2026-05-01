---
layout: page
title: Instructions
permalink: /instructions/
---

# Instructions: 3-Day Science Sprint

Welcome! These guides help your team use this site as a live, visual record of your sprint. Each day has clear prompts and short, practical steps.

- **Day 1 →** [Meet Your Team and Define Your Project](instructions/day1.md)
- **Day 2 →** [Build, Explore, and Apply New Skills](instructions/day2.md)
- **Day 3 →** [Synthesize, Polish, and Share](instructions/day3.md)

The final homepage should read like a compact evidence-backed synthesis: make claims, link artifacts, state confidence, name limitations, and show what others can reuse.

> Tip: Edit any page in your browser: open the file → click the pencil (✎) → make changes → **Commit changes**.

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

## Landmark stickers

Use the stickers like parking-garage landmarks:

- day color tells you when the task happens
- task code tells you the exact direction to follow
- sticker title tells you the work to add or refine
- the same sticker appears on the front page where that work belongs

For example, “D2-C Takeaways” means Day 2, task C. Find the same sticker on the front page to know where that work belongs.

## Editing this project site
Most summit participants should only edit Markdown files.
You can safely edit:

- the main project page content
- the People list on the main page
- notes, figures, links, and project updates
- references in `references.bib`

You should avoid editing:

- HTML templates
- CSS files
- theme overrides
- site configuration

Those files control layout and styling. They are intentionally separated from the content so the project page is easier to edit without breaking the site.

## How to edit the Public Front Page

Use this loop every time you update the public-facing page:

1. Open the public page and click **✏️ Edit this page**, or open `docs/index.md` in GitHub.
2. Replace the example text directly in the Markdown.
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
!!! note "D2-E: How to edit this section"
    Replace this note with short instructions for editors.
    Keep public-facing project text outside this note.
```

Instruction blocks with titles that start with `D1-`, `D2-`, `D3-`, `How to edit`, `Template instructions`, or `Replace this` are hidden when instructions are turned off on the front page.

## Where files go

| Put this here | Use it for |
|---|---|
| `docs/index.md` | Main public project page |
| `docs/assets/hero/` | Main banner or project identity image |
| `docs/assets/whiteboards/` | Whiteboard photos and brainstorm sketches |
| `docs/assets/explorations/` | Early plots, screenshots, rough maps, notebook screenshots |
| `docs/assets/figures/` | Polished figures and final visuals |
| `docs/assets/people/` | Optional team photos or profile images |
| `docs/assets/team/` | Team photos or headshots |
| `docs/assets/files/` | PDFs, briefs, slides, and downloadable materials |
| `docs/assets/stickers/` | Landmark sticker images used by the front page and instructions |
| Innovation Summit learner files | Source profiles that can be linked from the People table |
| `docs/references.bib` | BibTeX references cited from Markdown |
| `code/` | Scripts, notebooks, and reusable analysis code |
| `documentation/` | Longer notes that should not clutter the public homepage |

## Copy-paste patterns

Image with caption:

```markdown
![Short alt text](assets/figures/example.png)
*Figure 1. One sentence explaining what this visual shows and why it matters.*
```

Data source:

```markdown
- **Dataset name** — one sentence on what it contains and why we need it. [Link](https://example.org)
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
