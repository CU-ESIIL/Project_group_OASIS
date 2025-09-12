---
layout: page
title: Using the Git/GitHub Widget in JupyterLab (JupyterHub)
permalink: /instructions/push/
---

# Using the Git/GitHub Widget in JupyterLab (JupyterHub)

This page assumes your repository **already exists** and has been cloned into JupyterHub. It also assumes you’ve already set up **SSH authentication** (see the [Link to GitHub](link-to-github.md) page before continuing).

[![Launch in CyVerse DE](https://img.shields.io/badge/Launch-CyVerse%20DE-0b6efd?style=flat-square)](https://de.cyverse.org/apps/de/faf1d268-44cc-11ed-9715-008cfa5ae621/launch?saved-launch-id=dc65718e-1964-4d11-99ad-bf901cddda99)

---

## 1) Open the Git panel

1. Make sure you are in the **top-level folder of your repository** in the File Browser.
2. On the **left sidebar**, click the **Git icon** (branch symbol). Two possible views appear:

### A) Not in a repository (screenshot view)

If you are not inside a Git repo folder, the Git panel shows **three large blue buttons**:

* **Open the FileBrowser** – take you back to the file browser.
* **Initialize a Repository** – turn the current folder into a new Git repo.
* **Clone a Repository** – copy an existing repo from GitHub into this environment.

If you see this, you need to navigate into the correct repo folder that you cloned earlier.

### B) Inside a repository (full interface)

When you are in a repo folder, the Git panel shows:

* **Top section:** *Current Repository* and *Current Branch*.
* **Tabs:** *Changes* and *History*.
* **Changes tab:** split into **Staged**, **Changed**, and **Untracked**.

  * **Staged:** files ready to commit.
  * **Changed:** modified files that Git already tracks.
  * **Untracked:** new files Git doesn’t know about until staged.
* **Bottom:** commit message fields (*Summary* and optional *Description*) and a **Commit** button.
* **Push/Pull icons:** at the very top-right of JupyterLab. Small up/down arrows show an **orange dot** when there are changes to push or pull.

---

## 2) Daily workflow: Pull → Stage → Commit → Push

### A) Pull changes from GitHub

* Always start by clicking the **Pull** button (down arrow at the top). If it has an orange dot, there are updates from GitHub.

### B) Stage and commit your edits

1. Edit notebooks, scripts, or files as needed.
2. In the **Git panel → Changes tab**, look under **Changed** and **Untracked**.
3. Stage files by clicking the **`+`** next to each, or use **Stage All**.
4. Enter a short commit message in the **Summary** box.
5. Click **Commit**.

### C) Push your commits to GitHub

* If the **Push** (up arrow) has an orange dot, click it to send your commits to GitHub.

---

## 3) Fixing common problems

### A) Push rejected (non-fast-forward)

* Cause: GitHub has changes you don’t.
* Fix: click **Pull** first. If conflicts appear, resolve them (see below).

### B) Merge conflicts

1. Conflicted files appear under **Changed** and contain conflict markers:

   ```
   <<<<<<< HEAD
   your edits
   =======
   teammate’s edits
   >>>>>>> origin/main
   ```
2. Manually fix, save, stage, commit, then push.

### C) Wrong folder / no Git controls

* If you only see the **three blue buttons**, you’re not in your repo folder. Use the File Browser to open the cloned repo and re-open the Git panel.

---

## 4) Quick reference

* **Always Pull first.**
* Then Stage → Commit → Push.
* **Changed** = modified tracked files.
* **Untracked** = new files you must stage to add.
* Look for **orange dots** on the push/pull icons.
* Commit messages go in the **Summary** box.

---

This simplified workflow covers the essential steps for using the Git widget in JupyterHub once your repo is already cloned.
