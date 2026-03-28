---
name: Error Patterns
type: template
tags: [errors, patterns]
order: 29
description: Project-specific error handling patterns and types (agent-filled)
---
<Fill Error Patterns>
Analyze the project's error handling approach and document:
- Primary error propagation mechanism (exceptions, Result/Option types, error codes, HTTP statuses)
- Custom error types/classes the project defines, and when to use each
- Whether errors are logged at the point of origin or at the boundary
- Expected error response shape for APIs (if applicable)
- How third-party errors are handled (wrap, re-raise, convert to domain errors)
- Retry or fallback patterns in use

Verify: search for custom error/exception classes and trace how they propagate.

Ask the user:
- Is there a retry/fallback policy for external service failures?
- Are there error types that should never be caught silently?
</Fill Error Patterns>
