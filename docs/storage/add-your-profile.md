# Add Your Profile

Your profile Markdown file is what the public site reads to display your information.

## Steps

1. Open your learner file from the Innovation Summit learner folder:
   <https://github.com/CU-ESIIL/Innovation-Summit-2026/tree/main/docs/learners>
2. Copy it into this project under `docs/people/`.
3. Use a lowercase, hyphen-separated filename such as `jane-doe.md`.
4. Copy the template below into your file.
5. Fill in the fields you want to share.
6. Add a short bio below the front matter.
7. Save your file.
8. Ask your group editor to add your file to the homepage index.

## Profile template

```yaml
---
name: Jane Doe
slug: jane-doe
role: Learner
affiliation: University or organization
pronouns:
github: janedoe
photo:
project_role: Data exploration and visualization
summary: One to two sentence summary used on the homepage card.
interests:
  - Remote sensing
skills:
  - Python
---
```

Write a short bio below the front matter. If `summary` is blank, the homepage card uses the first paragraph.

## Photos and avatars

GitHub avatar is easiest. Add your GitHub username in the `github:` field and the site will use:

```text
https://github.com/your-username.png
```

A separate `photo:` is optional. Put images in `docs/assets/people/` and reference them like this:

```yaml
photo: assets/people/jane-doe.jpg
```

If neither `photo` nor `github` is provided, the card shows initials.

## Group editor steps

1. Open `docs/_data/people.yml`.
2. Copy an existing `profile:` line.
3. Replace the file path with the new person’s file.
4. Save and commit.

Example:

```yaml
people:
  - profile: people/jane-doe.md
  - profile: people/sam-rivera.md
```

Keep `docs/_data/people.yml` as an index only. Do not duplicate profile summaries, skills, interests, or contact details there.
