---
name: Database Conventions
type: static
tags: [database, sql]
order: 38
description: Naming, migration, and query conventions for databases
---
## Database Conventions

- Use consistent snake_case naming for all tables and columns
- Always include `created_at` and `updated_at` timestamp columns on every table
- Write idempotent migrations that are safe to re-run without side effects
- Validate query performance with `EXPLAIN` (or `EXPLAIN ANALYZE`) before recommending new indexes
