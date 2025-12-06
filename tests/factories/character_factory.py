
"""Factory for creating Character model instances for tests."""

from domain.models.character import Character


def create_character(name="Default Name", **kwargs):
    """Create a Character instance with default or provided attributes."""
    return Character(name=name, **kwargs)
