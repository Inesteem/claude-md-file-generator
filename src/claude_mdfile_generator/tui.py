"""Terminal UI for module management and claude.md generation."""

import os
import shlex
import subprocess
import tempfile
from pathlib import Path

import questionary
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

from .bundled import bundled_modules_path, copy_bundled_modules
from .generator import generate
from .models import Module, ModuleType
from .storage import delete_module, list_modules, save_module

console = Console()

DEFAULT_MODULES_DIR = Path.home() / ".config" / "claude-mdfile-generator" / "modules"


def _is_bundled(modules_dir: Path) -> bool:
    """Check if the modules directory is the read-only bundled path."""
    try:
        return modules_dir.resolve() == bundled_modules_path().resolve()
    except Exception:
        return False


def _ensure_writable(modules_dir: Path) -> Path:
    """If modules_dir is the bundled (read-only) path, copy to user config dir and switch.

    Returns the writable modules directory.
    """
    if not _is_bundled(modules_dir):
        return modules_dir

    console.print(
        "[yellow]Bundled modules are read-only. "
        f"Copying to {DEFAULT_MODULES_DIR} for editing...[/yellow]"
    )
    count = copy_bundled_modules(DEFAULT_MODULES_DIR)
    console.print(f"[green]Copied {count} modules to {DEFAULT_MODULES_DIR}[/green]")
    return DEFAULT_MODULES_DIR


def _checkbox_auto_advance(message: str, choices: list[questionary.Choice]) -> list | None:  # pyright: ignore[reportReturnType]
    """Checkbox prompt where space toggles AND moves to the next item."""
    from questionary.prompts.checkbox import InquirerControl  # pyright: ignore[reportPrivateImportUsage]

    question = questionary.checkbox(message, choices=choices)
    app = question.application

    # Find the InquirerControl instance in the layout
    ic = None
    for win in app.layout.find_all_windows():
        if isinstance(win.content, InquirerControl):
            ic = win.content
            break

    if ic is None:
        return question.ask()

    # Patch the space keybinding to also advance the cursor after toggling
    for binding in app.key_bindings.bindings:  # pyright: ignore[reportOptionalMemberAccess]
        if binding.keys == (" ",):
            original_handler = binding.handler

            def patched_handler(event, _orig=original_handler, _ic=ic):  # type: ignore[no-untyped-def]
                _orig(event)
                _ic.select_next()

            binding.handler = patched_handler
            break

    return question.ask()


def get_modules_dir() -> Path:
    env = os.environ.get("CLAUDE_MD_MODULES_DIR")
    if env:
        return Path(env)
    return DEFAULT_MODULES_DIR


def _edit_in_editor(initial_content: str = "") -> str | None:
    """Open the user's $EDITOR with initial content and return the result."""
    editor_cmd = shlex.split(os.environ.get("EDITOR", "vi"))
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False) as f:
        f.write(initial_content)
        f.flush()
        tmp_path = f.name
    try:
        result = subprocess.run([*editor_cmd, tmp_path])
        if result.returncode != 0:
            return None
        return Path(tmp_path).read_text()
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def _display_modules_table(modules: list[Module]) -> None:
    if not modules:
        console.print("[dim]No modules found.[/dim]")
        return
    table = Table(title="Available Modules")
    table.add_column("Name", style="bold cyan")
    table.add_column("Type", style="green")
    table.add_column("Order", justify="right")
    table.add_column("Tags")
    table.add_column("Description", style="dim")
    for m in modules:
        table.add_row(
            m.name,
            m.type.value,
            str(m.order),
            ", ".join(m.tags) if m.tags else "-",
            m.description or "-",
        )
    console.print(table)


def action_browse_and_generate(modules_dir: Path) -> None:
    modules = list_modules(modules_dir)
    if not modules:
        console.print("[yellow]No modules found. Create some first![/yellow]")
        return

    choices = [
        questionary.Choice(
            title=f"{m.name} [{m.type.value}] - {m.description or 'No description'}",
            value=m,
        )
        for m in modules
    ]
    selected = _checkbox_auto_advance(
        "Select modules to include in your claude.md:",
        choices=choices,
    )

    if not selected:
        console.print("[dim]No modules selected.[/dim]")
        return

    output = generate(selected)
    console.print(Panel(Markdown(output), title="Preview", border_style="green"))

    output_path = questionary.path("Output path:", default="CLAUDE.md").ask()
    if not output_path:
        return

    out = Path(output_path)
    if out.exists():
        overwrite = questionary.confirm(f"{out} already exists. Overwrite?", default=False).ask()
        if not overwrite:
            return
    try:
        out.write_text(output)
        console.print(f"[bold green]Written to {output_path}[/bold green]")
    except OSError as e:
        console.print(f"[red]Failed to write: {e}[/red]")


