from domain.constants.languages import Language

from pydantic import BaseModel

class Race(BaseModel):
    name: str
    description: str | None = None
    speed: int = 30
    size: str = "Medium"
    languages: list[Language] = []
    traits: list[str] = []
