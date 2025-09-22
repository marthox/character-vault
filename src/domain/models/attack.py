'''
Attack model used in dnd.

How is attack structured?
- It includes a saving throw, attack modifier, damage, range, proficiency, and description.
- Saving throw is an optional attribute that can be set to an Attribute.
- Attack modifier is required and must be an Attribute.
- Damage is a dictionary mapping DamageType to another dictionary of Dice and their counts.
- Range defaults to 5, indicating melee range.
- Proficiency indicates if the character is proficient with the attack.
- Description provides additional context for the attack.

How does damage work?
- Damage is represented as a dictionary where keys are DamageType and values are dictionaries
  mapping Dice to the number of dice rolled.
- For example, {DamageType.SLASHING: {Dice.D8: 1, Dice.D6: 2}} means the attack deals 1d8 + 2d6 slashing damage.
'''

from pydantic import BaseModel, PositiveInt
from typing import Dict, Optional

from domain.constants.dice import Dice
from domain.constants.attribute import Attribute
from domain.constants.damage_type import DamageType

class Attack(BaseModel):
    saving_throw: Optional[Attribute] = None
    attack_attribute: Attribute
    damage: Dict[DamageType, Dict[Dice, PositiveInt]]
    range: PositiveInt = 5
    proficient: bool = False
    description: str = ""
