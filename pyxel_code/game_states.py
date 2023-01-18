from time import time, sleep
from abc import ABC, abstractmethod
from os.path import join as path_join
from random import randint as RI

import pyxel as px

from pyxel_code.constants import *
from pyxel_code.utils import *

from old_code.npc_classes import *
from old_code.character_builder import Player
from .image_classes import *
from pyxel_code.save_level_heal import Save, Level, Rest
from .message_classes import CombatText
from old_code.dicts import background_stats

class GameState(ABC):
    def __init__(self, game):
        self.game = game
        self._next_state = self
        self.game.player.game_state = self
        self.character_info = Sidebar(**sidebar['character_info'])
        self.item_info = Sidebar(**sidebar['items'])
        self.MOUSE_LOCATION = ''
        # self.text_timer = 0
        self.speed = 1.5
        self.time_last_frame = time()
        self.dt = 0
        self._is_clicking = False
        self._register_click = False
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
        self.game.player.bag.draw()

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

                if self.name != 'Combat':
                    if item == self.exit and px.btnr(px.MOUSE_BUTTON_LEFT):
                        # self.go_back()
                        self._next_state = TownScreenState(self.game)

                    if self.name == "The Shining Forest" or self.name == "The Underbelly":
                        if item == self.explore and px.btnr(px.MOUSE_BUTTON_LEFT):
                            self.game._previous_state = self
                            print(f"Entering combat state: {self.game._previous_state.name}")
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
        # print(self.game._previous_state.name)
        # print(f'next state {self._next_state.name}')
        if self.name == "Combat" and self.game._previous_state.name == 'The Shining Forest':
            self.set_previous_state()
            self._next_state = ShiningForestMapState(self.game)
        elif self.name == "Combat" and self.game._previous_state.name == 'The Underbelly':
            self.set_previous_state()
            self._next_state = UnderbellyMapState(self.game)


        # self.trans_state= self.game._previous_state
        # self.game._previous_state = self._next_state
        # self._next_state = self.trans_state

    def to_town(self):
        self._next_state= TownScreenState(self.game)

    def end_game(self):
        self._next_state = EndGameScreen(self.game)

    def is_clicking(self):
        return self._register_click

    def update_clicking_state(self):
        # If not is clicking and mouse is down update is clicking
        if not self._is_clicking and px.btnr(px.MOUSE_BUTTON_LEFT):
            self._is_clicking = True
            self._register_click = True
        # If is clicking and mouse is down should not register as click
        elif self._is_clicking and px.btnr(px.MOUSE_BUTTON_LEFT):
            self._register_click = False
        # Otherwise if is clicking and mouse is not down set is_clicking to false
        else:
            self._is_clicking = False
            self._register_click = False

    def draw(self):
        self.update_clicking_state()
        # px.cls(0)
        self.draw_layers()
        self.check_mouse_position()
        self.game.player.draw_sidebar()
        self.draw_name()
        self.draw_explorer()
        self.display_text()

    def set_previous_state(self):
        self.game._previous_state = self

    def draw_name(self):
        if self.name != 'Combat':
            px.text(73, 1, f"{self.name}", 7)
        
        if self.game.player.exploring == True:
            if self.name == "The Underbelly" or self.name == "The Shining Forest":
                if self.game.explored > 0 and self.game.explored < 3:
                    name = location_names[self.name][0]
                elif self.game.explored >= 3 and self.game.explored < 6:
                    name = location_names[self.name][1]
                elif self.game.explored >= 6 and self.game.explored < 9:
                    name = location_names[self.name][2].format(player = self.game.player.name)
                elif self.game.explored >= 9:
                    name = location_names[self.name][3]
            px.text(168, 1, f"{name}", 7)

    def draw_explorer(self):
        if self.game.player.exploring == True:
            if self.name == "The Underbelly" or self.name == "The Shining Forest":
                if self.game.explored > 0 and self.game.explored < 3:
                    x, y = player_sprite_locations[self.name][0]
                elif self.game.explored >= 3 and self.game.explored < 6:
                    x, y = player_sprite_locations[self.name][1]
                elif self.game.explored >= 6 and self.game.explored < 9:
                    x, y = player_sprite_locations[self.name][2]
                elif self.game.explored >= 9:
                    x, y = player_sprite_locations[self.name][3]
                px.blt(x, y, 2, 8, self.game.player.v, 8, 8, 7)

    def display_text(self):
        if len(self.game.text) > 0:
            # self.game.text_timer = 0
            if self.game.text[-1] != Interactable.unfreeze:
                print('adding unfreeze')
                self.game.text.append(Interactable.unfreeze)

            if self.game.text[0] == Interactable.unfreeze:
                Interactable.unfreeze()
                self.game.text.pop(0)

            else:
                CombatText(**self.game.text[0])

