# Project Group OASIS — Starter Website & README Kit

This guide is written for people who may be brand new to GitHub. It will show you, step by step, how to use this repository as both:

1. A **website** to communicate your science to others.
2. A **hub for sharing code** within your group.


**Template users:** If you are using this repository as a template, start with [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) for the required name and link updates.

---

## 1) Understanding the Repository

Think of this repository like a **shared online folder**. Inside it, there are a few important parts:

* **README.md** — This file (what you are reading now). It explains how things work.
* **data/** — Optional. Small datasets can go here.
* **outputs/** — Optional. Figures, results, and reports can go here.

### Storage

- **Code (`code/`)** — Share scripts, notebooks, and analysis utilities. Keep filenames clear and include short comments at the top so teammates understand the purpose quickly.
- **Documentation (`docs/` and `documentation/`)** — Everything inside `docs/` powers the public website, while `documentation/` can host internal notes or extended write-ups. Update these areas regularly so the story on the site and your working docs stay in sync.

---

## 2) How to Update the Website

The website is built from the `docs/` folder. Every time you change a file there, the website updates automatically.

### Step by Step

1. In the repository, click the **docs/** folder.
2. Click on `index.md`. This is the home page of your website.
3. In the top right, click the pencil icon (✏️) to edit.
4. Change the text to describe your project (for example, add your team’s name and a short description of what you’re studying).
5. Scroll down. In the **Commit changes** box, write a short message like `updated homepage with project info`.
6. Click **Commit changes**.

> That’s it! In about a minute, refresh your website link and you’ll see your changes.

**Note:** If your website is not set up yet, go to **Settings → Pages → Build and deployment**. Set the Source to **Deploy from a branch**, then choose `main` and `/docs`. GitHub will give you a link to your site.

---

## 3) How to Share Code

Code lives in the `src/` folder. You can put scripts, Jupyter notebooks, or R files here.

### Step by Step

1. In the repository, click the **src/** folder.
2. Click **Add file → Upload files** (to add something from your computer), or **Create new file**.
3. Name your file something clear, like `data_cleaning.py` or `fire_analysis.R`.
4. At the top of the file, write a short comment about what the code does.
5. Scroll down, write a commit message like `added first data cleaning script`, and click **Commit changes**.

Now your teammates can see and use your code.

---

## 4) Common Tasks

* **Add a new webpage:** Create a new `.md` file inside `docs/` (like `methods.md`). It will become a new page on your site.
* **Add a picture:** Put the file in `docs/assets/` and add it to a page with `![caption](assets/filename.png)`.
* **Add team members:** Edit `docs/team.md` to add names and roles.

---

## 5) Tips for Beginners

* Don’t worry about breaking things — everything can be fixed, and old versions are saved.
* Small updates are valuable. Even a one-line change is a real contribution.
* Write commit messages as if explaining to your future self.
* Large data files (over \~50 MB) should not go in GitHub. Instead, link to them from the `data/` page.

---

## 6) Learn More

* [GitHub Pages basics](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
* [Editing files in your browser](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)

---

## 7) First Things to Try

1. Edit the `docs/index.md` file and add your project description.
2. Add yourself to the `docs/team.md` page.
3. Upload your first code file to the `src/` folder.
4. Refresh your website link and see your changes live.

Congratulations — you’re now using GitHub to communicate your science and share code!

---

## Beginner Mode: From zero to website (no command line)

> This section is written for someone who has **never used GitHub**. Follow it in order. You can do all of this in your web browser.

### What you need

* A GitHub account (free). If you don’t have one: [https://github.com](https://github.com) → **Sign up**.
* A link to your group’s repository (ask your instructor/lead if you don’t have it).

### Step 1 — Join your group’s repo

1. Open the invitation link you received by email or in GitHub notifications.
2. Click **Accept invitation**. You now have permission to edit.

**Why this matters:** GitHub only lets approved people change files. Accepting the invite gives you access.

### Step 2 — Open the project home

1. Visit your repository link (it looks like `https://github.com/ORG/Project_group_OASIS`).
2. You’ll see folders like `docs/`, `src/`, and files like `README.md`.

**Why this matters:** This is the “front door” to your project’s files.

### Step 3 — Turn on the website (GitHub Pages)

1. Click **Settings** (top menu of the repo).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose **main** and **/docs** folder.
5. Click **Save**. A green box will show the site link after it builds (usually 1–2 minutes).

**Why this matters:** This tells GitHub to publish everything inside `docs/` as a website.

### Step 4 — Edit the homepage text

