"""Smoke tests for the TUI layer."""

from pathlib import Path
from unittest.mock import patch

from claude_mdfile_generator.tui import DEFAULT_MODULES_DIR, get_modules_dir


class TestGetModulesDir:
    def test_default(self):
        with patch.dict("os.environ", {}, clear=True):
            result = get_modules_dir()
            assert result == DEFAULT_MODULES_DIR

    def test_from_env(self):
        with patch.dict("os.environ", {"CLAUDE_MD_MODULES_DIR": "/tmp/my-modules"}):
            result = get_modules_dir()
            assert result == Path("/tmp/my-modules")


class TestRunTui:
    def test_exit_immediately(self):
        """TUI should exit cleanly when user selects Exit."""
        with patch("claude_mdfile_generator.tui.questionary") as mock_q:
            mock_q.select.return_value.ask.return_value = "Exit"
            from claude_mdfile_generator.tui import run_tui

            run_tui(modules_dir=Path("/tmp/nonexistent-test-dir"))
