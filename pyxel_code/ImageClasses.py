import pyxel as px 
from abc import ABC, abstractclassmethod
import time

class DisplayImage:
    def __init__(self, x, y, bank, u, v, w, h, colkey=7) -> None:
        self.x = x
        self.y = y
        self.bank = bank
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)

class Sprite(DisplayImage): 
    def __init__(self, u, v, x=96, y=24, bank=2, w=16, h=16) -> None:
        super().__init__(x, y, bank, u, v, w, h)
        self.running= False

    def run(self):
        if self.running == False:
            self.y -= 2
            # // Transforming logic //
            # self.u += 8
            self.running = True
        elif self.running == True:
            self.y += 2
            # // Transforming logic //
            # self.u -= 8
            self.running = False

class Background(DisplayImage):
    def __init__(self,  u, v, bank=0, x=72, y=8, w=128, h=128):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.u = u
        self.v = v
        self.bank = bank

        super().__init__(self.x, self.y, self.bank, self.u, self.v, self.w, self.h)

    def draw(self):
        px.bltm(self.x, self.y, tm=self.bank, u=self.u, v=self.v, w=self.w, h=self.h)

class Clickable:
    def intersects(self, mouse_location:tuple):
        is_intersected = False
        if (
            px.mouse_x > self.x and px.mouse_x < self.x + self.w
            and px.mouse_y > self.y and px.mouse_y < self.y + self.h + 2
        ):
            is_intersected = True
            return is_intersected

    def intersection(self):
        pass

class Sidebar(DisplayImage):
    def __init__(self, x, y, u, v, name, offset, w=64, h=128, bank=0) -> None:
        self.name =name
        self.offset = offset
        super().__init__(x, y,bank, u, v, w, h)

    def draw(self):
        px.bltm(self.x, self.y, tm=self.bank, u=self.u, v=self.v, w=self.w, h=self.h)
        px.text(self.x + self.offset, self.y+8, f'{self.name.title()}', 10)

class Entrance(DisplayImage, Clickable):
    def __init__(self, entrance_dict:dict):
        self.name= entrance_dict['name']
        self.x = entrance_dict['x']
        self.y = entrance_dict['y']
        self.bank = entrance_dict['bank']
        self.u = entrance_dict['u']
        self.v = entrance_dict['v']
        self.w = entrance_dict['w']
        self.h = entrance_dict['h']
        self.colkey = entrance_dict['colkey']
        self.entrance_dict = entrance_dict
        self.color = entrance_dict['color']
        self.offset = entrance_dict['offset']

    
    def intersection(self):
        self.flag = Pointer(self.entrance_dict)
        self.flag.draw()
        px.text(self.x - self.offset, self.y - 24, self.name, self.color)
        # px.blt(ted['Blacksmith']['x'], ted['Blacksmith']['y'] - 16, ted['Blacksmith']['bank'], 
        # ted['Blacksmith']['u'], ted['Blacksmith']['v']-16, ted['Blacksmith']['w'], ted['Blacksmith']['h'], 0)

# class Button(Clickable, DisplayImage): 
#     def __init__(self, x, y, bank, u, v, w, h, owner) -> None:
#         super().__init__(x, y, bank, u, v, w, h)
#     def intersection(self):
#         owner._next_state = BlacksmithScreen(self.game)

class ShopItem(Clickable, DisplayImage):
    def __init__(self, x, y, u, v, w, h, name, bank=2, colkey=7,) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)

        self.name =name

    def intersection(self):
        px.text(84, 84, self.name, 7)


class Rat(Sprite): 
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.u = 32
        self.v = 0
        self.w = 16
        self.h = 16
        super().__init__(x=self.x, y=self.y, bank=0, u=self.u, v= self.v, w=self.w, h=self.h)

class Mouse(Sprite):
    def __init__(self, x, y,u=0) -> None:
        self.u = 8
        super().__init__(x, y, 0, 0, 16, 8, 8)

    
class Pointer(Sprite):
    def __init__(self, entrance_dict:dict) -> None:
        self.x = entrance_dict['x']
        self.y = entrance_dict['y'] - 16
        self.u = entrance_dict['u']
        self.bank = entrance_dict['bank']
        self.v = entrance_dict['v']-16
        self.w = entrance_dict['w']
        self.h = entrance_dict['h']
        self.colkey = 0
        super().__init__(x=self.x, y=self.y, bank=self.bank, u=self.u, v= self.v, w=self.w, h=self.h)
