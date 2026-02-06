# Customizing Claude Code for Python Development: A Practical Guide

**Target Audience:** Python developers who want consistent, high-quality code

---

## TL;DR

**Problem:** You repeat the same context every time you ask Claude for help with Python development.

**Solution:** Build a 3-tier customization system that teaches Claude your standards permanently.

**What You'll Learn:**

- How CLAUDE.md injects context into every conversation automatically
- Using Rules (always-on) + Guidelines (on-demand) for token-efficient guidance
- Creating domain-specific Skills for on-demand workflows
- Building read-only Subagents for code review
- Complete configuration structure for teams

**Time Investment:** 30 minutes setup + 5 min per project
**Expected ROI:** 5-10 minutes saved per development task (80% time reduction)
**Break-even:** After 3-6 development tasks

---

## The Problem: Explaining Yourself Over and Over

Every time you start a new conversation, you're back to zero context.

You ask Claude to help with a data processing function, and it gives you generic
Python. No type hints. No error handling. No input validation.

So you type: *"Add type hints."* Then: *"Handle the edge case where data is None."*
Then: *"Use logging instead of print."*

By the time you get working code, you've spent 10 minutes explaining what you wanted instead of 2 minutes getting it.

This guide shows you how to fix that. Permanently.

---

## What You'll Build

| Without Customization | With Customization |
| ---------------------- | ------------------- |
| Generic Python code | Typed, documented functions |
| Missing error handling | Proper exception handling |
| No input validation | Built-in validation |
| Context overload (all tokens loaded) | Token-efficient (load only what you need) |
| 10-15 minutes per task | 2-3 minutes per task |

---

## The Three-Tier Customization Architecture

Claude Code's customization system operates through three hierarchical tiers:

### Tier 1: Always-On (Rules)
- **Location:** `~/.claude/rules/`
- **Loading:** Auto-loaded every session
- **Purpose:** Critical constraints (security, testing, tools)
- **Token usage:** Always consumed
- **Files:** `security.md`, `testing.md`, `tools.md`

### Tier 2: On-Demand (Guidelines)
- **Location:** `~/.claude/guidelines/`
- **Loading:** Loaded when needed via Read tool
- **Purpose:** Domain-specific patterns (Python, API, Database)
- **Token usage:** Saves tokens - only load what's needed
- **Files:** `python.md`, `api-design.md`, `database.md`, `documentation.md`

### Tier 3: Workflows (Skills)
- **Location:** `~/.claude/skills/`
- **Loading:** On-demand when triggered
- **Purpose:** Step-by-step procedures (refactoring, research, review)
- **Token usage:** Only when skill is activated
- **Files:** `code-refactoring/`, `fresh-review/`, `web-research/`

### Tier 4: Specialized Workers (Subagents)
- **Location:** `~/.claude/agents/`
- **Loading:** Spawned for specific tasks
- **Purpose:** Constrained AI workers (code review, testing)
- **Token usage:** Isolated context
- **Files:** `code-reviewer.md`

**Key Insight:** Lower tiers provide broader context, higher tiers provide specific
constraints. This progressive disclosure saves tokens while ensuring comprehensive guidance.

---

## Tier 1: Rules – Always-On Critical Constraints

### How It Works

Rules are **automatically loaded** into every conversation. They contain critical constraints that must always be followed:

- **Security requirements** - Input validation, secret management
- **Testing requirements** - Coverage thresholds, verification pyramid
- **Tool commands** - Standard commands for linting, testing, formatting

### File Format

Rules are standard Markdown files (no YAML frontmatter required):

```markdown
# Rule Name

## Core Requirements
- Requirement 1
- Requirement 2

## STOP & ASK Triggers
You must stop and ask if:
1. Condition 1
2. Condition 2
```

### Rules Directory Structure

```text
~/.claude/rules/
├── security.md    # Security constraints (always loaded)
├── testing.md     # Testing requirements (always loaded)
└── tools.md       # Tool reference (always loaded)
```

### Why This Matters

**Without Rules:**
- **You:** *"Help me write a function"*
- **Claude:** *"Here's code..."* [No security checks, no testing requirements]

**With Rules:**
- **You:** *"Help me write a function"*
- **Claude:** *"I'll create this with input validation, error handling, and tests as required..."*

Security and testing standards are **automatically enforced**.

