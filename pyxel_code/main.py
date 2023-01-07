import pyxel
import time
import random
from os.path import join as path_join

from ImageClasses import *
from utils import *
# from shop_controller import ShopController

ted = {
    'Blacksmith': { 'x':48, 'y': 48, 'bank': 0, 'u': 0, 'v': 40, 'w':16, 'h':16, 'colkey': 0, 'name': 'Blacksmith', 'color': 8, "offset": 10},
    "Alchemist's Shop": {'x':16, 'y': 80, 'bank': 0, 'u': 16, 'v': 40, 'w':16, 'h':16, 'colkey': 0, 'name': 'Alchemist', 'color': 3, "offset": 10},
    "Inn": {'x':64, 'y': 80, 'bank': 0, 'u': 32, 'v': 40, 'w':16, 'h':16, 'colkey': 0, 'name': 'Inn', 'color': 10, "offset": -4},
    "shining_forest": {'x':112, 'y': 32, 'bank': 0, 'u': 0, 'v': 72, 'w':16, 'h':16, 'colkey': 0, 'name': 'Shining Forest', 'color': 7, "offset": 32},
    'underbelly': {'x':112, 'y': 96, 'bank': 0, 'u': 16, 'v': 72, 'w':16, 'h':16, 'colkey': 10, 'name': 'The Underbelly', 'color': 7, "offset": 32},
}


class App:
    def __init__(self):
        pyxel.init(142, 142, title="My Pyxel App", fps=60, display_scale=5)
        pyxel.load(path_join("assets", "dragons_tail.pyxres"))
        self.bg = Background(background['town'])
        self.MOUSE_LOCATION = ''
        pyxel.mouse(True)     
        self.blacksmith = Entrance(ted['Blacksmith'])
        self.alchemist = Entrance(ted["Alchemist's Shop"])
        self.inn = Entrance(ted['Inn'])
        self.underbelly = Entrance(ted['underbelly'])
        self.shining_forest = Entrance(ted['shining_forest'])
        self.shop = None

        # time
        self.speed = 1.5
        # self.time_last_frame = time.time()
        self.dt=0
        # self.time_since_last_move = 0


        pyxel.run(self.update, self.draw)

    def update(self):
        # time_this_frame = time.time()
        # self.dt = time_this_frame - self.time_last_frame
        # self. time_last_frame = time_this_frame
        # self.time_since_last_move += self.dt
        self.MOUSE_LOCATION = pyxel.mouse_x, pyxel.mouse_y
        if pyxel.btnr(301) == True:
                pyxel.text(36, 1, "clicked", 7)

        # if self.time_since_last_move >= 1/self.speed:
        #     self.time_since_last_move=0

        #     self.mouse.run()
        #     self.rat1.run()
        #     if self.blacksmith.intersects(self.MOUSE_LOCATION):
        #         self.blacksmith.flag.run()

        pass

    def check_mouse_position(self):
        if self.blacksmith.intersects(self.MOUSE_LOCATION):
            self.blacksmith.intersection()
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) == True:
                pyxel.text(32,1, 'clicked',7)
                self.bg.bank = 1
                pyxel.load(path_join('assets', 'shop_screen.py'))

        if self.inn.intersects(self.MOUSE_LOCATION):
            self.inn.intersection()
        if self.alchemist.intersects(self.MOUSE_LOCATION):
            self.alchemist.intersection()
        if self.underbelly.intersects(self.MOUSE_LOCATION):
            self.underbelly.intersection()
        if self.shining_forest.intersects(self.MOUSE_LOCATION):
            self.shining_forest.intersection()



    def draw(self):
        pyxel.cls(9)

        # // Creating Background
        self.bg.draw()

        pyxel.text(1, 1, f"{self.MOUSE_LOCATION}", 7)
        self.blacksmith.draw()
        self.inn.draw()
        self.alchemist.draw()
        self.shining_forest.draw()
        self.underbelly.draw()
        # if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        #         pyxel.text(36, 1, "clicked", 7)
        #  // Starting mouse tracking //
        self.check_mouse_position()

        


App()

