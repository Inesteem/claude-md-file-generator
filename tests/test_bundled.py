"""Tests for bundled module/skill access and copy functions."""

from claude_mdfile_generator.bundled import (
    bundled_modules_path,
    bundled_skills_path,
    copy_bundled_modules,
    copy_bundled_skills,
)


class TestBundledPaths:
    def test_bundled_modules_path_exists(self):
        path = bundled_modules_path()
        assert path.exists()
        assert path.is_dir()

    def test_bundled_skills_path_exists(self):
        path = bundled_skills_path()
        assert path.exists()
        assert path.is_dir()


class TestCopyBundledModules:
    def test_copies_files_to_target(self, tmp_path):
        dest = tmp_path / "modules"
        count = copy_bundled_modules(dest)
        assert dest.is_dir()
        assert count > 0
        md_files = list(dest.glob("*.md"))
        assert len(md_files) == count

    def test_creates_destination_directory(self, tmp_path):
        dest = tmp_path / "nested" / "modules"
        assert not dest.exists()
        copy_bundled_modules(dest)
        assert dest.is_dir()

    def test_skips_existing_files(self, tmp_path):
        dest = tmp_path / "modules"
        # First copy: all files should be copied
        first_count = copy_bundled_modules(dest)
        assert first_count > 0

        # Second copy: no files should be copied (all already exist)
        second_count = copy_bundled_modules(dest)
        assert second_count == 0

    def test_existing_file_content_is_not_overwritten(self, tmp_path):
        dest = tmp_path / "modules"
        dest.mkdir()
        # Pre-create one file with custom content
        existing_file = dest / "git-rules.md"
        original_content = "custom content that should not be overwritten"
        existing_file.write_text(original_content)

        copy_bundled_modules(dest)

        # The pre-existing file must not have been overwritten
        assert existing_file.read_text() == original_content

    def test_returns_count_of_newly_copied_files(self, tmp_path):
        dest = tmp_path / "modules"
        dest.mkdir()
        # Pre-create one file so it gets skipped
        (dest / "git-rules.md").write_text("pre-existing")

        count = copy_bundled_modules(dest)
        total = len(list(bundled_modules_path().glob("*.md")))
        assert count == total - 1


class TestCopyBundledSkills:
    def test_copies_fill_md(self, tmp_path):
        dest = tmp_path / "skills"
        count = copy_bundled_skills(dest)
        assert count > 0
        assert (dest / "fill.md").exists()

    def test_creates_destination_directory(self, tmp_path):
        dest = tmp_path / "nested" / "skills"
        assert not dest.exists()
        copy_bundled_skills(dest)
        assert dest.is_dir()

    def test_skips_existing_skills(self, tmp_path):
        dest = tmp_path / "skills"
        first_count = copy_bundled_skills(dest)
        assert first_count > 0
        second_count = copy_bundled_skills(dest)
        assert second_count == 0
