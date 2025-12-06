'''Defines the Item model used in dnd.'''

from pydantic import BaseModel

class Item(BaseModel):
    '''Represents an item in the game.'''
    name: str