class TitleScreen(GameState):
    def on_enter(self):
        self.clear_layers()
        self.bg = Background(**background['title'])
        Layer.back.append(self.bg)

    def check_mouse_position(self):
        if (px.btnr(px.MOUSE_BUTTON_LEFT) and px.mouse_x > 120 
        and px.mouse_x < 152 and px.mouse_y > 88 and px.mouse_y < 104):
            self._next_state = IntroScreen(self.game)


    def draw(self):
        self.update_clicking_state()
        # self.draw_layers()
        self.bg.draw()
        self.check_mouse_position()
        # self.game.player.draw_sidebar()


class IntroScreen(GameState):
    def on_enter(self):
        self.clear_layers()
        px.cls(0)

    def check_mouse_position(self):
        if px.btnr(px.MOUSE_BUTTON_LEFT):
            self._next_state = ClassChoiceScreen(self.game)    

    def draw(self):
        self.update_clicking_state()
        # self.draw_layers()
        self.check_mouse_position()
        px.text(4, 12, game_text['intro_screen'], 7)
        # self.game.player.draw_sidebar()

class ClassChoiceScreen(GameState):
    def on_enter(self):
        self.clear_layers()
        px.cls(0)
        self.bg = Background(**background['class_choice'])
        self.blacksmith = Player(**background_stats["Nakat'th"]['stats'], game=self.game)
        self.alchemist = Player(**background_stats["Gragta'th"]['stats'], game=self.game)
        self.scavenger = Player(**background_stats[ "Clichtka"]['stats'], game=self.game)
        self.explorer = Player(**background_stats["Bortorb"]['stats'], game=self.game)

        self.options = [self.alchemist, self.blacksmith, self.explorer, self.scavenger]

        for item in self.options:
            Layer.main.append(item)
            Interactable.main.append(item)

    def check_mouse_position(self):
         for item in Interactable.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()

            if px.btnr(px.MOUSE_BUTTON_LEFT):
                if (self.blacksmith.intersects(self.MOUSE_LOCATION)
                 or self.alchemist.intersects(self.MOUSE_LOCATION)
                 or self.explorer.intersects(self.MOUSE_LOCATION)
                 or self.scavenger.intersects(self.MOUSE_LOCATION)):
                    if self.blacksmith.intersects(self.MOUSE_LOCATION):
                        self.game.player = self.blacksmith
                    if self.alchemist.intersects(self.MOUSE_LOCATION):
                        self.game.player = self.alchemist
                    if self.scavenger.intersects(self.MOUSE_LOCATION):
                        self.game.player = self.scavenger
                    if self.explorer.intersects(self.MOUSE_LOCATION):
                        self.game.player = self.explorer

                    px.cls(0)
                    self.game.player.x = 164
                    self.game.player.y = 64
                    self.game.player.u = 0
                    self._next_state = TownScreenState(self.game) 


    def draw(self):
        self.bg.draw()
        self.update_clicking_state()
        self.check_mouse_position()
        for item in Layer.main:
            item.draw()
        # self.game.player.draw_sidebar()

class EndGameScreen(GameState):
    def on_enter(self):
        self.clear_layers()
        px.cls(0)
        px.play(1, 4)
        self.game.text_timer = 0

    def check_mouse_position(self):
        if px.btnr(px.MOUSE_BUTTON_LEFT) and self.game.text_timer > 1:
            self._next_state = CreditsScreen(self.game)

    def draw(self):
        self.update_clicking_state()
        # self.draw_layers()
        self.check_mouse_position()
        px.text(4, 12, game_text['end_game_story'], 7)
        # self.game.player.draw_sidebar()

