from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    index = ROOT / "docs" / "index.md"
    instructions = ROOT / "docs" / "instructions.md"
    mkdocs = ROOT / "mkdocs.yml"
    css = ROOT / "docs" / "stylesheets" / "extra.css"
    tokens = ROOT / "docs" / "stylesheets" / "tokens.css"
    hooks = ROOT / "hooks.py"
    references = ROOT / "docs" / "references.bib"
    people_dir = ROOT / "docs" / "people"
    stickers_dir = ROOT / "docs" / "assets" / "stickers"
    logo = ROOT / "docs" / "assets" / "oasis_logo.png"
    group_logo = ROOT / "docs" / "assets" / "esiil_content" / "group_logo.svg"
    event_group_logo = ROOT / "docs" / "assets" / "esiil_content" / "event_group_logo.png"
    logo_override = ROOT / "docs" / "overrides" / "partials" / "logo.html"
    ai_dir = ROOT / "docs" / "ai-for-sustainability"

    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    instructions_text = instructions.read_text(encoding="utf-8") if instructions.exists() else ""
    mkdocs_text = mkdocs.read_text(encoding="utf-8") if mkdocs.exists() else ""
    css_text = css.read_text(encoding="utf-8") if css.exists() else ""
    tokens_text = tokens.read_text(encoding="utf-8") if tokens.exists() else ""
    hooks_text = hooks.read_text(encoding="utf-8") if hooks.exists() else ""
    references_text = references.read_text(encoding="utf-8") if references.exists() else ""

    require(index.exists(), "docs/index.md is missing.", errors)
    require("## How to use this page" in index_text, "Front page sticker legend is missing.", errors)
    for section in [
        "People",
        "Project Question",
        "Specialty Tracks and Strategy",
        "Data Exploration",
        "Methods and Code",
        "Results",
        "Polished Outputs",
    ]:
        require(section in index_text, f"Front page section '{section}' is missing.", errors)
    require("section-sticker" not in index_text and "assets/stickers/tasks/" in index_text,
            "Public Front Page should use shared task sticker images, not old section-sticker markup.", errors)
    require("<div" not in index_text and "<table" not in index_text,
            "Public Front Page should avoid participant-facing raw HTML layout.", errors)
    require('--8<-- "people/' not in index_text, "Public Front Page should not include local People profile snippets.", errors)
    require("Innovation-Summit-2026/tree/main/docs/learners" in index_text,
            "People section should link to the Innovation Summit learner folder.", errors)
    require("Innovation-Summit-2026/blob/main/docs/learners/" in index_text,
            "People section should include example learner profile file links.", errors)
    require("## Featured Outputs" not in index_text, "Featured Outputs section should be removed.", errors)
    require("https://what-uses-more.com" in index_text, "What Uses More button/link is missing.", errors)
    require("assets/files/project_brief.pdf" in index_text and "Polished Outputs" in index_text,
            "Project brief PDF should be linked near polished outputs.", errors)
    require("View shared code" in index_text and "Methods and Code" in index_text,
            "Code button should be placed in the methods section.", errors)
    require("Open the ESIIL Data Library" in index_text and "https://cu-esiil.github.io/data-library/innovation-summit-2025/" in index_text,
            "Data button should point to the ESIIL Data Library in context.", errors)
    require("[@" in index_text, "Public Front Page should use BibTeX citation keys.", errors)
    require("{{ references }}" in index_text, "Public Front Page should include references marker.", errors)
    require("## How to edit the Public Front Page" in instructions_text,
            "Instructions edit guide section is missing.", errors)
    require("## Where files go" in instructions_text, "Instructions file map is missing.", errors)
    require("Innovation-Summit-2026/tree/main/docs/learners" in instructions_text,
            "Instructions should explain linking to existing learner profile files.", errors)
    require("Most summit participants should only edit Markdown files." in instructions_text,
            "Markdown-safe editing guidance is missing.", errors)
    require("docs/references.bib" in instructions_text, "Instructions should explain BibTeX references.", errors)

    for day in ["day1", "day2", "day3"]:
        day_text = (ROOT / "docs" / "instructions" / f"{day}.md").read_text(encoding="utf-8")
        require("../assets/stickers/tasks/" in day_text and "{ .task-sticker }" in day_text,
                f"{day}.md should show task stickers from the shared sticker assets.", errors)

    for folder in ["hero", "whiteboards", "explorations", "figures", "team", "files", "stickers"]:
        require((ROOT / "docs" / "assets" / folder).is_dir(), f"docs/assets/{folder}/ is missing.", errors)

    require("toc.integrate" not in mkdocs_text, "toc.integrate should not be enabled.", errors)
    require("content.action.edit" in mkdocs_text, "MkDocs edit action should remain enabled.", errors)
    require("site_name: \"OASIS Project Group Template\"" in mkdocs_text,
            "Header site title should remain visible and persistent.", errors)
    require("Day 1 — Meet Your Team and Define Your Project" in mkdocs_text,
            "Day 1 nav title should match the orientation page.", errors)
    require("AI for Sustainability" in mkdocs_text, "AI for Sustainability nav section is missing.", errors)
    require("Defining AI: ai-for-sustainability/defining-ai.md" in mkdocs_text,
            "Defining AI nav item is missing.", errors)
    require("Defining Sustainability: ai-for-sustainability/defining-sustainability.md" in mkdocs_text,
            "Defining Sustainability nav item is missing.", errors)
    require("What Does It Cost?: ai-for-sustainability/what-does-it-cost.md" in mkdocs_text,
            "What Does It Cost nav item is missing.", errors)
    require("Specialty Tracks" in mkdocs_text, "Specialty Tracks nav section is missing.", errors)
    require(mkdocs_text.find("AI for Sustainability") < mkdocs_text.find("Specialty Tracks"),
            "AI for Sustainability should appear before Specialty Tracks in nav.", errors)
    require("logo: 'assets/oasis_logo.png'" in mkdocs_text, "Header logo should use docs/assets/oasis_logo.png.", errors)
    require("homepage: https://cu-esiil.github.io/Project_group_OASIS/" in mkdocs_text,
            "Material homepage should point the logo to the Project_group_OASIS homepage.", errors)
    require("custom_dir:" not in mkdocs_text, "custom_dir should not point to a missing overrides folder.", errors)
    require("extra_javascript:" not in mkdocs_text, "Sidebar logo JavaScript workaround should not be registered.", errors)
    require("home-brand-link.js" not in mkdocs_text, "Sidebar logo JavaScript workaround should not be referenced.", errors)
    require(logo.exists(), "docs/assets/oasis_logo.png is missing.", errors)
    require(group_logo.exists(), "docs/assets/esiil_content/group_logo.svg is missing.", errors)
    require(event_group_logo.exists(), "docs/assets/esiil_content/event_group_logo.png is missing.", errors)
    require(references.exists(), "docs/references.bib is missing.", errors)
    require("@misc{oasisProjectTemplate" in references_text, "Template reference BibTeX entry is missing.", errors)
    require((people_dir / "README.md").exists(), "People README is missing.", errors)
    require((people_dir / "template.md").exists(), "People template is missing.", errors)
    for sticker in ["people", "question", "tracks", "data", "methods", "results", "outputs"]:
        require((stickers_dir / f"{sticker}.png").exists(), f"Sticker asset {sticker}.png is missing.", errors)
    task_stickers = [
        "d1-a", "d1-b", "d1-c", "d1-d", "d1-e", "d1-f",
        "d2-a", "d2-b", "d2-c", "d2-d", "d2-e", "d2-f", "d2-g",
        "d3-a", "d3-b", "d3-c", "d3-d", "d3-e", "d3-f",
    ]
    for sticker in task_stickers:
        sticker_path = f"assets/stickers/tasks/{sticker}.svg"
        require((stickers_dir / "tasks" / f"{sticker}.svg").exists(),
                f"Task sticker asset {sticker}.svg is missing.", errors)
        require(sticker_path in index_text,
                f"Public Front Page should show task sticker {sticker}.svg.", errors)
    require((ai_dir / "defining-ai.md").exists(), "Defining AI page is missing.", errors)
    require((ai_dir / "defining-sustainability.md").exists(), "Defining Sustainability page is missing.", errors)
    require((ai_dir / "what-does-it-cost.md").exists(), "What Does It Cost page is missing.", errors)
    require("https://what-uses-more.com" in (ai_dir / "what-does-it-cost.md").read_text(encoding="utf-8"),
            "What Does It Cost page should embed or link to the calculator.", errors)
    require(not logo_override.exists(), "Custom logo override should be removed so Material handles the homepage link.", errors)
    require(".md-sidebar--primary .md-nav__title" in css_text and "display: flex" in css_text,
            "Sidebar branding area should be visible for the group logo.", errors)
    require(".md-sidebar--primary .md-nav__title" in css_text and "font-size: 0" in css_text,
            "Sidebar title text node should be hidden while keeping the logo visible.", errors)
    require(".md-sidebar--primary .md-nav__title .md-logo" in css_text and "display: block" in css_text,
            "Sidebar group logo should render on the existing Material logo link.", errors)
    require("event_group_logo.png" in css_text,
            "Sidebar branding area should use the event group logo asset.", errors)
    require(".md-sidebar--primary .md-nav__title .md-ellipsis" in css_text and "display: none" in css_text,
            "Sidebar title text should be hidden while keeping the logo visible.", errors)
    require(".md-header__title {\n  display: none;" not in css_text,
            "Header title text should not be hidden.", errors)
    require(".md-header__topic + .md-header__topic" in css_text and "display: none" in css_text,
            "Dynamic section title should be hidden so the header keeps the project/group name.", errors)
    require(".md-typeset h1" in css_text and "var(--oasis-color-primary-blue)" in css_text,
            "Main page title should use ESIIL brand blue.", errors)
    require("assets/stickers/people.png" not in css_text and "tasks/d1-a.svg" not in css_text,
            "Homepage should use shared task sticker files in Markdown, not CSS-injected section stickers.", errors)
    require(".md-typeset h1" in css_text and "color: var(--oasis-color-primary-blue)" in css_text,
            "Main content title should use ESIIL brand blue.", errors)
    require(".task-sticker" in css_text, "Instruction task sticker styles are missing.", errors)
    require('h1[id^="day-1"]' in css_text and 'h1[id^="day-2"]' in css_text and 'h1[id^="day-3"]' in css_text,
            "Day color styling is missing.", errors)
    require('[data-md-color-scheme="slate"]' in tokens_text,
            "Dark mode token overrides are missing.", errors)
    require('[data-md-color-scheme="slate"] body' in css_text,
            "Dark mode page styling is missing.", errors)
    require("REFERENCE_MARKER" in hooks_text and "references.bib" in hooks_text,
            "Citation hook should render references from docs/references.bib.", errors)

    if errors:
        print("Template regression check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Template regression check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
