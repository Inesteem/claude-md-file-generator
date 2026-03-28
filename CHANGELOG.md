# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-28

### Added

- Interactive TUI for browsing, selecting, creating, editing, and deleting modules
- 42 bundled modules (22 template, 20 static) covering project setup, workflow, code quality, security, ops, TODOs, and changelogs
- Agent skill (`fill.md`) for filling 22 template placeholder types
- Agent skill (`compose-claude-md.md`) for end-to-end agent-driven CLAUDE.md composition
- Final review pass in fill skill: checks for duplicated advice, contradictions, irrelevant sections, and restructuring opportunities
- Non-interactive CLI: `claude-md list` and `claude-md generate` subcommands for agent/script use
- `claude-md list` with `--json`, `--tags`, `--type` filtering
- `claude-md generate` with `--modules`, `--tags`, `--type`, `--exclude`, `-o` output
- `claude-md init` to bootstrap user modules from the bundled library
- `claude-md init-skills` to install agent skills
- `--bundled` for access to bundled modules
- `--modules-dir` and `CLAUDE_MD_MODULES_DIR` environment variable for custom module paths
- `--version` flag
- Static + template companion module pattern for project-specific customization
- Path traversal protection in module storage
- ruff (linter + formatter) and pyright (type checker) configuration
