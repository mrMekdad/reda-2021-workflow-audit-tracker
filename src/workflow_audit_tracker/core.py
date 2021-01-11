"""Core workflow for Workflow Audit Tracker by Red@."""

PROJECT_NAME = "Workflow Audit Tracker"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
