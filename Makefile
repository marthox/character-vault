install-hooks:
	chmod +x hooks/pre-commit
	ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
	@echo "Pre-commit hook installed."

check:
	cd character-manager && uv run pytest && uv run ruff check src/ tests/ && uv run pylint src/ && uv run mypy src/