def action_create_module(modules_dir: Path) -> None:
    name = questionary.text("Module name:").ask()
    if not name:
        return

    mod_type = questionary.select(
        "Module type:",
        choices=[
            questionary.Choice("static - User-defined content", value="static"),
            questionary.Choice("template - Placeholder for agent to fill", value="template"),
        ],
    ).ask()
    if not mod_type:
        return

    description = questionary.text("Short description (optional):").ask()
    tags_str = questionary.text("Tags (comma-separated, optional):").ask()
    order_str = questionary.text("Sort order (default 50):").ask()

    tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []
    order = int(order_str) if order_str and order_str.isdigit() else 50

    if mod_type == "template":
        tag_name = questionary.text(
            "Template tag name — will be wrapped as <Fill TagName> (e.g. Architecture):", default=name
        ).ask()
        hint = questionary.text("Instructions for the agent:").ask() or "Fill in this section."
        content = f"<Fill {tag_name}>\n{hint}\n</Fill {tag_name}>\n"
    else:
        console.print("[dim]Opening editor for module content...[/dim]")
        content = _edit_in_editor(f"## {name}\n\n")
        if content is None:
            console.print("[red]Editor returned an error. Aborting.[/red]")
            return

    module = Module(
        name=name,
        type=ModuleType(mod_type),
        content=content,
        tags=tags,
        order=order,
        description=description or None,
    )
    path = save_module(module, modules_dir)
    console.print(f"[bold green]Module saved: {path}[/bold green]")


def action_edit_module(modules_dir: Path) -> None:
    modules = list_modules(modules_dir)
    if not modules:
        console.print("[yellow]No modules to edit.[/yellow]")
        return

    choices = [questionary.Choice(title=m.name, value=m) for m in modules]
    selected = questionary.select("Select module to edit:", choices=choices).ask()
    if not selected:
        return

    what = questionary.select(
        "What to edit?",
        choices=["Content", "Metadata (name, tags, order, description)"],
    ).ask()
    if not what:
        return

    if what == "Content":
        new_content = _edit_in_editor(selected.content)
        if new_content is None:
            console.print("[red]Editor returned an error.[/red]")
            return
        selected.content = new_content
    else:
        new_name = questionary.text("Name:", default=selected.name).ask()
        new_desc = questionary.text("Description:", default=selected.description or "").ask()
        new_tags = questionary.text("Tags:", default=", ".join(selected.tags)).ask()
        new_order = questionary.text("Order:", default=str(selected.order)).ask()

        old_filename = selected.filename
        if new_name:
            selected.name = new_name
        selected.description = new_desc or None
        selected.tags = [t.strip() for t in new_tags.split(",") if t.strip()] if new_tags else []
        selected.order = int(new_order) if new_order and new_order.isdigit() else selected.order

        # Remove old file if slug changed
        if selected.filename != old_filename:
            old_path = modules_dir / old_filename
            if old_path.exists():
                old_path.unlink()

    path = save_module(selected, modules_dir)
    console.print(f"[bold green]Module updated: {path}[/bold green]")


def action_delete_module(modules_dir: Path) -> None:
    modules = list_modules(modules_dir)
    if not modules:
        console.print("[yellow]No modules to delete.[/yellow]")
        return

    choices = [questionary.Choice(title=m.name, value=m) for m in modules]
    selected = questionary.select("Select module to delete:", choices=choices).ask()
    if not selected:
        return

    confirm = questionary.confirm(f"Delete '{selected.name}'?", default=False).ask()
    if confirm:
        delete_module(selected, modules_dir)
        console.print(f"[bold red]Deleted: {selected.name}[/bold red]")


def run_tui(modules_dir: Path | None = None) -> None:
    """Main TUI loop."""
    if modules_dir is None:
        modules_dir = get_modules_dir()

    console.print(
        Panel("[bold]Claude MD Generator[/bold]\nCompose claude.md files from reusable modules", border_style="blue")
    )

    while True:
        _display_modules_table(list_modules(modules_dir))
        console.print()

        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Browse & select modules → generate claude.md",
                "Create new module",
                "Edit existing module",
                "Delete module",
                "Exit",
            ],
        ).ask()

        if action is None or action == "Exit":
            console.print("[dim]Goodbye![/dim]")
            break
        elif action.startswith("Browse"):
            action_browse_and_generate(modules_dir)
        elif action.startswith("Create"):
            modules_dir = _ensure_writable(modules_dir)
            action_create_module(modules_dir)
        elif action.startswith("Edit"):
            modules_dir = _ensure_writable(modules_dir)
            action_edit_module(modules_dir)
        elif action.startswith("Delete"):
            modules_dir = _ensure_writable(modules_dir)
            action_delete_module(modules_dir)
