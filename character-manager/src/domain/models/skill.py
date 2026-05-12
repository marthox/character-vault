'''Defines the Skill model used in dnd.'''

from pydantic import BaseModel

from domain.constants.attribute import Attribute

class Skill(BaseModel):
    '''Represents a skill in the game.'''
    name: str
    description: str
    primary_attribute: Attribute
    proficient: bool = False
    expertise: bool = False
