# People Profiles

The public front page shows a people gallery generated from `docs/_data/people.yml`.

To add a person to the public front page:

1. Open `docs/_data/people.yml`.
2. Add one plain-text entry under `people:`.
3. Link to their profile file in the Innovation Summit learner folder:
   <https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners>
4. If you have a profile image, upload it to `docs/assets/people/` and reference it with `image: assets/people/file-name.jpg`.

```yaml
- name: Your Name
  role: Learner
  image: assets/people/your-name.jpg
  focus: Short focus area
  skills:
    - Python
    - GIS
  brings: One short note about what you bring to the group
  profile_url: https://github.com/CU-ESIIL/Innovation-Summit-2026/blob/main/docs/learners/your-file-name.md
```

Only `name` is required. If `role` is missing, the gallery shows `Learner`. If `image`, `focus`, `skills`, `brings`, or `profile_url` are missing, that part of the card is hidden or replaced with initials.

Privacy rule: do not publicly expose both email and GitHub in the same visible profile block. Prefer one optional profile link rather than raw contact data.
