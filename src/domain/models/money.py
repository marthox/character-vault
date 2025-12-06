'''Defines the Money model used in dnd.'''

from pydantic import BaseModel

class Money(BaseModel):
    '''Represents an amount of money in various denominations.'''
    copper: int = 0
    silver: int = 0
    gold: int = 0
    platinum: int = 0
