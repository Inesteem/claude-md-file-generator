---
name: CI Pipeline
type: template
tags: [ci, tooling, automation]
order: 27
description: CI/CD pipeline configuration and checks (agent-filled and verified)
---
<Fill CI Pipeline>
Identify the CI/CD setup for this project and document:
- Which CI system is used (e.g. GitHub Actions, GitLab CI, Jenkins, CircleCI)
- Where the config lives (e.g. .github/workflows/, .gitlab-ci.yml)
- What checks run on each PR (tests, lint, type check, build, etc.)
- What checks run on merge to main (deploy, publish, release, etc.)
- Required checks that must pass before merging
- Any matrix testing (multiple OS, Python/Node versions, etc.)

Verify: read the CI config files and confirm the documented commands match
what is actually configured. If no CI is set up, state that explicitly.
</Fill CI Pipeline>
