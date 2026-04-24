from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
REFERENCE_MARKER = "{{ references }}"
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


def on_page_markdown(markdown, page, config, files, **kwargs):
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
