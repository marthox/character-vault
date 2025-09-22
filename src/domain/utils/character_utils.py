from domain.models.character import Character
from domain.models.attribute import Attribute
from domain.models.death_saves import DeathSaves

def create_character(**kwargs) -> Character:
    """Create a default character with specified attributes."""
    invalid_keys = kwargs.keys() - set(Character.model_fields)
    if invalid_keys:
        raise ValueError(f"Invalid attribute(s): {', '.join(invalid_keys)}")
    return Character(**kwargs)

def create_attribute(**kwargs) -> Attribute:
    """Create a default attribute dictionary."""
    invalid_keys = kwargs.keys() - set(Attribute.model_fields)
    if invalid_keys:
        raise ValueError(f"Invalid attribute(s): {', '.join(kwargs.keys() - set(Attribute.model_fields))}")
    return Attribute(**{key: kwargs.get(key, 10) for key in Attribute.model_fields.keys()})

def create_death_saves(successes: int = 0, failures: int = 0) -> DeathSaves:
    """Create a DeathSaves object with specified successes and failures."""
    return DeathSaves(successes=successes, failures=failures)

def export_character(character: Character) -> dict:
    """Export character data to a dictionary."""
    return {}   