"""Tests for the CLI entry point."""

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from claude_mdfile_generator import __version__
from claude_mdfile_generator.bundled import bundled_modules_path, bundled_skills_path
from claude_mdfile_generator.cli import main


class TestVersionFlag:
    def test_version_outputs_version(self, capsys):
        with pytest.raises(SystemExit) as exc, patch("sys.argv", ["claude-md", "--version"]):
            main()
        assert exc.value.code == 0
        captured = capsys.readouterr()
        assert __version__ in captured.out

    def test_version_via_subprocess(self):
        result = subprocess.run(
            [sys.executable, "-m", "claude_mdfile_generator.cli", "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert __version__ in result.stdout


class TestInitFlag:
    def test_init_copies_modules_to_default_dir(self, tmp_path):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "--init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules") as mock_copy,
        ):
            mock_copy.return_value = 5
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_copies_modules_to_explicit_dir(self, tmp_path):
        dest = tmp_path / "custom-modules"
        with (
            patch("sys.argv", ["claude-md", "--init", "--modules-dir", str(dest)]),
            patch("claude_mdfile_generator.cli.copy_bundled_modules") as mock_copy,
        ):
            mock_copy.return_value = 3
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_prints_copied_count(self, tmp_path, capsys):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "--init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules", return_value=7),
        ):
            main()
        captured = capsys.readouterr()
        assert "7" in captured.out

    def test_init_prints_none_overwritten_when_zero(self, tmp_path, capsys):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "--init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules", return_value=0),
        ):
            main()
        captured = capsys.readouterr()
        assert "already existed" in captured.out or "none overwritten" in captured.out


class TestInitSkillsFlag:
    def test_init_skills_copies_to_given_dir(self, tmp_path):
        dest = tmp_path / "skills"
        with (
            patch("sys.argv", ["claude-md", "--init-skills", str(dest)]),
            patch("claude_mdfile_generator.cli.copy_bundled_skills") as mock_copy,
        ):
            mock_copy.return_value = 1
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_skills_actually_copies_fill_md(self, tmp_path):
        dest = tmp_path / "skills"
        with patch("sys.argv", ["claude-md", "--init-skills", str(dest)]):
            main()
        assert (dest / "fill.md").exists()


class TestBundledFlag:
    def test_bundled_flag_resolves_to_bundled_modules_path(self):
        expected_path = Path(str(bundled_modules_path()))
        with (
            patch("sys.argv", ["claude-md", "--bundled"]),
            patch("claude_mdfile_generator.cli.run_tui") as mock_run_tui,
        ):
            main()
        mock_run_tui.assert_called_once_with(modules_dir=expected_path)

    def test_bundled_modules_path_is_a_real_directory(self):
        path = bundled_modules_path()
        assert path.is_dir()

    def test_bundled_skills_path_is_a_real_directory(self):
        path = bundled_skills_path()
        assert path.is_dir()
