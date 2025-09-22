from pydantic import BaseModel, PositiveInt, Field

class Attribute(BaseModel):
    strength: PositiveInt = 10
    dexterity: PositiveInt = 10
    constitution: PositiveInt = 10
    intelligence: PositiveInt = 10
    wisdom: PositiveInt = 10
    charisma: PositiveInt = 10
