'''
This file represents the SpellComponents model used in dnd.

How is SpellComponents structured?
- It includes attributes for verbal, somatic, and material components.
- Verbal and somatic components are boolean flags indicating if the spell requires them.
- Material components are a dictionary mapping component names to their respective currencies and counts.

How do material components work?
- Material components are represented as a dictionary where keys are component names
  and values are lists of Currency objects with their respective counts.
- For example, {"golden_rod": {Currency.GOLD, 50}} means the spell requires 50 gold pieces worth of a golden rod.
'''

from typing import Dict
from pydantic import BaseModel

from domain.constants.currency import Currency

class SpellComponents(BaseModel):
    '''Represents the components required for casting a spell.'''
    verbal: bool = False
    somatic: bool = False
    material: bool = False
    material_components: Dict[str, Dict[Currency, int]]= {}
