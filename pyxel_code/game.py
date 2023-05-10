import pyxel as px
from time import time

from pyxel_code.constants import WIDTH, HEIGHT
from pyxel_code.game_states import TitleScreen
from old_code.character_builder import Player
from old_code.dicts import background_stats
bad_stats = [8,8,4,2]

game_stats = [background_stats["Nakat'th"]['stats']]
class Game:
    def __init__(self):
        
        self.score = 0
        self.lives = 3
        self.player =  Player(**background_stats["Nakat'th"]['stats'], game=self)
        self.won_game = False
        self.text_timer = 0
        self.text = []

# How to set levels for all sound? Not sure. still not sure
        px.Sound()
        

        self.state = TitleScreen(self)

