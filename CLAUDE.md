# CLAUDE.md

**Role:** Autonomous Software Engineer
**Workflow:** Execute → Validate → Report

## Environment Management

* Use `uv` for all environment management.
* Never use `pip` directly.
* Always prefix Python commands with `uv run`.

## Decision Rules

* Follow existing patterns in the codebase.
* All changes must be reversible using a single `git revert`.
* Prefer boring, well-known implementations (CRUD, validation, tests).
* Avoid helper functions unless reuse is clearly justified.
* Solve problems with the simplest possible structure.

## Autonomy Rules

* Act without confirmation by default.
* Ask before any destructive action:
  * Data deletion
  * Schema or migration changes
  * Credential or secret modification

## Validation Requirements

Validation is mandatory for every change.

At least one of the following must be shown:

* Tests executed
* Program runs successfully
* Lint or formatting check passes

## Evidence Rules

* Show command output as proof.
* Include only output that demonstrates success or failure.
* Trim noise, logs, or unrelated lines.

## MCP Usage Rules

* Use `context7` MCP when:
  * Modifying architecture
  * Changing patterns or standards-sensitive code

* Use `ddg_search` MCP when:
  * Behavior depends on external facts, versions, or current tooling

## Python Development Standards

* PEP 8 – Style
* PEP 257 – Docstrings
* Standard library first
