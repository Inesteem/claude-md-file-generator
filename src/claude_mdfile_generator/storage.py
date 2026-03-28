"""CRUD operations for module files (markdown with YAML frontmatter)."""

import logging
from pathlib import Path

import yaml

from .models import Module, ModuleType

logger = logging.getLogger(__name__)


class StorageError(Exception):
    """Raised when a module file cannot be parsed."""


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a markdown file into YAML frontmatter dict and body content."""
    if not text.startswith("---"):
        raise StorageError("File does not contain YAML frontmatter (no opening ---)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise StorageError("File has opening --- but no closing ---")
    meta = yaml.safe_load(parts[1])
    if not isinstance(meta, dict):
        raise StorageError("Frontmatter is not a valid YAML mapping")
    body = parts[2]
    if body.startswith("\n"):
        body = body[1:]
    return meta, body


def _serialize_frontmatter(meta: dict, body: str) -> str:
    """Combine a metadata dict and body into a frontmatter markdown string."""
    fm = yaml.dump(meta, default_flow_style=False, sort_keys=False).strip()
    return f"---\n{fm}\n---\n{body}"


def load_module(path: Path) -> Module:
    """Parse a .md file with YAML frontmatter into a Module."""
    text = path.read_text()
    meta, body = _parse_frontmatter(text)

    if "name" not in meta:
        raise StorageError(f"Module file {path} missing required field: name")
    if "type" not in meta:
        raise StorageError(f"Module file {path} missing required field: type")

    return Module(
        name=meta["name"],
        type=ModuleType(meta["type"]),
        content=body,
        tags=meta.get("tags", []),
        order=meta.get("order", 50),
        description=meta.get("description"),
    )


def save_module(module: Module, directory: Path) -> Path:
    """Serialize a Module to a .md file. Returns the written path."""
    directory.mkdir(parents=True, exist_ok=True)
    meta = {
        "name": module.name,
        "type": module.type.value,
        "tags": module.tags,
        "order": module.order,
    }
    if module.description:
        meta["description"] = module.description

    path = directory / module.filename
    path.write_text(_serialize_frontmatter(meta, module.content))
    return path


def delete_module(module: Module, directory: Path) -> None:
    """Remove the module's file."""
    path = directory / module.filename
    if not path.exists():
        raise FileNotFoundError(f"Module file not found: {path}")
    path.unlink()


def list_modules(directory: Path) -> list[Module]:
    """Load all .md files in directory, sorted by order then name."""
    if not directory.exists():
        return []
    modules = []
    for path in sorted(directory.glob("*.md")):
        try:
            modules.append(load_module(path))
        except (StorageError, ValueError) as e:
            logger.warning("Skipping %s: %s", path.name, e)
    modules.sort(key=lambda m: (m.order, m.name))
    return modules
