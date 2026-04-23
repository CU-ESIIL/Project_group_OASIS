# Project Group Template

This repository is a template for ESIIL Project Groups.

The website is built from the docs/ folder using MkDocs.

## Preview locally

pip install mkdocs-material
mkdocs serve

## Build site

mkdocs build --strict --clean

## Site Health

The site generates a non-blocking health report during the build.

The report appears at the bottom of the homepage and flags common issues such as missing files, placeholder links, or incomplete template fields.

Warnings do not prevent the site from publishing.

## Editing Pages

Use the edit icon on the website to open the corresponding markdown file in GitHub edit mode.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.
