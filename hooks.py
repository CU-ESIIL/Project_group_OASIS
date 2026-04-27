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


def load_people() -> list[dict[str, object]]:
    people_path = DOCS / "_data" / "people.yml"
    if not people_path.exists():
        return []
    data = yaml.safe_load(people_path.read_text(encoding="utf-8")) or {}
    people = data.get("people", [])
    return people if isinstance(people, list) else []


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
        image = clean_text(person.get("image"))
        focus = clean_text(person.get("focus"))
        brings = clean_text(person.get("brings"))
        profile_url = clean_text(person.get("profile_url"))
        skills = as_list(person.get("skills"))
        initials = initials_for(name)

        if image and (is_external_url(image) or local_asset_exists(image)):
            avatar = (
                f'<img class="people-card__image" src="{escape(image)}" '
                f'alt="{escape(name)} profile image">'
            )
        else:
            avatar = f'<div class="people-card__avatar" aria-hidden="true">{escape(initials)}</div>'

        rows: list[str] = []
        if focus:
            rows.append(f'<p class="people-card__meta"><strong>Focus:</strong> {escape(focus)}</p>')
        if skills:
            tags = "".join(f"<span>{escape(skill)}</span>" for skill in skills)
            rows.append(f'<div class="people-card__skills" aria-label="Skills">{tags}</div>')
        if brings:
            rows.append(f'<p class="people-card__meta"><strong>Brings:</strong> {escape(brings)}</p>')
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
            f'<p class="people-card__role">{escape(role)}</p>'
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
