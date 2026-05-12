'''
Defines the attribute model for character attributes in an RPG system inspired by D&D.
'''

from pydantic import BaseModel, PositiveInt

class Attribute(BaseModel):
    '''Represents a character's attributes such as strength, dexterity, etc.'''
    strength: PositiveInt = 10
    dexterity: PositiveInt = 10
    constitution: PositiveInt = 10
    intelligence: PositiveInt = 10
    wisdom: PositiveInt = 10
    charisma: PositiveInt = 10
