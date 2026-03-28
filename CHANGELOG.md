# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-28

### Added

- Interactive TUI for browsing, selecting, creating, editing, and deleting modules
- 42 bundled modules (22 template, 20 static) covering project setup, workflow, code quality, security, ops, TODOs, and changelogs
- Agent skill (`fill.md`) for filling 22 template placeholder types
- Final review pass in fill skill: checks for duplicated advice, contradictions, irrelevant sections, and restructuring opportunities
- `--init` to bootstrap user modules from the bundled library
- `--bundled` for read-only access to bundled modules
- `--init-skills` to install the fill agent skill
- `--modules-dir` and `CLAUDE_MD_MODULES_DIR` environment variable for custom module paths
- `--version` flag
- Static + template companion module pattern for project-specific customization
- Path traversal protection in module storage
- ruff (linter + formatter) and pyright (type checker) configuration
