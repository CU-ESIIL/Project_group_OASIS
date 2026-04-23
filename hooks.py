from pathlib import Path


def on_config(config, **kwargs):
    report = Path(__file__).resolve().parent / "docs" / "_site_health.md"
    if not report.exists():
        report.write_text(
            "Site Health\n\n"
            "⚠ Attention needed\n\n"
            "⚠ Missing required file: docs/_site_health.md\n\n"
            "This report is generated automatically during the site build. Fix these items in the repository to improve the site.\n",
            encoding="utf-8",
        )
    return config
