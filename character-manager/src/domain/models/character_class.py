'''
This module defines the CharacterClass model for character classes in an RPG system inspired by D&D.
'''

from typing import Dict, Annotated, List
from pydantic import AfterValidator, PositiveInt, Field

from domain.constants.attribute import Attribute
from domain.constants.sources import Source
from domain.constants.dice import Dice

from domain.models.base_class import BaseClass

def normalize_name(class_name: str) -> str:
    '''Normalizes the character class name to title case.'''
    return class_name.title()

class CharacterClass(BaseClass):
    '''Represents a character class with its attributes and requirements.'''
    name: Annotated[str, AfterValidator(normalize_name)]
    source: Source = Field(...)

    primary_ability: List[Attribute] = Field(..., min_length=1)
    hit_point_die: Dice = Field(...)
    multiclass_requirements: Dict[Attribute, PositiveInt] = Field(...)
