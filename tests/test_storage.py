"""Tests for the storage layer (CRUD operations on module files)."""

import pytest
from claude_mdfile_generator.models import Module, ModuleType
from claude_mdfile_generator.storage import (
    load_module,
    save_module,
    delete_module,
    list_modules,
    StorageError,
)


class TestSaveAndLoad:
    def test_round_trip(self, modules_dir, sample_static_module):
        modules_dir.mkdir()
        path = save_module(sample_static_module, modules_dir)
        loaded = load_module(path)
        assert loaded.name == sample_static_module.name
        assert loaded.type == sample_static_module.type
        assert loaded.content == sample_static_module.content
        assert loaded.tags == sample_static_module.tags
        assert loaded.order == sample_static_module.order
        assert loaded.description == sample_static_module.description

    def test_round_trip_template(self, modules_dir, sample_template_module):
        modules_dir.mkdir()
        path = save_module(sample_template_module, modules_dir)
        loaded = load_module(path)
        assert loaded.type == ModuleType.TEMPLATE
        assert "<Architecture>" in loaded.content

    def test_save_creates_file(self, modules_dir, sample_static_module):
        modules_dir.mkdir()
        path = save_module(sample_static_module, modules_dir)
        assert path.exists()
        assert path.name == "git-rules.md"

    def test_save_overwrites_existing(self, modules_dir, sample_static_module):
        modules_dir.mkdir()
        save_module(sample_static_module, modules_dir)
        updated = Module(
            name="Git Rules",
            type=ModuleType.STATIC,
            content="Updated content\n",
        )
        path = save_module(updated, modules_dir)
        loaded = load_module(path)
        assert loaded.content == "Updated content\n"

    def test_save_creates_directory_if_missing(self, modules_dir, sample_static_module):
        path = save_module(sample_static_module, modules_dir)
        assert path.exists()

    def test_load_minimal_frontmatter(self, tmp_path):
        f = tmp_path / "minimal.md"
        f.write_text("---\nname: Minimal\ntype: static\n---\nSome content\n")
        mod = load_module(f)
        assert mod.name == "Minimal"
        assert mod.type == ModuleType.STATIC
        assert mod.content == "Some content\n"
        assert mod.tags == []
        assert mod.order == 50

    def test_load_missing_name_raises(self, tmp_path):
        f = tmp_path / "bad.md"
        f.write_text("---\ntype: static\n---\ncontent\n")
        with pytest.raises(StorageError, match="name"):
            load_module(f)

    def test_load_missing_type_raises(self, tmp_path):
        f = tmp_path / "bad.md"
        f.write_text("---\nname: Test\n---\ncontent\n")
        with pytest.raises(StorageError, match="type"):
            load_module(f)

    def test_load_no_frontmatter_raises(self, tmp_path):
        f = tmp_path / "nofm.md"
        f.write_text("Just plain markdown\n")
        with pytest.raises(StorageError):
            load_module(f)

    def test_load_nonexistent_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_module(tmp_path / "nope.md")


class TestDelete:
    def test_delete_removes_file(self, modules_dir, sample_static_module):
        modules_dir.mkdir()
        path = save_module(sample_static_module, modules_dir)
        assert path.exists()
        delete_module(sample_static_module, modules_dir)
        assert not path.exists()

    def test_delete_nonexistent_raises(self, modules_dir, sample_static_module):
        modules_dir.mkdir()
        with pytest.raises(FileNotFoundError):
            delete_module(sample_static_module, modules_dir)


class TestListModules:
    def test_list_populated(self, populated_modules_dir):
        modules = list_modules(populated_modules_dir)
        assert len(modules) == 2
        names = [m.name for m in modules]
        assert "Git Rules" in names
        assert "Architecture" in names

    def test_list_sorted_by_order(self, populated_modules_dir):
        modules = list_modules(populated_modules_dir)
        assert modules[0].order <= modules[1].order

    def test_list_empty_dir(self, modules_dir):
        modules_dir.mkdir()
        modules = list_modules(modules_dir)
        assert modules == []

    def test_list_nonexistent_dir(self, modules_dir):
        modules = list_modules(modules_dir)
        assert modules == []

    def test_list_skips_corrupt_files(self, populated_modules_dir):
        (populated_modules_dir / "corrupt.md").write_text("not valid frontmatter")
        modules = list_modules(populated_modules_dir)
        assert len(modules) == 2  # corrupt file skipped

    def test_list_skips_non_md_files(self, populated_modules_dir):
        (populated_modules_dir / "notes.txt").write_text("not a module")
        modules = list_modules(populated_modules_dir)
        assert len(modules) == 2
