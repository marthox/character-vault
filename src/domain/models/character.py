'''
Defines the Character model for the RPG system inspired in D&D.
'''

from uuid import UUID
from typing import List, Dict
from pydantic import PositiveInt, NonNegativeInt

from domain.models.base_class import BaseClass
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

class Character(BaseClass):
    '''
    A class to represent a character in the RPG system inspired in D&D.

    Attributes:
        id (UUID):
            Unique identifier for the character.
        player (UUID):
            Unique identifier for the player who owns the character.
        name (str | None):
            The name of the character.
        character_appearance (str | None):
            Description of the character's appearance.
        allies_and_organizations (str | None):
            Allies and organizations associated with the character.
        character_backstory (str | None): 
            The backstory of the character.
        additional_features_and_traits (str | None):
            Additional features and traits of the character.
        treasure (str | None):
            Treasure owned by the character.
        main_class (str | CharacterClass | None):
            The main class of the character.
        multi_classes (str | List[CharacterClass] | None):
            Multi-classes of the character.
        level (PositiveInt):
            The level of the character (default is 1).
        background (str | Background | None):
            The background of the character.
        race (str | Race | None):
            The race of the character.
        subrace (str | Subrace | None):
            The subrace of the character.
        alignment (str | Alignment | None):
            The alignment of the character.
        experience (NonNegativeInt):
            The experience points of the character (default is 0).
        inspiration (NonNegativeInt):
            The inspiration points of the character (default is 0).
        proficiency_bonus (PositiveInt):
            The proficiency bonus of the character (default is 2).
        saving_throws (List[Attribute]):
            List of saving throw attributes the character is proficient in.
        features (List[str]):
            List of features the character has.
        skills (List[Skill]):
            List of skills the character is proficient in.
        weapons_proficiencies (List[str]):
            List of weapon proficiencies the character has.
        armor_proficiencies (List[str]):
            List of armor proficiencies the character has.
        tool_proficiencies (List[str]):
            List of tool proficiencies the character has.
        other_proficiencies (List[str]):
            List of other proficiencies the character has.
        languages (List[str]):
            List of languages the character knows.
        attributes (Attribute):
            The character's attributes (str, dex, con, int, wis, cha).
        armor_class (PositiveInt):
            The armor class of the character (default is 10).
        initiative (NonNegativeInt):
            The initiative bonus of the character (default is 0).
        speed (PositiveInt):
            The speed of the character in feet (default is 30).
        max_hit_points (PositiveInt):
            The maximum hit points of the character (default is 10).
        current_hit_points (int):
            The current hit points of the character (default is 10).
        temporary_hit_points (NonNegativeInt):
            The temporary hit points of the character (default is 0).
        hit_dice (Dict[CharacterClass, NonNegativeInt]):
            Dictionary mapping character classes to the number of hit dice the character has.
        spell_slots (SpellSlots):
            The spell slots available to the character.
        death_saves (DeathSaves):
            The death saves of the character (successes and failures).
        attacks (List[Attack]):
            List of attacks the character can perform.
        spell_book (List[Spell]):
            List of spells the character knows.
        personality_traits (List[str]):
            List of personality traits of the character.
        ideals (List[str]):
            List of ideals of the character.
        bonds (List[str]):
            List of bonds of the character.
        flaws (List[str]):
            List of flaws of the character.
        inventory (List[Item]):
            List of items in the character's inventory.
    '''

    player: UUID

    name: str | None = None
    character_appearance: str | None = None
    allies_and_organizations: str | None = None
    character_backstory: str | None = None
    additional_features_and_traits: str | None = None
    treasure: str | None = None

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
