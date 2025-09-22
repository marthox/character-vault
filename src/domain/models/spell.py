'''
This file defines the Spell model used in dnd.

How is spell structured?
- It includes name, level, school, and various attributes related to casting.
- Level must be between 0 and 9.
- School indicates the type of magic (e.g., Evocation, Illusion).
- Casting ability, time, range, and components are specified.
- Description provides details about the spell's effects.
- Higher level effects can be specified for casting at levels above 1st.
- Attacks can be associated with the spell.

This structure allows for a comprehensive representation of spells in role-playing games,
accommodating various magical effects and casting requirements.

How do casting times work?
You have two casting times, one for normal casting and one for ritual casting (if applicable), and a duration.

- Casting time is a dictionary mapping a CastingTime, to an integer representing the amount
  of that casting time required for the spell.
  for example, {CastingTime.ACTION: 1} means the spell takes 1 action to cast.
  {CastingTime.ACTION: 1, CastingTime.BONUS_ACTION: 1} means the spell takes 1 action or 1 bonus action to cast.

- Ritual casting time is optional and can be set to None if the spell does not have a ritual casting time.
  it works the same way as casting time, but it is only used when casting the spell as a ritual.
  for example, {CastingTime.MINUTE: 10} means the spell takes 10 minutes to cast as a ritual.

- Duration is a dictionary mapping a CastingTime to an integer representing the amount
  of that casting time the spell lasts.
  for example, {CastingTime.MINUTE: 1} means the spell lasts for 1 minute.
  {CastingTime.HOUR: 1, CastingTime.MINUTE: 30} means the spell lasts for 1 hour and 30 minutes.

  
How do higher level effects work?
- Higher level effects can be either a string description or a dictionary mapping an integer level
  to a list of tuples, each containing an integer and a Dice type.
  
- For example, {2: [(1, Dice.D6)], 3: [(2, Dice.D6)]} means that when the spell is cast at 2nd level,
  it deals an additional 1d6 damage, and when cast at 3rd level, it deals an additional 2d6 damage.
'''

from pydantic import BaseModel, Field, PositiveInt
from typing import Optional, List, Dict

from domain.models.attack import Attack
from domain.models.spell_components import SpellComponents

from domain.constants.dice import Dice
from domain.constants.magic_school import MagicSchool
from domain.constants.attribute import Attribute
from domain.constants.common_time import CommonTime

class Spell(BaseModel):
    name: str
    level: PositiveInt = Field(ge=0, le=9)
    school: MagicSchool

    is_ritual: bool = False
    requires_concentration: bool = False
    duration: str | Dict[CommonTime, PositiveInt] = CommonTime.INSTANTANEOUS

    spell_casting_attribute: Attribute
    casting_time: Dict[CommonTime, PositiveInt] = Field(default={CommonTime.ACTION: 1}, min_length=1)
    ritual_casting_time: Optional[Dict[CommonTime, PositiveInt]] = None
    range: PositiveInt = 5
    components: SpellComponents

    description: str
    higher_level_effects: Optional[
        str | Dict[PositiveInt, Dict[PositiveInt, Dice]]
    ] = None
    attacks: List[Attack] = []
