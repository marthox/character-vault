'''
Alignment model used in dnd.

How is alignment structured?
- It includes a description, morality, and ethics.
- Morality can be "Good", "Neutral", or "Evil".
- Ethics can be "Lawful", "Neutral", or "Chaotic".

This structure allows for a flexible representation of character alignment
in role-playing games, accommodating various moral and ethical perspectives
following the alignment matrix commonly used in tabletop RPGs.

                  Law vs Chaos
-------------------------------------------------|
| Lawful Good   | Neutral Good | Chaotic Good    |
-------------------------------------------------|
| Lawful Neural | True Neutral | Chaotic Neutral | Good vs Evil
-------------------------------------------------|
| Lawful Evil   | Neutral Evil | Chaotic Evil    |
-------------------------------------------------|
'''

from pydantic import BaseModel
from enum import Enum

class _Morality(Enum):
    good: str = "Good"
    neutral: str = "Neutral"
    evil: str = "Evil"

class _Ethics(Enum):
    lawful: str = "Lawful"
    neutral: str = "Neutral"
    chaotic: str = "Chaotic"    

class Alignment(BaseModel):
    description: str | None = None
    ethics: _Ethics
    morality: _Morality