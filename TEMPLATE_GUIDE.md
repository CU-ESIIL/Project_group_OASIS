# Template Customization Checklist

This repository is a template for new project groups. After you generate a project-specific copy, walk through the sections below before adding new content. The checklist is written so you can copy/paste the steps into Codex (or any coding assistant) to make the required edits for you.

---

## 1. Prepare the repository

1. **Rename the repo** – On GitHub go to **Settings → General → Repository name** and rename it to match your project. If you already cloned the repo locally, update the remote with `git remote set-url origin <new_repo_url>`.
2. **Enable GitHub Actions** – When GitHub shows the banner “Workflows aren’t being run,” open the **Actions** tab and click **I understand, enable workflows** so deployment jobs can start.

---

## 2. Update configuration and metadata

### MkDocs configuration (`mkdocs.yml`)

Ask Codex to open `mkdocs.yml` and update the following keys so the published site shows the correct project details:

- `site_name`: plain-language project or group name (e.g., `"Mountain Snow Analysis"`).
- `site_url`: `https://<org>.github.io/<repo>` (replace with your organization/user and new repo name).
- `repo_name`: short display label such as `"ORG/Project"`.
- `repo_url`: the full GitHub URL to the repository.
- Confirm the `theme`, `nav`, and plugins look right for your project. Update any navigation labels that still reference “Project Group OASIS.”
- Update the `nav` item labeled **Your persistent storage** so it links to your team’s CyVerse folder. Replace `Group_1` in the URL with the number that matches your repository name (for example, a repo ending in `_5` should use `Group_5`). If the shared link needs a unique `resourceId`, grab the correct link directly from the Data Store interface while viewing your group’s folder.

### Top-level files

- `README.md`: change the title, short description, and any sample URLs to your new project name.
- `CITATION.cff`: edit `title`, `abstract`, author list, and other metadata to reflect your team.
- `LICENSE`: this template uses the MIT License; update the copyright line if needed.

### Search-and-replace the old name

Run a repository-wide search for `Project_group_OASIS` and replace it with your new repo name. Pay attention to:

- Front-matter in the Markdown files inside `docs/` (for example, hero images or repo links).
- Any sample links in documentation under `docs/orientation/`.
- YAML config files in `.github/` and `workflows/` if you copied them forward.

---

## 3. Refresh the website content

Use the bullets below as prompts for Codex so it can edit each file.

- `docs/index.md`
  - Update the first-level heading to your project name.
  - Rewrite the intro section with your project summary, goals, or call to action.
  - Keep the page public-facing: title, hero image, purpose, people, collaboration, methods, refinement, polished results, citations, and health report.
  - Place links where they help the reader: data links in data/methods sections, code links in methods sections, and PDF links near polished outputs.
  - Keep the final results claim-based. Each insight should link evidence, state confidence, name limitations, and point to reusable outputs or next steps.
  - Do not rebuild a top-level button cluster or Featured Outputs section.
- `docs/people/`
  - Give each person their own Markdown file so simultaneous edits do not collide.
  - Include name, role/affiliation, what they are excited to work on, short background, skills/data, a human detail, and one profile link.
  - Do not publish email and GitHub handles together.
- `docs/references.bib`
  - Add sources as BibTeX entries and cite them in Markdown with `[@citationKey]`.
  - Leave `{{ references }}` where the generated reference list should appear.
- `docs/project_template.md`
  - Adjust the front-matter fields (`repo_owner`, `repo_name`, `contact_slack`, `contact_email`, etc.).
  - Replace placeholder hero images, figures, and descriptive text with your team’s content.
- `docs/code.md`
  - List important analysis scripts or notebooks and link to their paths in the repo.
- `docs/updates.md`
  - Add your first status entry or remove the placeholder timeline.
- `docs/resources/`
  - Add links to shared drives, data catalogs, or collaboration tools relevant to your group.

If you are using any of the orientation materials, skim the files in `docs/orientation/` and swap in screenshots or instructions that match your environment.

---

## 4. Persistent storage instructions

Update `docs/instructions/save-to-persistent-storage.md` so it points to your team’s storage location. Edit the `GROUP_NAME`, base path, and any screenshots that mention the original template.

> **Reminder:** The template ships with `Group_1` placeholders for the navigation link and shell snippets. Swap these for your group’s identifier (matching the number in your repo name). If your team has a custom share link from the Data Store, copy it from the CyVerse web UI to keep the `resourceId` accurate.

---

## 5. Turn on GitHub Pages with MkDocs

1. Open **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**. This tells GitHub to use the provided `Deploy site (MkDocs)` workflow.
3. Still on the Pages screen, make sure **Allow GitHub Actions to deploy to GitHub Pages** is enabled (GitHub may prompt you automatically on first deploy).
4. Go to the **Actions** tab, open the **Deploy site (MkDocs)** workflow, and run it (click **Run workflow** → `main`). The workflow builds the MkDocs site and publishes it to Pages.
5. Once the job succeeds, your site will be available at `https://<org>.github.io/<repo>/`. Update the `site_url` in `mkdocs.yml` if the link differs.

---

## 6. Final checks

- Confirm all navigation links in the live site work as expected.
- Confirm the homepage reads like a polished public-facing example that a new group can replace with its own narrative.
- Confirm image placeholders and raw file links are still present so non-technical editors can replace artifacts from GitHub.
- Delete any leftover placeholder sections or TODO comments.
- Share the Pages URL with your team once you verify the site renders correctly.

Keep this file for future reference so anyone (or any assistant) can re-run the setup steps if needed.
