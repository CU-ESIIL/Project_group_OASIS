---
layout: page
title: Day 2 — Data & Methods
permalink: /instructions/day2/
---

# Day 2 — Data & Methods
**Focus:** try a few datasets and analyses. Keep it visual, keep it simple. Update the site to reflect what you test.

## 1) Explore the Data Library & Analytics Library
- Browse your **Data Library** for candidate datasets (portals, STAC catalogs, archives). Capture links and notes.
- Browse your **Analytics Library** for example workflows (scripts, notebooks).
- Log 2–4 promising items on **Home** → `docs/index.md` under:
  - **Data sources we’re exploring** (links + 1-line notes)
  - **Methods / technologies we’re testing** (stats, models, viz)

## 2) Transfer or access data via gocmd (if needed)
> Use when moving files to/from institutional storage (e.g., CyVerse Data Store).

**Install & initialize gocmd (Linux):**
```bash
# Download latest gocmd and extract
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -

# Initialize and verify identity
./gocmd init
./gocmd whoami
```

**Example transfers:**

```bash
# Upload a local file to the Data Store
./gocmd put ./outputs/figure1.png /iplant/home/YOUR_USER/sprint/figure1.png

# Download from the Data Store to your working dir
./gocmd get /iplant/home/YOUR_USER/sprint/input.csv ./data/input.csv
```

> Keep large data out of GitHub. Store externally, link from the **Data** page.

## 3) Show early results (visual-first)

* Add **Prototype visuals** on **Home** → `docs/index.md`:

  * A static figure (PNG)
  * A small GIF for change over time (if you have one)
  * An iframe map or relevant portal view
* Add brief captions: what it shows and why it matters.

## 4) Link runnable code

* Put scripts/notebooks in `src/`.
* On **Code** (`docs/code.md`), add a short entry per script: what it does, inputs, how to run.
* Keep names clear: `src/pipeline.py`, `src/notebooks/explore.ipynb`.

## 5) Day 2 checklist

* [ ] 2–4 data sources listed with links on **Home**.
* [ ] 1–2 methods listed on **Home**.
* [ ] At least one prototype visual added.
* [ ] Code linked from **Code** page.
* [ ] Large files moved via gocmd (or linked externally).

