---
layout: page
title: Day 1 — Define & Explore
permalink: /instructions/day1/
---

# Day 1 — Define & Explore
**Focus:** get to know each other, define the question and hypotheses, and make your first edits to the website. Try a simple Git pull/push from CyVerse if you have time.

## 1) Start with people
- Names, roles, what each person wants to learn or contribute in 3 days.
- Add your names to **[Team](https://cu-esiil.github.io/Project_group_OASIS/#team)** (top nav → Team). Edit the table, keep it simple.

## 2) Define your product, question(s) and hypotheses
Open **Home** → edit `docs/index.md` → fill in:
- **Our product**: describe the desired, tangible outcomes for your group
- **Our question(s)**: 2–4 bullets; invite divergent framings.
- **Hypotheses / intentions**: short, plain-language "we think…" statements.
- **Why this matters (upshot)**: who benefits and how decisions could change.

> Keep text short. One strong visual per section is ideal.

## 3) Add a quick visual (whiteboard/smartphone photo)
- Take a photo of your whiteboard or notes.
- Upload to `docs/assets/` (Code tab → docs → assets → **Add file → Upload files**).
- Reference it in `docs/index.md` under **Field notes / visuals**:
  ```markdown
  ![Whiteboard brainstorm](assets/day1_whiteboard.jpg)
  *Caption: What this shows and why it’s useful today.*
  ```

* **Commit changes** to publish.

## 4) Optional: try Git pull/push from CyVerse (basic)

> If you’re using a CyVerse Jupyter environment and want to sync with GitHub.

[![Launch in CyVerse DE](https://img.shields.io/badge/Launch-CyVerse%20DE-0b6efd?style=flat-square)](https://de.cyverse.org/apps/de/faf1d268-44cc-11ed-9715-008cfa5ae621/launch?saved-launch-id=dc65718e-1964-4d11-99ad-bf901cddda99)

**Clone the repo (HTTPS is easiest for beginners):**

```bash
# In your CyVerse terminal
cd ~
# Replace with your repo URL (green "Code" button → HTTPS)
git clone https://github.com/ORG/REPO.git
cd REPO
```

**Make a tiny change and push it back:**

```bash
echo "hello from cyverse $(date)" >> docs/updates.md
git add docs/updates.md
git commit -m "Add Day 1 note from CyVerse"
# You may be prompted for GitHub credentials (use a Personal Access Token if needed)
git push origin main
```

**Pull the latest changes (when others edit in the browser):**

```bash
git pull origin main
```

> If HTTPS auth is confusing, it’s fine to edit in the browser only. You can learn SSH keys later.

## 5) Day 1 checklist

* [ ] Team added to **Team** page.
* [ ] Questions, hypotheses, and upshot filled in on **Home**.
* [ ] One visual added (whiteboard/notes photo).
* [ ] (Optional) CyVerse: cloned repo and pushed a small change.

