import pyxel as px
from time import time

from pyxel_code.constants import WIDTH, HEIGHT
from pyxel_code.game_states import TownScreenState

class Game:
    def __init__(self):

        self.score = 0
        self.lives = 3

        self.won_game = False

        self.state = TownScreenState(self)
        # self.state = GameStateVictory(self)