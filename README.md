# Customizing Claude Code for Python Development: A Practical Guide

**Target Audience:** Python developers who want consistent, high-quality code

---

## TL;DR

**Problem:** You repeat the same context every time you ask Claude for help with Python development.

**Solution:** Build a 5-layer customization system that teaches Claude your standards permanently.

**What You'll Learn:**

- How CLAUDE.md injects context into every conversation automatically
- Using Rules (auto-loaded) + Shared (on-demand) for token-efficient guidance
- Creating domain-specific Skills for on-demand workflows
- Building read-only Subagents for code review
- Complete configuration structure for teams

**Time Investment:** 30 minutes setup + 5 min per project
**Expected ROI:** 5-10 minutes saved per development task (80% time reduction)
**Break-even:** After 3-6 development tasks

---

## The Problem: Explaining Yourself Over and Over

Here's the thing about using AI for Python development: it's incredibly useful, but it has one massive friction point.

Every. Single. Time. you start a new conversation, you're back to zero context.

You ask Claude to help with a data processing function, and it gives you generic Python. No type hints. No error handling for edge cases. No input validation.

So you type: *"Add type hints."* Then: *"Handle the edge case where data is None."* Then: *"Use logging instead of print."*

By the time you get working code, you've spent 10 minutes explaining what you wanted instead of 2 minutes getting it.

Sound familiar?

The issue isn't Claude's capability—it's that **every conversation starts from zero context**. You're repeating the same requirements:

- *"Use type hints"*
- *"Add proper error handling"*
- *"Follow PEP 8"*

This guide shows you how to fix that. Permanently.

---

## What You'll Build

By the end of this guide, you'll have a system where:

| Without Customization | With Customization |
|----------------------|-------------------|
| Generic Python code | Typed, documented functions |
| Missing error handling | Proper exception handling |
| No input validation | Built-in validation |
| Context overload (all tokens loaded) | Token-efficient (load only what you need) |
| 10-15 minutes per task | 2-3 minutes per task |

The difference? A 5-layer architecture that transforms Claude into a Python expert.

---

## The Five-Layer Customization Architecture

Here's how it works. Claude Code's customization system operates through five hierarchical layers:

### Layer 5: Specialized Workers (Subagents)

- Code reviewers, security auditors
- Tools: Read-only, Haiku model

### Layer 4: Domain Knowledge (Skills)

- On-demand triggered workflows
- Cross-project reusable knowledge
- User-initiated actions

### Layer 3: Modular Rules (.claude/shared/)

- Path-specific domain knowledge
- Loaded automatically like CLAUDE.md
- High priority context

### Layer 2: Context Injection (CLAUDE.md)

- Project standards
- Common commands
- Code style rules

### Layer 1: Foundation Model (Claude 3.7)

- Core reasoning and code generation

Each layer builds on the previous one. Here's the key insight: **lower layers provide broader context, higher layers provide specific constraints**.

- **CLAUDE.md** (Layer 2) is loaded into every conversation automatically with high priority
- **Rules** (Layer 3) are loaded automatically like CLAUDE.md but can be path-specific
- **Skills** (Layer 4) are loaded on-demand when Claude detects relevant tasks or user triggers them
- **Subagents** (Layer 5) are spawned with specific tool restrictions

The result? A knowledge hierarchy that persists across conversations. Let's build it.

---

## Layer 2: CLAUDE.md – Your Project's DNA

### How It Works

CLAUDE.md is a configuration file that Claude **automatically injects into every conversation**. When you start Claude Code, it searches for CLAUDE.md using hierarchical discovery:

```
Priority 1: ./CLAUDE.md (project root) - HIGHEST
Priority 2: ../CLAUDE.md (parent directories)
Priority 3: ~/.claude/CLAUDE.md (user defaults) - LOWEST
```

Found files are concatenated and injected into every conversation's system prompt. The content has high attention weight and influences all responses.

### File Format

CLAUDE.md is standard Markdown:

- Any valid Markdown (headers, lists, code blocks)
- No YAML frontmatter required (unlike Skills)
- Keep it under 500 lines for performance
- UTF-8 encoding required

### Minimal Template

```markdown
# Python Project Standards

## Code Style
- Use type hints for all functions
- Follow PEP 8 naming conventions
- [ADD YOUR OWN: linting tools, formatting rules]

## Testing
- Write pytest tests
- [ADD YOUR OWN: coverage requirements, test patterns]

## Tools
- [ADD YOUR OWN: dependency manager, frameworks]

## Notes
- [ADD YOUR OWN: project-specific guidelines]
```

