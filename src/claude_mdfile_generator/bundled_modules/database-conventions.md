---
name: Database Conventions
type: static
tags: [database, sql]
order: 38
description: Naming, migration, and query conventions for databases
---
## Database Conventions

- Use consistent snake_case naming for all tables and columns
- Include `created_at` and `updated_at` timestamp columns on entity tables; omit them on simple join tables or static lookup tables where they add no value
- Define foreign key constraints explicitly — do not rely on application-level enforcement alone
- Write idempotent migrations that are safe to re-run without side effects
- Validate query performance with `EXPLAIN` (or `EXPLAIN ANALYZE`) before recommending new indexes
- Wrap multi-step schema changes in transactions where the database supports transactional DDL
