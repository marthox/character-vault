# Orchestrator Restructure Design

**Date:** 2026-05-16
**Status:** Approved

## Overview

Convert `character-vault` from a monorepo FastAPI app into a service orchestrator. The current application code moves into a standalone `character-manager` git repo, which is then added back as a git submodule. The root repo becomes the orchestration layer — responsible for Docker composition and, later, IaS tooling (Terraform, AWS CDK, or similar).

## Repository Structure

### character-vault (orchestrator)

```
character-vault/
├── services/
│   └── character-manager/    ← git submodule → github.com/<user>/character-manager
├── infra/                    ← empty placeholder for future IaS (Terraform, CDK, etc.)
├── docker-compose.yml        ← composes all services and shared dependencies
├── .gitignore
└── README.md
```

### character-manager (new standalone repo)

```
character-manager/
├── src/
│   ├── main.py
│   ├── adapters/
│   │   ├── inbound/
│   │   └── outbound/
│   └── domain/
│       ├── constants/
│       ├── logic/
│       ├── models/
│       ├── ports/
│       └── utils/
├── tests/
│   ├── conftest.py
│   ├── factories/
│   └── unit/
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── .python-version
├── .github/                  ← CI/CD pipelines (moved from character-vault)
├── .vscode/                  ← editor settings (moved from character-vault)
├── .gitignore
└── README.md
```

## Docker Configuration

### character-manager/Dockerfile

Multi-stage build using uv for fast, reproducible installs:

```dockerfile
FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev
COPY src/ ./src/

FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
```

### character-vault/docker-compose.yml

Root orchestrator composes all services and shared infrastructure:

```yaml
services:
  character-manager:
    build:
      context: ./services/character-manager
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/characterdb
    depends_on:
      - db

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: characterdb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Credentials here are dev-only placeholders. Production secrets will be injected via environment variables or a secrets manager.

## CI/CD Strategy

Each service repo owns its own pipelines (Option A). The `character-manager` repo will contain `.github/workflows/` for build, test, and deploy. The orchestrator (`character-vault`) does not run per-service CI — it may later run integration tests or coordinate cross-service deployments.

## Migration Steps (One-Time)

1. Create a new GitHub repo `character-manager`
2. Extract current `character-vault` history into `character-manager` using `git filter-repo`, preserving commits for `src/`, `tests/`, `pyproject.toml`, `uv.lock`, `.python-version`, `.github/`, `.vscode/`, `.gitignore`
3. Push extracted history to the new remote
4. In `character-vault`: remove all service files, clean up root, add `character-manager` as a submodule at `services/character-manager`
5. Add orchestrator files: `docker-compose.yml`, `infra/.gitkeep`, updated `README.md`, updated `.gitignore`
6. Commit and push `character-vault`

## Day-to-Day Developer Workflow

```bash
# Clone orchestrator with all submodules
git clone --recurse-submodules https://github.com/<user>/character-vault

# Work on a service
cd services/character-manager
git checkout -b my-feature
# make changes, commit, push to character-manager repo

# Update orchestrator's submodule pointer to latest
cd ../..
git add services/character-manager
git commit -m "Update character-manager to latest"
```

The orchestrator always pins to a specific commit of each submodule — this is intentional. The pointer is bumped explicitly when a service update is ready to be integrated.

## Adding Future Services

Each new service follows the same pattern:
1. Create a standalone repo (e.g., `character-tracker`)
2. Add a `Dockerfile` to that repo
3. Add the repo as a submodule: `git submodule add <url> services/character-tracker`
4. Add the service to `docker-compose.yml` in the orchestrator

## Out of Scope

- Terraform / AWS CDK setup (future, `infra/` is a placeholder)
- Makefile / convenience scripts (can be added when needed)
- Production secrets management (handled at deployment time)
- Integration tests at the orchestrator level (future)
