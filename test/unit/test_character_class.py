import pytest

from ..conftest import game, combat_state

from old_code.character_builder import Character

def test_bag_existence(game):
    assert game.player.bag

# @pytest.mark.skip
# def test_bag_contents(game):
#     assert game.player.bag.slots['dagger']
#     assert game.player.bag.slots['axe']
#     assert game.player.bag.slots['sword']
#     assert game.player.bag.slots['leather_armor']

def test_strength_level_up(game):
    game.player.level_attribute('STR', 52)
    assert game.player.strength == 52


def test_dexterity_level_up(game):
    game.player.level_attribute('DEX', 25)
    assert game.player.dexterity == 25


def test_intelligence_level_up(game):
    game.player.level_attribute('INT', 74)
    assert game.player.intelligence == 74


def test_constitution_level_up(game):
    game.player.level_attribute('CON', 13)
    assert game.player.constitution == 13

@pytest.mark.xfail
def test_level_up_fail(game):
    game.player.level_attribute('CON', 2)
    assert game.player.constitution == 22