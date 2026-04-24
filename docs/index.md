# OASIS Project Group Template

<p style="text-align: right;"><a href="https://github.com/CU-ESIIL/Project_group_OASIS/edit/main/docs/index.md" title="Edit this page">✏️ Edit this page</a></p>

<!-- =========================================================
HERO: replace the title, impact sentence, hero image, and links.
========================================================= -->

![Wide banner for the project](assets/hero/hero.jpg)
[Open current hero file](assets/hero/hero.jpg)

Replace this heading with your group’s project title. Replace this sentence with one sentence on impact: in 3 days, our group will create or test **what** for **whom**, using **which evidence or artifact**.

**[Project brief (PDF)](assets/files/project_brief.pdf) · [View shared code](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code) · [Data & access](data.md)**

> **About this site:** This is a public, in-progress record of a 3-day project at the Innovation Summit. Edit the page as you work, commit small changes often, and use the Site Health report at the bottom to find unfinished template fields.

---

## How to edit this project page

Use this loop every time you update the site:

1. Open the public page and click **✏️ Edit this page**, or open `docs/index.md` in GitHub.
2. Replace the instructional text directly in the Markdown.
3. Upload images and files to the matching folder under `docs/assets/`.
4. Reference images with relative paths, such as `assets/figures/main_result.png`.
5. Scroll to **Commit changes** in GitHub and commit before moving on.
6. Wait for GitHub Pages to rebuild, then refresh the public site.
7. If old placeholder text still appears, you edited the wrong file or the site has not rebuilt yet.

**Quality check:** A useful project page states what changed, shows the artifact that supports it, and names what remains uncertain. Write claims, not activity logs. Avoid generic phrases like “we explored,” “we discussed,” or “more work is needed” unless you explain exactly what was explored, decided, or unresolved.

### Where files go

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

### Copy-paste patterns

Image with caption:

