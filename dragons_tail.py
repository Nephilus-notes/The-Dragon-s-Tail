# import pdb; pdb.set_trace()
from time import time

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.game import Game
from pyxel_code.image_classes import Sidebar
from pyxel_code.utils import sidebar


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, title="From the Dragon's Tail", fps=15, capture_sec=5, display_scale=5)
        px.load("assets/dragons_tail.pyxres")
        # px.fullscreen(True)

        self.MOUSE_LOCATION = ''

        self.pt = time()  # Buffer previous time
        self.game = Game()
        self.paused = False


        

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

        


App()