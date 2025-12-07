"""Language constants for D&D characters."""

from enum import Enum

class Language(Enum):
    """Enum representing available languages in D&D."""
    COMMON = "common"
    DWARVISH = "dwarvish"
    ELVISH = "elvish"
    GIANT = "giant"
    GNOMISH = "gnomish"
    HALFLING = "halfling"
    ORC = "orc"
    ABYSSAL = "abyssal"
    CELESTIAL = "celestial"
    DRACONIC = "draconic"
    DEEP_SPEECH = "deep speech"
    INFERNAL = "infernal"
    PRIMORDIAL = "primordial"
    SYLVAN = "sylvan"
    UNDERCOMMON = "undercommon"
    OTHER = "other"
