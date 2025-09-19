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

# Configure iRODS (accept defaults for Host/Port/Zone; use your CyVerse username)
./gocmd init

# Quick sanity check: can you list your home?
./gocmd ls i:/iplant/home/YOUR_USER
```

> `i:` indicates an iRODS remote path. Omit `i:` for local filesystem paths.

**Example transfers:**

```bash
# Single file download (shared path → local ./data/)
./gocmd get --progress -K --icat \
  i:/iplant/home/shared/earthlab/nfs_career/outputs/SUMMER_2024/Buffalo_creek-BC1-06_20_24/Buffalo_creek-BC1-06_20_24_1_all_layers.tif \
  ./data/

# Folder download (entire collection)
./gocmd get --progress -K --icat -r \
  i:/iplant/home/shared/earthlab/nfs_career/outputs/SUMMER_2024/Buffalo_creek-BC3-06_20_24 \
  ./data/

# Upload a results folder to your home
./gocmd put --progress -K --icat -r \
  ./outputs/run_01 \
  i:/iplant/home/YOUR_USER/projects/myproj/outputs/run_01

# Optional sync-like upload to skip unchanged files
./gocmd put --progress -K --icat --diff -r \
  ./outputs/run_01 \
  i:/iplant/home/YOUR_USER/projects/myproj/outputs/run_01
```

> **Troubleshooting:**
```bash
# If a path "is not found", list upward, then drill down to confirm exact names
./gocmd ls i:/iplant/home/shared/earthlab/nfs_career/outputs/SUMMER_2024
./gocmd ls i:/iplant/home/shared/earthlab/nfs_career/outputs/SUMMER_2024/Buffalo*

# Inspect type and permissions if a collection exists but transfers fail
./gocmd stat i:/iplant/home/shared/earthlab/nfs_career/outputs/SUMMER_2024/<EXACT_NAME>
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
* Save all of your scripts and notebooks in the [code/](https://github.com/cu-esiil/Project_group_OASIS/tree/main/code) folder. This keeps everyone’s work in one place and makes it easy to find later. Don’t worry if your code isn’t perfect—the important thing is to make it runnable and shareable.
* After you’ve run your code, take a screenshot or save the result as a file. Then add it to the **Code** page (`docs/code.md`) so others can see what your code does. Even a quick plot or table is great!
* On **Code** (`docs/code.md`), add a short entry for each workflow: what it does, required inputs, how to run it, and where to view the output (linked image, iframe, or hosted artifact). Use the template below to get started:

````markdown
### Fire perimeter analysis
**What this code does:** Shows how fire perimeters grow each day using FIRED polygons.  
**Inputs needed:** `data/fired_perimeters.geojson`  
**How to run it:**
```bash
python code/fire_perimeter_analysis.py
```
**What to look for:** The script makes a plot of fire spread over time.  
**Results:** [spread_plot.png](results/spread_plot.png)
````

## 5) Day 2 checklist

* [ ] 2–4 data sources listed with links on **Home**.
* [ ] 1–2 methods listed on **Home**.
* [ ] At least one prototype visual added.
* [ ] Code linked from **Code** page.
* [ ] Large files moved via gocmd (or linked externally).

