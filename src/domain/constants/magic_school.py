"""Magic school constants for D&D spells."""

from enum import Enum

class MagicSchool(Enum):
    """Enum representing schools of magic in D&D."""
    ABJURATION = "abjuration"
    CONJURATION = "conjuration"
    DIVINATION = "divination"
    ENCHANTMENT = "enchantment"
    EVOCATION = "evocation"
    ILLUSION = "illusion"
    NECROMANCY = "necromancy"
    TRANSMUTATION = "transmutation"
    OTHER = "Other"
