# Post-Template Setup Checklist

After creating a repository from this template, follow the steps below to prepare your MkDocs site for deployment.

## Update `mkdocs.yml`
- Set `site_name` to your project's title.
- Update `site_url` to `https://<org>.github.io/<repo>/` so navigation links point to the deployed site.
- Set `repo_url` to the GitHub URL of your new repository.

## Review GitHub settings in the new repository
- **Settings → Pages**: set **Source** to **GitHub Actions**.
- **Settings → Actions → General**: under **Workflow permissions**, choose **Read and write permissions**.
- **Settings → Environments → github-pages**: allow deployments from **All branches** or add the `main` branch explicitly.

## Common pitfalls & fixes
- **Branch "main" not allowed** → adjust the `github-pages` environment's branch policy to include `main`.
- **Multiple artifacts named github-pages** → ensure the workflow only contains one `upload-pages-artifact` step.
- **Build fails due to missing plugins** → add each referenced plugin to `requirements.txt` and rerun the workflow.
- **Blank site** → confirm `mkdocs build` outputs files to the `dist/` directory and that `site_url` matches your `https://<org>.github.io/<repo>/` path.

## Trigger the first deployment
Push a small change to `docs/index.md` or run the workflow manually with **Run workflow** (workflow_dispatch) to start the initial publish.