class CreditsScreen(GameState):
    def on_enter(self):
        self.clear_layers()
        px.cls(0)
        self.game.text_timer = 0

    def check_mouse_position(self):
        if px.btnr(px.MOUSE_BUTTON_LEFT) and self.game.text_timer > 1:
            self._next_state = TownScreenState(self.game)

    def draw(self):
        self.update_clicking_state()
        # self.draw_layers()
        self.check_mouse_position()
        px.text(4, 12, game_text['credit_screen'], 7)
        # self.game.player.draw_sidebar()



class TownScreenState(GameState):
    def on_enter(self):
        self.name = "Town"
        self.clear_layers()

        px.play(1, 0, loop=True)


        self.game.player.exploring = False
        self.bg = Background(**background['town'])
        Layer.back.append(self.bg)

        self.blacksmith = Entrance(self, ted['Blacksmith'])
        self.alchemist = Entrance(self, ted["Alchemist's Shop"])
        self.underbelly = Entrance(self, ted['underbelly'])
        self.inn = Entrance(self, ted['Inn'])
        self.shining_forest = Entrance(self, ted['shining_forest'])
        self.build_interactables([ self.blacksmith, 
        self.alchemist, self.inn, self.shining_forest 
        , self.underbelly])


    
    def check_mouse_position(self):
         for item in Interactable.main:
            if item.intersects(self.MOUSE_LOCATION):
                item.intersection()
            if self.blacksmith.intersects(self.MOUSE_LOCATION) and px.btnr(px.MOUSE_BUTTON_LEFT):
                    self._next_state = BlacksmithScreen(self.game) 

            if self.inn.intersects(self.MOUSE_LOCATION) and px.btnr(px.MOUSE_BUTTON_LEFT):
                    self._next_state = InnScreen(self.game)

            if self.alchemist.intersects(self.MOUSE_LOCATION) and px.btnr(px.MOUSE_BUTTON_LEFT):
                    self._next_state = AlchemistScreen(self.game) 

            if self.underbelly.intersects(self.MOUSE_LOCATION) and px.btnr(px.MOUSE_BUTTON_LEFT):
                    self._next_state = UnderbellyMapState(self.game)

            if self.shining_forest.intersects(self.MOUSE_LOCATION) and px.btnr(px.MOUSE_BUTTON_LEFT):
                    self._next_state = ShiningForestMapState(self.game)



class BlacksmithScreen(GameState):
    def on_enter(self):
        self.name = "Blacksmith"

        self.clear_layers()

        self.bg = Background(**background['blacksmith'])
        self.items = []
        for num in range(6):
            # add logic so you can't buy again
            item = ShopItem(self.game.player, **items[num], id=num)
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
            item = ShopItem(self.game.player, **items[num], id=num)
            self.items.append(item)
        self.build_interactables(self.items)
        self.build_exit()

        Layer.back.append(self.bg)



class InnScreen(GameState):
    def on_enter(self):
        self.name = "Inn"
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
        px.play(1, 3, loop=True)


        self.bg = Background(**background['shining_forest'])
        self.build_buttons()
        Layer.back.append(self.bg)


class UnderbellyMapState(GameState):
    def on_enter(self):
        self.name = "The Underbelly"
        self.clear_layers()
        px.play(1, 1, loop=True)

        self.bg = Background(**background['underbelly'])
        self.build_buttons()
        Layer.back.append(self.bg)


