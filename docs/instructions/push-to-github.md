---
layout: page
title: Push and Pull with the JupyterLab Git Widget
permalink: /instructions/push/
---

# Push and Pull with the JupyterLab Git Widget

This page covers moving code, Markdown, notebooks, and small project files between your JupyterLab instance and GitHub. Do not use GitHub for large data. Use persistent storage for large files and outputs.

## The CRT cloud workflow

In the Cloud Triangle, this page covers **instance to/from GitHub**.

!!! info "Cloud Triangle pages"
    1. [Connect instance to GitHub](link-to-github.md)
    2. **Instance to/from GitHub:** this page
    3. [Instance to/from persistent storage](save-to-persistent-storage.md)

!!! tip "What goes where?"
    Code and text go to GitHub. Large data and outputs go to persistent storage. Active work happens in JupyterLab.

| Task | Best tool |
|---|---|
| Edit the website text | GitHub / Git widget |
| Save a notebook or script | GitHub / Git widget |
| Save a small figure used on the site | GitHub / Git widget |
| Save a large dataset | Persistent storage / `gocmd` |
| Save model outputs or large intermediate files | Persistent storage / `gocmd` |
| Work interactively during a session | JupyterLab |
| Share final public code | GitHub |
| Share final public data | Persistent storage or approved data archive |

GitHub is not the place for large raw datasets, huge rasters, model outputs, or temporary working files. Put those in persistent storage and commit a small note, README, or metadata file to GitHub that explains where the data lives.

Before using this page, complete [Connect instance to GitHub](link-to-github.md) so HTTPS push and pull work from this JupyterLab instance.

[Launch the OASIS JupyterLab app](https://de.cyverse.org/apps/de/c0956b30-3f32-11f0-9712-008cfa5ae621/launch){ .oasis-launch-button target="_blank" rel="noopener" }

## 1) Open the Git panel

1. Make sure you are in the **top-level folder of your repository** in the File Browser.
2. On the **left sidebar**, click the **Git icon** (branch symbol). Two possible views appear.

### A) Not in a repository

If you are not inside a Git repo folder, the Git panel shows three large blue buttons:

- **Open the FileBrowser** — takes you back to the file browser.
- **Initialize a Repository** — turns the current folder into a new Git repo.
- **Clone a Repository** — copies an existing repo from GitHub into this environment.

If you see this and you already cloned the repo, navigate into the correct repo folder in the File Browser and reopen the Git panel.

If you have not cloned yet, go back to [Connect instance to GitHub](link-to-github.md) and clone with the HTTPS repository link.

### B) Inside a repository

When you are in a repo folder, the Git panel shows:

- **Current Repository** and **Current Branch**
- **Changes** and **History** tabs
- changed and untracked files
- commit message fields
- push and pull controls

Small orange dots on push or pull controls usually mean there are changes waiting to move between GitHub and JupyterLab.

## 2) Daily workflow: Pull → Stage → Commit → Push

### A) Pull changes from GitHub

Start by clicking **Pull**. This brings the latest work from GitHub into your JupyterLab instance.

Pull first so you do not accidentally work on an older copy of the project.

### B) Stage and commit your edits

1. Edit notebooks, scripts, Markdown pages, or small site assets.
2. In the **Git panel → Changes** tab, look under **Changed** and **Untracked**.
3. Stage files by clicking the **`+`** next to each file, or use **Stage All** when you are sure every listed file belongs in the commit.
4. Enter a short commit message in the **Summary** box.
5. Click **Commit**.

Commit messages should say what changed, such as:

```text
Add Day 2 data notes
```

or:

```text
Update results figure caption
```

### C) Push your commits to GitHub

Click **Push** to send your commits from JupyterLab back to GitHub.

After pushing, refresh the GitHub repository or public site to confirm the change landed.

## 3) Coordinate with teammates

When multiple people edit the same project, GitHub helps keep track of changes, but it still helps to coordinate.

Use GitHub for:

- Markdown pages
- scripts
- notebooks
- small figures used on the site
- README files and notes that explain where data lives

Use persistent storage for:

- raw datasets
- large rasters
- model outputs
- intermediate results
- temporary files that should survive after the container stops

Persistent storage is not a replacement for GitHub. It keeps data safe, but it does not provide the same version history, issue tracking, pull requests, or website publishing workflow.

## 4) Fixing common problems

### Push rejected

Cause: GitHub has changes that your JupyterLab instance does not have yet.

Fix: click **Pull** first. If conflicts appear, resolve them, commit, and push again.

### Merge conflicts

Conflicted files contain blocks labeled with your version and the incoming version, separated by a divider. They usually look like this in the editor:

```text
[start of your version]
your edits
[divider]
teammate's edits
[end of incoming version]
```

Open the file, choose what should remain, delete the conflict markers, save, stage, commit, and push.

### Wrong folder or no Git controls

If you only see the three blue buttons, you may not be inside your repo folder. Use the File Browser to open the cloned repo and reopen the Git panel.

### GitHub asks for credentials again

Your web authentication may have timed out. Reopen `startup/github_web_auth.ipynb`, repeat the first-cell device login, then run the second cell again. The full steps are on [Connect instance to GitHub](link-to-github.md).

### File is too large for GitHub

Move the file to persistent storage with `gocmd`. Then commit a small note, README, or metadata file to GitHub explaining where the data lives. Use [Instance to/from persistent storage](save-to-persistent-storage.md) for the data transfer steps.

## 5) Quick reference

- Always **Pull** first.
- Stage only the files that belong in the commit.
- Commit with a short message.
- Push your commits to GitHub.
- Put large data and outputs in persistent storage.
- Put code, Markdown, notebooks, and small website figures in GitHub.
