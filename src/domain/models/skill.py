from enum import Enum
from pydantic import BaseModel

from domain.constants.attribute import Attribute

class Skill(BaseModel):
    name: str
    description: str
    primary_attribute: Attribute
    proficient: bool = False
    expertise: bool = False
