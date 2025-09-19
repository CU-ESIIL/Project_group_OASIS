---
layout: default
title: "OASIS: 3-Day Team Template"
subtitle: "A friction-free guide for collaborative research sprints"
hero_image: assets/template/hero.svg
team_logo: assets/template/team-logo.svg
contact_slack: "#oasis-project-room"
contact_email: "team@example.org"
repo_owner: "cu-esiil"
repo_name: "Project_group_OASIS"
edit_path: "docs/project_template.md"
---

# {{ page.title }}

{{ page.subtitle }}

{% if page.hero_image %}
<img src="{{ page.hero_image }}" alt="Hero Image" />
{% else %}
<div style="width:100%;height:200px;background:#eee;display:flex;align-items:center;justify-content:center;">Set `hero_image` in front matter</div>
{% endif %}

{% if page.team_logo %}
<img src="{{ page.team_logo }}" alt="Team Logo" />
{% endif %}

[✏️ Edit this page](https://github.com/{{ page.repo_owner }}/{{ page.repo_name }}/edit/main/{{ page.edit_path }})  
Slack: {{ page.contact_slack }} · Email: [{{ page.contact_email }}](mailto:{{ page.contact_email }})

*If this link 404s, set `repo_owner`, `repo_name`, and `edit_path` in the front matter.*

<nav style="position:sticky; top:0; background:#fff; padding:0.5rem; border-bottom:1px solid #ccc;">
[Day 1](#day1) · [Day 2](#day2) · [Day 3](#day3) · [Resources](#resources)
</nav>

## Contents
- [Day 1](#day1)
- [Day 2](#day2)
- [Day 3](#day3)
- [Resources](#resources)
- [FAQ](#faq)

<a id="day1"></a>
<details>
<summary><strong>Day 1 — Kickoff &amp; Page Setup</strong></summary>

### Objectives
- Form your team and assign roles
- Draft a project one-liner to align expectations
- Swap in your hero and team images
- Make and push your first commit

### Steps
1. **Project One-liner** – In one sentence, describe what you will explore.  
   *Example: *Collect and analyze rainfall data to model flash flood risks.*
2. **Edit this page** – Replace placeholders in the front matter above.
3. **Team Roles** – Fill in the table:

```markdown
| Role  | Name | Responsibilities |
|---|---|---|
| Lead | _(your name)_ | Coordinates tasks, keeps time |
| Data | _(your name)_ | Finds/preps data, documents sources |
| Methods | _(your name)_ | Runs analysis, records parameters |
| Comms | _(your name)_ | Summarizes outcomes, crafts visuals |
```

4. **Swap Images** – Follow the Image Replacement Micro-Guide in [Resources](#resources) to update `hero_image` and insert a team photo.
5. **Commit & Push**  
   - *Web editor:* click **✏️ Edit this page**, make changes, write a short commit message, and **Commit changes**.  
   - *Clone route:* `git clone <repo-url>` → edit locally → `git add -A` → `git commit -m "initial setup"` → `git push`.

### Copy-paste Snippet
```markdown
Project one-liner: _(write it here)_
```

### Day 1 Checklist
- [ ] One-liner added
- [ ] Team roles filled
- [ ] Hero & team images swapped
- [ ] Commit pushed to main

</details>

<a id="day2"></a>
<details>
<summary><strong>Day 2 — Data &amp; Analysis Sandbox</strong></summary>

### Objectives
- Pick a dataset and document its source
- Run a tiny analysis using Python or R
- Save at least one result figure
- Note what worked or failed

### Steps
1. **Explore Libraries** – Start with these resources:
   - [Data Library](https://example.com/data-library) – replace with real link.
   - [Analytics Library](https://example.com/analytics-library) – replace with real link.
2. **Select Data** – Choose one dataset and note its source.
   *Example: *NOAA daily precipitation for Boulder County.*
3. **Set Up Tools** – Optional `gocmd` quickstart for Linux:

```bash
# Linux quickstart
GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -
./gocmd init

# Quick sanity check: can you list your home?
./gocmd ls i:/iplant/home/YOUR_USER
```

   > *(macOS uses a different tarball)*
4. **Minimal Analysis** – Run one of the snippets:

```python
# Python example
import pandas as pd
url = "https://example.com/data.csv"  # replace with real URL
df = pd.read_csv(url)
print(df.head())
```

```r
# R example
url <- "https://example.com/data.csv"  # replace with real URL
df <- read.csv(url)
head(df)
```

5. **Record Results** – Save a figure into `assets/results/`:

```markdown
<!-- Save figures into assets/results/ and reference below -->
![Result Figure](assets/results/example.png)
```

6. **Document Learnings** – Jot down commands or pitfalls in the Results section.

### Day 2 Checklist
- [ ] Dataset chosen and cited
- [ ] Analysis snippet executed
- [ ] Figure saved to assets/results/
- [ ] Notes captured in Results section

</details>

<a id="day3"></a>
<details>
<summary><strong>Day 3 — Plan &amp; Share</strong></summary>

### Objectives
- Draft a plan-on-a-page for next steps
- Create a short communication artifact
- Prepare a demo for sharing
- Decide who will own follow-ups

### Steps
1. **Plan on a Page** – Outline what’s next:
   - [ ] Goals
   - [ ] Data needed
   - [ ] Methods to try
   - [ ] Roles & timeline
2. **Comms Box** – Prepare a 100-word abstract and image:

```markdown
<!-- 100-word abstract example -->
Climate extremes threaten mountain ecosystems. In three days we built a rainfall model
and produced early visualizations to guide local decision-makers.

<!-- Replace the image below with your artifact -->
![Outreach Graphic](assets/results/placeholder.png)
```

3. **Demo Checklist**
   - [ ] Show the updated project page
   - [ ] Display one analysis result
   - [ ] Share the plan-on-a-page
   - [ ] Collect feedback and record next actions

### Day 3 Checklist
- [ ] Plan drafted
- [ ] Abstract & image added
- [ ] Demo items rehearsed
- [ ] Next steps assigned

</details>

## Resources
<a id="resources"></a>

### Image Replacement Micro-Guide
1. **Save** your image as a simple filename, e.g., `team.jpg` (no spaces).
2. **Upload** it to `docs/assets/team/` (or `assets/team/` if this page is at repo root).
3. **Reference** it in Markdown: `![Team Photo](assets/team/team.jpg)`.
4. If the image doesn’t show: check for typos and confirm the path in GitHub.

```markdown
<!-- Replace the image below with your team photo -->
![Team Photo](assets/team/team.jpg)
```

*Encourage per-team folders like `assets/team-alpha/`, `assets/team-bravo/`, etc., to avoid collisions.*

> **Tip:** If your image doesn’t render, open it in the repo to copy the exact path.
> **Warning:** Don’t rename folders in `assets/` after linking them on the page.

### Common Pitfalls & How to Avoid Them
- [ ] Broken image paths → use `assets/<team>/filename.ext` and avoid spaces.
- [ ] Editing the wrong file → use the **Edit this page** link; confirm `edit_path`.
- [ ] Merge conflicts → if collaborating, prefer **web edits** + short, frequent commits.
- [ ] Pushing from cloud notebooks → verify SSH is configured or use the web editor.

## FAQ
<a id="faq"></a>

**Q: The edit link doesn’t work.**  
A: Update `repo_owner`, `repo_name`, and `edit_path` in the front matter.

**Q: Where do I put large data files?**  
A: Store them outside the repo and link to them in `docs/data.md`.

**Q: Can I use branches?**  
A: Yes, but for quick sprints stick to `main` and small commits.

---

<small>
{{ page.repo_name }} — Last updated {{ site.time | date: "%Y-%m-%d" }} · Slack: {{ page.contact_slack }} · Email: [{{ page.contact_email }}](mailto:{{ page.contact_email }})
</small>

