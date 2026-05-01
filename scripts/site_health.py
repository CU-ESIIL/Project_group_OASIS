from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ModuleNotFoundError:  # Keep this script runnable with plain system Python.
    yaml = None

from check_stickers import sticker_issues

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPORT = DOCS / "_site_health.md"
MKDOCS = ROOT / "mkdocs.yml"
PEOPLE_DATA = DOCS / "_data" / "people.yml"
REQUIRED = ["docs/index.md", "docs/example.md", "mkdocs.yml", "README.md", "AGENTS.md", "PROMPT_ACTION_LOG.md",
            "docs/stylesheets/tokens.css", "docs/stylesheets/extra.css",
            "docs/javascripts/presentation-mode.js", "docs/instructions/day1.md",
            "docs/instructions/day2.md", "docs/instructions/day3.md",
            "docs/people/template.md", "docs/storage/add-your-profile.md",
            "docs/references.bib", "docs/_data/people.yml"]
ASSET_DIRS = ["docs/assets/hero", "docs/assets/whiteboards", "docs/assets/explorations",
              "docs/assets/figures", "docs/assets/team", "docs/assets/files",
              "docs/assets/stickers", "docs/assets/people"]
PLACEHOLDERS = ["[link]", "TODO", "TBD", "CHANGE_ME", "REPLACE_ME"]
NAV_ITEMS = ["Home", "Example", "Instructions", "AI for Sustainability", "Specialty Tracks", "Cloud Triangle", "Links", "Orientation"]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def nav_labels(text: str) -> list[str]:
    labels, in_nav = [], False
    for line in text.splitlines():
        if not in_nav:
            in_nav = line.strip() == "nav:"
            continue
        if line and not line.startswith((" ", "\t", "-")):
            break
        match = re.match(r"^\s{2}-\s+([^:]+):\s*", line)
        if match:
            labels.append(match.group(1).strip())
    return labels


def text_files() -> list[Path]:
    docs_files = [path for path in sorted(DOCS.rglob("*.md")) if path.name != "_site_health.md"]
    return [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "PROMPT_ACTION_LOG.md", MKDOCS] + docs_files


def missing_file_issues() -> list[str]:
    return [f"⚠ Missing required file: {path}" for path in REQUIRED if not (ROOT / path).exists()]


def missing_asset_dir_issues() -> list[str]:
    return [f"⚠ Missing asset folder: {path}" for path in ASSET_DIRS if not (ROOT / path).is_dir()]


def placeholder_issues() -> list[str]:
    issues = []
    for path in text_files():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in PLACEHOLDERS:
            if needle in text:
                issues.append(f"⚠ Placeholder detected: {needle} in {path.relative_to(ROOT)}")
    return issues


def navigation_issues() -> list[str]:
    labels = nav_labels(MKDOCS.read_text(encoding="utf-8")) if MKDOCS.exists() else []
    return [f"⚠ Navigation issue: missing nav item '{item}' in mkdocs.yml" for item in NAV_ITEMS if item not in labels]


def sticker_validation_issues() -> list[str]:
    return [
        f"⚠ Sticker navigation issue: {issue}"
        for issue in sticker_issues()
    ]


def is_external_or_anchor(raw: str) -> bool:
    return raw.startswith(("http://", "https://", "mailto:", "#"))


def resolve_docs_target(raw: str) -> Path | None:
    target = unquote(raw.strip().strip("<>").split("#", 1)[0].split("?", 1)[0])
    if not target or is_external_or_anchor(target) or target.startswith("/"):
        return None
    if target.startswith("../"):
        return (PEOPLE_DATA.parent / target).resolve()
    return (DOCS / target).resolve()


def parse_simple_people_yaml(text: str) -> list[dict[str, object]]:
    people: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list_key: str | None = None
    in_people = False

    for line in text.splitlines():
        raw = line.rstrip()
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "people:":
            in_people = True
            continue
        if not in_people:
            continue
        if raw.startswith("  - "):
            current = {}
            people.append(current)
            current_list_key = None
            remainder = raw[4:].strip()
            if ":" in remainder:
                key, value = remainder.split(":", 1)
                current[key.strip()] = value.strip()
            continue
        if current is None:
            continue
        if raw.startswith("    - ") and current_list_key:
            current.setdefault(current_list_key, [])
            value = raw[6:].strip()
            if isinstance(current[current_list_key], list) and value:
                current[current_list_key].append(value)
            continue
        if raw.startswith("    ") and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = value
                current_list_key = None
            else:
                current[key] = []
                current_list_key = key

    return people


def people_gallery_issues() -> list[str]:
    if not PEOPLE_DATA.exists():
        return [f"⚠ People gallery issue: missing {PEOPLE_DATA.relative_to(ROOT)}"]

    text = PEOPLE_DATA.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            data = yaml.safe_load(text) or {}
        except yaml.YAMLError as exc:
            return [f"⚠ People gallery issue: {PEOPLE_DATA.relative_to(ROOT)} is not valid YAML ({exc})"]
    else:
        data = {"people": parse_simple_people_yaml(text)}

    people = data.get("people", [])
    if not isinstance(people, list):
        return [f"⚠ People gallery issue: {PEOPLE_DATA.relative_to(ROOT)} should contain a `people:` list"]

    issues: list[str] = []
    for index, person in enumerate(people, start=1):
        if not isinstance(person, dict):
            issues.append(f"⚠ People gallery issue: entry {index} should be a YAML mapping")
            continue

        profile = str(person.get("profile", "") or "").strip()
        if not profile:
            issues.append(f"⚠ People gallery issue: entry {index} should use `profile: people/first-last.md`")
            continue

        if any(key in person for key in ["name", "summary", "skills", "interests", "focus", "brings", "profile_url"]):
            issues.append(f"⚠ People gallery issue: entry {index} should keep profile text in Markdown, not people.yml")

        profile_path = resolve_docs_target(profile)
        if profile_path is not None and not profile_path.is_file():
            issues.append(f"⚠ People gallery issue: profile file does not exist: {profile}")
            continue

        if profile_path is not None and profile_path.is_file():
            profile_text = profile_path.read_text(encoding="utf-8")
            if not profile_text.startswith("---\n"):
                issues.append(f"⚠ People gallery issue: {profile} should start with YAML front matter")

    return issues


def internal_link_issues() -> list[str]:
    issues = []
    for path in [p for p in sorted(DOCS.rglob("*.md")) if p.name != "_site_health.md"]:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`]+`", "", text)
        for raw in LINK_RE.findall(text):
            target = unquote(raw.strip().strip("<>").split("#", 1)[0])
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                issues.append(f"⚠ Internal link issue: {path.relative_to(ROOT)} links to missing target '{raw}'")
    return issues


def write_report(issues: list[str]) -> None:
    lines = ["Site Health", ""]
    if not issues:
        lines.append("✓ No issues detected.")
    else:
        lines.extend(["⚠ Attention needed", ""])
        lines.extend(issues)
    lines.extend(["", "This report is generated automatically during the site build. Fix these items in the repository to improve the site."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    issues = (
        missing_file_issues()
        + missing_asset_dir_issues()
        + placeholder_issues()
        + navigation_issues()
        + internal_link_issues()
        + sticker_validation_issues()
        + people_gallery_issues()
    )
    write_report(issues)
    print(f"Generated {REPORT.relative_to(ROOT)} with {len(issues)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
