from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from check_stickers import sticker_issues

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPORT = DOCS / "_site_health.md"
MKDOCS = ROOT / "mkdocs.yml"
REQUIRED = ["docs/index.md", "mkdocs.yml", "README.md", "AGENTS.md", "PROMPT_ACTION_LOG.md",
            "docs/stylesheets/tokens.css", "docs/stylesheets/extra.css",
            "docs/instructions/day1.md", "docs/instructions/day2.md", "docs/instructions/day3.md",
            "docs/people/template.md", "docs/references.bib"]
ASSET_DIRS = ["docs/assets/hero", "docs/assets/whiteboards", "docs/assets/explorations",
              "docs/assets/figures", "docs/assets/team", "docs/assets/files",
              "docs/assets/stickers"]
PLACEHOLDERS = ["[link]", "TODO", "TBD", "CHANGE_ME", "REPLACE_ME"]
NAV_ITEMS = ["Public Front Page", "Instructions", "AI for Sustainability", "Specialty Tracks", "Manuals", "Storage", "Orientation"]
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
    )
    write_report(issues)
    print(f"Generated {REPORT.relative_to(ROOT)} with {len(issues)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
