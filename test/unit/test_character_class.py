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
    end_game_character.level_attribute('STR', 52)
    assert end_game_character.strength == 52


def test_dexterity_level_up(end_game_character):
    end_game_character.level_attribute('DEX', 25)
    assert end_game_character.dexterity == 25


def test_intelligence_level_up(end_game_character):
    end_game_character.level_attribute('INT', 74)
    assert end_game_character.intelligence == 74


def test_constitution_level_up(end_game_character):
    end_game_character.level_attribute('CON', 13)
    assert end_game_character.constitution == 13

@pytest.mark.xfail
def test_level_up_fail(end_game_character):
    end_game_character.level_attribute('CON', 2)
    assert end_game_character.constitution == 22