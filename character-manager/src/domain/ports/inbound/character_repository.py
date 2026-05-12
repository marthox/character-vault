from abc import ABC, abstractmethod

class GetCharacterByIdUseCase(ABC):
    @abstractmethod
    def execute(self, character_id: str):
        """Retrieve a character by its unique identifier."""

class GetCharactersByPlayerIdUseCase(ABC):
    @abstractmethod
    def execute(self, player_id: str):
        """Retrieve all characters associated with a specific player."""
