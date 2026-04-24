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

## Landmark stickers

Use the stickers like parking-garage landmarks:

- day color tells you when the task happens
- sticker design tells you where the work belongs on the main page
- task letter tells you the sequence for that day

For example, “Day 2C, Specialty Tracks and Strategy” means Day 2, task C, in the section marked by the Specialty Tracks and Strategy sticker.

## Editing this project site
Most summit participants should only edit Markdown files.
You can safely edit:
- the main project page content
- your own People profile file
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

## Where files go

| Put this here | Use it for |
|---|---|
| `docs/index.md` | Main public project page |
| `docs/assets/hero/` | Main banner or project identity image |
| `docs/assets/whiteboards/` | Whiteboard photos and brainstorm sketches |
| `docs/assets/explorations/` | Early plots, screenshots, rough maps, notebook screenshots |
| `docs/assets/figures/` | Polished figures and final visuals |
| `docs/assets/team/` | Team photos or headshots |
| `docs/assets/files/` | PDFs, briefs, slides, and downloadable materials |
| `docs/assets/stickers/` | Landmark sticker images used by the front page and instructions |
| `docs/people/` | One Markdown profile file per person |
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

People profile:

```markdown
### Jane Doe

**Role or affiliation**

Data lead, example institution.

**What I am excited to explore**

One or two sentences on what you are curious about in this project.

**Skills, data, or perspectives I bring**

Skills, datasets, tools, field experience, design skills, or facilitation skills.

**Something human**

A small detail that helps others connect with you.

**Optional link**

[Profile link](https://example.org)
```

Create one file per person in `docs/people/`, then include that file from `docs/index.md`. This helps teammates edit their own entry without creating merge conflicts. Prefer one profile link over raw contact details; do not publish email and GitHub handles together.

Citation:

```markdown
This sentence uses a source [@oasisProjectTemplate].
```

Add BibTeX entries to `docs/references.bib`, then cite them with `[@citationKey]` on `docs/index.md`. Keep `{{ references }}` where the generated reference list should appear.
