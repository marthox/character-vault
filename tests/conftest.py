"""Shared pytest fixtures for all tests."""

from uuid import uuid4

import pytest

from src.domain.utils.character_utils import create_character

@pytest.fixture
def base_character():
    """Create a basic test character."""
    return create_character(
        player=uuid4(),
        name="Willow",
        main_class="Fighter",
        race="Human",
        alignment="Neutral Good",
    )
