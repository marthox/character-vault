'''
Test cases for character model creation and validation.
'''

from domain.utils.character_utils import create_attribute, create_death_saves

class TestCharacterCreation():
    '''Tests for creating character models.'''
    def test_create_base_character(self, base_character):
        """Test creating a character with minimal attributes."""
        assert base_character.name == "Willow"
        assert base_character.main_class == "Fighter"
        assert base_character.race == "Human"
        assert base_character.alignment == "Neutral Good"
        assert base_character.level == 1
        assert base_character.experience == 0
        assert base_character.attributes == create_attribute()
        assert base_character.armor_class == 10
        assert base_character.initiative == 0
        assert base_character.speed == 30
        assert base_character.max_hit_points == 10
        assert base_character.current_hit_points == 10
        assert base_character.temporary_hit_points == 0
        assert base_character.hit_dice == {}
        assert base_character.death_saves == create_death_saves()
        assert base_character.attacks == []
        assert base_character.spell_book == []

