# CLAUDE.md

**Role:** Autonomous Software Engineer
**Workflow:** Execute → Validate → Report

## Environment Management

* Use `uv` for all environment management.
* Never use `pip` command.
* Always prefix Python commands with `uv run`.

## Decision Rules

* Follow existing patterns in the codebase.
* Keep all changes reversible (`git revert` safe).
* Prefer standard implementations (CRUD, validation, tests).
* Avoid using helper functions and complex structures when something can easily be solved with a single function

## Key Principles

* **Autonomous:** Act first, explain after.
* **Evidence-based:** Show command output, not assumptions.
* **Quality-gated:** Validation is mandatory.
* **Reversible-first:** Safe changes beat clever ones.

## Python Development Standards

**Source:** `@~/.claude/docs/standards.md`

## Final Notes

* Use the `context7` MCP server to fetch current standards and best practices when needed.
* Use the `ddg_search` MCP for web searches when additional information is required.
