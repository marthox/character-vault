from enum import Enum

class DamageType(Enum):
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
