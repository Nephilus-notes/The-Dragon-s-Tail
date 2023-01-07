import pyxel
from os.path import join

import ImageClasses as images

class ShopController:
    def __init__(self, shoptoken:int):
        self.shoptoken = shoptoken

        pass

    def build_screen(self):
        pyxel.cls(0)
        pyxel.load('shop_screen.pyxres')
        self.shop = images.Shop(bank=self.shoptoken)
        self.shop.draw()

class App:
    def __init__(self):
        pyxel.init(142, 142, title="My Pyxel App", fps=60, display_scale=5)
        pyxel.load(join('assets', 'shop_screen.pyxres'))
        self.MOUSE_LOCATION = ''
        self.shop = images.Background(bank=1)
        self.MOUSE_LOCATION = pyxel.mouse_x, pyxel.mouse_y

        pyxel.run(self.update, self.draw)


    def update(self):
        self.MOUSE_LOCATION = pyxel.mouse_x, pyxel.mouse_y

    def check_mouse_position(self):
        # if self.blacksmith.intersects(self.MOUSE_LOCATION):
        #     self.blacksmith.pointer()
        pass


    def draw(self):
        pyxel.cls(0)

        # // Creating Background

                        # number in question
        # pyxel.bltm(8,8, 1, 0, 0, 128, 128)
        self.shop.draw()
        pyxel.text(40,1, f"{self.shop.bank}", 7)
        pyxel.text(1, 1, f"{self.MOUSE_LOCATION}", 7)


        self.check_mouse_position()

App()