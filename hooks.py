from pathlib import Path
from html import escape
import re

import yaml


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
REFERENCE_MARKER = "{{ references }}"
PEOPLE_GALLERY_MARKER = "{{ people_gallery }}"
DAY_MARKER_TEMPLATE = '<span class="oasis-day-marker" data-oasis-day="{day}" aria-hidden="true"></span>'
PUBLIC_MODE_MARKER = '<span class="oasis-public-mode-marker" aria-hidden="true"></span>'
CITATION_RE = re.compile(r"\[@([A-Za-z0-9_:\-]+)\]")
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", re.S)
FIELD_RE = re.compile(r"(\w+)\s*=\s*[\{\"](.+?)[\}\"]\s*,?", re.S)


def on_config(config, **kwargs):
    report = DOCS / "_site_health.md"
    if not report.exists():
        report.write_text(
            "Site Health\n\n"
            "⚠ Attention needed\n\n"
            "⚠ Missing required file: docs/_site_health.md\n\n"
            "This report is generated automatically during the site build. Fix these items in the repository to improve the site.\n",
            encoding="utf-8",
        )
    return config


def clean_bib_value(value: str) -> str:
    return " ".join(value.replace("\n", " ").replace("--", "–").split())


def load_bibliography() -> dict[str, dict[str, str]]:
    bib_path = DOCS / "references.bib"
    if not bib_path.exists():
        return {}

    entries: dict[str, dict[str, str]] = {}
    text = bib_path.read_text(encoding="utf-8")
    for entry_type, key, body in ENTRY_RE.findall(text):
        fields = {name.lower(): clean_bib_value(value) for name, value in FIELD_RE.findall(body)}
        fields["entry_type"] = entry_type.lower()
        entries[key] = fields
    return entries


def author_label(author: str) -> str:
    if not author:
        return "Source"
    if " and " in author:
        first = author.split(" and ", 1)[0]
        surname = first.split(",", 1)[0].strip("{} ")
        return f"{surname} et al."
    if author.startswith("{") and author.endswith("}"):
        return author.strip("{}")
    return author.split(",", 1)[0].strip("{} ")


def citation_label(key: str, entry: dict[str, str] | None) -> str:
    if not entry:
        return key
    author = author_label(entry.get("author", ""))
    year = entry.get("year", "n.d.")
    return f"{author}, {year}"


def reference_line(key: str, entry: dict[str, str] | None) -> str:
    if not entry:
        return f"- <span id=\"ref-{key}\"></span>Missing BibTeX entry for `{key}`."

    author = clean_bib_value(entry.get("author", "Unknown author")).strip("{}")
    year = entry.get("year", "n.d.")
    title = entry.get("title", "Untitled").strip("{}")
    container = entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or entry.get("note", "")
    url = entry.get("url", "")

    parts = [f"- <span id=\"ref-{key}\"></span>{author}. ({year}). *{title}*."]
    if container:
        parts.append(f" {container}.")
    if url:
        parts.append(f" [{url}]({url}).")
    return "".join(parts)


def clean_text(value: object, fallback: str = "") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text or fallback


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [clean_text(item) for item in value if clean_text(item)]
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return [clean_text(value)]


def is_external_url(value: str) -> bool:
    return value.startswith(("http://", "https://", "mailto:"))


def local_asset_exists(value: str) -> bool:
    if not value or is_external_url(value) or value.startswith(("/", "#")):
        return False
    return (DOCS / value).resolve().is_file()


def initials_for(name: str) -> str:
    parts = [part for part in re.split(r"\s+", name.strip()) if part]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return f"{parts[0][0]}{parts[-1][0]}".upper()


def profile_slug(value: str) -> str:
    stem = value.rstrip("/").rsplit("/", 1)[-1].replace(".md", "")
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-") or "profile"


def title_from_slug(value: str) -> str:
    return " ".join(part.capitalize() for part in profile_slug(value).split("-")) or "Unnamed person"


def profile_path_for(value: str) -> Path | None:
    if not value or is_external_url(value) or value.startswith(("/", "#")):
        return None
    return (DOCS / value).resolve()


def profile_url_for(value: str) -> str:
    if not value:
        return ""
    if value.startswith("https://raw.githubusercontent.com/"):
        return value.replace(
            "https://raw.githubusercontent.com/CU-ESIIL/Innovation-Summit-2026/main/",
            "https://github.com/CU-ESIIL/Innovation-Summit-2026/blob/main/",
        )
    if is_external_url(value):
        return value
    if value.endswith(".md"):
        return value[:-3] + "/"
    return value


def split_profile_markdown(text: str) -> tuple[dict[str, object], str]:
    if text.startswith("---\n"):
        _, front_matter, body = text.split("---", 2)
        try:
            parsed = yaml.safe_load(front_matter) or {}
        except yaml.YAMLError:
            parsed = {}
        return parsed if isinstance(parsed, dict) else {}, body.strip()
    return {}, text.strip()


def first_profile_paragraph(body: str) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if line.startswith("#"):
            continue
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.startswith(("-", "*", ">")):
            continue
        current.append(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line))
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs[0] if paragraphs else ""


