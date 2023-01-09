from time import time, sleep
from abc import ABC, abstractmethod
from os.path import join as path_join
from random import randint as RI

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.utils import *

from old_code.npc_classes import *
from .image_classes import *
from pyxel_code.save_level_heal import Save, Level, Rest
from .combat_classes import CombatText

class GameState(ABC):
    def __init__(self, game):
        self.game = game
        self._next_state = self
        # self.trans_state = self
        # self.game._previous_screen = self
        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])
        self.MOUSE_LOCATION = ''
        self.speed = 1.5
        self.time_last_frame = time()
        self.dt = 0
        # self.time_since_last_move = 0
        self.text_timer = 0
        self.on_enter()


    @abstractmethod
    def on_enter(self):
        pass


    def update(self): #dt, t = time variables
        self.MOUSE_LOCATION = px.mouse_x, px.mouse_y 

        time_this_frame = time()
        self.dt = time_this_frame - self.time_last_frame
        self.time_last_frame = time_this_frame
        self.game.text_timer += self.dt


        # add sprites to running class list and check to make them move

        

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
                    # self.go_back()
                    self._next_state = TownScreenState(self.game)


                # if self.name == "Inn":
                #     if px.btn(px.MOUSE_BUTTON_LEFT):
                #         print("in the inn")
                #         if item == self.rest:
                #             self.game.player.current_hp = self.game.player.hp
                #             self.game.player.current_mp = self.game.player.max_mp
                #             px.text(108, 96, "Health restored", 7) # Add time function on this: 5 secs

                #         elif item == self.level:
                #             self.strength = self.game.player.strength
                #             self.dex = self.game.player.dex
                #             self.intelligence = self.game.player.intelligence
                #             self.con = self.game.player.constitution
                            
                #             px.text(128, 84, "change interactables to frozen, add new interactables", 10) 

                #         elif item == self.save:
                #             px.text(108, 84, "api call, saved", 7) 

                if self.name == "The Shining Forest" or self.name == "The Underbelly":
                    if item == self.explore and px.btn(px.MOUSE_BUTTON_LEFT):
                        self.game._previous_screen = self
                        print(f"Entering combat state: {self.game._previous_screen.name}")
                        self._next_state = CombatState(self.game)


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

    def build_sprites(self, class_instances:list):
        for sprite in class_instances:
            Layer.main.append(sprite)

    def go_back(self):
        # print(self.game._previous_screen.name)
        # print(f'next state {self._next_state.name}')
        if self.name == "Combat" and self.game._previous_screen.name == 'Shining Forest':
            # print('back from shining forest')
            self.set_previous_state()
            self._next_state = ShiningForestMapState(self.game)
        elif self.name == "Combat" and self.game._previous_screen.name == 'The Underbelly':
            # print('back from underbelly')
            self.set_previous_state()
            self._next_state = UnderbellyMapState(self.game)


        # self.trans_state= self.game._previous_screen
        # self.game._previous_screen = self._next_state
        # self._next_state = self.trans_state

    def to_town(self):
        self._next_state= TownScreenState(self.game)

    def draw(self):
        # px.cls(0)
        self.draw_layers()
        self.check_mouse_position()
        self.game.player.draw_sidebar()

    def set_previous_state(self):
        self.game._previous_screen = self

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

    
    def check_mouse_position(self):
        if self.blacksmith.intersects(self.MOUSE_LOCATION):
            self.blacksmith.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = BlacksmithScreen(self.game) 
        if self.inn.intersects(self.MOUSE_LOCATION):
            self.inn.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                px.text(1,1, "clicked", 7)
                self._next_state = InnScreen(self.game)
        if self.alchemist.intersects(self.MOUSE_LOCATION):
            self.alchemist.intersection()
            if px.btn(px.MOUSE_BUTTON_LEFT):
                self._next_state = AlchemistScreen(self.game) 
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



class InnScreen(GameState):
    def on_enter(self):
        self.name = "Inn"
        print(self.name)
        self.clear_layers()

        self.bg = Background(**background['inn'])
        self.build_exit()
        self.level = Level(self.game.player)
        self.rest = Rest(self.game.player)
        self.save = Save(self.game.player)

        self.build_interactables([self.level, self.rest, self.save])

        Layer.back.append(self.bg)


