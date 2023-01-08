from time import time
from abc import ABC, abstractmethod
from os.path import join as path_join

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.utils import *

from old_code.npc_classes import *
from .image_classes import *

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
        Layer.back = []
        Layer.main = []
        Layer.fore = []

    def get_next_state(self):
        return self._next_state

    def draw_layers(self):
        # px.cls(Background.color)
        for item in Layer.back:
            item.draw()
        for item in reversed(Layer.main):
            item.draw()
        for item in Layer.fore:
            item.draw()
    
    def check_mouse_position(self):
        for item in Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw_hud(self):
        # Score on top right
        score = str(self.game.score)
        x = WIDTH - len(score) * 4 - 1

    def build_buttons(self):
        self.exit = Button(self)
        self.explore = ExploreButton(self)
        Layer.main.append(self.exit)
        Layer.main.append(self.explore)

    def build_exit(self):
        self.exit = Button(self)
        Layer.main.append(self.exit)

    def build_interactables(self, class_instances:list):
        for instance in class_instances:
            Layer.main.append(instance)
            Interactable.main.append(instance)
            self.name = instance

    def build_sprites(self, class_instances:list):
        for sprite in class_instances:
            Layer.main.append(sprite)

class TownScreenState(GameState):
    def on_enter(self):
        self.clear_layers()

        self.blacksmith = Entrance(ted['Blacksmith'])
        self.alchemist = Entrance(ted["Alchemist's Shop"])
        self.underbelly = Entrance(ted['underbelly'])
        self.inn = Entrance(ted['Inn'])
        self.shining_forest = Entrance(ted['shining_forest'])
        self.build_interactables([ self.blacksmith, 
        self.alchemist, self.inn, self.shining_forest 
        , self.underbelly])

        self.bg = Background(**background['town'])
        Layer.back.append(self.bg)


        self.MOUSE_LOCATION = ''


    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

        pass 
    
    def check_mouse_position(self):
        if self.blacksmith.intersects(self.MOUSE_LOCATION):
            self.blacksmith.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = BlacksmithScreen(self.game) # add shoptoken to dictate which shop it is, also add self.player
        if self.inn.intersects(self.MOUSE_LOCATION):
            self.inn.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = InnScreen(self.game)
        if self.alchemist.intersects(self.MOUSE_LOCATION):
            self.alchemist.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                self._next_state = AlchemistScreen(self.game) # add shoptoken to dictate which shop it is, also add self.player
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

        self.bg = Background(**background['blacksmith'])
        # self.items = []
        for num in range(6):
            item = ShopItem(**item_location[num])
            Layer.main.append(item)
        self.build_exit()


        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

    def check_mouse_position(self):
        for item in Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class AlchemistScreen(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = Background(**background['alchemist'])
        # self.items = []
        for num in range(8,11):
            item = ShopItem(**item_location[num])
            Layer.main.append(item)
        self.build_exit()

        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 
 
    def check_mouse_position(self):
        for item in Layer.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()


class InnScreen(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = Background(**background['inn'])
        self.build_exit()

        Layer.back.append(self.bg)
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


        self.bg = Background(**background['shining_forest'])

        self.build_buttons()

        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()

class UnderbellyMapState(GameState):
    def on_enter(self):
        self.clear_layers()

        self.bg = Background(**background['underbelly'])
        self.build_buttons()
        Layer.back.append(self.bg)
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

        self.bg = Background(**background['combat'])
        self.exit = Button(self)
        Layer.main.append(self.exit)

        self.enemy = ShadeFireFox()
        Layer.main.append(self.enemy)
        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    
        pass

    def update(self):
        pass 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()


class Button(Clickable, DisplayImage): 
    def __init__(self, owner, x=152, y=127, bank=1, u=0, v=0, w=32, h=8, colkey=10) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.owner = owner

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 8, self.y +2, "Town", 7)

    def intersection(self):
        if px.btn(px.MOUSE_BUTTON_LEFT):
            self.owner._next_state = TownScreenState(self.owner.game)

class ExploreButton(Button):
    def __init__(self, owner, x=120, y=72, bank=1, u=0, v=0, w=32, h=8, colkey=10) -> None:
        super().__init__(owner, x, y, bank, u, v, w, h, colkey)
    
    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 2, self.y +2, "Explore", 7)

    def intersection(self):
        if px.btn(px.MOUSE_BUTTON_LEFT):
            self.owner._next_state = CombatState(self.owner.game)