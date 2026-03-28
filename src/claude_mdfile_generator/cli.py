"""CLI entry point with interactive TUI and non-interactive subcommands."""

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .bundled import bundled_modules_path, copy_bundled_modules, copy_bundled_skills
from .generator import generate
from .storage import list_modules
from .tui import DEFAULT_MODULES_DIR, _module_source, run_tui


def _resolve_modules_dir(args: argparse.Namespace) -> Path:
    """Resolve the modules directory from CLI args.

    Priority: --modules-dir > --bundled > user config dir (if non-empty) > bundled fallback.
    """
    if args.modules_dir:
        return args.modules_dir
    if getattr(args, "bundled", False):
        return Path(str(bundled_modules_path()))
    # Fall back to user config dir if it exists and has modules, otherwise use bundled
    if DEFAULT_MODULES_DIR.exists() and any(DEFAULT_MODULES_DIR.glob("*.md")):
        return DEFAULT_MODULES_DIR
    return Path(str(bundled_modules_path()))


def cmd_tui(args: argparse.Namespace) -> None:
    """Launch the interactive TUI."""
    run_tui(modules_dir=_resolve_modules_dir(args))


def cmd_list(args: argparse.Namespace) -> None:
    """List available modules."""
    modules_dir = _resolve_modules_dir(args)
    modules = list_modules(modules_dir)

    if not modules:
        print(f"No modules found in {modules_dir}", file=sys.stderr)
        sys.exit(1)

    if args.tags:
        filter_tags = {t.strip().lower() for t in args.tags.split(",")}
        modules = [m for m in modules if filter_tags & {t.lower() for t in m.tags}]

    if args.type:
        modules = [m for m in modules if m.type.value == args.type]

    if args.json:
        data = [
            {
                "name": m.name,
                "type": m.type.value,
                "source": _module_source(m),
                "order": m.order,
                "tags": m.tags,
                "description": m.description,
                "filename": m.filename,
            }
            for m in modules
        ]
        print(json.dumps(data, indent=2))
    else:
        for m in modules:
            source = _module_source(m)
            tags = ", ".join(m.tags) if m.tags else ""
            desc = m.description or ""
            print(f"{m.order:3d} | {m.type.value:8s} | {source:7s} | {m.name:40s} | {tags:30s} | {desc}")


def cmd_generate(args: argparse.Namespace) -> None:
    """Generate a claude.md from selected modules."""
    modules_dir = _resolve_modules_dir(args)
    all_modules = list_modules(modules_dir)

    if not all_modules:
        print(f"No modules found in {modules_dir}", file=sys.stderr)
        sys.exit(1)

    selected = all_modules

    # Filter by names
    if args.modules:
        names = {n.strip().lower() for n in args.modules.split(",")}
        selected = [m for m in selected if m.name.lower() in names]
        missing = names - {m.name.lower() for m in selected}
        if missing:
            print(f"Warning: modules not found: {', '.join(sorted(missing))}", file=sys.stderr)

    # Filter by tags
    if args.tags:
        filter_tags = {t.strip().lower() for t in args.tags.split(",")}
        selected = [m for m in selected if filter_tags & {t.lower() for t in m.tags}]

    # Filter by type
    if args.type:
        selected = [m for m in selected if m.type.value == args.type]

    # Exclude by names
    if args.exclude:
        exclude_names = {n.strip().lower() for n in args.exclude.split(",")}
        selected = [m for m in selected if m.name.lower() not in exclude_names]

    if not selected:
        print("No modules matched the selection criteria.", file=sys.stderr)
        sys.exit(1)

    output = generate(selected)

    if args.output:
        out = Path(args.output)
        if args.append and out.exists():
            existing = out.read_text()
            output = existing.rstrip("\n") + "\n\n" + output
            print(f"Appended {len(selected)} modules to {out}", file=sys.stderr)
        else:
            print(f"Written {len(selected)} modules to {out}", file=sys.stderr)
        out.write_text(output)
    else:
        print(output)


def cmd_init(args: argparse.Namespace) -> None:
    """Copy bundled modules to user directory."""
    dest = args.modules_dir or DEFAULT_MODULES_DIR
    count = copy_bundled_modules(dest)
    print(f"Copied {count} bundled modules to {dest}")
    if count == 0:
        print("(all modules already existed, none overwritten)")


def cmd_init_skills(args: argparse.Namespace) -> None:
    """Copy bundled skills to a directory."""
    count = copy_bundled_skills(args.dest)
    print(f"Copied {count} bundled skills to {args.dest}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="claude-md",
        description="Generate claude.md files from reusable modules",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--modules-dir",
        type=Path,
        default=None,
        help="Path to modules directory (default: ~/.config/claude-mdfile-generator/modules)",
    )
    parser.add_argument(
        "--bundled",
        action="store_true",
        help="Use the 42 modules shipped with the package",
    )

    subparsers = parser.add_subparsers(dest="command")

    # --- list ---
    p_list = subparsers.add_parser("list", help="List available modules (non-interactive)")
    p_list.add_argument("--json", action="store_true", help="Output as JSON")
    p_list.add_argument("--tags", type=str, default=None, help="Filter by tags (comma-separated)")
    p_list.add_argument("--type", choices=["static", "template"], default=None, help="Filter by module type")
    p_list.set_defaults(func=cmd_list)

    # --- generate ---
    p_gen = subparsers.add_parser("generate", help="Generate claude.md from selected modules (non-interactive)")
    p_gen.add_argument("--modules", type=str, default=None, help="Module names to include (comma-separated)")
    p_gen.add_argument("--tags", type=str, default=None, help="Include modules matching these tags (comma-separated)")
    p_gen.add_argument("--type", choices=["static", "template"], default=None, help="Include only this module type")
    p_gen.add_argument("--exclude", type=str, default=None, help="Module names to exclude (comma-separated)")
    p_gen.add_argument("-o", "--output", type=str, default=None, help="Output file path (default: stdout)")
    p_gen.add_argument(
        "--append", action="store_true", help="Append to existing file instead of overwriting (requires -o)"
    )
    p_gen.set_defaults(func=cmd_generate)

    # --- init ---
    p_init = subparsers.add_parser("init", help="Copy bundled modules to your modules directory")
    p_init.set_defaults(func=cmd_init)

    # --- init-skills ---
    p_skills = subparsers.add_parser("init-skills", help="Copy bundled skills to a directory")
    p_skills.add_argument("dest", type=Path, help="Destination directory (e.g. ~/.claude/skills)")
    p_skills.set_defaults(func=cmd_init_skills)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        # No subcommand — launch interactive TUI (backwards compatible)
        # Also handle legacy --init and --init-skills flags
        run_tui(modules_dir=_resolve_modules_dir(args))


if __name__ == "__main__":
    main()