class CombatState(GameState):
    def on_enter(self):
        self.name = "Combat"
        self.clear_layers()
        self.player = self.game.player
        self.bg = Background(**background['combat'])
        px.play(1, 2, loop=True)
        self.round_count = 0
        self.initiative_list = []
        # self.build_exit() # For debugging purposes, MUST DELETE PREPRODUCTION
        self.player_action = ''
        self.player_abilities = []
        Layer.back.append(self.bg)   

        if self.player.exploring == False:
            self.game.explored = 0
            self.player.exploring = True

        self.game.explored += 1
        if self.game.explored == 11 and self.game._previous_state.name == 'The Shining Forest':
            self._next_state = EndGameScreen(self.game)
        print(f"exploring: {self.game.explored}")


        if self.game.explored == 1 or self.game.explored % 3 == 0:
            # text for new areas
            pass

        if self.game.explored == 10 and self.game._previous_state.name == 'The Shining Forest':
            self.enemy = GraithApple()
        else:
            self.enemy = self.choose_enemy()

        Layer.main.append(self.enemy)


        self.check_init()
        self.time_hook()
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
            print(combatant.name)
            if combatant == self.player:
                if self.player_action == 0 or self.player_action == 3:
                    flee_response = combatant.abilities[self.player_action](self.enemy)
                    if self.player.fleeing:
                        return self.add_text("You retreat.\n[Click to Continue]", {"combat_won":False, "combat_ongoing":False})
            
                    
                else:
                    combatant.abilities[self.player_action]()

                # player.    attack                  (enemy)
            elif combatant == self.enemy:
                ability_index = 0# RI(0,2)
                if ability_index == 0:
                    combatant.abilities[ability_index](self.player)
                else:
                    combatant.abilities[ability_index]()
                # sleep(1)
            if self.player.current_hp <= 0:
                return self.add_text("""You lost the battle
Returning to town...\n[Click to Continue]""", {"combat_won":False, "combat_ongoing":False})
            elif self.enemy.current_hp<= 0:
                return self.player_reward()
        self.check_status()
            


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
        if self.enemy.class_name == 'graith_queen':
            self.player.currency += self.enemy.currency
            self.player.lifetime_currency += self.enemy.currency
            scythe = PlayerEquippableItem(self.player, **items[7], id = 7)
            self.player.bag.add_item(scythe)
            return self.add_text(f"""Found trophies: {self.enemy.currency}
Death's Scythe!""", {"combat_ongoing":False})

        elif self.enemy.class_name == 'shadefire_fox':
            self.player.currency += self.enemy.currency
            self.player.lifetime_currency += self.enemy.currency
            bonemail = PlayerEquippableItem(self.player, **items[6], id = 6)
            self.player.bag.add_item(bonemail)
            return self.add_text(f"""Found trophies: {self.enemy.currency}
Bone Armor!""", {"combat_ongoing":False})
        else:
            self.player.currency += self.enemy.currency
            self.player.lifetime_currency += self.enemy.currency

            return self.add_text(f"""Found trophies: {self.enemy.currency}
[Click to Continue]""", {"combat_ongoing":False})

    def check_status(self):
        self.round_inc()
        for combatant in self.initiative_list:
            print(combatant.name)
            if combatant.dodging == True:
                if combatant.dodge_round >= 2:
                    print(combatant.dodge_round)
                    print("still dodging")
                    combatant.undodge()
                            # reset the combatant.dodge so that dodge can be used again.
                else:
                    combatant.dodge_round += 1
                    print(f'dodging for {combatant.dodge_round} rounds')
                    break
            if combatant.defended == True:
                if combatant.defend_round >= 2:
                    combatant.undefend()
                    break
                else:
                    print(f'defended {combatant.defend_round}')
                    combatant.defend_round += 1
                    break

    def draw(self):
        self.draw_layers()
        self.enemy.combat_draw()
        self.player.combat_draw()
        self.check_mouse_position()
        self.player.draw_sidebar()
        self.display_text()

    def choose_enemy(self):
        return encounter_function_list[self.game.explored//3](self.game._previous_state.name)

    def add_text(self:object, text:str, kwarg_dict:dict):
        print(f'Game text length = {len(self.game.text)}')
        print(self.game.text)

        if len(self.game.text) < 1:
            self.game.text.append({'combat_state': self, 'combat_text': text, **kwarg_dict})
        elif len(self.game.text) >= 1:
            if self.game.text[-1] == Interactable.unfreeze:
                print('popping')
                popped = self.game.text.pop()
                self.game.text.append({'combat_state': self, 'combat_text': text, **kwarg_dict})
                self.game.text.append(popped)
            else:
                self.game.text.append({'combat_state': self, 'combat_text': text, **kwarg_dict})