> **Customize this template** for your project's specific needs, frameworks, and team standards.

### Why This Matters: A Concrete Example

**Without CLAUDE.md:**

- **You:** *"Help me write a function to process user data"*
- **Claude:** *"Here's a generic Python function..."* [No types, no validation, 10 min of corrections needed]

**With CLAUDE.md:**

- **You:** *"Help me write a function to process user data"*
- **Claude:** *"I'll create a typed function with Pydantic validation, proper error handling, and logging as per your standards..."*

The context is **automatically loaded**. You get exactly what you need on the first try.

---

## Layer 3: Rules & Shared – Modular Domain Knowledge

### Two-Part Architecture

This configuration uses a **two-part modular system** to balance token efficiency with comprehensive guidance:

**Part 1: Rules Directory (`.claude/rules/`)**

- **Auto-loaded** with high priority (like CLAUDE.md)
- Contains **loading instructions** and critical operational info
- Consumes context tokens every session
- Keep minimal and focused

**Part 2: Shared Directory (`.claude/shared/`)**

- **On-demand reference library**
- Contains detailed domain-specific best practices
- Loaded only when needed via explicit references
- Token-efficient: no unnecessary loading

Think of it this way:

- **CLAUDE.md** = Master config (always loaded, project-wide)
- **Rules** = Loading manifest (auto-loaded, tells you what else to load)
- **Shared** = Reference library (loaded on-demand, detailed guidance)
- **Skills** = Training manuals (loaded on-demand when triggered)

### Rules vs Shared vs Skills

| Feature | Rules (`.claude/rules/`) | Shared (`.claude/shared/`) | Skills |
|---------|---------------------------|---------------------------|--------|
| **Loading** | Automatic | On-demand (manual) | On-demand (triggered) |
| **Priority** | High | N/A (manual load) | Lower |
| **Token Usage** | Consumes tokens | Saves tokens | Consumes when loaded |
| **Use Case** | Loading guidance, critical info | Detailed reference material | Workflows and procedures |
| **Example** | When to load guidelines | Python best practices | Code refactoring workflow |

**When to use Rules:** Information that must be available immediately to know what else to load.

**When to use Shared:** Comprehensive domain knowledge referenced on-demand to save tokens.

**When to use Skills:** Step-by-step workflows triggered by specific tasks.

### How It Works

1. Claude loads `CLAUDE.md` (high-level principles)
2. Claude auto-loads all files from `rules/` (loading instructions)
3. Based on the task, Claude manually loads relevant files from `shared/`
4. Skills load on-demand when specific tasks are detected

### Example Loading Flow

```
Session Start:
├── CLAUDE.md (auto-loaded)
├── rules/rule-index.md (auto-loaded)
└── "Working on Python API"
    ├── Read ~/.claude/shared/python.md (manual)
    ├── Read ~/.claude/shared/api-design.md (manual)
    └── Read ~/.claude/shared/security.md (manual)
```

This ensures Claude has exactly the context needed—no more, no less.

### Shared Reference Template

When creating new reference files in `shared/`, use this structure:

```markdown
---
name: your-rule-name
description: What this rule covers
paths:
  - "src/api/**/*.py"  # [ADD/REMOVE: path patterns]
---

# Your Rule Title

## Domain Knowledge
- [ADD YOUR PATTERNS: specific to this domain]

## Code Examples
```python
# [ADD YOUR EXAMPLES]
```

## Constraints

- [ADD YOUR REQUIREMENTS]

```

> **Customize this template** for your specific domain areas (APIs, database, security, etc.).

---

## Layer 4: Skills – On-Demand Workflows

### What Are Skills?

Skills are **specialized knowledge bundles** stored as Markdown files with YAML frontmatter. Unlike CLAUDE.md (which provides general context), skills contain:
- Design patterns
- Framework-specific best practices
- Code templates
- Testing strategies

Skills can be stored at different levels:
- **Project skills:** `.claude/skills/` (specific to your project, version-controlled)
- **User skills:** `~/.claude/skills/` (available across all your projects)

Skills are loaded on-demand when Claude detects a relevant task through keyword matching or invoked directly with `/skill-name`.

### How Skills Load

1. Claude scans `.claude/skills/` and `~/.claude/skills/` for skills
2. Skills are discovered from nested directories for monorepo support
3. Each skill must start with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: What this skill does
   ---
   ```

1. Claude matches your request against skill descriptions
2. Matched skill content is injected into the conversation

Skills are loaded on-demand, not automatically. Claude decides when to use them based on your request.

### Minimal Skill Template

```markdown
---
name: your-skill-name
description: Brief description of what this skill does
---

