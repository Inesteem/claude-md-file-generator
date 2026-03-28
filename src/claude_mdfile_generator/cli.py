"""CLI entry point."""

import argparse
from pathlib import Path

from .tui import run_tui


def main():
    parser = argparse.ArgumentParser(description="Generate claude.md files from reusable modules")
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=None,
        help="Path to modules directory (default: ~/.config/claude-mdfile-generator/modules)",
    )
    args = parser.parse_args()
    run_tui(modules_dir=args.modules_dir)


if __name__ == "__main__":
    main()
