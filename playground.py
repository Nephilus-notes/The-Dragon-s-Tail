import pyxel as px
from time import time
from abc import ABC, abstractmethod
from os.path import join as path_join


from old_code.npc_classes import *
from old_code.character_builder import Player
from old_code.dicts import background_stats
from pyxel_code.image_classes import * 
from pyxel_code.constants import *
from pyxel_code.utils import *
from pyxel_code.game_states import TownScreenState


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, title="From the Dragon's Tail", capture_sec=0)
        px.load(path_join("assets", "dragons_tail.pyxres"))
        # px.fullscreen(True)
        self.MOUSE_LOCATION = ''
        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])
        self.leather = ShopItem(**item_location[3], id =3)
        self.enemy = ShadeFireFox()
        Layer.main.append(self.enemy)

        self.player = Player('Crae', **background_stats['b']['stats'])
        # Layer.main.append(self.player)
        # for num in range(6):
            # item = ShopItem(**item_location[num])
            # Layer.main.append(item)

        px.mouse(SHOW_CURSOR)
        px.run(self.update, self.draw)

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y

    def draw(self):
        px.cls(0)
        bg = Background(**background['combat'])
        bg.draw()
        self.character_info.draw()
        self.item_info.draw()
        # px.bltm(8, 8, 0, 0, 256, 64, 128)
        # px.bltm(192, 8, 0, 64, 256, 64, 128)

        for itm in Layer.main:
            itm.draw()
        self.player.combat_draw()
        self.player.draw_sidebar()
        # px.text(1,1, f'{self.player.name}', 1)
        # self.leather.draw()
        # px.blt(96,24,2,0,0,16,16,7)
        # px.bltm(8, 8, 0, background['town']['u'], background['town']['v'], 128, 128)
        # px.bltm(8, 8, 0, background['blacksmith']['u'], background['blacksmith']['v'], 128, 128)
        # px.bltm(8, 8, 0, background['alchemist']['u'], background['alchemist']['v'], 128, 128)



App()