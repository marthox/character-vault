from typing import Callable


from domain.models.character import Character

SaveCharacterFn = Callable[[Character], None]
