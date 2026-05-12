'''Defines the Feat model used in dnd.'''

from pydantic import BaseModel

from domain.constants.feat_category import FeatCategory

class Feat(BaseModel):
    '''Represents a feat in the game.'''
    name: str
    description: str
    source: str
    category: FeatCategory

    prerequisites: list[str] = []
    benefits: list[str] = []
