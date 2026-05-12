"""Damage type constants for D&D."""

from enum import Enum

class DamageType(Enum):
    """Enum representing different types of damage in D&D."""
    # Physical
    SLASHING = "slashing"
    PIERCING = "piercing"
    BLUDGEONING = "bludgeoning"

    # Elemental
    ACID = "acid"
    FIRE = "fire"
    THUNDER = "thunder"
    COLD = "cold"
    LIGHTNING = "lightning"
    POISON = "poison"

    # Magical
    RADIANT = "radiant"
    PSYCHIC = "psychic"
    FORCE = "force"
    NECROTIC = "necrotic"
