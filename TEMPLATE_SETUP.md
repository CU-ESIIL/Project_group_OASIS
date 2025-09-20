# Template Setup Guide

Welcome! After creating a repository from this template, complete the following steps to ensure your MkDocs site deploys successfully on GitHub Pages.

## Update site metadata
- Edit `mkdocs.yml` and customize `site_name`, `site_url`, and `repo_url` to match your project.

## Review GitHub Pages environment settings
- In **Settings → Environments → github-pages**, verify that deployments from the `main` branch (or "All branches") are allowed. Adjust the allowed branches if necessary.

## Confirm organization permissions
- If you are using this template within an organization that restricts GitHub Actions, ask an administrator to permit Actions for the new repository before triggering the workflow.

## Quick fixes for common errors
- **Branch not allowed**: Update the allowed branches for the `github-pages` environment so it accepts `main`.
- **Multiple artifacts uploaded**: Make sure only one Pages artifact is uploaded by your workflow and remove extra upload steps.
- **Blank site after deployment**: Confirm that `mkdocs build` outputs content into the `dist` directory and that required theme or plugin dependencies are installed.
