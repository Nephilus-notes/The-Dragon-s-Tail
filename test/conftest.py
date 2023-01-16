import pytest
import pyxel as px

from pyxel_code.game_states import *
from old_code.character_builder import Character
from old_code.item_screen import Backpack, EquippedItems
from pyxel_code.utils import items as itm
from pyxel_code.game import Game

@pytest.fixture
def game():
    game= Game()
    return game

@pytest.fixture
def combat_state(game):
    game.state = CombatState(game)

    return game.state