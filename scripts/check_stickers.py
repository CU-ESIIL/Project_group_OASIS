from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def sticker_issues(root: Path = ROOT) -> list[str]:
    del root
    issues: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if ".task-sticker" in text or "assets/stickers/tasks/" in text:
            issues.append(f"Retired task-sticker markup remains in {path.relative_to(ROOT)}.")
        if 'id="edit-D' in text or 'id="guide-D' in text:
            issues.append(f"Retired D1/D2/D3 sticker anchor remains in {path.relative_to(ROOT)}.")
    return issues


def main() -> int:
    issues = sticker_issues()
    if issues:
        print("Sticker cleanup validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Sticker cleanup validation passed; task-sticker workflow is retired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