def load_profile(profile: str) -> dict[str, object]:
    path = profile_path_for(profile)
    profile_url = profile_url_for(profile)
    if path and path.is_file():
        meta, body = split_profile_markdown(path.read_text(encoding="utf-8"))
        meta["profile"] = profile
        meta["profile_url"] = profile_url
        if not clean_text(meta.get("summary")):
            fallback = first_profile_paragraph(body)
            if fallback:
                meta["summary"] = fallback
        if not clean_text(meta.get("name")):
            meta["name"] = title_from_slug(profile)
        return meta

    return {
        "name": title_from_slug(profile),
        "role": "Learner",
        "profile": profile,
        "profile_url": profile_url,
        "summary": "Profile details are not available yet. Add or copy this learner Markdown file to complete the card.",
        "missing_profile": True,
    }


def load_people() -> list[dict[str, object]]:
    people_path = DOCS / "_data" / "people.yml"
    if not people_path.exists():
        return []
    data = yaml.safe_load(people_path.read_text(encoding="utf-8")) or {}
    entries = data.get("people", [])
    if not isinstance(entries, list):
        return []

    people: list[dict[str, object]] = []
    for entry in entries:
        if isinstance(entry, str):
            people.append(load_profile(entry))
            continue
        if not isinstance(entry, dict):
            continue
        profile = clean_text(entry.get("profile"))
        if profile:
            people.append(load_profile(profile))
    return people


def render_people_gallery() -> str:
    people = load_people()
    if not people:
        return (
            '<p class="people-gallery-empty">'
            "No people are listed yet. Add entries to <code>docs/_data/people.yml</code>."
            "</p>"
        )

    cards: list[str] = ['<section class="people-gallery" aria-label="Project group people">']
    for person in people:
        if not isinstance(person, dict):
            continue

        name = clean_text(person.get("name"), "Unnamed person")
        role = clean_text(person.get("role"), "Learner")
        affiliation = clean_text(person.get("affiliation"))
        pronouns = clean_text(person.get("pronouns"))
        photo = clean_text(person.get("photo"))
        github = clean_text(person.get("github"))
        project_role = clean_text(person.get("project_role"))
        summary = clean_text(person.get("summary"))
        profile_url = clean_text(person.get("profile_url"))
        interests = as_list(person.get("interests"))[:3]
        skills = as_list(person.get("skills"))
        initials = initials_for(name)

        if photo and (is_external_url(photo) or local_asset_exists(photo)):
            avatar = (
                f'<img class="people-card__image" src="{escape(photo)}" '
                f'alt="{escape(name)} profile image">'
            )
        elif github:
            avatar = (
                f'<img class="people-card__image" src="https://github.com/{escape(github)}.png" '
                f'alt="{escape(name)} GitHub avatar">'
            )
        else:
            avatar = f'<div class="people-card__avatar" aria-hidden="true">{escape(initials)}</div>'

        rows: list[str] = []
        role_parts = [role]
        if affiliation:
            role_parts.append(affiliation)
        if pronouns:
            role_parts.append(pronouns)
        role_line = " · ".join(part for part in role_parts if part)
        if project_role:
            rows.append(f'<p class="people-card__project-role">{escape(project_role)}</p>')
        if summary:
            rows.append(f'<p class="people-card__summary">{escape(summary)}</p>')
        if interests:
            tags = "".join(f"<span>{escape(interest)}</span>" for interest in interests)
            rows.append(f'<div class="people-card__chips people-card__chips--interests" aria-label="Interests">{tags}</div>')
        if skills:
            tags = "".join(f"<span>{escape(skill)}</span>" for skill in skills[:3])
            rows.append(f'<div class="people-card__chips people-card__chips--skills" aria-label="Skills">{tags}</div>')
        if profile_url:
            rows.append(
                f'<a class="people-card__link" href="{escape(profile_url)}">'
                "View learner file"
                "</a>"
            )

        cards.append(
            '<article class="people-card">'
            f"{avatar}"
            f'<h3 class="people-card__name">{escape(name)}</h3>'
            f'<p class="people-card__role">{escape(role_line)}</p>'
            + "".join(rows)
            + "</article>"
        )

    cards.append("</section>")
    return "\n".join(cards)


def on_page_markdown(markdown, page, config, files, **kwargs):
    if (page.meta or {}).get("public_mode_toggle") and "oasis-public-mode-marker" not in markdown:
        markdown = f"{PUBLIC_MODE_MARKER}\n\n{markdown}"

    oasis_day = str((page.meta or {}).get("oasis_day", "")).strip()
    if oasis_day in {"1", "2", "3"} and "oasis-day-marker" not in markdown:
        markdown = f"{DAY_MARKER_TEMPLATE.format(day=oasis_day)}\n\n{markdown}"

    if PEOPLE_GALLERY_MARKER in markdown:
        markdown = markdown.replace(PEOPLE_GALLERY_MARKER, render_people_gallery())

    if REFERENCE_MARKER not in markdown:
        return markdown

    bibliography = load_bibliography()
    cited_keys: list[str] = []

    def replace_citation(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in cited_keys:
            cited_keys.append(key)
        label = citation_label(key, bibliography.get(key))
        return f"[{label}](#ref-{key})"

    markdown = CITATION_RE.sub(replace_citation, markdown)

    if cited_keys:
        references = ["## References", ""]
        references.extend(reference_line(key, bibliography.get(key)) for key in cited_keys)
        markdown = markdown.replace(REFERENCE_MARKER, "\n".join(references))
    else:
        markdown = markdown.replace(REFERENCE_MARKER, "")

    return markdown
