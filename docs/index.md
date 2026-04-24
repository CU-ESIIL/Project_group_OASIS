# OASIS Fire Speed Working Example

![Forest landscape with fire-speed contours](assets/hero/hero.jpg)

**Purpose:** This example front page shows how a project group can turn a 3-day sprint into a clear public story: a focused question, a visible team, early artifacts, method choices, uncertainty, and polished share-out figures.

## People

<div class="people-grid" markdown>

--8<-- "people/jane-doe.md"

--8<-- "people/john-smith.md"

</div>

## Idea Generation & Collaboration

The group began with a practical question: how can fire perimeter data be translated into visuals that make spread speed easier to compare across events, places, and time windows? That framing borrows from earlier fire-spread modeling work [@finney1998].

![Whiteboard notes from early framing](assets/whiteboards/day1_whiteboard.jpg)
*Early notes captured the core comparison problem: speed is not just where fire moved, but how quickly the boundary changed and where uncertainty enters the story.*

Useful starting points included perimeter datasets, prior fire-spread literature, and lightweight visualization tools that could produce interpretable figures quickly.

- **Fire perimeter records** — used to derive spatial change through time.
- **Time-step comparison workflows** — used to test whether spread could be summarized consistently.
- **Small-multiple figures** — used to compare events without requiring an interactive dashboard.

## Methods Development & Early Results

The first pass focused on producing quick visual artifacts rather than a perfect model. The group tested data joins, time-window choices, and figure layouts to see which outputs made the main pattern easiest to inspect.

![Early exploration plot](assets/explorations/explore_data_plot.png)
*First-pass output showing whether the available data can support a visible comparison. This kind of rough figure is useful even when it exposes gaps or confusing assumptions.*

<p><a class="md-button" href="data.md">Open data notes</a></p>

Early method notes:

- Convert perimeter change into comparable time intervals.
- Flag gaps where time stamps or geometry quality limit interpretation.
- Use static figures first, then decide whether an interactive view is worth the extra effort.

<p><a class="md-button" href="https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code">View shared code</a></p>

## Refinement

Refinement should turn rough artifacts into claims. For this example, the most useful shift is from “we mapped fire perimeters” to “we can compare where and when perimeter change was fastest, with caveats about data timing.”

![Static fire-speed figure](assets/figures/figure1.png)
*Figure 1. A refined static figure should identify the key pattern and explain what decision or scientific question it supports.*

![Animated perimeter-change concept](assets/figures/change.gif)
*Figure 2. A short animation can show change through time, but the caption should still name the uncertainty that remains.*

## Polished Results & Figures

The final share-out should make a small number of evidence-backed claims. Keep each claim tied to a figure, notebook, data product, or other artifact.

### Headline Takeaway

Fire-spread comparison becomes more reusable when perimeter change is summarized as a small set of time-aware visual products rather than a long activity log.

### Core Insights

- **Comparable time steps matter:** Fire-speed visuals are only as interpretable as the time windows behind them.
  **Evidence:** [Lead conclusion visual](assets/figures/fire_hull.png)
  **Confidence:** Medium — the workflow is useful, but source-data timing still limits precision.

- **Panel figures help reveal where the method works:** Small multiples make it easier to compare events and notice outliers.
  **Evidence:** [Supporting panel figure](assets/figures/hull_panels.png)
  **Confidence:** Medium — the visual pattern is clear, but the layout still needs testing with more events.

- **A reusable output beats a one-time map:** The strongest product is a workflow that another group can rerun with new perimeter data.
  **Evidence:** [Shared code](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code)
  **Confidence:** Low to Medium — the template exists, but each new dataset needs validation.

![Lead conclusion visual](assets/figures/fire_hull.png)
*Primary result. This figure should carry the main claim for the public share-out.*

![Supporting panel figure](assets/figures/hull_panels.png)
*Supporting result. This panel should show comparison, uncertainty, or a useful failed attempt.*

![Complementary result figure](assets/figures/main_result.png)
*Complementary result. This figure should point toward the next version of the workflow.*

<p><a class="md-button md-button--primary" href="assets/files/project_brief.pdf">Read the project brief PDF</a></p>

## Next Steps

- Test the workflow on additional fire events.
- Add a confidence field to each figure or data product.
- Turn the most reusable steps into a short notebook.
- Share the outputs with groups comparing disturbance speed, recovery, or monitoring workflows.

<p><a class="md-button" href="https://what-uses-more.com">Compare computing costs</a></p>

## Cite & Reuse

This site is a reusable project-group template [@oasisProjectTemplate]. Replace this example citation with the sources, datasets, and software your group actually used.

License: MIT unless noted. See dataset licenses on the **[Data](data.md)** page.

{{ references }}

## Site Health

--8<-- "_site_health.md"
