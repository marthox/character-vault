from domain.models.character import Character

def create_character(name="Default Name", **kwargs):
    return Character(name=name, **kwargs)
