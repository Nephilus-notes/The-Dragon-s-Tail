from time import time


import pyxel as px

from .image_classes import *
from .utils import *


class CombatText(DisplayImage):
    def __init__(self, combat_state:object, combat_text:str, start_time: float, display_time =2,
    combat_ongoing:bool=True, combat_won:bool = True, x=76, y=84, bank=1, u=0, 
    v=192, w=120, h=56, colkey=7 ) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.combat_won = combat_won
        self.combat_ongoing = combat_ongoing
        self.start = start_time
        self.combat_state = combat_state
        self.game = combat_state.game
        self.text = combat_text
        self.layer = Layer.fore
        self.display_time = display_time
        self.start_draw()
        self.reset_timer()
        # pass in the combat state, the combat end text, and whether the battle was won or not (bool)

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 16, self.y + 16, self.text, 7)

        if self.combat_ongoing == False:
            Interactable.freeze()
            if self.combat_won == False:
                # if self.combat_state.game.player.current_hp > 0:
                #     print('fleeing')
                # else:
                #     print('lost')
                
                if self.game.text_timer >= self.display_time:
                        # self.reset_timer()
                    px.cls(0)
                if self.game.text_timer >= self.display_time:
                    self.game.player.current_hp = self.game.player.hp
                    self.combat_state.to_town()

            if self.combat_won:
                if px.btn(px.MOUSE_BUTTON_LEFT):
                    self.combat_state.go_back()

        elif self.combat_ongoing == True:
            Interactable.freeze()
            if self.game.text_timer >= self.display_time:
                print('2seconds passed')
                self.stop_draw()
                Interactable.unfreeze()


    def stop_draw(self):
        print('removing')
        self.layer.remove(self)

    # def update(self):
    #     Interactable.freeze()
    #     if self.combat_state.text_timer >= 4 and self.combat_ongoing:
    #         Interactable.unfreeze()
    #         self.stop_draw()
        
        # elif self.combat_ongoing == False:


    def start_draw(self):
        self.layer.append(self)

    def reset_timer(self):
        self.game.text_timer = 0
