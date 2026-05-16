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
