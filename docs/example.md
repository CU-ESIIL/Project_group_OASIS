---
title: Example Project Page
---

# Example Project Page

![Fire spread progression over a mountain landscape](assets/hero/hero.png)

This example shows what a completed OASIS project group page can become after a team fills in the blank homepage template. It uses a fire polygon velocity project as a concrete model for writing a public-facing project story, documenting methods, sharing figures, and preserving a reusable synthesis.

We often talk about how fast a wildfire moves. But once a fire is seen from space as a changing polygon rather than a line of flame, speed stops being a single, obvious thing.

A perimeter can push forward in one direction, expand everywhere at once, wrinkle and branch, or even rearrange internally without gaining much new area. Each of these changes is real. Each can be measured. And each can yield a different answer to the same question: how fast did the fire move?

This example project takes that ambiguity seriously. It develops a practical way to think about, and measure, fire polygon velocity by comparing several definitions on the same evolving fire. The aim is not to declare a single correct metric, but to show what each measure captures, what it leaves out, and how the choice of metric shapes the story we tell about fire.

## People { #people }

This project is meant to be shaped by the people in the room: their field experience, data skills, modeling instincts, design sense, and curiosity about how spatial fire records become scientific claims.

| Name | Role / affiliation | What they are excited to work on | Skills, data, or perspective they bring |
|---|---|---|---|
| [Ty Tuff](https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners) | Learner / ESIIL | Fire polygon velocity framing | Fire modeling, open science, scientific storytelling |
| [Aakriti Joshi](https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners) | Learner | Remote sensing and perimeter interpretation | Earth observation, Python, GIS |
| Jane Example | Learner | Data visualization and public story | Figure design, uncertainty, public communication |
| John Example | Learner | Methods and reproducible workflow | Python, notebooks, spatial analysis |

## Project Question { #project-question }

How should we measure the velocity of an evolving fire polygon, and how does the choice of metric change the story we tell about fire spread?

In fire behavior science, rate of spread has a clear meaning: how quickly a flame front advances through fuel under given conditions [@finney1998]. That concept underpins both models and operational thinking.

Satellite-era fire records are different. They often arrive as daily or near-daily outlines of burned area derived from products such as MODIS, VIIRS, Landsat, MTBS, or related fire-perimeter datasets. Those outlines are not simple lines moving forward. They are shapes that grow, stretch, fold, and sometimes reorganize.

The translation from local spread to polygon change is therefore not straightforward. If a perimeter extends eastward, gains area, develops fine-scale structure, and shifts its center of mass, which of those changes counts as velocity? Different definitions answer that question in different ways.

The gap this project addresses is quiet but important: the same fire can appear fast or slow, stable or erratic, depending on how velocity is defined. Without a clear taxonomy, these differences can be mistaken for disagreement rather than recognized as different views of the same evolving system.

![Day 1 whiteboard notes](assets/whiteboards/day1_whiteboard.jpg)
*This whiteboard captures the first version of the polygon-velocity question: define what counts as movement, compare several velocity metrics, and keep metric choice visible as part of the interpretation.*

## Specialty Tracks and Strategy { #specialty-tracks-and-strategy }

The example group uses the summit tracks as a division of labor. One subgroup focuses on geospatial workflows for comparing evolving polygons. Another uses AI-assisted synthesis to organize fire-behavior concepts, metric definitions, and interpretation notes. A third focuses on visualization and communication: how to show that different velocity metrics are not competing answers, but different lenses on polygon change.

The shared strategy is to keep the fire sequence constant and change only the definition of velocity. That makes the differences among metrics visible and interpretable before introducing the additional complexity of observational data.

## Data Exploration { #data-exploration }

[Open the NDVI cube example in a new tab](assets/examples/cubedynamics_ndvi_1_year.html) →

The first data pass uses a ten-day synthetic fire sequence designed to be realistic but readable. The sequence grows directionally, develops irregular structure, and exhibits branching behavior. Starting with a controlled example allows the group to isolate geometric effects before moving to noisier satellite-derived perimeter products.

Useful data products for this example include daily perimeter polygons, derived boundary samples, area-change summaries, centroid positions, and distance-based comparisons between successive perimeters. In a real-data extension, the same workflow could be applied to MTBS, MODIS, VIIRS, Landsat, or related fire perimeter products.

![Early exploration plot](assets/explorations/explore_data_plot.png)
*This early exploration checks how much the apparent velocity changes when the same evolving polygon is summarized by different geometric measurements.*

