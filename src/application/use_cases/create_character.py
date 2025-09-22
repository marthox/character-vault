from domain.models.character import Character
from ports.character_repository import SaveCharacterFn

def create_character_use_case(
    character_info: dict,
    save_character_fn: SaveCharacterFn
) -> Character:
    character = Character(**character_info)
    save_character_fn(character)
    return character.id