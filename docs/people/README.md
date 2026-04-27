# People Profiles

The public front page shows a people gallery generated from learner Markdown profile files.

Most groups should:

1. Find learner files in the Innovation Summit 2026 repository:
   <https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners>
2. Copy the selected group members into `docs/people/`.
3. Let each person edit only their own Markdown file.
4. Add each profile file to `docs/_data/people.yml`.

Keep `docs/_data/people.yml` as an index only:

```yaml
people:
  - profile: people/your-name.md
```

Do not duplicate `summary`, `skills`, `interests`, or other profile text in YAML. The homepage card reads that information from the Markdown front matter.

If `photo` is missing, the card tries a GitHub avatar from `github:`. If both are missing, the card shows initials.

Privacy rule: do not publicly expose both email and GitHub in the same visible profile block. Prefer one optional profile link rather than raw contact data.
