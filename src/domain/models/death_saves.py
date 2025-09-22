from pydantic import BaseModel, NonNegativeInt

class DeathSaves(BaseModel):
    successes: NonNegativeInt = 0
    failures: NonNegativeInt = 0
