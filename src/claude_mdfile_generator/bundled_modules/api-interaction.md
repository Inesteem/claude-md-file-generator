---
name: API Interaction
type: static
tags: [api, http]
order: 34
description: Safe and correct patterns for working with HTTP APIs
---
## API Interaction

- Use the project's standard secret placeholders (defined in Security) in all curl and HTTP client examples
- Set explicit timeouts on all HTTP requests; never rely on client or OS defaults
- Respect API rate limits; add backoff or retry logic where appropriate
- Handle pagination and continuation tokens — never assume a single response contains all results
- Check HTTP status codes explicitly; do not assume 2xx — handle 4xx/5xx with appropriate error messages
- Always include explicit headers in `curl` and HTTP client examples (e.g. `Content-Type`, `Authorization`)
