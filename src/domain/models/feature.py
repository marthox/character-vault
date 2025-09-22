from pydantic import BaseModel

from domain.constants.feat_category import FeatCategory

class Feat(BaseModel):
    name: str
    description: str
    source: str
    category: FeatCategory

    prerequisites: list[str] = []
    benefits: list[str] = []
