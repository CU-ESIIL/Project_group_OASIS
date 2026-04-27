from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = DOCS / "stickers.md"
INDEX = DOCS / "index.md"

ANCHOR_RE = re.compile(r"<(?:span|a)\s+[^>]*id=[\"']([^\"']+)[\"'][^>]*>")
LINKED_STICKER_RE = re.compile(
    r"\[!\[([^\]]+)\]\(([^)]+)\)(?:\{[^}]*task-sticker[^}]*\})?\]\(([^)]+)\)"
)
STICKER_CODE_RE = re.compile(r"[dD][1-3]-[A-Ga-g]")


@dataclass(frozen=True)
class StickerTask:
    code: str
    day: int
    task: str
    edit_anchor: str
    guide_anchor: str
    front_section: str

    @property
    def guide_file(self) -> Path:
        return DOCS / "instructions" / f"day{self.day}.md"

    @property
    def image_path(self) -> str:
        return f"assets/stickers/tasks/{self.code.lower()}.svg"

    @property
    def guide_image_path(self) -> str:
        return f"../assets/stickers/tasks/{self.code.lower()}.svg"


@dataclass(frozen=True)
class StickerLink:
    source: Path
    alt: str
    image: str
    target: str

    @property
    def code(self) -> str | None:
        match = STICKER_CODE_RE.search(self.alt)
        return match.group(0) if match else None


