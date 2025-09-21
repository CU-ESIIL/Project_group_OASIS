# Template Setup Checklist

## First run
- **Settings → Pages**: set **Source** to **GitHub Actions**.
- **Settings → Actions → General**: under **Workflow permissions**, choose **Read and write permissions**.
- *(Optional)* **Settings → Environments → github-pages**: allow deployments from **main** (or all branches) so the workflow can publish without manual approval.

## MkDocs checklist
- Update `mkdocs.yml` with your project's `site_name`, `site_url`, and `repo_url`.
- Ensure every plugin listed in `mkdocs.yml` also appears in `requirements.txt`.

## Common pitfalls
- **Branch `main` not allowed** → relax the `github-pages` environment branch rule or add `main` explicitly.
- **Multiple artifacts detected** → keep only one `actions/upload-pages-artifact` step in the workflow.
- **Missing MkDocs plugins** → install each plugin used by `mkdocs.yml` by adding it to `requirements.txt`.