# Your Skill Name

## Patterns
- [ADD YOUR PATTERNS: design patterns, code templates]

## Best Practices
- [ADD YOUR RULES: error handling, testing approaches]

## Code Templates
```python
# [ADD YOUR TEMPLATE]
def example_function():
    pass
```

## Checklist

- [ ] [ADD YOUR ITEMS]

```

> **Customize this template** with your domain-specific knowledge and patterns.

### Skill Loading in Action

When you ask: *"Help me create an API endpoint for user registration"*

1. Claude detects keywords: "API", "endpoint", "user registration"
2. Matches `python-expert` skill
3. Loads skill patterns:
   - FastAPI route structure
   - Pydantic validation models
   - Proper error handling
   - Test templates

The skill transforms generic code generation into **domain-aware development**.

---

## Layer 5: Subagents – Specialized Workers

### What Are Subagents?

Subagents are **constrained AI workers** designed for specific tasks. Unlike the main Claude instance which has full tool access, subagents can be restricted to:
- Read-only tools (safety for code reviews)
- Specific tool subsets (e.g., only Bash and Read)
- Different AI models (Haiku for speed, Sonnet for complex analysis)

### Configuration

Subagents are defined in Markdown files with YAML frontmatter:

```yaml
---
name: subagent-name
description: What this subagent does
model: haiku | sonnet | opus | inherit  # haiku=fast/cheap, sonnet=balanced, opus=capable
tools:
  - Read
  - Bash
disallowedTools:
  - Write
  - Edit
permissionMode: askUser | acceptSuggested | bypassPermissions
---
```

**Tool Access:** Allowlist (`tools`) or denylist (`disallowedTools`). Permission modes control prompt handling.

### Use Case: Code Review Subagent

You want a **read-only subagent** that reviews code before commits. This prevents accidental modifications during review.

### Minimal Subagent Template

```markdown
---
name: your-subagent-name
description: What this subagent does
model: haiku  # or sonnet, opus
tools:
  - Read
  # [ADD/REMOVE TOOLS: Bash, Write, Edit, etc.]
disallowedTools:
  - Write  # [ADD RESTRICTIONS]
permissionMode: askUser  # or acceptSuggested, bypassPermissions
---

# Your Subagent

## Task
[DESCRIBE WHAT THIS SUBAGENT DOES]

## Checklist
- [ ] [ADD YOUR REVIEW CRITERIA]

## Output Format
```

[DESCRIBE EXPECTED OUTPUT FORMAT]

```

## Rules
- [ADD YOUR CONSTRAINTS]
```

> **Customize this template** for your specific review or task automation needs.

### How to Use the Subagent

From your main Claude conversation:

**You:** *"Use the code-reviewer to review src/models/user.py before we merge"*

Claude spawns the subagent, which:

1. Loads with read-only permissions
2. Reviews the Python file
3. Checks type hints, error handling, security
4. Returns a structured report

The subagent **isolates the review context** from your main conversation, keeping your workspace clean while ensuring thorough review.

---

## Complete Directory Structure

Here's how to organize your Claude Code customization:

### Root Files

- `CLAUDE.md` - Universal defaults (high-level principles)
- `settings.json` - Tool permissions and hooks

### rules/

- `rule-index.md` - Guidelines loading reference (auto-loaded)

### shared/

- `security.md` - Security best practices
- `testing.md` - Testing requirements
- `tools.md` - Tool usage guidelines
- `python.md` - Python coding standards
- `database.md` - Database best practices
- `api-design.md` - API design patterns
- `documentation.md` - Documentation standards

### skills/

- `python-expert/SKILL.md` - Python development skill
- `web-research/SKILL.md` - For researching libraries
- `code-quality/SKILL.md` - Linting and validation

### agents/

- `code-reviewer.md` - Read-only code reviewer
- `python-expert.md` - Full Python development agent
- `test-writer.md` - Test generation agent

### Configuration Hierarchy

Priority levels (highest to lowest):

| Priority Level | Location | Contents |
|---------------|----------|----------|
| 1 (Highest) | `.claude/` (project) | CLAUDE.md, rules/, shared/, agents/, skills/ |
| 2 | `~/.claude/` (user) | CLAUDE.md, rules/, shared/, agents/, skills/ |
| 3 (Lowest) | System | Default settings |

When multiple CLAUDE.md files exist, they are concatenated with higher priority files overriding lower priority ones.

---

## Real Results: Before & After

Here's what actually changed after implementing this system:

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

**Before:** Inconsistent patterns across team members, missing type hints, different docstring styles

**After:** Standardized type hints and error handling, consistent docstrings, validated patterns

### Knowledge Transfer

**Before:** New team members need 2-3 weeks to learn standards

**After:** Standards enforced automatically via CLAUDE.md, new team members productive immediately

### Break-Even Analysis

- **Setup time:** 30 minutes
- **Time saved per task:** 12 minutes
- **Break-even point:** After 3 tasks
- **Monthly savings (10 tasks):** 2 hours of engineering time

---

## Quick Reference: Essential Commands

### Getting Started

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/init` | Auto-generate CLAUDE.md from codebase | Starting new project |
| `/clear` | Reset conversation context | Switching tasks or clearing cache |
| `/agents` | Manage subagents (create, edit, delete) | Setting up custom agents |
| `/hooks` | Configure automated hooks | Adding validation automation |