def strip_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def load_registry() -> list[StickerTask]:
    if not REGISTRY.exists():
        return []

    tasks: list[StickerTask] = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [strip_cell(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] == "Sticker" or set(cells[0]) <= {"-"}:
            continue
        try:
            day = int(cells[1])
        except ValueError:
            continue
        tasks.append(
            StickerTask(
                code=cells[0],
                day=day,
                task=cells[2],
                edit_anchor=cells[3],
                guide_anchor=cells[4],
                front_section=cells[5],
            )
        )
    return tasks


def markdown_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def anchors_for(path: Path) -> list[str]:
    if not path.exists():
        return []
    return ANCHOR_RE.findall(path.read_text(encoding="utf-8"))


def links_for(path: Path) -> list[StickerLink]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    return [
        StickerLink(path, alt, image, target)
        for alt, image, target in LINKED_STICKER_RE.findall(text)
        if "assets/stickers/tasks/" in image
    ]


def split_target(target: str) -> tuple[str, str]:
    clean = unquote(target.strip().strip("<>"))
    path, _, anchor = clean.partition("#")
    return path, anchor


def resolve_target(source: Path, target: str) -> tuple[Path, str] | None:
    path_text, anchor = split_target(target)
    if path_text.startswith(("http://", "https://", "mailto:")):
        return None
    target_path = source if not path_text else (source.parent / path_text).resolve()
    try:
        target_path = target_path.relative_to(ROOT)
    except ValueError:
        return None
    return ROOT / target_path, anchor


def sticker_issues(root: Path = ROOT) -> list[str]:
    del root  # The checker is intentionally rooted at this repository.
    issues: list[str] = []
    tasks = load_registry()
    if not tasks:
        return ["Missing sticker registry: expected docs/stickers.md with a task table."]

    by_code = {task.code: task for task in tasks}
    for task in tasks:
        if task.code != task.code.upper():
            issues.append(f"Sticker ID has inconsistent casing: expected uppercase, got {task.code}.")
        if task.edit_anchor != f"edit-{task.code}":
            issues.append(f"{task.code}: front-page anchor should be edit-{task.code}, found {task.edit_anchor}.")
        if task.guide_anchor != f"guide-{task.code}":
            issues.append(f"{task.code}: directions anchor should be guide-{task.code}, found {task.guide_anchor}.")
        if not task.guide_file.exists():
            issues.append(f"Missing directions file for {task.code}: expected {task.guide_file.relative_to(ROOT)}.")
        image_file = DOCS / task.image_path
        if not image_file.exists():
            issues.append(f"Missing sticker image for {task.code}: expected {image_file.relative_to(ROOT)}.")

    anchors_by_file = {path: anchors_for(path) for path in markdown_files()}
    edit_codes = {
        anchor.removeprefix("edit-")
        for anchor in anchors_by_file.get(INDEX, [])
        if anchor.startswith("edit-")
    }
    guide_codes = {
        anchor.removeprefix("guide-")
        for path, anchors in anchors_by_file.items()
        if path.match(str(DOCS / "instructions" / "day*.md"))
        for anchor in anchors
        if anchor.startswith("guide-")
    }
    registry_codes = set(by_code)

    for code in sorted(registry_codes - edit_codes):
        issues.append(f"Missing front-page edit anchor for {code}: expected edit-{code} in docs/index.md.")
    for code in sorted(edit_codes - registry_codes):
        issues.append(f"Unexpected front-page sticker anchor edit-{code}: add it to docs/stickers.md or fix the ID.")
    for code in sorted(registry_codes - guide_codes):
        task = by_code[code]
        issues.append(
            f"Missing guide anchor for {code}: expected guide-{code} in {task.guide_file.relative_to(ROOT)}."
        )
    for code in sorted(guide_codes - registry_codes):
        issues.append(f"Unexpected directions sticker anchor guide-{code}: add it to docs/stickers.md or fix the ID.")

    sticker_links = [link for path in markdown_files() for link in links_for(path)]
    links_by_code: dict[str, list[StickerLink]] = {}
    for link in sticker_links:
        code = link.code
        if code is None:
            issues.append(f"{link.source.relative_to(ROOT)} has a task-sticker link without a D#-letter code in alt text.")
            continue
        if code != code.upper():
            issues.append(f"{link.source.relative_to(ROOT)} uses inconsistent sticker casing in alt text: {code}.")
        links_by_code.setdefault(code.upper(), []).append(link)

        target = resolve_target(link.source, link.target)
        if target is None:
            issues.append(f"{link.source.relative_to(ROOT)} has sticker {code} pointing outside the site: {link.target}.")
            continue
        target_path, target_anchor = target
        if target_anchor not in anchors_by_file.get(target_path, []):
            issues.append(
                f"{link.source.relative_to(ROOT)} sticker {code} links to missing anchor "
                f"{target_anchor} in {target_path.relative_to(ROOT)}."
            )

    for code, task in by_code.items():
        links = links_by_code.get(code, [])
        if len(links) != 2:
            issues.append(f"{code} should appear as a linked sticker exactly twice; found {len(links)}.")
            continue

        front_links = [link for link in links if link.source == INDEX]
        guide_links = [link for link in links if link.source == task.guide_file]
        if len(front_links) != 1:
            issues.append(f"{code} should have one linked sticker on docs/index.md; found {len(front_links)}.")
        if len(guide_links) != 1:
            issues.append(
                f"{code} should have one linked sticker on {task.guide_file.relative_to(ROOT)}; found {len(guide_links)}."
            )

        if front_links:
            front = front_links[0]
            expected_target = f"instructions/day{task.day}.md#{task.guide_anchor}"
            if front.target != expected_target:
                issues.append(f"{code} front-page sticker should link to {expected_target}; found {front.target}.")
            if front.image != task.image_path:
                issues.append(f"{code} front-page sticker should use {task.image_path}; found {front.image}.")

        if guide_links:
            guide = guide_links[0]
            expected_target = f"../index.md#{task.edit_anchor}"
            if guide.target != expected_target:
                issues.append(f"{code} directions sticker should link to {expected_target}; found {guide.target}.")
            if guide.image != task.guide_image_path:
                issues.append(f"{code} directions sticker should use {task.guide_image_path}; found {guide.image}.")

    return issues


def main() -> int:
    issues = sticker_issues()
    if issues:
        print("Sticker validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"Sticker validation passed for {len(load_registry())} task sticker pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
