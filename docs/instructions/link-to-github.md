---
layout: page
title: Link JupyterLab to GitHub
permalink: /instructions/link/
---

# Link JupyterLab to GitHub

We now use GitHub web authentication as the main way to connect JupyterLab to GitHub. This is easier for most participants than SSH. You will run a small notebook, copy a one-time code, approve the login in GitHub, and then return to JupyterLab to finish setup.

Use this page when you need to authenticate GitHub, clone your project repository, or refresh your credentials after they time out.

## Step 1 — Launch the OASIS JupyterLab app

[Launch the OASIS JupyterLab app](https://de.cyverse.org/apps/de/c0956b30-3f32-11f0-9712-008cfa5ae621/launch){ .oasis-launch-button target="_blank" rel="noopener" }

Click the launch button and wait for the CyVerse/VICE JupyterLab instance to start. This can take a few minutes.

The container opens with a `startup` folder. Inside that folder is the notebook you will use for GitHub login:

```text
startup/github_web_auth.ipynb
```

If you want to see the app page before launching, use the [non-launch app page](https://de.cyverse.org/apps/de/c0956b30-3f32-11f0-9712-008cfa5ae621){ target="_blank" rel="noopener" }.

## Step 2 — Open the GitHub web auth notebook

In JupyterLab, use the file browser on the left to open:

```text
startup/github_web_auth.ipynb
```

This notebook handles GitHub web authentication for the running JupyterLab instance.

## Step 3 — Run the first cell and approve GitHub login

Run the first notebook cell.

It starts GitHub CLI web authentication and prints two important things:

- a one-time code, such as `6C3C-5CE8`
- a GitHub device login link, usually `https://github.com/login/device`

Then:

1. Copy the one-time code from the notebook output.
2. Open the GitHub device login link in a browser.
3. Paste the code when GitHub asks for it.
4. Continue through the GitHub authorization screens.
5. Approve the authentication.

There may be several clicks and device authentication steps. That is normal.

## Step 4 — Run the second cell to save the authentication

After GitHub says authentication is complete, return to `startup/github_web_auth.ipynb`.

Run the second notebook cell.

This configures Git to use the GitHub web authentication you just approved. After this step, Git pushes and pulls should work through HTTPS in this JupyterLab instance.

## Step 5 — Add Git identity on first commit or push

Authentication proves that you have access to GitHub. Git may still need to know who should be credited for the commits you make.

On your first commit or push, Git may ask for:

- your GitHub name
- your GitHub email

This is normal. It tells Git who should be credited for changes made from this JupyterLab instance.

## Step 6 — Clone your repository using HTTPS

Before cloning, make sure the file browser is at the top folder level. You should see folders such as `data`, `home`, `Project_group_OASIS`, or `startup`.

Do not clone from inside `data` or `home`; the Git sidebar works best when you start from the top level.

Then clone the repository:

1. Click the Git icon in the left sidebar.
2. Use the blue Git action buttons.
3. Click **Clone a Repository**.
4. Paste the HTTPS repository link.
5. Click **Clone**.
6. Confirm that the repository appears in the left file browser.

Use the HTTPS clone link for this workflow. This is different from the SSH clone link used in older instructions. SSH still works as a backup for advanced users, but HTTPS is the recommended path for the workshop.

### How to copy the HTTPS clone link

1. Open your project repository on GitHub.
2. Click the green **Code** button.
3. Choose the **HTTPS** tab.
4. Copy the URL. It should look like:

```text
https://github.com/CU-ESIIL/Project_group_OASIS.git
```

Use your group’s repository URL, not necessarily the example above.

## Step 7 — Push and pull changes

After the repository is cloned and web authentication is configured, you should be able to push and pull using the JupyterLab Git interface.

For the usual editing workflow, use:

1. **Pull** before you start editing.
2. Edit files.
3. Stage changed files.
4. Commit with a short message.
5. Push your commits to GitHub.

See [Git/GitHub Widget in JupyterLab](push-to-github.md) for the day-to-day Git sidebar workflow.

## If authentication stops working

GitHub web authentication can expire, especially if the instance is left running for a few days.

Common symptoms:

- pushing stops working
- GitHub or Git asks for credentials again
- the Git interface no longer has permission

Fix it by repeating the notebook authentication:

1. Reopen `startup/github_web_auth.ipynb`.
2. Run the first cell.
3. Copy the new one-time code.
4. Approve the GitHub device login.
5. Return to the notebook.
6. Run the second cell again.

You do not need to reclone the repository just because authentication expired.

## SSH backup option

SSH is no longer the main workflow for this workshop. Use GitHub web authentication and HTTPS cloning first.

Advanced users can still use SSH as a backup if they already know how to manage keys in temporary JupyterLab environments:

1. Create an SSH key inside the running JupyterLab instance.
2. Add the public key to GitHub under **Settings → SSH and GPG keys**.
3. Use the SSH clone link, which looks like `git@github.com:ORG/REPO.git`.
4. Make sure the repository remote uses SSH instead of HTTPS.

If you are unsure which path to use, use the web authentication notebook and the HTTPS clone link.
