import pyxel as px
from time import time

from pyxel_code.constants import WIDTH, HEIGHT
from pyxel_code.game_states import TownScreenState
from old_code.character_builder import Player
from old_code.dicts import background_stats

class Game:
    def __init__(self):

        self.score = 0
        self.lives = 3
        self.player = Player("Crae", **background_stats['b']['stats'], game=self)
        self.won_game = False
        self.text_timer = 0

        self.state = TownScreenState(self)

