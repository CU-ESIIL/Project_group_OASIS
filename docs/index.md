---
title: How Fast is a Fire?
public_mode_toggle: true
---

# How Fast is a Fire?

![Fire spread progression over a mountain landscape](assets/hero/hero.png)

Fire spread is not a simple outward expansion. It is shaped by wind, fuel continuity, terrain, and the geometry of the growing fire perimeter. This example project asks how quickly a fire front can accelerate when wind and fuels align, and how a group might document that question using maps, observations, and simple reproducible analysis.

??? note "Show template guidance"
    Template guidance is on by default so workshop instructions are visible. Turn **Show template guidance** off in the sidebar to preview a cleaner public-facing version.

    Replace the example fire-spread narrative with your group’s actual purpose statement. Keep the first public paragraph to 1–2 sentences that say what your group is trying to understand, why it matters, and what evidence or product you want to share.

## How to use this page
This page is your group’s working project record. The visible narrative should read like a public project page; the collapsible guidance blocks tell editors what to replace during the summit.

The task stickers are landmarks. They help you match each day-by-day direction to the place on this page where that work belongs. The same sticker appears in the instructions and on the matching front-page section.

- **People** — who is in the group and what each person brings
- **Project Question** — what your group decided to explore
- **Specialty Tracks and Strategy** — how your group is using the summit trainings
- **Data Exploration** — datasets, maps, plots, and first observations
- **Methods and Code** — workflows, notebooks, scripts, and reproducible steps
- **Results** — patterns, findings, and interpretations
- **Polished Outputs** — final figures, PDFs, slides, or other shareable products

??? note "How to edit this section"
    Keep this orientation short. It should help editors understand the page without becoming part of the project’s final public story.

    In Public Mode, this guidance is hidden so readers see the project narrative, figures, people, outputs, and references.

## People { #people }

