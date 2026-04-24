---
layout: page
title: Instructions
permalink: /instructions/
---

# Instructions: 3-Day Science Sprint

Welcome! These guides help your team use this site as a live, visual record of your sprint. Each day has clear prompts and short, practical steps.

- **Day 1 →** [Define & Explore](instructions/day1.md)  
- **Day 2 →** [Data & Methods](instructions/day2.md)  
- **Day 3 →** [Insights & Sharing](instructions/day3.md)

The final homepage should read like a compact evidence-backed synthesis: make claims, link artifacts, state confidence, name limitations, and show what others can reuse.

> Tip: Edit any page in your browser: open the file → click the pencil (✎) → make changes → **Commit changes**.

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

Team member row:

```markdown
| Name | Role | Contact | GitHub |
|---|---|---|---|
| Jane Doe | Data lead | jane@example.org | @janedoe |
```
