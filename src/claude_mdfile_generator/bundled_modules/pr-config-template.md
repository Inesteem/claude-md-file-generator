---
name: PR Configuration
type: template
tags: [git, pr, workflow]
order: 12
description: Project-specific PR conventions, reviewers, and labels (agent-filled)
---
<Fill PR Configuration>
Identify the project's PR workflow specifics and document:
- PR template location (e.g. .github/PULL_REQUEST_TEMPLATE.md)
- Required reviewers or CODEOWNERS patterns
- Label conventions (e.g. needs-review, breaking-change, size labels)
- Required CI checks that must pass before merge
- Auto-merge rules (if configured)
- Base branch for PRs (if not main/master)

Verify: check for PR template files, CODEOWNERS, branch protection config,
and label definitions in GitHub/GitLab settings files.

Ask the user:
- Are there required reviewers or CODEOWNERS for specific paths?
- Do you use labels on PRs? If so, what conventions?
</Fill PR Configuration>
