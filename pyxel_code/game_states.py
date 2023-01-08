from time import time
from abc import ABC, abstractmethod
from os.path import join as path_join

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.utils import *

from old_code.npc_classes import *
from .image_classes import *
from pyxel_code.save_level_heal import Save, Level, Rest

class GameState(ABC):
    def __init__(self, game, player):
        self.game = game
        self._next_state = self
        self.on_enter()
        self.player=player
        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])

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
        Interactable.main = []
        Interactable.frozen = []

    def get_next_state(self):
        return self._next_state

    def draw_layers(self):
        Layer.back.append(self.character_info)
        Layer.back.append(self.item_info)
        # px.cls(Background.color)
        for item in Layer.back:
            item.draw()
        for item in reversed(Layer.main):
            item.draw()
        for item in Layer.fore:
            item.draw()
    
    def check_mouse_position(self):
        for item in Interactable.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()
                if item == self.exit and px.btn(px.MOUSE_BUTTON_LEFT):
                    self._next_state = TownScreenState(self.game, self.player)


                if self.name == "Inn":
                    if item == self.rest and px.btn(px.MOUSE_BUTTON_LEFT):
                        self.game.player.current_hp = self.game.player.hp
                        self.game.player.current_mp = self.game.player.max_mp
                        px.text(108, 96, "Health restored", 7) # Add time function on this: 5 secs

                    elif item == self.level and px.btn(px.MOUSE_BUTTON_LEFT):
                        self.strength = self.game.player.strength
                        self.dex = self.game.player.dex
                        self.intelligence = self.game.player.intelligence
                        self.con = self.game.player.constitution
                        
                        px.text(128, 84, "change interactables to frozen, add new interactables", 10) 

                    elif item == self.save and px.btn(px.MOUSE_BUTTON_LEFT):
                        px.text(108, 84, "api call, saved", 7) 

                if self.name == "The Shining Forest" or self.name == "The Underbelly":
                    if px.btn(px.MOUSE_BUTTON_LEFT):
                        self._next_state = CombatState(self.game, self.player)


    def draw_hud(self):
        # Score on top right
        score = str(self.game.score)
        x = WIDTH - len(score) * 4 - 1

    def build_buttons(self):
        self.exit = Button(self)
        self.explore = ExploreButton(self)
        Layer.main.append(self.exit)
        Layer.main.append(self.explore)
        Interactable.main.append(self.exit)
        Interactable.main.append(self.explore)

    def build_exit(self):
        self.exit = Button(self)
        Layer.main.append(self.exit)
        Interactable.main.append(self.exit)

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
        self.name = "Town"
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
                self._next_state = BlacksmithScreen(self.game, self.player) # add shoptoken to dictate which shop it is, also add self.player
        if self.inn.intersects(self.MOUSE_LOCATION):
            self.inn.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = InnScreen(self.game, self.player)
        if self.alchemist.intersects(self.MOUSE_LOCATION):
            self.alchemist.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                self._next_state = AlchemistScreen(self.game, self.player) # add shoptoken to dictate which shop it is, also add self.player
                px.text(1,1, "clicked", 7)
        if self.underbelly.intersects(self.MOUSE_LOCATION):
            self.underbelly.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = UnderbellyMapState(self.game, self.player)
        if self.shining_forest.intersects(self.MOUSE_LOCATION):
            self.shining_forest.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = ShiningForestMapState(self.game, self.player)

    def draw(self):
        # px.cls(0)
        self.draw_layers()
        self.check_mouse_position()
        self.player.draw_sidebar()

class BlacksmithScreen(GameState):
    def on_enter(self):
        self.name = "Blacksmith"

        self.clear_layers()

        self.bg = Background(**background['blacksmith'])
        self.items = []
        for num in range(6):
            item = ShopItem(**item_location[num], id=num)
            self.items.append(item)
        self.build_interactables(self.items)
        self.build_exit()


        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 


    def draw(self):
        self.draw_layers()
        self.check_mouse_position()
        self.game.player.draw_sidebar()

class AlchemistScreen(GameState):
    def on_enter(self):
        self.name = "Alchemist"
        self.clear_layers()

        self.bg = Background(**background['alchemist'])
        self.items = []
        for num in range(8,11):
            item = ShopItem(**item_location[num], id=num)
            self.items.append(item)
        self.build_interactables(self.items)
        self.build_exit()

        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    

    def update(self):
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

    def draw(self):
        self.draw_layers()
        self.check_mouse_position()
        self.player.draw_sidebar()


class InnScreen(GameState):
    def on_enter(self):
        self.name = "Inn"
        print(self.name)
        self.clear_layers()

        self.bg = Background(**background['inn'])
        self.build_exit()
        self.level = Level(self.game.player)
        self.rest = Rest()
        self.save = Save()

        self.build_interactables([self.level, self.rest, self.save])

        Layer.back.append(self.bg)
        self.MOUSE_LOCATION = ''    
        # self.bg_town = Town()
        pass

    def update(self):
        pass 


    def draw(self):
        self.draw_layers()
        self.check_mouse_position()
        self.player.draw_sidebar()

class ShiningForestMapState(GameState):
    def on_enter(self):
        self.name = "The Shining Forest"
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
        self.player.draw_sidebar()

class UnderbellyMapState(GameState):
    def on_enter(self):
        self.name = "The Underbelly"
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
        self.player.draw_sidebar()

class CombatState(GameState):
    def on_enter(self):
        self.name = "Combat"
        self.clear_layers()
        self.bg = Background(**background['combat'])
        self.build_exit() # For debugging purposes, MUST DELETE PREPRODUCTION

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
        self.player.draw_sidebar()

