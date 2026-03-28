---
name: Dependency Management
type: static
tags: [dependencies]
order: 30
description: Keeping dependencies minimal and well-justified
---
## Dependency Management

- Justify every non-standard dependency — prefer stdlib solutions when they are sufficient
- Document why each dependency exists in a comment or in the project docs
- Handle optional dependencies with import-time guards and skip decorators in tests, not scattered conditionals
- Keep the total dependency count minimal; each dep is a future maintenance burden
- Pin dependency versions in lockfiles for reproducibility; use ranges only in library metadata
- Audit dependencies for known vulnerabilities before adding or upgrading (e.g. `npm audit`, `pip-audit`)