[Open the ESIIL Data Library](https://cu-esiil.github.io/data-library/innovation-summit-2025/){ .md-button }
[Document your group data notes](data.md){ .md-button }

## Methods and Code { #methods-and-code }

The example workflow keeps the analysis intentionally small and inspectable: load the synthetic perimeter sequence, calculate seven velocity metrics for each time step, group those metrics by what they emphasize, and export figures that can be checked by someone outside the group.

The seven definitions are organized into functional groups:

- **Core baselines:** optimal transport and area gain per perimeter length.
- **Diagnostic surge detectors:** longest vector and P95 advance.
- **Conservative proxies:** mean advance and equivalent radius growth.
- **Niche translation measure:** centroid drift.

These categories are heuristic rather than exhaustive. Their purpose is to clarify how different definitions emphasize different aspects of change: growth, translation, deformation, rare advances, or stable summary behavior.

[View shared code](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code){ .md-button }

## Results { #results }

The central result is that polygon-derived velocity is not a single objective quantity. It depends on how change is defined and measured.

Three claims are worth carrying into a public share-out:

- **Velocity depends on definition.** Across the synthetic sequence, all metrics detect growth, but they diverge in magnitude and interpretation. Some emphasize rare, rapid advances; others describe steady expansion; others capture whole-system rearrangement.
- **Growth and reorganization are different signals.** Area gain per perimeter length reports velocity only when new area is added. Optimal transport, under the cost formulation used here, measures the displacement needed to transform one polygon into the next. That means a fire can show little new area gain while still undergoing substantial internal reorganization.
- **Extreme metrics are informative but selective.** The longest-vector metric highlights the single largest advance between perimeters, making it sensitive to rare leaps such as spotting or branching runs. P95 advance offers a more stable upper-tail version. These measures are useful for head-fire or surge questions, but less appropriate for typical spread.
- **Stable summaries can hide structure.** Mean advance and equivalent radius growth produce smooth, comparable time series. That stability is useful, but it can obscure anisotropy, directional runs, and boundary complexity. Centroid drift captures net migration, but misses expansion that occurs without large translation.

The same fire can support multiple, internally consistent descriptions of its motion. That does not indicate a flaw in the metrics. It reflects the fact that each definition is a lens on a complex, evolving shape. Metric choice is therefore not just a technical detail; it shapes the scientific claim.

![Lead conclusion visual](assets/figures/fire_hull.png)
*This supports the main result by showing how an evolving fire perimeter can produce different velocity interpretations depending on which geometric change is measured.*

![Supporting panel figure](assets/figures/hull_panels.png)
*These panels compare alternate summaries of the same polygon sequence, showing how stable metrics, tail metrics, and translation metrics emphasize different parts of the story.*

## Polished Outputs { #polished-outputs }

The most reusable output from this example is a practical taxonomy and decision framework for fire polygon velocity.

Specifically, the project provides:

- A side-by-side comparison of seven velocity metrics.
- A controlled synthetic sequence for interpreting metric behavior.
- A functional grouping of metrics by what they measure.
- Guidance for selecting metrics based on the question at hand.

The work is intentionally focused on method and interpretation. The synthetic sequence isolates geometry, but real satellite-derived perimeters introduce additional complexities: pixel stair-steps, temporal compositing, truncated narrow runs, and sensor-specific biases. These factors can inflate or dampen distance-based measures. The framework does not remove those uncertainties; it makes them visible.

Next steps are to carry the framework into real data and models:

- Apply the taxonomy to MTBS, MODIS, VIIRS, Landsat, and related products.
- Evaluate how resolution and smoothing affect each metric.
- Compare observed polygon velocities with model outputs.
- Develop tools that help users select metrics for specific purposes.
- Extend the framework toward a moment-based synthesis separating growth, translation, dilation, and deformation.

![Complementary result figure](assets/figures/main_result.png)
*This public-facing figure summarizes the workflow from evolving perimeter observations to a cautious, metric-aware interpretation of fire polygon velocity.*

[Read the project brief PDF](assets/files/project_brief.pdf){ .md-button .md-button--primary }
[Compare computing costs](https://what-uses-more.com){ .md-button }

## Cite & Reuse

This example page cites the reusable OASIS template [@oasisProjectTemplate] and a classic fire spread modeling reference [@finney1998]. A completed group page should also cite the fire perimeter products, software, notebooks, and project outputs used to support its claims.

License: MIT unless noted. See dataset licenses on the **[Data](data.md)** page.

{{ references }}
