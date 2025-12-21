# Security Standards

## Secret Management

- No hard-coded secrets, tokens, or credentials
- Use environment variables for sensitive data
- SSH key-based authentication where possible
- Secret rotation via environment configuration
- Never commit sensitive values
- Do not touch secrets or credentials unless instructed
- Do not assume environment details

## Code Review Security Checklist

- No hard-coded secrets, tokens, or credentials in code
- Input validation where applicable
- Proper error handling that doesn't expose sensitive information
- No unnecessary network calls or external dependencies
- Validation of all external inputs and data sources

## Access & Authentication

- Prefer secure authentication methods (SSH keys, tokens)
- Validate inputs at all boundaries
- Use Pydantic Settings for environment variable validation
- Support `.env` for local and real environment variables for production

## Security Testing

- Run security checks as part of development workflow
- Use `uv run pip-audit` for security vulnerability scanning
- Regular rotation of credentials and tokens
- Monitor for potential security issues in dependencies
