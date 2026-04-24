from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    index = ROOT / "docs" / "index.md"
    mkdocs = ROOT / "mkdocs.yml"
    css = ROOT / "docs" / "stylesheets" / "extra.css"
    logo = ROOT / "docs" / "assets" / "oasis_logo.png"
    group_logo = ROOT / "docs" / "assets" / "esiil_content" / "group_logo.svg"
    logo_override = ROOT / "docs" / "overrides" / "partials" / "logo.html"

    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    mkdocs_text = mkdocs.read_text(encoding="utf-8") if mkdocs.exists() else ""
    css_text = css.read_text(encoding="utf-8") if css.exists() else ""

    require(index.exists(), "docs/index.md is missing.", errors)
    require("## How to edit this project page" in index_text, "Homepage edit guide section is missing.", errors)
    require("### Where files go" in index_text, "Homepage file map is missing.", errors)
    require("Day 1 checklist" in index_text, "Day 1 checklist is missing.", errors)
    require("Day 2 checklist" in index_text, "Day 2 checklist is missing.", errors)
    require("Final share-out checklist" in index_text, "Final share-out checklist is missing.", errors)

    for folder in ["hero", "whiteboards", "explorations", "figures", "team", "files"]:
        require((ROOT / "docs" / "assets" / folder).is_dir(), f"docs/assets/{folder}/ is missing.", errors)

    require("toc.integrate" not in mkdocs_text, "toc.integrate should not be enabled.", errors)
    require("content.action.edit" in mkdocs_text, "MkDocs edit action should remain enabled.", errors)
    require("Specialty Tracks" in mkdocs_text, "Specialty Tracks nav section is missing.", errors)
    require("site_name: \"OASIS Project Group Template\"" in mkdocs_text,
            "Header site title should be visible again.", errors)
    require("logo: 'assets/oasis_logo.png'" in mkdocs_text, "Header logo should use docs/assets/oasis_logo.png.", errors)
    require("homepage: https://cu-esiil.github.io/Project_group_OASIS/" in mkdocs_text,
            "Material homepage should point the logo to the Project_group_OASIS homepage.", errors)
    require("custom_dir:" not in mkdocs_text, "custom_dir should not point to a missing overrides folder.", errors)
    require("extra_javascript:" not in mkdocs_text, "Sidebar logo JavaScript workaround should not be registered.", errors)
    require("home-brand-link.js" not in mkdocs_text, "Sidebar logo JavaScript workaround should not be referenced.", errors)
    require(logo.exists(), "docs/assets/oasis_logo.png is missing.", errors)
    require(group_logo.exists(), "docs/assets/esiil_content/group_logo.svg is missing.", errors)
    require(not logo_override.exists(), "Custom logo override should be removed so Material handles the homepage link.", errors)
    require(".md-sidebar--primary .md-nav__title" in css_text and "display: flex" in css_text,
            "Sidebar branding area should be visible for the group logo.", errors)
    require(".md-sidebar--primary .md-nav__title" in css_text and "font-size: 0" in css_text,
            "Sidebar title text node should be hidden while keeping the logo visible.", errors)
    require("group_logo.svg" in css_text,
            "Sidebar branding area should use the group logo asset.", errors)
    require(".md-sidebar--primary .md-nav__title .md-ellipsis" in css_text and "display: none" in css_text,
            "Sidebar title text should be hidden while keeping the logo visible.", errors)
    require(".md-header__title {\n  display: none;" not in css_text,
            "Header title text should not be hidden.", errors)

    if errors:
        print("Template regression check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Template regression check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
