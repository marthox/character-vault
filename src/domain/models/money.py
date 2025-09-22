from pydantic import BaseModel

class Money(BaseModel):
    copper: int = 0
    silver: int = 0
    gold: int = 0
    platinum: int = 0