### Development Workflow

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start Claude Code in current directory | `cd ~/project && claude` |
| `claude --dangerously-skip-permissions` | Skip all permission prompts | `claude --dangerously-skip-permissions` |
| `claude -p "prompt"` | Run one-off prompt | `claude -p "Review this code"` |

### Debug Commands

```bash
# Check Claude version
claude --version

# List available subagents
claude /agents

# Verify configuration loaded
claude -p "What are my project standards according to CLAUDE.md?"

# Clear context and restart
/clear
```

### File Locations Quick Reference

| File Type | Location | Notes |
|-----------|----------|-------|
| CLAUDE.md | Project root | Auto-loaded every session |
| Skills | `~/.claude/skills/` | Loaded on-demand |
| Subagents | `~/.claude/agents/` | Must use `/agents` command |
| Settings | `~/.claude/settings.json` | Global configuration |

---

## Complete Workflow Example

Here's how all layers work together in practice:

### Scenario: Create API Endpoint for User Registration

**Step 1: Context Loading**

- Claude automatically loads CLAUDE.md with your Python standards
- Type hints, error handling, and testing procedures are already known

**Step 2: Skill Activation**

- You ask: *"Create a user registration endpoint"*
- Claude detects keywords and loads `python-expert` skill
- Decision trees guide FastAPI structure
- Patterns are automatically applied

**Step 3: Implementation**

```python
# Claude generates this automatically with full context
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None

@router.post("/users/register")
async def register_user(user: UserRegistration) -> dict:
    """Register a new user.

    Args:
        user: User registration data

    Returns:
        dict: Registration result with user ID

    Raises:
        HTTPException: If email already exists
    """
    try:
        # Check if user exists
        existing = await get_user_by_email(user.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Create user
        user_id = await create_user(user)
        logger.info(f"User registered: {user_id}")

        return {"user_id": user_id, "status": "registered"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Registration failed: {e}")
        raise HTTPException(status_code=500, detail="Registration failed")
```

**Step 4: Pre-Commit Review**

- You: *"Use the code-reviewer to review this before commit"*
- Claude spawns code-reviewer subagent
- Subagent reviews with read-only permissions
- Returns structured report with quality assessment

**Result:** Production-ready code with proper type hints, error handling, and tests, generated in 3 minutes instead of 15.

---

## Conclusion: From Generic to Specialized

Claude Code's customization architecture transforms it from a general-purpose assistant into a **domain-aware Python development partner**. By leveraging:

- **CLAUDE.md** for persistent project context
- **Skills** for domain knowledge and best practices
- **Subagents** for specialized, constrained tasks

You eliminate repetitive explanations and ensure consistent, standards-compliant code.

The configuration is **portable, version-controllable, and team-shareable**. New team members get instant access to your organization's best practices without the learning curve.

**The bottom line:** 30 minutes of setup saves you 12 minutes on every development task. After just 3 tasks, you're ahead. After 10 tasks, you've saved 2 hours.

### Get Started Now

Ready to customize Claude Code for your Python development workflow?

**Check out the complete configuration:** [github.com/sydasif/.claude](https://github.com/sydasif/.claude)

Fork it, adapt it to your projects, and turn Claude into your Python development expert.

---

## Resources

- **Claude Code Documentation:** [code.claude.com/docs](https://code.claude.com/docs)
- **Python Type Hints:** [docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)
- **pytest Documentation:** [docs.pytest.org](https://docs.pytest.org)
- **FastAPI Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **PEP 8 Style Guide:** [peps.python.org/pep-0008](https://peps.python.org/pep-0008)
- **YAML Frontmatter Spec:** [yaml.org/spec](https://yaml.org/spec/)

---

**License:** MIT – Feel free to use and modify for your organization.

**Questions?** Open an issue on the GitHub repo.

---

*Happy coding!* 🐍✨
