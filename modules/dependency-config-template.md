---
name: Dependency Configuration
type: template
tags: [dependencies, tooling]
order: 30
description: Project-specific package manager, lock files, and dependency policies (agent-filled)
---
<Fill Dependency Configuration>
Identify the project's dependency management setup and document:
- Package manager(s) in use (pip, npm, cargo, go modules, etc.)
- Lock file path(s) and the correct command to update them
- Dependency specification file(s) (pyproject.toml, package.json, etc.)
- Banned or discouraged packages (if any policy exists)
- Vendored dependency locations (if any)
- Monorepo considerations (workspaces, shared deps)

Verify: locate lock files and dependency config. Check if a lockfile
exists and is committed.

Ask the user:
- Are there any packages or categories of packages that should not be added?
- Is there a policy for vetting new dependencies (license, popularity, etc.)?
</Fill Dependency Configuration>
