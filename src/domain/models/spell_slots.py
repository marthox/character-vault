from pydantic import BaseModel, Field, NonNegativeInt

class SpellLevelSlots(BaseModel):
    total: NonNegativeInt = 0
    used: NonNegativeInt = 0

class SpellSlots(BaseModel):
    first_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    second_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    third_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    fourth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    fifth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    sixth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    seventh_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    eighth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)
    ninth_level: SpellLevelSlots = Field(default_factory=SpellLevelSlots)