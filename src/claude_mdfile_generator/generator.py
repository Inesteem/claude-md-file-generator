"""Compose selected modules into a claude.md string."""

from .models import Module


def generate(modules: list[Module]) -> str:
    """Produce a claude.md string from selected modules, sorted by order then name."""
    if not modules:
        return ""
    sorted_modules = sorted(modules, key=lambda m: (m.order, m.name))
    sections = [m.content.rstrip("\n") for m in sorted_modules]
    return "\n\n".join(sections) + "\n"
