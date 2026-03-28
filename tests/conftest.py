"""Shared test fixtures."""

import pytest
from pathlib import Path
from claude_mdfile_generator.models import Module, ModuleType


@pytest.fixture
def sample_static_module():
    return Module(
        name="Git Rules",
        type=ModuleType.STATIC,
        content="## Git Rules\n\n- Use conventional commits\n- Never force push to main\n",
        tags=["git", "workflow"],
        order=10,
        description="Git workflow conventions",
    )


@pytest.fixture
def sample_template_module():
    return Module(
        name="Architecture",
        type=ModuleType.TEMPLATE,
        content="<Architecture>\nDescribe the high-level architecture of this project.\n</Architecture>\n",
        tags=["architecture"],
        order=20,
        description="Architecture overview (agent-filled)",
    )


@pytest.fixture
def modules_dir(tmp_path):
    return tmp_path / "modules"


@pytest.fixture
def populated_modules_dir(modules_dir, sample_static_module, sample_template_module):
    """A modules directory pre-populated with two sample modules."""
    modules_dir.mkdir()
    # Write static module
    modules_dir.joinpath("git-rules.md").write_text(
        "---\n"
        "name: Git Rules\n"
        "type: static\n"
        "tags: [git, workflow]\n"
        "order: 10\n"
        "description: Git workflow conventions\n"
        "---\n"
        "## Git Rules\n"
        "\n"
        "- Use conventional commits\n"
        "- Never force push to main\n"
    )
    # Write template module
    modules_dir.joinpath("architecture.md").write_text(
        "---\n"
        "name: Architecture\n"
        "type: template\n"
        "tags: [architecture]\n"
        "order: 20\n"
        "description: Architecture overview (agent-filled)\n"
        "---\n"
        "<Architecture>\n"
        "Describe the high-level architecture of this project.\n"
        "</Architecture>\n"
    )
    return modules_dir
