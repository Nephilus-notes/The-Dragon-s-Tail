from time import time
from abc import ABC, abstractmethod
from os.path import join as path_join

import pyxel as px

# import pyxel_code.ImageClasses as IC
from pyxel_code.constants import *
import pyxel_code.utils as u

from old_code.npc_classes import *


class GameState(ABC):
    def __init__(self, game):
        self.game = game
        self._next_state = self
        self.on_enter()

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def update(self, dt, t):
        pass

    @abstractmethod
    def draw(self):
        pass

    def clear_layers(self):
        u.Layer.back = []
        u.Layer.main = []
        u.Layer.fore = []

    def get_next_state(self):
        return self._next_state

    def draw_layers(self):
        # px.cls(Background.color)
        for item in u.Layer.back:
            item.draw()
        for item in reversed(u.Layer.main):
            item.draw()
        for item in u.Layer.fore:
            item.draw()
    
    def check_mouse_position(self):
        for item in u.Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw_hud(self):
        # Score on top right
        score = str(self.game.score)
        x = WIDTH - len(score) * 4 - 1
        # pos_txt = v2(x, 2) + Entity.offset
        # px.text(*pos_txt, score, WHITE)

class TownScreenState(GameState):
    def on_enter(self):
        self.clear_layers()
        self.bg = IC.Background(**u.background['town'])
        u.Layer.back.append(self.bg)
        self.blacksmith = IC.Entrance(u.ted['Blacksmith'])
        self.alchemist = IC.Entrance(u.ted["Alchemist's Shop"])
        self.inn = IC.Entrance(u.ted['Inn'])
        self.underbelly = IC.Entrance(u.ted['underbelly'])
        self.shining_forest = IC.Entrance(u.ted['shining_forest'])
        u.Layer.main.append(self.alchemist)
        u.Layer.main.append(self.blacksmith)
        u.Layer.main.append(self.inn)
        u.Layer.main.append(self.underbelly)
        u.Layer.main.append(self.shining_forest)

        self.MOUSE_LOCATION = ''


    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

        pass 
    
    def check_mouse_position(self):
        if self.blacksmith.intersects(self.MOUSE_LOCATION):
            self.blacksmith.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = BlacksmithScreen(self.game) # add shoptoken to dictate which shop it is, also add self.pu.layer
        if self.inn.intersects(self.MOUSE_LOCATION):
            self.inn.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = InnScreen(self.game)
        if self.alchemist.intersects(self.MOUSE_LOCATION):
            self.alchemist.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                self._next_state = AlchemistScreen(self.game) # add shoptoken to dictate which shop it is, also add self.pu.layer
                px.text(1,1, "clicked", 7)
        if self.underbelly.intersects(self.MOUSE_LOCATION):
            self.underbelly.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = UnderbellyMapState(self.game)
        if self.shining_forest.intersects(self.MOUSE_LOCATION):
            self.shining_forest.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = ShiningForestMapState(self.game)

    def draw(self):
        # px.cls(0)
        self.draw_layers()
        self.check_mouse_position()

class BlacksmithScreen(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = IC.Background(**u.background['blacksmith'])
        # self.items = []
        for num in range(6):
            item = IC.ShopItem(**u.item_location[num])
            u.Layer.main.append(item)
        self.exit = Button(self)
        u.Layer.main.append(self.exit)


        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

    def check_mouse_position(self):
        for item in u.Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class AlchemistScreen(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = IC.Background(**u.background['alchemist'])
        # self.items = []
        for num in range(8,11):
            item = IC.ShopItem(**u.item_location[num])
            u.Layer.main.append(item)
        self.exit = Button(self)
        u.Layer.main.append(self.exit)

        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 
 
    def check_mouse_position(self):
        for item in u.Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()


class InnScreen(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = IC.Background(**u.background['inn'])
        self.exit = Button(self)
        u.Layer.main.append(self.exit)

        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    
        # self.bg_town = Town()
        pass

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class ShiningForestMapState(GameState):
    def on_enter(self):
        self.clear_layers()


        self.bg = IC.Background(**u.background['combat'])

        self.exit = Button(self)
        u.Layer.main.append(self.exit)

        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class UnderbellyMapState(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = IC.Background(**u.background['underbelly'])
        self.exit = Button(self)
        u.Layer.main.append(self.exit)

        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    
        # self.bg_town = Town()
        pass

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class CombatState(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = IC.Background(**u.background['combat'])
        self.exit = Button(self)
        u.Layer.main.append(self.exit)

        # self.enemy = BrabaBat()
        # u.Layer.main.append(self.enemy)
        u.Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    
        # self.bg_town = Town()
        pass

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()


class Button(IC.Clickable, IC.DisplayImage): 
    def __init__(self, owner, x=152, y=127, bank=1, u=0, v=0, w=32, h=8, colkey=10) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.owner = owner

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 8, self.y +2, "Town", 7)

    def intersection(self):
        if px.btn(px.MOUSE_BUTTON_LEFT):
            self.owner._next_state = TownScreenState(self.owner.game)