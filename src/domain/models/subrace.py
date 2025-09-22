from pydantic import BaseModel

from domain.models.race import Race

class Subrace(BaseModel):
    base_race: Race
    name: str
    description: str
    speed: int = 30
    size: str = "Medium"
    languages: list[str] = []
    traits: list[str] = []
