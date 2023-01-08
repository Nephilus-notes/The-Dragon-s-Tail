# import pdb; pdb.set_trace()
from os.path import join as path_join
from time import time

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.game import Game
from pyxel_code.image_classes import Sidebar
from pyxel_code.utils import sidebar


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, title="From the Dragon's Tail", capture_sec=0, display_scale=5)
        px.load(path_join("assets", "dragons_tail.pyxres"))
        # px.fullscreen(True)

        self.MOUSE_LOCATION = ''

        self.pt = time()  # Buffer previous time
        self.game = Game()
        self.paused = False

        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])

        px.mouse(SHOW_CURSOR)
        px.run(self.update, self.draw)

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y

        if px.btnp(px.KEY_Q):
            px.quit()
        if px.btnp(px.KEY_P):
            if not self.paused:
                px.stop()
            else:
                self.pt = time()
                px.playm(3, loop=True)
            self.paused = not self.paused

        if not self.paused:

            self.game.state.update()
            self.game.state = self.game.state.get_next_state()

    def draw(self):
        px.cls(0)
        if not self.paused:
            self.game.state.draw()
        self.character_info.draw()
        self.item_info.draw()
        


App()