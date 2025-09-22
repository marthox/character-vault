from pydantic import BaseModel, Field, PositiveInt, NonNegativeInt
from typing import List, Dict
from uuid import UUID, uuid4

from domain.models.character_class import CharacterClass
from domain.models.background import Background
from domain.models.alignment import Alignment
from domain.models.skill import Skill
from domain.models.item import Item
from domain.models.attack import Attack
from domain.models.spell import Spell
from domain.models.race import Race
from domain.models.subrace import Subrace
from domain.models.death_saves import DeathSaves
from domain.models.attribute import Attribute
from domain.models.spell_slots import SpellSlots

class Character (BaseModel):
    id: UUID = Field(default_factory=uuid4)
    player: UUID

    name: str | None = None
    appearance: str | None = None
    description: str | None = None

    main_class: str | CharacterClass | None = None
    multi_classes: str | List[CharacterClass] | None = None
    level: PositiveInt = 1
    background: str | Background | None = None
    race: str | Race | None = None
    subrace: str | Subrace | None = None
    alignment: str | Alignment | None = None
    experience: NonNegativeInt = 0


    inspiration: NonNegativeInt = 0
    proficiency_bonus: PositiveInt = 2
    saving_throws: List[Attribute] = []
    features: List[str] = []
    skills: List[Skill] = []
    weapons_proficiencies: List[str] = []
    armor_proficiencies: List[str] = []
    tool_proficiencies: List[str] = []
    other_proficiencies: List[str] = []
    languages: List[str] = []

    attributes: Attribute = Attribute(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10
    )

    armor_class: PositiveInt = 10
    initiative: NonNegativeInt = 0
    speed: PositiveInt = 30
    max_hit_points: PositiveInt = 10
    current_hit_points: int = 10
    temporary_hit_points: NonNegativeInt = 0
    hit_dice: Dict[CharacterClass, NonNegativeInt] = {}

    spell_slots: SpellSlots = SpellSlots()

    death_saves: DeathSaves = DeathSaves(
        successes=0,
        failures=0
    )

    attacks: List[Attack] = []
    spell_book: List[Spell] = []

    personality_traits: List[str] = []
    ideals: List[str] = []
    bonds: List[str] = []
    flaws: List[str] = []

    inventory: List[Item] = []
