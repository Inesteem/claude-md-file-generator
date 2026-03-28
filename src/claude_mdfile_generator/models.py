"""Module data model for claude.md generation."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ModuleType(str, Enum):
    STATIC = "static"
    TEMPLATE = "template"


@dataclass
class Module:
    name: str
    type: ModuleType
    content: str
    tags: list[str] = field(default_factory=list)
    order: int = 50
    description: Optional[str] = None

    @property
    def slug(self) -> str:
        return self.name.lower().replace(" ", "-").replace("/", "-")

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"
