"""Tests for the CLI entry point."""

import json
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


class TestInitSubcommand:
    def test_init_copies_modules_to_default_dir(self, tmp_path):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules") as mock_copy,
        ):
            mock_copy.return_value = 5
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_copies_modules_to_explicit_dir(self, tmp_path):
        dest = tmp_path / "custom-modules"
        with (
            patch("sys.argv", ["claude-md", "--modules-dir", str(dest), "init"]),
            patch("claude_mdfile_generator.cli.copy_bundled_modules") as mock_copy,
        ):
            mock_copy.return_value = 3
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_prints_copied_count(self, tmp_path, capsys):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules", return_value=7),
        ):
            main()
        captured = capsys.readouterr()
        assert "7" in captured.out

    def test_init_prints_none_overwritten_when_zero(self, tmp_path, capsys):
        dest = tmp_path / "modules"
        with (
            patch("sys.argv", ["claude-md", "init"]),
            patch("claude_mdfile_generator.cli.DEFAULT_MODULES_DIR", dest),
            patch("claude_mdfile_generator.cli.copy_bundled_modules", return_value=0),
        ):
            main()
        captured = capsys.readouterr()
        assert "already existed" in captured.out or "none overwritten" in captured.out


class TestInitSkillsSubcommand:
    def test_init_skills_copies_to_given_dir(self, tmp_path):
        dest = tmp_path / "skills"
        with (
            patch("sys.argv", ["claude-md", "init-skills", str(dest)]),
            patch("claude_mdfile_generator.cli.copy_bundled_skills") as mock_copy,
        ):
            mock_copy.return_value = 1
            main()
        mock_copy.assert_called_once_with(dest)

    def test_init_skills_actually_copies_fill_md(self, tmp_path):
        dest = tmp_path / "skills"
        with patch("sys.argv", ["claude-md", "init-skills", str(dest)]):
            main()
        assert (dest / "fill.md").exists()


class TestBundledFlag:
    def test_bundled_flag_with_tui(self):
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


class TestListSubcommand:
    def test_list_outputs_modules(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "list"]):
            main()
        captured = capsys.readouterr()
        assert "Git Rules" in captured.out
        assert "static" in captured.out

    def test_list_json(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "list", "--json"]):
            main()
        data = json.loads(capsys.readouterr().out)
        assert isinstance(data, list)
        assert len(data) > 0
        assert "name" in data[0]
        assert "type" in data[0]
        assert "tags" in data[0]

    def test_list_filter_by_type(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "list", "--type", "template", "--json"]):
            main()
        data = json.loads(capsys.readouterr().out)
        assert all(m["type"] == "template" for m in data)

    def test_list_filter_by_tags(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "list", "--tags", "git", "--json"]):
            main()
        data = json.loads(capsys.readouterr().out)
        assert len(data) > 0
        assert all(any("git" in t.lower() for t in m["tags"]) for m in data)

    def test_list_empty_dir_exits_1(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()
        with patch("sys.argv", ["claude-md", "--modules-dir", str(empty), "list"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1


class TestGenerateSubcommand:
    def test_generate_all_to_stdout(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate"]):
            main()
        output = capsys.readouterr().out
        assert "## Git Rules" in output
        assert "## Security" in output

    def test_generate_select_by_name(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "--modules", "Git Rules,Security"]):
            main()
        output = capsys.readouterr().out
        assert "## Git Rules" in output
        assert "## Security" in output
        assert "## Performance" not in output

    def test_generate_exclude_by_name(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "--exclude", "Performance,Security"]):
            main()
        output = capsys.readouterr().out
        assert "## Performance" not in output
        assert "## Security" not in output
        assert "## Git Rules" in output

    def test_generate_filter_by_type(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "--type", "static"]):
            main()
        output = capsys.readouterr().out
        assert "<Fill " not in output
        assert "## Git Rules" in output

    def test_generate_filter_by_tags(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "--tags", "security"]):
            main()
        output = capsys.readouterr().out
        assert "## Security" in output

    def test_generate_to_file(self, tmp_path, capsys):
        out = tmp_path / "CLAUDE.md"
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "-o", str(out)]):
            main()
        assert out.exists()
        content = out.read_text()
        assert "## Git Rules" in content
        # Status message goes to stderr
        captured = capsys.readouterr()
        assert "Written" in captured.err

    def test_generate_warns_on_missing_modules(self, capsys):
        with patch("sys.argv", ["claude-md", "--bundled", "generate", "--modules", "Nonexistent Module"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1

    def test_generate_empty_dir_exits_1(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()
        with patch("sys.argv", ["claude-md", "--modules-dir", str(empty), "generate"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
