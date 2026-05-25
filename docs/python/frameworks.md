# Framework‑Specific Guidelines

## FastAPI / Pydantic v2

- Use `async def` for route handlers
- Leverage Pydantic v2 `BaseModel` for request/response validation
- Use `Depends()` for dependency injection
- Structure: `app/routers/`, `app/schemas/`, `app/services/`, `app/models/`
- Use `APIRouter` prefix with versioning (`/api/v1/...`)
- Prefer `SQLModel` or `SQLAlchemy 2.0` async for database access
- Configure CORS explicitly in production

## Django

- Keep business logic out of views – use services or model methods
- Use `select_related()` / `prefetch_related()` to avoid N+1 queries
- Write model `Meta` classes with `indexes`, `ordering`, `constraints`
- Use Django REST Framework (DRF) or `ninja` for APIs
- Configure `DATABASES` with connection pooling
- Set `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS in production

## Flask

- Use `flask-smorest` or `flask-apispec` for OpenAPI docs
- Application factory pattern: `create_app()`
- Keep config in `instance/` or env vars via `python-dotenv`
- Use `SQLAlchemy` with Flask‑Migrate (Alembic)