<span id="edit-D1-A"></span>
[![D1-A: Team](assets/stickers/tasks/d1-a.svg){ .task-sticker }](instructions/day1.md#guide-D1-A)
<span id="edit-D1-C"></span>
[![D1-C: People](assets/stickers/tasks/d1-c.svg){ .task-sticker }](instructions/day1.md#guide-D1-C)

This project is meant to be shaped by the people in the room: their field experience, data skills, modeling instincts, design sense, and curiosity about fire behavior.

??? note "D1-A / D1-C: How to edit the people gallery"
    Replace the example people below with the people in your group. To update the gallery, edit `docs/_data/people.yml`. Each entry is plain text plus a link to the person’s existing learner file in the Innovation Summit learner folder.

    [Find learner files in the Innovation Summit 2026 repository](https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners)

    Put profile images in `docs/assets/people/`. If an image is missing, the card will show initials instead.

{{ people_gallery }}

## Project Question { #project-question }

<span id="edit-D1-B"></span>
[![D1-B: Question](assets/stickers/tasks/d1-b.svg){ .task-sticker }](instructions/day1.md#guide-D1-B)
<span id="edit-D2-A"></span>
[![D2-A: Question](assets/stickers/tasks/d2-a.svg){ .task-sticker }](instructions/day2.md#guide-D2-A)
<span id="edit-D3-A"></span>
[![D3-A: Story](assets/stickers/tasks/d3-a.svg){ .task-sticker }](instructions/day3.md#guide-D3-A)

How fast can a fire front move when wind direction, fuel continuity, and slope align, and which simple measurements help explain that acceleration?

For this example project, the group treats fire spread as a spatial process that changes through time. The public story focuses on how the perimeter grows, where the fastest advance appears, and which sources of uncertainty should keep readers from over-interpreting a single map.

??? note "D1-B / D2-A / D3-A: How to edit the project question"
    Replace this section with your group’s project question. It is okay if the question changes during the summit.

    Helpful prompts:

    - What are we trying to understand?
    - Why does this question matter?
    - What would count as a useful answer by Day 3?
    - What are we still unsure about?

![Day 1 whiteboard notes](assets/whiteboards/day1_whiteboard.jpg)
*This whiteboard captures the first version of the fire-speed question: define a simple spread metric, compare it across terrain and wind contexts, and keep uncertainty visible.*

??? note "How to replace the whiteboard image"
    Upload a new whiteboard or notes photo to `docs/assets/whiteboards/`, update the image path above, and rewrite the caption so it says what decision the image supports.

## Specialty Tracks and Strategy { #specialty-tracks-and-strategy }

<span id="edit-D1-D"></span>
[![D1-D: Tracks](assets/stickers/tasks/d1-d.svg){ .task-sticker }](instructions/day1.md#guide-D1-D)
<span id="edit-D2-B"></span>
[![D2-B: Strategy](assets/stickers/tasks/d2-b.svg){ .task-sticker }](instructions/day2.md#guide-D2-B)
<span id="edit-D2-C"></span>
[![D2-C: Takeaways](assets/stickers/tasks/d2-c.svg){ .task-sticker }](instructions/day2.md#guide-D2-C)

The example group uses the summit tracks as a division of labor. One subgroup explores AI-assisted synthesis of fire reports and notes, another tests geospatial workflows for perimeter change, and a third focuses on how to communicate uncertainty without hiding the limits of a rapid workshop analysis.

??? note "D1-D / D2-B / D2-C: How to edit specialty track strategy"
    Replace this section with notes about how your group is using the summit specialty tracks.

    Capture:

    - which tracks people attended or plan to attend
    - what each person brought back from a track
    - how the training changed your project strategy
    - what skills your group still needs

## Data Exploration { #data-exploration }

<span id="edit-D1-E"></span>
[![D1-E: Data](assets/stickers/tasks/d1-e.svg){ .task-sticker }](instructions/day1.md#guide-D1-E)
<span id="edit-D2-E"></span>
[![D2-E: Explore](assets/stickers/tasks/d2-e.svg){ .task-sticker }](instructions/day2.md#guide-D2-E)
<span id="edit-D3-C"></span>
[![D3-C: Clean Up](assets/stickers/tasks/d3-c.svg){ .task-sticker }](instructions/day3.md#guide-D3-C)

The first data pass compares fire perimeter snapshots with terrain, fuel, and wind context. The goal is not to build a full operational fire model; it is to identify whether simple, transparent measurements can show where the fire appears to speed up or slow down.

Useful data products for this example include perimeter polygons, timestamped observations, elevation-derived slope, wind summaries, and a simple table of spread-distance estimates.

??? note "D1-E / D2-E / D3-C: How to edit data exploration"
    Replace this section with the datasets, maps, plots, screenshots, tables, or first observations your group is using to understand the question.

    Strong data notes say what the dataset contains, why it matters, and what remains uncertain.

![Early exploration plot](assets/explorations/explore_data_plot.png)
*This early plot tests whether the apparent spread distance changes by observation interval. It is useful because it exposes both a possible acceleration signal and the sensitivity of that signal to timestamp quality.*

??? note "How to replace the exploration figure"
    Upload rough plots, screenshots, maps, or GIFs to `docs/assets/explorations/`. Rewrite the caption so it says what the figure shows, what surprised you, and what still does not make sense.

[Open the ESIIL Data Library](https://cu-esiil.github.io/data-library/innovation-summit-2025/){ .md-button }
[Document your group data notes](data.md){ .md-button }

## Methods and Code { #methods-and-code }

<span id="edit-D1-F"></span>
[![D1-F: Notes](assets/stickers/tasks/d1-f.svg){ .task-sticker }](instructions/day1.md#guide-D1-F)
<span id="edit-D2-D"></span>
[![D2-D: Methods](assets/stickers/tasks/d2-d.svg){ .task-sticker }](instructions/day2.md#guide-D2-D)

The example workflow keeps the analysis intentionally small: load perimeter and terrain layers, align timestamps, estimate distance moved between observations, summarize spread rates, and export figures that can be checked by someone outside the group. Code and notes should make the assumptions visible rather than hiding them inside a polished figure.

??? note "D1-F / D2-D: How to edit methods and code"
    Replace this section with the tools, notebooks, scripts, workflows, or repeatable steps your group tried.

    Include:

    - what you tried
    - what worked
    - what did not work
    - where the code or notebook lives
    - what someone else would need to reproduce or extend the work

[View shared code](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code){ .md-button }

## Results { #results }

<span id="edit-D2-F"></span>
[![D2-F: Results](assets/stickers/tasks/d2-f.svg){ .task-sticker }](instructions/day2.md#guide-D2-F)
<span id="edit-D3-B"></span>
[![D3-B: Results](assets/stickers/tasks/d3-b.svg){ .task-sticker }](instructions/day3.md#guide-D3-B)
<span id="edit-D3-E"></span>
[![D3-E: Present](assets/stickers/tasks/d3-e.svg){ .task-sticker }](instructions/day3.md#guide-D3-E)

The example result is a cautious one: the fastest apparent spread occurs where the perimeter has a long, wind-aligned edge and relatively continuous fuel. The evidence is suggestive rather than definitive because observation timing, perimeter uncertainty, and local wind variation can all change the estimated speed.

Three claims are worth carrying into a public share-out:

- **Spread speed depends on geometry.** A growing perimeter can advance unevenly, so one average speed hides important local variation.
- **Simple figures can still be useful.** A transparent map plus a short rate table may be easier to reuse than a complex model that cannot be explained quickly.
- **Uncertainty is part of the result.** The analysis should say where measurement limits could change the interpretation.

??? note "D2-F / D3-B / D3-E: How to edit results"
    Replace this section with emerging results, patterns, findings, surprises, or honest limits. A strong result makes a claim, points to evidence, and names uncertainty.

    Useful result statements can sound like:

    - We are starting to see...
    - One pattern that surprised us was...
    - This result is still uncertain because...
    - The data do not yet support...

![Lead conclusion visual](assets/figures/fire_hull.png)
*This supports the main result by showing where the estimated fire front expands fastest along the example perimeter.*

![Supporting panel figure](assets/figures/hull_panels.png)
*These panels compare alternate ways of summarizing spread, showing that the conclusion is sensitive to how observation intervals are grouped.*

??? note "How to replace result figures"
    Upload final or near-final figures to `docs/assets/figures/`. Captions should say which claim each figure supports and what caveat a reader should remember.

## Polished Outputs { #polished-outputs }

<span id="edit-D2-G"></span>
[![D2-G: Plan](assets/stickers/tasks/d2-g.svg){ .task-sticker }](instructions/day2.md#guide-D2-G)
<span id="edit-D3-D"></span>
[![D3-D: Outputs](assets/stickers/tasks/d3-d.svg){ .task-sticker }](instructions/day3.md#guide-D3-D)
<span id="edit-D3-F"></span>
[![D3-F: Next Steps](assets/stickers/tasks/d3-f.svg){ .task-sticker }](instructions/day3.md#guide-D3-F)

The most reusable outputs from this example are a brief PDF, a small code workflow, the final spread-rate figures, and a handoff note explaining what would need to be checked before making any operational claim.

The next step would be to test the same workflow on a second fire event and compare whether the same simple spread metrics remain interpretable.

??? note "D2-G / D3-D / D3-F: How to edit polished outputs"
    Replace this section with the final things you want people to find after the summit: polished figures, a PDF, slides, a notebook, a data product, or a short handoff note.

![Complementary result figure](assets/figures/main_result.png)
*This public-facing figure summarizes the example workflow from perimeter observations to a cautious spread-speed interpretation.*

[Read the project brief PDF](assets/files/project_brief.pdf){ .md-button .md-button--primary }
[Compare computing costs](https://what-uses-more.com){ .md-button }

## Cite & Reuse

This example page cites the reusable OASIS template [@oasisProjectTemplate] and a classic fire spread modeling reference [@finney1998]. Replace these with the sources, datasets, software, and project outputs your group actually used.

License: MIT unless noted. See dataset licenses on the **[Data](data.md)** page.

??? note "How to edit citations and site health"
    Add sources to `docs/references.bib`, then cite them with citation keys such as `[@oasisProjectTemplate]`.

    Keep the generated Site Health report visible in Edit Mode while preparing the page:

    --8<-- "_site_health.md"

{{ references }}
