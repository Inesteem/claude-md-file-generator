"""Access bundled modules and skills shipped with the package."""

import shutil
from importlib import resources
from pathlib import Path


def bundled_modules_path() -> Path:
    """Return the path to the bundled modules directory."""
    return Path(str(resources.files("claude_mdfile_generator") / "bundled_modules"))


def bundled_skills_path() -> Path:
    """Return the path to the bundled skills directory."""
    return Path(str(resources.files("claude_mdfile_generator") / "bundled_skills"))


def copy_bundled_modules(dest: Path) -> int:
    """Copy all bundled modules to dest directory. Returns count of files copied."""
    dest.mkdir(parents=True, exist_ok=True)
    src = bundled_modules_path()
    count = 0
    for f in sorted(src.iterdir()):
        if f.name.endswith(".md"):
            target = dest / f.name
            if not target.exists():
                shutil.copy2(f, target)
                count += 1
    return count


def copy_bundled_skills(dest: Path) -> int:
    """Copy all bundled skills to dest directory. Returns count of files copied."""
    dest.mkdir(parents=True, exist_ok=True)
    src = bundled_skills_path()
    count = 0
    for f in sorted(src.iterdir()):
        if f.name.endswith(".md"):
            target = dest / f.name
            if not target.exists():
                shutil.copy2(f, target)
                count += 1
    return count
