"""Tests for the Module model and ModuleType enum."""

import pytest

from claude_mdfile_generator.models import Module, ModuleType


class TestModuleType:
    def test_static_value(self):
        assert ModuleType.STATIC == "static"

    def test_template_value(self):
        assert ModuleType.TEMPLATE == "template"

    def test_from_string(self):
        assert ModuleType("static") is ModuleType.STATIC
        assert ModuleType("template") is ModuleType.TEMPLATE

    def test_invalid_type_raises(self):
        with pytest.raises(ValueError):
            ModuleType("invalid")


class TestModule:
    def test_create_static_module(self):
        mod = Module(
            name="Git Rules",
            type=ModuleType.STATIC,
            content="## Git Rules\n- Use conventional commits\n",
        )
        assert mod.name == "Git Rules"
        assert mod.type == ModuleType.STATIC
        assert mod.content.startswith("## Git Rules")

    def test_create_template_module(self):
        mod = Module(
            name="Architecture",
            type=ModuleType.TEMPLATE,
            content="<Architecture>\nDescribe the high-level architecture.\n</Architecture>\n",
        )
        assert mod.type == ModuleType.TEMPLATE
        assert "<Architecture>" in mod.content

    def test_default_values(self):
        mod = Module(name="Test", type=ModuleType.STATIC, content="x")
        assert mod.tags == []
        assert mod.order == 50
        assert mod.description is None

    def test_custom_order_and_tags(self):
        mod = Module(
            name="Test",
            type=ModuleType.STATIC,
            content="x",
            tags=["git", "workflow"],
            order=10,
            description="Short summary",
        )
        assert mod.tags == ["git", "workflow"]
        assert mod.order == 10
        assert mod.description == "Short summary"

    def test_slug_simple(self):
        mod = Module(name="Git Rules", type=ModuleType.STATIC, content="x")
        assert mod.slug == "git-rules"

    def test_slug_special_characters(self):
        mod = Module(name="CI/CD Pipeline", type=ModuleType.STATIC, content="x")
        assert mod.slug == "ci-cd-pipeline"

    def test_slug_multiple_spaces(self):
        mod = Module(name="My  Great  Module", type=ModuleType.STATIC, content="x")
        assert mod.slug == "my--great--module"

    def test_filename(self):
        mod = Module(name="Git Rules", type=ModuleType.STATIC, content="x")
        assert mod.filename == "git-rules.md"

    def test_slug_unicode(self):
        mod = Module(name="Über Module", type=ModuleType.STATIC, content="x")
        assert mod.slug == "über-module"

    def test_slug_already_lowercase(self):
        mod = Module(name="simple", type=ModuleType.STATIC, content="x")
        assert mod.slug == "simple"