---

## Tier 2: Guidelines – On-Demand Domain Knowledge

### How It Works

Guidelines are **reference materials** loaded on-demand via the Read tool.
They contain detailed domain-specific best practices:

- **Python patterns** - Type hints, async patterns, framework selection
- **API design** - RESTful principles, versioning, authentication
- **Database patterns** - ORM usage, query optimization, migrations
- **Documentation standards** - README format, docstrings, ADRs

### Loading Guidelines

Guidelines are NOT auto-loaded. You explicitly load them when needed:

```text
# Before working on Python code
Read ~/.claude/guidelines/python.md

# Before designing an API
Read ~/.claude/guidelines/api-design.md

# Before database work
Read ~/.claude/guidelines/database.md
```

### Token Efficiency

This approach saves context tokens:

| Approach | Tokens Used | When Loaded |
|----------|-------------|-------------|
| All in CLAUDE.md | 5000+ | Every session |
| Rules + Guidelines | 800 (rules) + 0-2000 (on-demand) | Rules always, Guidelines when needed |
| **Savings** | **60-80%** | - |

### Guidelines Directory Structure

```text
~/.claude/guidelines/
├── python.md           # Python development patterns
├── api-design.md       # API design patterns
├── database.md         # Database best practices
└── documentation.md    # Documentation standards
```

---

## Tier 3: Skills – On-Demand Workflows

### What Are Skills?

Skills are **specialized knowledge bundles** stored as Markdown files with YAML frontmatter. They contain:

- Step-by-step workflows
- Design patterns
- Code templates
- Checklists

### How Skills Load

1. Skills are discovered from `~/.claude/skills/` directories
2. Each skill has a SKILL.md with YAML frontmatter:

   ```yaml
   ---
   name: skill-name
   description: What this skill does and when to use it
   ---
   ```

3. Skills load on-demand when Claude detects relevant tasks
4. Multiple files can be bundled (SKILL.md + references/)

### Skills Directory Structure

```text
~/.claude/skills/
├── code-refactoring/
│   └── SKILL.md          # Code modernization workflow
├── fresh-review/
│   └── SKILL.md          # Systematic review process
└── web-research/
    └── SKILL.md          # Research strategies
```

### Skill Loading in Action

When you ask: *"Help me refactor this legacy code"*

1. Claude detects "refactor" keyword
2. Loads `code-refactoring` skill
3. Applies modernization checklist:
   - Convert to f-strings
   - Add type hints
   - Use pathlib
   - Migrate to dataclasses

---

## Tier 4: Subagents – Specialized Workers

### What Are Subagents?

Subagents are **constrained AI workers** designed for specific tasks. They can be restricted to:

- Read-only tools (safety for code reviews)
- Specific tool subsets
- Different AI models (Haiku for speed, Sonnet for complex analysis)

### Configuration

Subagents are defined in Markdown files with YAML frontmatter:

```yaml
---
name: subagent-name
description: What this subagent does
model: haiku | sonnet | opus | inherit
tools:
  - Read
  - Bash
disallowedTools:
  - Write
  - Edit
---
```

### Use Case: Code Review Subagent

A **read-only subagent** reviews code before commits:

```yaml
---
name: code-reviewer
description: Semantic code review using specific skills
color: "#FFFF00"
skills:
   - code-refactoring
---
```

The subagent:
1. Loads with read-only permissions
2. Reviews the code
3. Checks against rules and guidelines
4. Returns a structured report

---

## Complete Directory Structure

Here's the consolidated configuration structure:

```text
~/.claude/
├── CLAUDE.md                    # Core principles (auto-loaded)
├── rules/                       # ALWAYS-ON (critical constraints)
│   ├── security.md              # Security requirements
│   ├── testing.md               # Testing requirements
│   └── tools.md                 # Tool commands
├── guidelines/                  # ON-DEMAND (domain patterns)
│   ├── python.md                # Python patterns
│   ├── api-design.md            # API patterns
│   ├── database.md              # Database patterns
│   └── documentation.md         # Documentation standards
├── agents/                      # SUBAGENTS (specialized workers)
│   └── code-reviewer.md         # Read-only code reviewer
└── skills/                      # SKILLS (on-demand workflows)
    ├── code-refactoring/        # Code modernization
    ├── fresh-review/            # Systematic review
    └── web-research/            # Research workflows
```

