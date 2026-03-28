---
name: Environment Setup
type: static
tags: [environment, setup]
order: 32
description: Rules for handling environment variables and paths
---
## Environment Setup

- Compute all paths relative to the project root — never hardcode absolute paths
- Access only environment variables documented in the project's env reference (e.g. `.env.example` or README)
- Use the project's standard secret placeholders (defined in Security) in all example configurations and demos
- Document every required environment variable with its name, purpose, and an example value
- Fail fast with a clear error when a required environment variable is missing — never fall back to an implicit default for security-sensitive values
