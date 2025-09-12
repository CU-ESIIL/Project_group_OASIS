# Template Customization Checklist

This repository is a template for new project groups. After cloning or copying it, work through the steps below to update names and links to your group's information.

## 1. Rename the repository
- On GitHub go to **Settings → General → Repository name** and rename it to your project.
- If you already cloned the repo locally, update the remote: `git remote set-url origin <new_repo_url>`.

## 2. Update MkDocs configuration (`mkdocs.yml`)
- `site_name`: your project or group name.
- `site_url`: `https://<org>.github.io/<new_repo_name>`.
- `repo_name`: the display name of your repository.
- `repo_url`: full GitHub URL for the repo.

## 3. Update top-level files
- `README.md`: change the title and any example links to use your new repo name.
- `CITATION.cff`: set the `title` and other metadata (authors, version, DOI) for your project.

## 4. Customize project template page (`docs/project_template.md`)
- Edit the front matter fields such as `repo_owner`, `repo_name`, `contact_slack`, and `contact_email`.
- Replace placeholder text, images, and links with your team's content.

## 5. Fix links to this repository
- Search the entire repository for `Project_group_OASIS` and replace it with your new repo name.
- Pay special attention to image links in `docs/index.md`, `docs/orientation/cyverse_basics.md`, `docs/orientation/docker_basics.md`, and `docs/orientation/art_gallery*`.
- Linux example: `rg -l 'Project_group_OASIS' docs | xargs sed -i 's/Project_group_OASIS/<new_repo_name>/g'`.

## 6. Persistent storage instructions
- In `docs/instructions/save-to-persistent-storage.md`, set `GROUP_NAME` to your team's folder name and update any paths.

## 7. Verify GitHub Pages
- In **Settings → Pages**, set the source to **Deploy from a branch**, branch `main`, folder `/docs`.
- After committing changes, confirm the site builds at your updated `site_url`.

Work through this list before adding new content. Keep this file for future reference or remove it after setup.