### Configuration Hierarchy

Priority levels (highest to lowest):

| Priority Level | Location | Contents |
|---------------|----------|----------|
| 1 (Highest) | `.claude/` (project) | Project-specific overrides |
| 2 | `~/.claude/` (user) | User defaults |
| 3 (Lowest) | System | Default settings |

---

## Real Results: Before & After

### Time Per Task

**Before:** 15 minutes average
- 5 min: Explaining context and standards
- 5 min: Reviewing and correcting generic code
- 5 min: Adding type hints and tests

**After:** 3 minutes average
- 1 min: Requesting the task
- 2 min: Reviewing Claude's output (already correct)

**Savings:** 12 minutes per task (80% reduction)

### Code Quality

**Before:** Inconsistent patterns, missing type hints, different docstring styles

**After:** Standardized type hints, consistent error handling, validated patterns

### Knowledge Transfer

**Before:** New team members need 2-3 weeks to learn standards

**After:** Standards enforced automatically, new team members productive immediately

---

## Quick Reference: Essential Commands

### Getting Started

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/init` | Auto-generate CLAUDE.md from codebase | Starting new project |
| `/clear` | Reset conversation context | Switching tasks |
| `/agents` | Manage subagents | Setting up custom agents |

### Development Workflow

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start Claude Code in current directory | `cd ~/project && claude` |
| `claude -p "prompt"` | Run one-off prompt | `claude -p "Review this code"` |

### Loading Guidelines

```text
# Before Python development
Read ~/.claude/guidelines/python.md

# Before API design
Read ~/.claude/guidelines/api-design.md

# Before database work
Read ~/.claude/guidelines/database.md
```

### File Locations Quick Reference

| File Type | Location | Loading |
|-----------|----------|---------|
| CLAUDE.md | `~/.claude/CLAUDE.md` | Auto-loaded every session |
| Rules | `~/.claude/rules/` | Auto-loaded every session |
| Guidelines | `~/.claude/guidelines/` | On-demand via Read tool |
| Skills | `~/.claude/skills/` | On-demand when triggered |
| Agents | `~/.claude/agents/` | Spawned for specific tasks |

---

## Complete Workflow Example

### Scenario: Create API Endpoint for User Registration

#### Step 1: Context Loading

- Claude automatically loads:
  - `CLAUDE.md` (core principles)
  - `rules/security.md` (security requirements)
  - `rules/testing.md` (testing requirements)
  - `rules/tools.md` (tool commands)

#### Step 2: Load Relevant Guidelines

```text
Read ~/.claude/guidelines/python.md
Read ~/.claude/guidelines/api-design.md
```

#### Step 3: Implementation

Claude generates code following all loaded standards:
- Type hints (from python.md)
- FastAPI patterns (from api-design.md)
- Input validation (from security.md)
- Error handling (from security.md)
- Test structure (from testing.md)

#### Step 4: Pre-Commit Review

```text
Use the code-reviewer to review this before commit
```

Claude spawns the code-reviewer subagent which:
1. Reviews with read-only permissions
2. Checks against all rules and guidelines
3. Returns structured report

**Result:** Production-ready code in 3 minutes instead of 15.

---

## Conclusion: From Generic to Specialized

This 3-tier architecture transforms Claude Code from a general-purpose
assistant into a **domain-aware Python development partner**:

- **Rules** for always-on critical constraints
- **Guidelines** for on-demand domain knowledge
- **Skills** for specialized workflows
- **Subagents** for constrained tasks

**Key Benefits:**
- 60-80% token savings vs loading everything
- Security and testing always enforced
- Domain knowledge available when needed
- No cross-references or duplication
- Clear separation of concerns

**The bottom line:** 30 minutes of setup saves you 12 minutes on every development task. After just 3 tasks, you're ahead.

---

## Resources

- **Claude Code Documentation:** [code.claude.com/docs](https://code.claude.com/docs)
- **Python Type Hints:** [docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)
- **pytest Documentation:** [docs.pytest.org](https://docs.pytest.org)
- **FastAPI Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **PEP 8 Style Guide:** [peps.python.org/pep-0008](https://peps.python.org/pep-0008)

---

**License:** MIT – Feel free to use and modify for your organization.

---

*Happy coding!* 🐍✨
