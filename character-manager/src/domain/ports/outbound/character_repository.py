from typing import Callable
from uuid import UUID
from abc import ABC, abstractmethod

from domain.models.character import Character

class CharacterRepository(ABC):
    @abstractmethod
    def get_character_by_id(self, character_id: UUID) -> Character | None:
        """Retrieve a character by its unique identifier."""

    @abstractmethod
    def save_character(self, character: Character) -> Character:
        """Save or update a character in the repository.""" 

    @abstractmethod
    def delete_character(self, character_id: UUID) -> Character:
        """Delete a character from the repository by its unique identifier."""

    @abstractmethod
    def list_characters(self, filter_func: Callable[[Character], bool]) -> list[Character]:
        """List all characters, optionally filtered by a provided function."""

    @abstractmethod
    def save(self, character: Character) -> None:
        """Alias for save_character method."""
