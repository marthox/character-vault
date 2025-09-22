import pytest

from domain.utils.character_utils import create_attribute, create_character, create_death_saves
from uuid import uuid4

# Fixture to create a character for testing

@pytest.fixture
def base_character():
    return create_character(
        player=uuid4(),
        name="Willow",
        main_class="Fighter",
        race = "Human",
        alignment = "Neutral Good",
    )

class TestCharacterCreation():
    def test_create_base_character(self, character):
        """Test creating a character with minimal attributes."""
        assert character.name == "Willow"   
        assert character.main_class == "Fighter"
        assert character.race == "Human"
        assert character.alignment == "Neutral Good"
        assert character.level == 1
        assert character.experience == 0
        assert character.attributes == create_attribute()
        assert character.armor_class == 10
        assert character.initiative == 0
        assert character.speed == 30
        assert character.max_hit_points == 10
        assert character.current_hit_points == 10
        assert character.temporary_hit_points == 0
        assert character.hit_dice == {}
        assert character.death_saves == create_death_saves()
        assert character.attacks == []
        assert character.spell_book == []
