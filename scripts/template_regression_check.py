from __future__ import annotations

import re
from pathlib import Path

from check_stickers import sticker_issues


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def paragraphs(text: str) -> list[str]:
    clean = re.sub(r"```.*?```", "", text, flags=re.S)
    clean = re.sub(r"!!! note.*?(?=\n## |\Z)", "", clean, flags=re.S)
    return [
        block.strip()
        for block in re.split(r"\n\s*\n", clean)
        if block.strip() and not block.lstrip().startswith(("#", "|", "!", "[", "{{", "-", "---"))
    ]


def main() -> int:
    errors: list[str] = []
    index = ROOT / "docs" / "index.md"
    example = ROOT / "docs" / "example.md"
    instructions = ROOT / "docs" / "instructions.md"
    day1 = ROOT / "docs" / "instructions" / "day1.md"
    day2 = ROOT / "docs" / "instructions" / "day2.md"
    day3 = ROOT / "docs" / "instructions" / "day3.md"
    mkdocs = ROOT / "mkdocs.yml"
    css = ROOT / "docs" / "stylesheets" / "extra.css"
    mode_toggle = ROOT / "docs" / "javascripts" / "mode-toggle.js"
    presentation_mode = ROOT / "docs" / "javascripts" / "presentation-mode.js"

    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    example_text = example.read_text(encoding="utf-8") if example.exists() else ""
    instructions_text = instructions.read_text(encoding="utf-8") if instructions.exists() else ""
    day_texts = {
        "day1": day1.read_text(encoding="utf-8") if day1.exists() else "",
        "day2": day2.read_text(encoding="utf-8") if day2.exists() else "",
        "day3": day3.read_text(encoding="utf-8") if day3.exists() else "",
    }
    mkdocs_text = mkdocs.read_text(encoding="utf-8") if mkdocs.exists() else ""
    css_text = css.read_text(encoding="utf-8") if css.exists() else ""
    mode_toggle_text = mode_toggle.read_text(encoding="utf-8") if mode_toggle.exists() else ""
    presentation_mode_text = presentation_mode.read_text(encoding="utf-8") if presentation_mode.exists() else ""

    require(index.exists(), "docs/index.md is missing.", errors)
    require(example.exists(), "docs/example.md is missing.", errors)
    require("public_mode_toggle: true" in index_text, "Home should keep public_mode_toggle: true.", errors)
    require("# Project Group Home" in index_text, "Home should be titled Project Group Home.", errors)
    require("[See a completed example](example.md){ .md-button }" in index_text,
            "Home should link to the completed Example page.", errors)
    require("| Name | Role / affiliation | Focus | Skills |" in index_text and "| | | | |" in index_text,
            "Home should contain an empty editable people table.", errors)
    require("## Report Out (Day 2 — 2 minutes) { #report-out-day2 }" in index_text,
            "Home should include the Day 2 report-out section.", errors)
    require("## Final Report Out (Day 3 — 6 minutes) { #report-out-day3 }" in index_text,
            "Home should include the Day 3 final report-out section.", errors)
    require("{{ references }}" in index_text, "Home should keep the references marker.", errors)
    require(".task-sticker" not in index_text and "edit-D" not in index_text,
            "Home should not use retired sticker markup or edit anchors.", errors)
    require("<div" not in index_text and "<table" not in index_text,
            "Home should stay Markdown-first without raw layout HTML.", errors)
    require(all(len(paragraph.split()) <= 24 for paragraph in paragraphs(index_text)),
            "Home visible text should stay sparse; guidance belongs in notes.", errors)

    require("title: Example Project Page" in example_text and "# Example Project Page" in example_text,
            "Example should have the Example Project Page title.", errors)
    require("This page shows what a completed group project can look like." in example_text,
            "Example should link users back to editing Home.", errors)
    require("!!! note" not in example_text and "public_mode_toggle: true" not in example_text,
            "Example should be clean public-facing prose without instruction toggles.", errors)
    require("report-out-day2" not in example_text and "report-out-day3" not in example_text,
            "Example should not include Home report-out scaffold anchors.", errors)
    require("![Early exploration plot]" in example_text and "![Lead result visual]" in example_text,
            "Example should include figure references.", errors)
    for section in [
        "## People",
        "## Project Question",
        "## Specialty Tracks and Strategy",
        "## Data Exploration",
        "## Methods and Code",
        "## Results",
        "## Polished Outputs",
        "## Cite & Reuse",
        "## Next Steps",
    ]:
        require(section in example_text, f"Example section missing: {section}.", errors)
    require(len([p for p in paragraphs(example_text) if len(p.split()) >= 35]) >= 10,
            "Example should contain complete report-style paragraphs.", errors)

    require("nav:\n  - Home: index.md\n  - Example: example.md" in mkdocs_text,
            "MkDocs nav should start with Home and Example.", errors)
    require("javascripts/mode-toggle.js" in mkdocs_text and "javascripts/presentation-mode.js" in mkdocs_text,
            "Mode toggle and presentation scripts should be registered.", errors)

    require("template-guidance-toggle" in mode_toggle_text and "Instructions on" in mode_toggle_text,
            "Instructions on/off toggle behavior is missing.", errors)
    require("ensureInstructionsToggle" in mode_toggle_text and ".md-sidebar--secondary .md-sidebar__inner" in mode_toggle_text,
            "Instructions toggle should be created in the right sidebar.", errors)
    require("isHomePage" in presentation_mode_text and "report-out-day2" in presentation_mode_text,
            "Presentation mode should be scoped to Home and report-out sections.", errors)
    require("oasis-report-out-visible" in presentation_mode_text,
            "Presentation mode should mark report-out content before hiding other sections.", errors)

    require("margin-top: -0.5rem" in css_text and "font-size: 1.02rem" in css_text and "font-weight: 800" in css_text,
            "Primary sidebar Home spacing and typography fixes are missing.", errors)
    require(".md-sidebar--secondary .md-sidebar__scrollwrap" in css_text and "padding-top: var(--oasis-space-3)" in css_text,
            "Right sidebar top padding fix is missing.", errors)
    require(".oasis-sidebar-utilities li::marker" in css_text and 'content: ""' in css_text,
            "Sidebar utility marker cleanup is missing.", errors)
    require("h2#report-out-day2" in css_text and "h2#report-out-day3" in css_text,
            "Report-out section emphasis styles are missing.", errors)
    require("body.presentation-mode .md-typeset > *" in css_text and "oasis-report-out-visible" in css_text,
            "Presentation mode should hide non-report-out Home content.", errors)
    require(".task-sticker" not in css_text,
            "Retired task-sticker CSS should be removed.", errors)

    require("Landmark stickers" not in instructions_text and ".task-sticker" not in instructions_text,
            "Instructions overview should not describe the retired sticker workflow.", errors)
    for day, text in day_texts.items():
        require(".task-sticker" not in text and "guide-D" not in text,
                f"{day} should not use retired sticker buttons or anchors.", errors)
        require("../index.md" in text and "../example.md" in text,
                f"{day} should point groups to Home and Example appropriately.", errors)
    require("Report Out (2 minutes)" in day_texts["day2"],
            "Day 2 instructions should include report-out guidance.", errors)
    require("Final Report Out (6 minutes)" in day_texts["day3"],
            "Day 3 instructions should include final report-out guidance.", errors)

    sticker_errors = sticker_issues()
    require(not sticker_errors, "Retired sticker cleanup failed:\n" + "\n".join(sticker_errors), errors)

    if errors:
        print("Template regression check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Template regression check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
