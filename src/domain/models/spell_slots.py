'''Defines the SpellSlots model used in dnd.'''

from pydantic import BaseModel, Field, NonNegativeInt

class SpellLevelSlots(BaseModel):
    '''Represents spell slots for a specific spell level.'''
    total: NonNegativeInt = 0
    used: NonNegativeInt = 0

class SpellSlots(BaseModel):
    '''Represents a character's spell slots across all spell levels.'''
    first_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    second_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    third_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    fourth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    fifth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    sixth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    seventh_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    eighth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    ninth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)