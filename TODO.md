# TODO (short-term) — Digital Nation Platform (backend)

Priority: High
- [ ] feature/db-integration
  - Implement async SQLAlchemy models for citizens, users, services, service_requests
  - Add Alembic migrations
  - Wire DATABASE_URL via environment variables (Settings)
- [ ] feature/keycloak-auth
  - Implement JWT verification using Keycloak JWKS (FastAPI dependency)
  - Implement role-based checks (admin, citizen, agency_officer)
- [ ] infra/docker-compose
  - Create docker-compose.dev.yml with services: backend, postgres, keycloak, minio, rabbitmq
  - Add sample env files for local dev
- [ ] feature/api-complete
  - Expand routers: services, requests, digital-id, interop
  - Add Pydantic request/response models, validation and error handling
