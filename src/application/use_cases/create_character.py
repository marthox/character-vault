'''
Use case for creating a new character.
'''

from domain.models.character import Character
from application.ports.character_repository import SaveCharacterFn

def create_character_use_case(
    character_info: dict,
    save_character_fn: SaveCharacterFn
) -> Character:
    '''Create a new character and save it to the repository.'''
    character = Character(**character_info)
    save_character_fn(character)
    return character.id
