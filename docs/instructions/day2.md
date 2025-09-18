---
layout: page
title: Day 2 — Data & Methods
permalink: /instructions/day2/
---

# Day 2 — Data & Methods
**Focus:** try a few datasets and analyses. Keep it visual, keep it simple. Update the site to reflect what you test.

## 1) Explore the Data Library & Analytics Library
- Browse your [**Data Library**](https://cu-esiil.github.io/data-library/innovation-summit-2025/) for candidate datasets (portals, STAC catalogs, archives). Capture links and notes.
- Browse your [**Analytics Library**](https://cu-esiil.github.io/analytics-library/innovation-summit-2025/) for example workflows (scripts, notebooks).
- Make edits on **Home** → `docs/index.md` under:
  - **Data sources we’re exploring**: Add 2-4 promising data sources (links + 1-line notes)
  - **Methods / technologies we’re testing**: Add 2-4 methods/technologies you're testing (stats, models, viz)

## 2) Transfer or access data via gocmd (if needed)
> Use when moving files to/from institutional storage (e.g., CyVerse Data Store).

**Install & initialize gocmd (Linux):**
```bash
# Download latest gocmd and extract
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -

# Initialize and authenticate
./gocmd init
./gocmd auth login  # follow prompts for CyVerse credentials

# Optionally confirm access to your home directory
./gocmd ls i:/iplant/home/YOUR_USER
```

> Remote Data Store paths must include the `i:` prefix (for example, `i:/iplant/home/...`). Local paths should omit it.

**Example transfers:**

```bash
# Upload a local file to the Data Store
./gocmd put ./outputs/figure1.png i:/iplant/home/YOUR_USER/sprint/figure1.png

# Download from the Data Store to your working dir
./gocmd get i:/iplant/home/YOUR_USER/sprint/input.csv ./data/input.csv
```

> Keep large data out of GitHub. Store externally, link from the **Data** page.

## 3) Show early results (visual-first)

* Add **Visuals** on **Home** → `docs/index.md`:

  * A static figure (PNG)
  * A small GIF for change over time (if you have one)
  * An iframe map or relevant portal view
* Add brief captions: what it shows and why it matters.

## 4) Link runnable code

* Run at least one workflow and capture a shareable output — a plot, table, map, or other scientific product. Save static outputs (PNG, GIF, JPG) to the site, or embed live results (for example, an iframe for an HTML widget or interactive table).
* Keep scripts and notebooks in `code/` with clear names (for example, `code/pipeline.py`, `code/notebooks/explore.ipynb`).
* On **Code** (`docs/code.md`), add a short entry for each workflow: what it does, required inputs, how to run it, and where to view the output (linked image, iframe, or hosted artifact).

## 5) Day 2 checklist

* [ ] 2–4 data sources listed with links on **Home**.
* [ ] 1–2 methods listed on **Home**.
* [ ] At least one prototype visual added.
* [ ] Code linked from **Code** page.
* [ ] Large files moved via gocmd (or linked externally).

