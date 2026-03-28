"""Module data model for claude.md generation."""

import re
from dataclasses import dataclass, field
from enum import StrEnum


class ModuleType(StrEnum):
    STATIC = "static"
    TEMPLATE = "template"


@dataclass
class Module:
    name: str
    type: ModuleType
    content: str
    tags: list[str] = field(default_factory=list)
    order: int = 50
    description: str | None = None

    @property
    def slug(self) -> str:
        s = self.name.lower()
        s = re.sub(r"[^a-z0-9\s-]", "", s)
        s = re.sub(r"[\s]+", "-", s)
        s = re.sub(r"-+", "-", s)
        return s.strip("-") or "unnamed"

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"
