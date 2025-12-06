'''
Defines the DeathSaves model for tracking death saving throws in an RPG system inspired by D&D.
'''

from pydantic import BaseModel, NonNegativeInt

class DeathSaves(BaseModel):
    '''Represents a character's death saving throws.'''
    successes: NonNegativeInt = 0
    failures: NonNegativeInt = 0