```markdown
![Short alt text](assets/figures/example.png)
*Figure 1. One sentence explaining what this visual shows and why it matters.*
[Replace this file in GitHub](assets/figures/example.png)
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

---

## Day 1 — Define & Explore

Edit this section during Day 1. Replace the prompts below with your group’s actual question, intended product, context, and one whiteboard or notes photo from `docs/assets/whiteboards/`.

### Day 1 checklist

- [ ] Replace the project title and one-sentence impact statement at the top of `docs/index.md`.
- [ ] Add the group question or intended product.
- [ ] Add at least one whiteboard, photo, or notes image from `docs/assets/whiteboards/`.
- [ ] Add 2-4 useful links to papers, datasets, or tools.
- [ ] Commit changes and refresh the public site.

### Product or question

- **Product:** Replace this with 1 sentence naming the tangible output your group will create.
- **Primary user:** Replace this with the person, community, or decision-maker who should use it.
- **Question:** Replace this with 1-3 specific questions your group will answer or clarify.
- **Done enough means:** Replace this with the minimum useful outcome by the end of the sprint.

### Why this matters

Replace this paragraph with 1-2 sentences explaining who is impacted and how this work could change a decision, assumption, workflow, or scientific understanding.

### Inspirations: papers, datasets, and tools

Replace these examples with 2-4 links your group actually used.

- **Publication:** Replace with a useful paper and link.
- **Dataset portal:** Replace with a data source and link.
- **Tool or method:** Replace with a tool, package, or workflow and link.

### Field notes or whiteboard photo

Replace this image by uploading a new file to `docs/assets/whiteboards/day1_whiteboard.jpg`, or change the image path below in `docs/index.md`.

![Whiteboard brainstorm placeholder](assets/whiteboards/day1_whiteboard.jpg)
[Open current whiteboard file](assets/whiteboards/day1_whiteboard.jpg)
*Caption: Replace this with what the artifact shows and which question, assumption, or disagreement it helped clarify.*

### Different perspectives

Replace this with 1-3 bullets that name disagreements, alternate framings, or decisions still open.

- Perspective or disagreement — why it matters for the project.

---

## Day 2 — Data & Methods

Edit this section during Day 2. Replace the prompts with data sources, first-pass visuals, methods, and known problems. Upload rough plots, maps, screenshots, and GIFs to `docs/assets/explorations/`.

### Day 2 checklist

- [ ] Add data source links and one-line descriptions.
- [ ] Add at least one first-pass plot, map, screenshot, or GIF.
- [ ] Add method or tool notes.
- [ ] Add known problems, uncertainties, or decisions needed.
- [ ] Commit changes and refresh the public site.

### Data sources

Replace these examples with the sources your group is actually testing.

- **Source A:** Replace with a link, coverage or scale, and the question it supports.
- **Source B:** Replace with a link and 1-line note on what it adds or why it may not work.

### First-pass visual

Replace this image by uploading a new file to `docs/assets/explorations/explore_data_plot.png`, or change the path below in `docs/index.md`.

![Early data pattern placeholder](assets/explorations/explore_data_plot.png)
[Open current exploration file](assets/explorations/explore_data_plot.png)
*Snapshot: Replace this with the initial pattern, data gap, or quality issue this reveals.*

### Methods and technologies

Replace these examples with 2-4 methods, tools, or workflows. Say what each one produces.

- Approach 1 — what it tests or produces.
- Approach 2 — what it tests or produces.
- Visualization — what someone should be able to see or compare.

### Problems, uncertainty, and decisions

Replace these examples with specific issues. Do not hide failures; they help the next group.

- Data gap or quality issue — why it matters.
- Method limitation or compute constraint — how it affects interpretation.
- Decision still needed — who needs to decide and by when.

### Prototype visuals

Replace these images with early results. Upload polished final visuals later to `docs/assets/figures/`.

#### Static figure

![Early pattern placeholder](assets/figures/figure1.png)
[Open current static figure](assets/figures/figure1.png)
*Figure 1. Replace this with what the visual suggests and which question or claim it may support.*

#### Animated change

![Temporal change animation placeholder](assets/figures/change.gif)
[Open current GIF](assets/figures/change.gif)
*Figure 2. Replace this with what changes across time and what uncertainty remains.*

#### Interactive map or external view

Replace this iframe with your own map, dashboard, or normal link. If an embed does not load, put the regular link directly under it.

<iframe
  title="Study area (OpenStreetMap)"
  src="https://www.openstreetmap.org/export/embed.html?bbox=-105.35%2C39.90%2C-105.10%2C40.10&layer=mapnik&marker=40.000%2C-105.225"
  width="100%" height="360" frameborder="0"></iframe>
<p><a href="https://www.openstreetmap.org/?mlat=40.000&mlon=-105.225#map=12/40.0000/-105.2250">Open full map</a></p>

---

## Final Share Out — Insights & Sharing

Edit this section on the final day. Replace the prompts with a small number of clear, evidence-backed insights that another person could reuse. Upload final visuals to `docs/assets/figures/`, team photos to `docs/assets/team/`, and PDFs or slides to `docs/assets/files/`.

### Final share-out checklist

- [ ] Add 2-3 headline findings or outcomes.
- [ ] Add 2-3 final visuals.
- [ ] Add next steps.
- [ ] Add team members.
- [ ] Replace the citation placeholder.
- [ ] Commit changes and verify the live page.

### Team or share-out photo

Replace this image by uploading a new file to `docs/assets/team/team_photo.jpg`, or change the path below in `docs/index.md`.

![Team photo placeholder](assets/team/team_photo.jpg)
[Open current team photo](assets/team/team_photo.jpg)

### One-sentence takeaway

Replace this with one specific sentence that states the core result, product, or lesson.

### Core insights

Add 3-5 insights. Each insight must make a claim and point to evidence. Avoid “we discussed” or “we explored.”

#### Insight 1 — replace with a short declarative title

- **What we found:** Replace with 1-2 specific sentences. State the claim, pattern, product, or lesson.
- **Why it matters:** Replace with the assumption, decision, workflow, or scientific question this affects.
- **Evidence / artifact:** Link to a figure, gallery, notebook, PDF, dashboard, data product, or raw output.
- **Confidence:** High / Medium / Low — briefly explain why.

#### Insight 2 — replace with a short declarative title

- **What we found:**
- **Why it matters:**
- **Evidence / artifact:**
- **Confidence:**

#### Insight 3 — replace with a short declarative title

- **What we found:**
- **Why it matters:**
- **Evidence / artifact:**
- **Confidence:**

### Visuals that tell the story

Highlight 2-3 visuals that make the share-out understandable without a long explanation. Replace each placeholder by uploading a file to `docs/assets/figures/` or changing the image path in `docs/index.md`.

![Lead conclusion visual placeholder](assets/figures/fire_hull.png)
[Open current lead visual](assets/figures/fire_hull.png)
*Caption: Replace this with what the visual shows and which insight or claim it supports.*

![Supporting panels placeholder](assets/figures/hull_panels.png)
[Open current supporting visual](assets/figures/hull_panels.png)
*Caption: Replace this with what the visual adds, compares, or documents. If it shows a failed attempt, say what failed and why that matters.*

![Complementary result placeholder](assets/figures/main_result.png)
[Open current result visual](assets/figures/main_result.png)
*Caption: Replace this with whether the visual is supporting evidence, a limitation, a workflow output, or a next-step prototype.*

### Surprises, failures, and limitations

Replace these examples with what did not work, what changed your thinking, or what remains uncertain.

- Surprise or failure 1 — why it matters.
- Surprise or failure 2 — why it matters.
- Limitation — what someone should not overclaim from this work.

### Reusable outputs

Replace these bullets with anything another group could directly reuse. Link artifacts when possible.

- Code / notebook:
- Dataset / derived data product:
- Figure / visualization:
- Brief / slides / PDF:
- Workflow or method:

### What’s next?

- Immediate follow-up:
- What we would do with one more week:
- What we would do with one more month:
- Who should see this next:

---

## Featured links (image buttons)

Replace the links and images below after you upload final files. Put PDFs, briefs, and slides in `docs/assets/files/`. Put button images or GIFs in `docs/assets/figures/` or keep the existing button files if they still fit.

<table>
<tr>
<td align="center" width="33%">
  <a href="assets/files/project_brief.pdf"><img src="assets/button_brief.gif" alt="Project brief PDF" width="240"><br><strong>Read the brief</strong></a>
</td>
<td align="center" width="33%">
  <a href="https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code"><img src="assets/button_code.gif" alt="View shared code" width="240"><br><strong>View code</strong></a>
</td>
<td align="center" width="33%">
  <a href="data.md"><img src="assets/button_data.gif" alt="Explore data" width="240"><br><strong>Explore data</strong></a>
</td>
</tr>
</table>

---

## Team

Replace the example rows with your team. Keep the table short.

| Name | Role | Contact | GitHub |
|------|------|---------|--------|
| Jane Doe | Lead | jane.doe@example.org | @janedoe |
| John Smith | Analyst | john.smith@example.org | @jsmith |

---

## Storage

**Code:** Keep shared scripts, notebooks, and utilities in the [`code/`](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code) directory. Document how to run them in a README or within the files so teammates and visitors can reproduce your workflow.

**Documentation:** Use the [`docs/`](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/docs) folder to publish project updates on this site. Longer internal notes can live in [`documentation/`](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/documentation); summarize key takeaways here so the public story stays current.

**Large files:** Keep large raw data outside GitHub. Link to shared storage or a data portal from this page or from [Data & access](data.md).

---

## Cite & reuse

Replace this citation before the final share-out:

> Project Group Authors. (2026). *OASIS project group output*. URL or DOI.

License: CC-BY-4.0 unless noted. See dataset licenses on the **[Data](data.md)** page.

---

## Site Health

Use this report before the final share-out. Fix missing files, broken internal links, and leftover unedited template markers.

--8<-- "_site_health.md"