1. Click the **Code** tab to return to the file view.
2. Open the `docs/` folder → click `index.md`.
3. Click the **pencil icon** to edit.
4. Change the title and first paragraph so they describe your project.
5. Scroll to the bottom, write a short **Commit message** (for example: `update homepage`).
6. Click **Commit changes**.

**Why this matters:** Saving (committing) creates a new version of your page and triggers the website to rebuild.

### Step 5 — See your changes online

1. Go back to **Settings → Pages** (or use the link shown there).
2. Open your site in a new tab.
3. Refresh after a minute if you don’t see changes yet.

**Why this matters:** Now you can share a public link to your project.

### Step 6 — Add a new page

1. In the `docs/` folder, click **Add file → Create new file**.
2. Name it something like `methods.md`.
3. Paste a small outline (what, why, how) and click **Commit changes**.
4. To add it to the top navigation, open `docs/_config.yml`, find `header_pages:`, and add `- methods.md` on its own line. Commit.

**Why this matters:** You can grow your site one page at a time.

### Step 7 — Add an image

1. Open `docs/assets/` → **Add file → Upload files** → pick your image.
2. In a page (e.g., `index.md`), insert: `![Alt text](assets/your_image.png)` and commit.

**Why this matters:** Images help explain your science.

### Step 8 — Share code with the team

1. Open the `src/` folder → **Add file** → upload a script or create a new file.
2. At the top of the file, write 2–3 lines that explain what it does, inputs, and outputs.
3. Commit changes.
4. In `docs/code.md`, add a short bullet linking to your file, e.g. `- src/pipeline.py — end-to-end pipeline` and commit.

**Why this matters:** The website becomes a clear map that points to your working code.

### Step 9 — Post an update

1. Open `docs/updates.md` → pencil icon.
2. Add a new dated section (copy the example) with 1–3 bullets of what changed.
3. Commit.

**Why this matters:** Small updates build a readable project history.

### Step 10 — Share the site link

* Copy the Pages URL from **Settings → Pages** and send it to your group or stakeholders.

**You’re done.** You’ve published a site and shared code without using the command line.

---

## Quick‑start checklist (printable)

* [ ] I can open the repo and see `docs/`, `src/`, and `README.md`.
* [ ] Pages is enabled: **main** + **/docs**.
* [ ] I edited `docs/index.md` and committed changes.
* [ ] I can open the public site link and see my edits.
* [ ] I added or uploaded one script to `src/`.
* [ ] I linked that script from `docs/code.md`.
* [ ] I posted one dated entry in `docs/updates.md`.

---

## Plain‑language glossary

* **Repository (repo):** Your project’s online folder.
* **Commit:** A saved change with a short note. Think “Save with a message.”
* **Branch:** A workspace for changes. Beginners can stay on **main**.
* **Pull request (PR):** A proposal to merge changes. Useful later; optional for now.
* **GitHub Pages:** A way to turn files in `docs/` into a website.
* **Markdown (`.md`):** A simple text format for writing pages with headings, links, and images.

---

## Troubleshooting (common fixes)

**I don’t see the Pages option.**
You might not have permission. Ask your lead to enable it, or ensure you’re in the repository’s **Settings** (not your user settings).

**My site URL shows 404.**
Wait 1–2 minutes after enabling Pages or after a commit. Refresh. Confirm **Source** is set to **Deploy from a branch** and **Branch** = `main` and **Folder** = `/docs`.

**My changes didn’t appear.**
Refresh the site. Confirm you edited a file inside `docs/`. Check commit history on the repo’s home page to see if your change saved.

**Images don’t load.**
Make sure the image is inside `docs/assets/` and the link is `![Alt text](assets/your_image.png)` (no leading slash).

**I uploaded a big file and got an error.**
GitHub limits file size. Keep data small in the repo. Link to external storage for big datasets.

**I’m afraid of breaking things.**
Every change is tracked. You can always edit again or revert. Small, frequent commits are safest.

---

## Teaching notes (why this pedagogy works)

* **Immediate reward:** Editing `index.md` shows a visible website change fast.
* **One mental model:** “Files in `docs/` become web pages.”
* **Low friction:** No installs or command line required.
* **Narrated steps:** Each action explains *why* it matters to build understanding.

---

## Next level (optional, later)

* Use branches + pull requests for review before merging to `main`.
* Add a `requirements.txt` or `environment.yml` to document software packages.
* Create a `CONTRIBUTING.md` with team norms (naming, reviews, issue labels).
* Add automatic checks (CI) to run tests when code changes.

