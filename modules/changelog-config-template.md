---
name: Changelog Configuration
type: template
tags: [docs, changelog, releases, tooling]
order: 33
description: Project-specific changelog setup and release process (agent-filled)
---
<Fill Changelog Configuration>
Identify the project's changelog and release setup and document:
- Whether a CHANGELOG.md (or equivalent) exists and its format
- Versioning scheme in use (semver, calver, or other)
- Where the version is defined (pyproject.toml, package.json, Cargo.toml, etc.)
- Whether changelog entries are automated (e.g. conventional-changelog, release-please, towncrier)
- Release process: manual tags, GitHub Releases, CI-triggered publish, etc.

Verify: check for CHANGELOG.md, version fields in config files, and release
automation in CI config.
If no changelog exists, state that explicitly and recommend creating one.

Ask the user:
- What is the release process? (manual, automated, CI-triggered?)
- Is there a versioning policy (semver strict, or more relaxed)?
</Fill Changelog Configuration>
