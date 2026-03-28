"""Tests for the claude.md generator."""

from claude_mdfile_generator.generator import generate
from claude_mdfile_generator.models import Module, ModuleType


class TestGenerate:
    def test_empty_modules(self):
        result = generate([])
        assert result == ""

    def test_single_static_module(self):
        mod = Module(name="Git Rules", type=ModuleType.STATIC, content="## Git Rules\n\n- commit often\n")
        result = generate([mod])
        assert "## Git Rules" in result
        assert "- commit often" in result

    def test_single_template_module(self):
        mod = Module(
            name="Architecture",
            type=ModuleType.TEMPLATE,
            content="<Architecture>\nFill this in.\n</Architecture>\n",
        )
        result = generate([mod])
        assert "<Architecture>" in result

    def test_multiple_modules_separated(self):
        m1 = Module(name="A", type=ModuleType.STATIC, content="Content A\n", order=10)
        m2 = Module(name="B", type=ModuleType.STATIC, content="Content B\n", order=20)
        result = generate([m1, m2])
        assert "Content A" in result
        assert "Content B" in result
        pos_a = result.index("Content A")
        pos_b = result.index("Content B")
        assert pos_a < pos_b

    def test_respects_order(self):
        m1 = Module(name="Second", type=ModuleType.STATIC, content="2\n", order=20)
        m2 = Module(name="First", type=ModuleType.STATIC, content="1\n", order=10)
        result = generate([m1, m2])
        assert result.index("1") < result.index("2")

    def test_order_tiebreaker_is_name(self):
        m1 = Module(name="Bravo", type=ModuleType.STATIC, content="B\n", order=10)
        m2 = Module(name="Alpha", type=ModuleType.STATIC, content="A\n", order=10)
        result = generate([m1, m2])
        assert result.index("A") < result.index("B")

    def test_deterministic(self):
        mods = [
            Module(name="C", type=ModuleType.STATIC, content="c\n", order=30),
            Module(name="A", type=ModuleType.STATIC, content="a\n", order=10),
            Module(name="B", type=ModuleType.STATIC, content="b\n", order=20),
        ]
        r1 = generate(mods)
        r2 = generate(mods)
        assert r1 == r2

    def test_modules_separated_by_blank_line(self):
        m1 = Module(name="A", type=ModuleType.STATIC, content="A\n", order=10)
        m2 = Module(name="B", type=ModuleType.STATIC, content="B\n", order=20)
        result = generate([m1, m2])
        assert "\n\n" in result

    def test_no_trailing_separator(self):
        m1 = Module(name="A", type=ModuleType.STATIC, content="A\n", order=10)
        result = generate([m1])
        assert not result.endswith("\n\n\n")
