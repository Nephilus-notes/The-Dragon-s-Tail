import pytest

from ..conftest import end_game_character, early_game_character

from old_code.character_builder import Character

def test_bag_existence(end_game_character):
    assert end_game_character.bag

def test_bag_contents(end_game_character):
    assert end_game_character.bag.slots['dagger']
    assert end_game_character.bag.slots['axe']
    assert end_game_character.bag.slots['sword']
    assert end_game_character.bag.slots['leather_armor']

def test_strength_level_up(end_game_character):
    end_game_character.level_attribute('strength')
    assert end_game_character.strength == 21
    end_game_character.level_attribute('strength')
    assert end_game_character.strength == 22
    end_game_character.level_attribute('strength')
    assert end_game_character.strength == 23
    end_game_character.level_attribute('strength')
    assert end_game_character.strength == 24

def test_dexterity_level_up(end_game_character):
    end_game_character.level_attribute('dexterity')
    assert end_game_character.dexterity == 21
    end_game_character.level_attribute('dexterity')
    assert end_game_character.dexterity == 22
    end_game_character.level_attribute('dexterity')
    assert end_game_character.dexterity == 23
    end_game_character.level_attribute('dexterity')
    assert end_game_character.dexterity == 24

def test_intelligence_level_up(end_game_character):
    end_game_character.level_attribute('intelligence')
    assert end_game_character.intelligence == 21
    end_game_character.level_attribute('intelligence')
    assert end_game_character.intelligence == 22
    end_game_character.level_attribute('intelligence')
    assert end_game_character.intelligence == 23
    end_game_character.level_attribute('intelligence')
    assert end_game_character.intelligence == 24

def test_constitution_level_up(end_game_character):
    end_game_character.level_attribute('constitution')
    assert end_game_character.constitution == 21
    end_game_character.level_attribute('constitution')
    assert end_game_character.constitution == 22
    end_game_character.level_attribute('constitution')
    assert end_game_character.constitution == 23
    end_game_character.level_attribute('constitution')
    assert end_game_character.constitution == 24

@pytest.mark.xfail
def test_level_up_fail(end_game_character):
    end_game_character.level_attribute('constitution')
    assert end_game_character.constitution == 20