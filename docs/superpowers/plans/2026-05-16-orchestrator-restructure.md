# Orchestrator Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `character-vault` into a service orchestrator by extracting the FastAPI app into a standalone `character-manager` git repo and adding it back as a submodule at `services/character-manager`.

**Architecture:** The root repo becomes a Docker-compose orchestrator pinning each service to a specific submodule commit. Each service owns its own repo, CI/CD, and Dockerfile. The orchestrator wires them together via `docker-compose.yml` and will later house IaS tooling in `infra/`.

**Tech Stack:** git, git-filter-repo, GitHub CLI (`gh`), Docker, Python 3.13, uv, FastAPI, PostgreSQL 17

---

## File Map

### character-manager (new standalone repo, lives at /tmp/character-manager-build during extraction)

| File | Action | Purpose |
|------|--------|---------|
| `src/` | extracted from character-vault | Application source |
| `tests/` | extracted from character-vault | Test suite |
| `pyproject.toml` | extracted from character-vault | Python project config |
| `uv.lock` | extracted from character-vault | Locked dependencies |
| `.python-version` | extracted from character-vault | Python version pin |
| `.github/` | extracted from character-vault | CI/CD pipelines |
| `.vscode/` | extracted from character-vault | Editor settings |
| `.gitignore` | extracted from character-vault | Python ignores |
| `README.md` | extracted then updated | Service-level docs |
| `Dockerfile` | created | Multi-stage uv build |

### character-vault (orchestrator, modified in-place)

| File | Action | Purpose |
|------|--------|---------|
| `src/` | removed | Moved to character-manager |
| `tests/` | removed | Moved to character-manager |
| `pyproject.toml` | removed | Moved to character-manager |
| `uv.lock` | removed | Moved to character-manager |
| `.python-version` | removed | Moved to character-manager |
| `.github/` | removed | Moved to character-manager |
| `.vscode/` | removed | Moved to character-manager |
| `services/character-manager/` | created (submodule) | Points to character-manager repo |
| `infra/.gitkeep` | created | Placeholder for future IaS |
| `docker-compose.yml` | replaced | Full orchestrator compose config |
| `.gitignore` | replaced | Orchestrator-level ignores |
| `README.md` | replaced | Orchestrator-level docs |

---

## Task 1: Install git-filter-repo

**Files:** none (tooling)

- [ ] **Step 1: Install git-filter-repo**

```bash
brew install git-filter-repo
```

- [ ] **Step 2: Verify installation**

```bash
git filter-repo --version
```

Expected output: a version string like `git filter-repo==2.47.0` (exact version may vary, any output confirms success)

---

## Task 2: Create character-manager GitHub repo

**Files:** new remote repo at `github.com/marthox/character-manager`

- [ ] **Step 1: Create the repo via gh CLI**

```bash
gh repo create marthox/character-manager \
  --public \
  --description "Character management service — part of the character-vault platform"
```

Expected output:
```
✓ Created repository marthox/character-manager on GitHub
```

- [ ] **Step 2: Verify repo exists**

```bash
gh repo view marthox/character-manager --json name,url
```

Expected output:
```json
{
  "name": "character-manager",
  "url": "https://github.com/marthox/character-manager"
}
```

---

## Task 3: Extract character-vault history into character-manager

Preserves git history for all service files. Works from a temporary clone so the original repo is untouched.

**Files:** `/tmp/character-manager-build/` (temporary clone)

- [ ] **Step 1: Clone character-vault to a temp directory**

```bash
git clone git@github.com:marthox/character-vault.git /tmp/character-manager-build
```

Expected output ends with: `Resolving deltas: done.`

- [ ] **Step 2: Run filter-repo to keep only service files**

```bash
cd /tmp/character-manager-build && git filter-repo \
  --path src/ \
  --path tests/ \
  --path pyproject.toml \
  --path uv.lock \
  --path .python-version \
  --path .github/ \
  --path .vscode/ \
  --path .gitignore \
  --path README.md \
  --force
```

Expected output includes lines like:
```
Parsed 7 commits
New history written in ...s; now repacking/cleaning...
```

- [ ] **Step 3: Verify only service files remain**

```bash
ls /tmp/character-manager-build
```

Expected output (only these items, no `docs/` or `docker-compose.yml`):
```
README.md   pyproject.toml   src   tests   uv.lock
.github     .gitignore       .python-version   .vscode
```

