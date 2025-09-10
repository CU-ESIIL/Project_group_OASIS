[![DOI](https://zenodo.org/badge/727888683.svg)](https://zenodo.org/doi/10.5281/zenodo.11166898)

# Project Group OASIS

Welcome to the collaboration space for the OASIS project group of the Environmental Data Science Innovation and Inclusion Lab (ESIIL). This repository and its companion website gather everything new teammates need to start working together.

## Getting Started
1. **Set up your environment** – install dependencies from `requirements.txt` or use the Docker images in `containers/`.
2. **Read the orientation materials** – check `docs/orientation/` for background and training.
3. **Preview the website** – run `mkdocs serve` and open <http://localhost:8000> to see the site locally.

## Repository Layout
- `docs/` – source files for the website.
  - `content/` – Markdown pages to communicate our science.
  - `images/` – figures and photos referenced on the site.
  - `code/` – sample snippets or notebooks linked from the site.
  - `meeting-notes/`, `orientation/`, `references/` – supporting documents.
- `workflows/` – reproducible analysis pipelines.
  - `code/` – scripts and notebooks.
  - `input/` – data required to run workflows.
  - `output/` – generated results.
- `containers/` – Docker and environment configurations.

## Contributing to the Website
1. Place new images in `docs/images/`.
2. Add or edit Markdown pages in `docs/content/` or other folders under `docs/`.
3. Include example code snippets or notebooks in `docs/code/`.
4. Run `mkdocs serve` to preview changes, then commit and open a pull request.

## Working with Workflows
Use the `workflows/` directory to share analysis code. Keep inputs and outputs in the dedicated subfolders and describe the steps in `workflows/README.md` so others can reproduce your work.

## Communication
Record meeting notes in `docs/meeting-notes/` and track tasks through GitHub Issues and pull requests.

Welcome aboard! We are excited to collaborate and share our science with the world.
