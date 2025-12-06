'''Defines the race model used in dnd.'''

from pydantic import BaseModel
from domain.constants.languages import Language

class Race(BaseModel):
    '''Represents a race in the game.'''
    name: str
    description: str | None = None
    speed: int = 30
    size: str = "Medium"
    languages: list[Language] = []
    traits: list[str] = []