- [ ] **Step 4: Add the character-manager remote**

```bash
cd /tmp/character-manager-build && git remote add origin git@github.com:marthox/character-manager.git
```

- [ ] **Step 5: Push the extracted history**

```bash
cd /tmp/character-manager-build && git push -u origin main
```

Expected output ends with:
```
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## Task 4: Add Dockerfile to character-manager

Multi-stage build using uv for fast, reproducible installs.

**Files:**
- Create: `Dockerfile` (in `/tmp/character-manager-build/`)

- [ ] **Step 1: Write the Dockerfile**

```bash
cat > /tmp/character-manager-build/Dockerfile << 'EOF'
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
EOF
```

- [ ] **Step 2: Commit the Dockerfile**

```bash
cd /tmp/character-manager-build && git add Dockerfile && git commit -m "Add multi-stage Dockerfile using uv"
```

Expected output:
```
[main ...] Add multi-stage Dockerfile using uv
 1 file changed, 11 insertions(+)
 create mode 100644 Dockerfile
```

---

## Task 5: Update character-manager README

Replace the orchestrator-focused README with service-level docs.

**Files:**
- Modify: `README.md` (in `/tmp/character-manager-build/`)

- [ ] **Step 1: Write the service README**

```bash
cat > /tmp/character-manager-build/README.md << 'EOF'
# Character Manager

