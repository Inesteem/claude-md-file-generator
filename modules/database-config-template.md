---
name: Database Configuration
type: template
tags: [database, sql, tooling]
order: 38
description: Project-specific database engine, ORM, and migration setup (agent-filled and verified)
---
<Fill Database Configuration>
Identify the database setup for this project and document:
- Whether the project uses a database at all
- Database engine(s): PostgreSQL, MySQL, SQLite, MongoDB, etc.
- ORM or query builder: SQLAlchemy, Prisma, Drizzle, ActiveRecord, etc.
- Migration tool and migration directory path
- How to run migrations (command)
- Naming conventions actually in use (detect from existing schema/models)
- Connection management pattern (pooling, connection string env var)

Verify: check for migration files, ORM config, database connection setup.
If no database is used, state that explicitly and recommend removing the
Database Conventions static module from this CLAUDE.md.

Ask the user:
- What database engine and ORM/migration tool does this project use?
</Fill Database Configuration>
