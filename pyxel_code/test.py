import pyxel as px
from time import time
from abc import ABC, abstractmethod
from os.path import join as path_join


from ImageClasses import * 
from pyxel_code.constants import *
from utils import *
from game_states import TownScreenState


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, title="From the Dragon's Tail", capture_sec=0)
        px.load(path_join("assets", "dragons_tail.pyxres"))
        # px.fullscreen(True)
        self.MOUSE_LOCATION = ''
        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])
        self.leather = ShopItem(**item_location[3])

        for num in range(6):
            item = ShopItem(**item_location[num])
            Layer.main.append(item)

        px.mouse(SHOW_CURSOR)
        px.run(self.update, self.draw)

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y

    def draw(self):
        px.cls(0)
        bg = Background(**background['blacksmith'])
        bg.draw()
        # px.bltm(8, 8, 0, 0, 256, 64, 128)
        # px.bltm(192, 8, 0, 64, 256, 64, 128)
        self.character_info.draw()
        self.item_info.draw()
        for itm in Layer.main:
            itm.draw()
        self.leather.draw()
        # px.blt(96,24,2,0,0,16,16,7)
        # px.bltm(8, 8, 0, background['town']['u'], background['town']['v'], 128, 128)
        # px.bltm(8, 8, 0, background['blacksmith']['u'], background['blacksmith']['v'], 128, 128)
        # px.bltm(8, 8, 0, background['alchemist']['u'], background['alchemist']['v'], 128, 128)



App()