class ShiningForestMapState(GameState):
    def on_enter(self):
        self.name = "The Shining Forest"
        self.clear_layers()


        self.bg = Background(**background['shining_forest'])

        self.build_buttons()

        Layer.back.append(self.bg)


class UnderbellyMapState(GameState):
    def on_enter(self):
        self.name = "The Underbelly"
        self.clear_layers()

        self.bg = Background(**background['underbelly'])
        self.build_buttons()
        Layer.back.append(self.bg)


class CombatState(GameState):
    def on_enter(self):
        self.name = "Combat"
        self.clear_layers()
        self.bg = Background(**background['combat'])
        self.round_count = 0
        self.initiative_list = []
        self.build_exit() # For debugging purposes, MUST DELETE PREPRODUCTION
        self.player = self.game.player
        self.player_action = ''
        self.player_abilities = []
        self.enemy = KraktRat()
        self.time_hook()
        Layer.main.append(self.enemy)
        Layer.back.append(self.bg)    
        self.check_init()

        self.build_action_buttons()
        
    def clear_action_list(self):
        self.action = ''

    def build_action_buttons(self):
        for index, ability in enumerate(self.player.abilities):
            self.player_abilities.append(AbilityButton(self, index, self.player))
        self.build_interactables(self.player_abilities)

    def take_actions(self):
        start_time = time()

        for combatant in self.initiative_list:
            if combatant == self.player:
                if self.player_action == 0 or self.player_action == 3:
                    flee_response = combatant.abilities[self.player_action](self.enemy)
                    if self.player.fleeing:
                        return CombatText(self, "You retreat in character.", time(), combat_won=False, combat_ongoing=False)
            
                    
                else:
                    combatant.abilities[self.player_action]()

                # player.    attack                  (enemy)
            elif combatant == self.enemy:
                ability_index = RI(0,2)
                if ability_index == 0:
                    combatant.abilities[ability_index](self.player)
                else:
                    combatant.abilities[ability_index]()
                print('enemy action')
                sleep(1)
            if self.player.current_hp <= 0:
                return CombatText(self, """You lost the battle
Return to town for healing...""", time(), combat_ongoing=False, combat_won=False)
            elif self.enemy.current_hp<= 0:
                return self.player_reward()
            


    def check_init(self):
        # compare the dex to the character in the 0 slot, and instert if their dex is lower. else, look at the next index and repeat the process.
        if self.player.dexterity >= self.enemy.dexterity:
            self.initiative_list = [self.player, self.enemy]
            # The player sees an enemy
        else:
            self.initiative_list = [self.enemy, self.player]
            # the player is ambushed by something 

    def time_hook(self):
        self.player.game = self.game
        self.player.combat_state = self
        self.enemy.game = self.game
        self.enemy.combat_state = self
    
    def round_inc(self):
        self.round_count += 1

    def player_reward(self):
        # display how much you got and increment player currency and lifetime_currency
        # print(f"You found trophies worth { self.enemy.currency } ")
        self.player.currency += self.enemy.currency
        self.player.lifetime_currency += self.enemy.currency
        return CombatText(self, f"""Found trophies: {self.enemy.currency}
[Press Enter]""", time(), combat_ongoing=False)

    def check_status(self):
        self.round_inc()
        for player in self.initiative_list:
            while player.dodging == True:
                if player.dodge >= 2:
                    player.dodging = False
                    player.undodge()
        # reset the player.dodge so that dodge can be used again.
                    break
                else:
                    player.dodge_round += 1
                    # print("dodge + 1!")
                    # print(player.dodge_round)
                    break
            while player.defended == True:
                if player.defend_round >= 2:
                    player.defended = False
                    player.undefend()
                    break
                else:
                    player.defend_round += 1
                    break
            # while player.fleeing == True:
            #     return CombatText(self, "You run away in game states", time(), combat_won=False, combat_ongoing=False)

    def draw(self):
        self.draw_layers()
        self.enemy.combat_draw()
        self.player.combat_draw()
        self.check_mouse_position()
        self.player.draw_sidebar()