Character management service — part of the [character-vault](https://github.com/marthox/character-vault) platform.

## Development

```bash
# Install dependencies
uv sync

# Run tests
pytest

# Run locally
fastapi dev src/main.py
```

## Docker

This service is built and run via the character-vault orchestrator.

```bash
# From the character-vault root
docker-compose up --build character-manager
```
EOF
```

- [ ] **Step 2: Commit and push**

```bash
cd /tmp/character-manager-build && git add README.md && git commit -m "Update README for standalone service" && git push
```

Expected output ends with:
```
main -> main
```

- [ ] **Step 3: Verify the repo on GitHub**

```bash
gh repo view marthox/character-manager
```

Confirm the description and README look correct.

---

## Task 6: Remove service files from character-vault

Strip all application code from the orchestrator root. The history is preserved in character-manager.

**Files:**
- Remove from `character-vault`: `src/`, `tests/`, `pyproject.toml`, `uv.lock`, `.python-version`, `.github/`, `.vscode/`

- [ ] **Step 1: Stage service files for removal**

```bash
cd /Users/marthox/Dev/character-vault && git rm -r src/ tests/ pyproject.toml uv.lock .python-version .github/ .vscode/
```

Expected output lists all removed files, e.g.:
```
rm 'src/__init__.py'
rm 'src/main.py'
...
rm '.vscode/settings.json'
```

- [ ] **Step 2: Verify only orchestrator files remain in the working tree**

```bash
ls /Users/marthox/Dev/character-vault
```

Expected (no src/, tests/, pyproject.toml, etc.):
```
README.md   docker-compose.yml   docs   .gitignore
```

- [ ] **Step 3: Clean up untracked Python artifacts (not tracked by git but left on disk)**

```bash
rm -rf /Users/marthox/Dev/character-vault/.venv \
        /Users/marthox/Dev/character-vault/.pytest_cache
```

---

## Task 7: Add character-manager as a submodule

**Files:**
- Create: `services/character-manager/` (submodule pointer)
- Create: `.gitmodules` (auto-created by git)

- [ ] **Step 1: Create the services directory**

```bash
mkdir -p /Users/marthox/Dev/character-vault/services
```

- [ ] **Step 2: Add character-manager as a submodule**

```bash
cd /Users/marthox/Dev/character-vault && git submodule add git@github.com:marthox/character-manager.git services/character-manager
```

Expected output:
```
Cloning into '/Users/marthox/Dev/character-vault/services/character-manager'...
```

- [ ] **Step 3: Verify the submodule is registered**

```bash
cat /Users/marthox/Dev/character-vault/.gitmodules
```

Expected:
```ini
[submodule "services/character-manager"]
	path = services/character-manager
	url = git@github.com:marthox/character-manager.git
```

- [ ] **Step 4: Verify submodule contents are present**

```bash
ls /Users/marthox/Dev/character-vault/services/character-manager
```

Expected (the service files cloned in):
```
Dockerfile   README.md   pyproject.toml   src   tests   uv.lock
```

---

## Task 8: Write orchestrator docker-compose.yml

**Files:**
- Modify: `docker-compose.yml`

- [ ] **Step 1: Write the full docker-compose config**

```bash
cat > /Users/marthox/Dev/character-vault/docker-compose.yml << 'EOF'
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
EOF
```

- [ ] **Step 2: Verify the file is valid YAML**

```bash
docker compose -f /Users/marthox/Dev/character-vault/docker-compose.yml config --quiet && echo "Valid"
```

Expected output: `Valid`

---

## Task 9: Create infra placeholder

**Files:**
- Create: `infra/.gitkeep`

- [ ] **Step 1: Create the infra directory with a gitkeep**

```bash
mkdir -p /Users/marthox/Dev/character-vault/infra && touch /Users/marthox/Dev/character-vault/infra/.gitkeep
```

- [ ] **Step 2: Verify**

```bash
ls -la /Users/marthox/Dev/character-vault/infra
```

Expected:
```
.gitkeep
```

---

## Task 10: Update orchestrator .gitignore and README

Replace Python-specific files with orchestrator-appropriate content.

**Files:**
- Modify: `.gitignore`
- Modify: `README.md`

- [ ] **Step 1: Write the orchestrator .gitignore**

```bash
cat > /Users/marthox/Dev/character-vault/.gitignore << 'EOF'
# Environment
.env
.env.*
!.env.example

# Logs
*.log

# OS
.DS_Store

# Docker
.docker/
EOF
```

- [ ] **Step 2: Write the orchestrator README**

```bash
cat > /Users/marthox/Dev/character-vault/README.md << 'EOF'
# Character Vault

Service orchestrator for the Character Vault platform.

## Services

| Service | Description | Repo |
|---------|-------------|------|
| [character-manager](services/character-manager) | Character management API | [marthox/character-manager](https://github.com/marthox/character-manager) |

## Getting Started

```bash
# Clone with all submodules
git clone --recurse-submodules git@github.com:marthox/character-vault.git

# Start all services
docker-compose up --build
```

## Adding a New Service

1. Create a standalone repo for the service with a `Dockerfile`
2. Add it as a submodule: `git submodule add <url> services/<name>`
3. Add the service to `docker-compose.yml`
4. Commit and push

## Infrastructure

Future IaS tooling (Terraform, AWS CDK, etc.) will live in `infra/`.
EOF
```

---

## Task 11: Final commit and push of character-vault

**Files:** all staged changes across tasks 6–10

- [ ] **Step 1: Check git status to review all staged and unstaged changes**

```bash
git -C /Users/marthox/Dev/character-vault status
```

Expected: staged deletions of service files, new files: `.gitmodules`, `services/character-manager`, `infra/.gitkeep`, and modifications to `docker-compose.yml`, `.gitignore`, `README.md`

- [ ] **Step 2: Stage remaining files**

```bash
cd /Users/marthox/Dev/character-vault && git add docker-compose.yml infra/.gitkeep .gitignore README.md
```

- [ ] **Step 3: Commit everything**

```bash
cd /Users/marthox/Dev/character-vault && git commit -m "$(cat <<'EOF'
Restructure: convert to service orchestrator

- Extract application code to standalone character-manager repo
- Add character-manager as git submodule at services/character-manager
- Add orchestrator docker-compose.yml with character-manager + postgres
- Add infra/ placeholder for future IaS tooling
- Replace Python .gitignore and README with orchestrator-level versions
EOF
)"
```

- [ ] **Step 4: Push to GitHub**

```bash
git -C /Users/marthox/Dev/character-vault push
```

Expected output:
```
main -> main
```

- [ ] **Step 5: Verify the final repo structure on GitHub**

```bash
gh repo view marthox/character-vault
```

And spot-check the submodule link resolves correctly:
```bash
gh browse --repo marthox/character-vault
```

- [ ] **Step 6: Smoke test — clone the orchestrator fresh with submodules**

```bash
git clone --recurse-submodules git@github.com:marthox/character-vault.git /tmp/character-vault-verify && ls /tmp/character-vault-verify/services/character-manager
```

Expected: the service files are present (Dockerfile, src/, tests/, etc.)

- [ ] **Step 7: Clean up temp directories**

```bash
rm -rf /tmp/character-manager-build /tmp/character-vault-verify
```
