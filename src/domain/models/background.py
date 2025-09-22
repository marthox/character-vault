'''
Background model used in dnd 2014.
'''

from pydantic import BaseModel, PositiveInt

from domain.models.skill import Skill
from domain.models.item import Item
from domain.models.feature import Feat

from domain.constants.languages import Language
from domain.constants.tools import Tool

class Background(BaseModel):
    name: str
    description: str
    source: str

    skill_proficiencies: list[Skill] = []
    tool_proficiencies: list[Tool | str] = []
    languages: list[Language | str] = []
    equipment: list[Item] = []
    initial_money: PositiveInt = 0
    feature: Feat | None = None

class Background2024(BaseModel):
    name: str
    description: str
    source: str
