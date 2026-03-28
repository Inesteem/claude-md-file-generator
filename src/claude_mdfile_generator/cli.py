"""CLI entry point."""

import argparse
from pathlib import Path

from .bundled import bundled_modules_path, copy_bundled_modules, copy_bundled_skills
from .tui import DEFAULT_MODULES_DIR, run_tui


def main():
    parser = argparse.ArgumentParser(description="Generate claude.md files from reusable modules")
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=None,
        help="Path to modules directory (default: ~/.config/claude-mdfile-generator/modules)",
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Copy bundled modules to your modules directory (skips existing files)",
    )
    parser.add_argument(
        "--init-skills",
        type=Path,
        default=None,
        metavar="DIR",
        help="Copy bundled skills (e.g. fill.md) to the given directory",
    )
    parser.add_argument(
        "--bundled",
        action="store_true",
        help="Use the bundled modules shipped with the package (read-only)",
    )
    args = parser.parse_args()

    if args.init:
        dest = args.modules_dir or DEFAULT_MODULES_DIR
        count = copy_bundled_modules(dest)
        print(f"Copied {count} bundled modules to {dest}")
        if count == 0:
            print("(all modules already existed, none overwritten)")
        return

    if args.init_skills:
        count = copy_bundled_skills(args.init_skills)
        print(f"Copied {count} bundled skills to {args.init_skills}")
        return

    if args.bundled:
        run_tui(modules_dir=Path(str(bundled_modules_path())))
    else:
        run_tui(modules_dir=args.modules_dir)


if __name__ == "__main__":
    main()
