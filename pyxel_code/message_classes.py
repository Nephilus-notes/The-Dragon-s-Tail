from time import time
from random import randint as RI
from threading import Timer

import pyxel as px

from old_code.dicts import *
from .image_classes import *
from .utils import *


class CombatText(DisplayImage):
    def __init__(self, combat_state:object, combat_text:str, display_time:float=1.5,
    combat_ongoing:bool=True, combat_won:bool = True, x=76, y=84, bank=1, u=0, 
    v=192, w=120, h=48, colkey=7 ) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.combat_won = combat_won
        self.combat_ongoing = combat_ongoing
        self.combat_state = combat_state
        self.game = combat_state.game
        self.text = combat_text
        self.layer = Layer.fore
        self.display_time = display_time
        self.start_draw()
        self.reset_timer()
        # print("combat text created")

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 8, self.y + 16, self.text, 7)
        Interactable.freeze()


        if self.combat_ongoing == False:

            if self.combat_won == False:
                # print('getting out of here')
                if px.btnr(px.MOUSE_BUTTON_LEFT):
                    # print(self.game.text_timer)
                    self.game.player.set_dependant_atts()
                    self.game.player.reset_flags()
                    # print(self.display_time)
                    px.cls(0)

                    self.remove_self()
                    self.to_town()


            if self.combat_won:
                # print('combat won!')
                # print(self.game.text_timer)
                # print(self.display_time)
                if px.btnr(px.MOUSE_BUTTON_LEFT):
                    # print(f'CombatText: game explored {self.game.explored} ')
                    self.game.player.set_combat_atts()
                    self.game.player.reset_flags()
                    if self.game.explored >= 11:
                        # print('to the trees')
                        try:
                            self.remove_self()
                        except:
                            print('popped once too many times')
                        self.combat_state.to_town()
                    else:
                        # print("going back")
                        try:
                            self.remove_self()
                        except:
                            print('popped once too many times')
                        self.combat_state.go_back()



        elif self.combat_ongoing == True:
            # print("combat ongoing")
            # print(self.game.text_timer)
            # print(self.display_time)
            if self.game.text_timer > self.display_time:
                # try:
                self.remove_self()
                # print('tried')

                # except:
                    # print("failed to clear")
                self.clear_message()


    def remove_self(self):
        # print('removing')
        # print('resetting timer')
        self.reset_timer()
        # print(self.game.text_timer)
        self.game.text.pop(0)
        Layer.fore.clear()
        Interactable.unfreeze()

    
    def clear_message(self):
        # print('trying to clear')
        Layer.fore.clear()
        Interactable.unfreeze()

    def start_draw(self):
        self.layer.append(self)

    def reset_timer(self):
        if self.game.text_timer > self.display_time:
            self.game.text_timer = 0

    def to_town(self):
        # print('running')
        self.game.player.current_hp = self.game.player.hp
        self.game.player.fleeing = False
        self.combat_state.to_town()
        Interactable.unfreeze()
