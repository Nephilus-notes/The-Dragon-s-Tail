from time import time
from random import randint as RI
from threading import Timer

import pyxel as px

from old_code.dicts import *
from .image_classes import *
from .utils import *


class CombatText(DisplayImage):
    def __init__(self, combat_state:object, combat_text:str, display_time =2,
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
        # self.end = display_time + self.start
        self.start_draw()
        self.reset_timer()
        # pass in the combat state, the combat end text, and whether the battle was won or not (bool)

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 16, self.y + 16, self.text, 7)
        Interactable.freeze()

        if self.combat_ongoing == False:

            if self.combat_won == False:
                self.game.player.reset_flags()
                if self.game.text_timer >= self.display_time:
                    px.cls(0)

                    self.to_town()


            if self.combat_won:
                if self.game.text_timer >= self.display_time and px.btn(px.MOUSE_BUTTON_LEFT):
                    print(f'CombatText: game explored {self.game.explored} ')
                    if self.game.explored >= 11:
                        # print('to the trees')
                        self.combat_state.to_town()
                    else:
                        # print("going back")
                        self.combat_state.go_back()



        elif self.combat_ongoing == True:
            if self.game.text_timer > self.display_time:
                try:
                    self.game.text.remove(self)
                    print('tried')
                except:
                    pass
                print('need to clear')
                self.clear_message()


    def remove_draw(self):
        # print('removing')
        self.layer.remove(self)

    def start_draw(self):
        self.layer.append(self)

    def reset_timer(self):
        self.game.text_timer = 0

    def to_town(self):
        print('running')
        self.game.player.current_hp = self.game.player.hp
        self.game.player.fleeing = False
        self.combat_state.to_town()
        Interactable.unfreeze()

    def clear_message(self):
        # print('trying to clear')
        self.remove_draw()
        Layer.fore.clear()
        Interactable.unfreeze()