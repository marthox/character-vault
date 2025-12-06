'''
Defines the alignment model used in D&D.

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

from enum import Enum

from pydantic import BaseModel

class _Morality(Enum):
    GOOD = "Good"
    NEUTRAL = "Neutral"
    EVIL = "Evil"

class _Ethics(Enum):
    LAWFUL = "Lawful"
    NEUTRAL = "Neutral"
    CHAOTIC = "Chaotic"

class Alignment(BaseModel):
    '''Represents a character's alignment in terms of ethics and morality. '''
    description: str | None = None
    ethics: _Ethics
    morality: _Morality
