---
title: Example Project Page
---

# Example Project Page

This page shows what a completed group project can look like. Edit the [Home page](index.md) to build your own.

![Fire perimeter scaling example](assets/hero/hero.png)

Wildfire spread is often described as if it were a line advancing through a landscape. That picture is useful at small scales, but large fires are seen from satellites as changing perimeters: complicated shapes that stretch, fold, branch, and merge. Once a fire becomes a polygon, speed is no longer only about how fast a front moves. It is also about how the boundary organizes growth.

This example project asks how the geometry of a fire perimeter constrains large-scale growth. The team focused on a simple diagnostic: the relationship between burned area and perimeter length through time. If fire growth behaves like local diffusion, perimeter should scale roughly as the square root of area. If growth is increasingly controlled by boundary complexity, the exponent should rise toward a boundary-driven regime.

## People { #people }

The group combined field experience, geospatial analysis, ecological modeling, and science communication. That mix mattered because the central question was both technical and interpretive: how should a team turn satellite-derived geometry into a claim about fire behavior?

| Name | Role / affiliation | Focus | Skills |
|---|---|---|---|
| Ty Tuff | ESIIL / facilitator | Fire-growth framing | Fire modeling, open science, synthesis |
| Aakriti Joshi | Learner | Fire perimeter data | Remote sensing, GIS, Python |
| Jane Example | Learner | Figure design | Visualization, uncertainty, public communication |
| John Example | Learner | Reproducible workflow | Python, notebooks, spatial analysis |

## Project Question { #project-question }

How does the geometry of a fire perimeter constrain its growth rate at large scales?

Specifically, the group asked whether observed fire perimeters follow diffusion-like scaling, where perimeter grows approximately as area to the one-half power, or whether large events shift toward a boundary-driven scaling closer to area to the two-thirds power. The distinction is more than mathematical. A diffusion-like fire can be summarized as steady outward expansion, while a boundary-driven fire suggests that edge complexity, branching, and directional runs increasingly shape the event.

The team treated this as a Day 3 diagnostic rather than a final theory of fire behavior. The goal was to build one clear, reusable analysis that could reveal whether perimeter geometry carries information about changing growth regimes. A useful answer would show a measurable pattern, name its limits, and leave behind code that another group could run on a different fire event.

## Specialty Tracks and Strategy { #specialty-tracks-and-strategy }

The group divided into three functional roles: data acquisition, analysis, and synthesis. The data team worked with event-level fire perimeter products and checked which fields were consistent enough to compare across time. The analysis team built a small Python workflow for computing area, perimeter, and log-log scaling behavior. The synthesis team focused on turning those diagnostics into a short public story with one figure and one claim.

The team deliberately prioritized a minimal working pipeline over a broad survey. Rather than compare every available fire product, they selected a small set of representative events and asked whether the same diagnostic behaved consistently. That choice kept the work achievable during the summit and made the final result easier to explain.

This strategy also gave the group a shared decision rule. If a task did not help produce the scaling figure, the notebook, or the short interpretation, it moved to next steps. That constraint was useful because it turned a large geospatial problem into a reportable result.

## Data Exploration { #data-exploration }

The team used event-level fire perimeter data to extract time series of burned area and perimeter length. Early exploration showed strong variability across events, especially in the first observations when perimeter estimates were sparse or coarse. Within individual fires, however, plotting log perimeter against log area produced approximately linear segments, suggesting that scaling behavior could be measured with a simple diagnostic.

The first plots were most useful as quality checks. Fires with abrupt geometry changes revealed likely data artifacts or changes in observation frequency. Events with smoother growth trajectories gave the team a cleaner test bed for comparing early and late growth. The group kept both kinds of cases visible, because the messy examples clarified where the method could fail.

![Early exploration plot](assets/explorations/explore_data_plot.png)

*Figure 1. A representative perimeter diagnostic compares area and boundary length through time, giving the team a quick way to see whether growth is compact, elongated, or increasingly complex.*

## Methods and Code { #methods-and-code }

For each fire event, the team computed area and perimeter for each available time step, then estimated the scaling exponent between log perimeter and log area. They used rolling-window regressions so the exponent could change as a fire evolved, rather than forcing a single value across the whole event. This made it possible to distinguish early growth from later perimeter organization.

The workflow was intentionally lightweight. It used Python, pandas, numpy, and standard geospatial libraries to load perimeters, calculate geometry, filter invalid records, and export a summary table. The core output was a figure showing each event trajectory in log-log space, with reference slopes for diffusion-like and boundary-driven scaling.

All code was written as a reusable notebook and a small script. The notebook explains the reasoning and displays intermediate figures; the script runs the same calculation on a selected event and writes out the summary data. That split made the analysis easier to inspect during the summit and easier to reuse afterward.

[View shared code](https://github.com/CU-ESIIL/Project_group_OASIS/tree/main/code){ .md-button }

## Results { #results }

The central result is that large-fire growth is not well described by a single compact-expansion model. Across the representative events, early fire growth was often compatible with diffusion-like scaling, with exponents near one-half. As fires expanded, several trajectories shifted upward toward exponents around 0.65 to 0.7, suggesting that boundary complexity increasingly shaped growth.

This supports one clear scientific claim: as fires become larger and more organized, perimeter geometry becomes part of the growth process rather than just a byproduct of it. A fire with a more complex boundary has more places to advance, stall, or branch, and that structure can change how area accumulates through time.

![Lead result visual](assets/figures/main_result.png)

*Figure 2. Representative log-log trajectories show a transition from compact early growth toward more boundary-driven scaling as fire events expand.*

The interpretation is promising but limited. Perimeter resolution, observation frequency, and smoothing choices all affect the measured exponent. Early fire boundaries can be especially uncertain, and a single daily perimeter may hide important sub-daily growth. The result should therefore be read as a geometric diagnostic, not a complete explanation of fire behavior.

Even with those limits, the diagnostic was useful. It gave the group a compact way to compare events, identify transitions, and discuss whether a fire was growing mainly by expansion, elongation, or boundary reorganization. That is exactly the kind of reusable synthesis a summit project can leave behind.

## Polished Outputs { #polished-outputs }

The group produced three reusable outputs: a notebook, a summary figure, and a short methods note. The notebook computes area-perimeter scaling for any selected fire event and exports the rolling exponent. The figure provides a compact visual summary of regime transitions. The methods note explains the assumptions and warns future users about resolution, smoothing, and early-observation uncertainty.

These outputs are designed to be extended by future groups. A next team could apply the same workflow to simulated fire data, compare multiple perimeter products, or test whether similar scaling appears under different fuels and weather conditions. The deliverable is not a final fire model. It is a clear diagnostic that makes one geometric question easier to ask.

[Read the project brief PDF](assets/files/project_brief.pdf){ .md-button .md-button--primary }

## Cite & Reuse

This example uses the Project OASIS template citation flow [@oasisProjectTemplate]. Reuse the structure, figures, and workflow patterns with attribution where appropriate. Dataset-specific credits and licenses should be added when a group replaces the example data with real perimeter products.

## Next Steps

Next steps include applying the framework to simulated fire perimeters where the true growth process is known, then comparing those results with observed fire products. The group also recommended testing how spatial resolution, smoothing, and observation interval affect the scaling exponent. Those checks would help determine when the diagnostic reflects fire behavior and when it mostly reflects the measurement system.

More broadly, geometric diagnostics like this could become useful screening tools for fire modeling. Before building a complex model, a team could ask whether an event looks compact, elongated, boundary-driven, or unstable. That first pass would not replace process-based modeling, but it could make model choice and interpretation more transparent.

{{ references }}
