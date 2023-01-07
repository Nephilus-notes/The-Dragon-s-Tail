from time import time
from abc import ABC, abstractmethod

import pyxel as px

class Updatable(ABC):

    updatables = []

    @abstractmethod
    def update(self, dt, t):
        pass

    def start_update(self):
        self.updatables.append(self)

    def stop_update(self):
        self.updatables.remove(self)


class Layer:
    back = []  # background
    main = []  # Buildings, Characters
    fore = []  # Projectiles, on hit animations


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    def set_draw_layer(self, layer: Layer):
        if hasattr(self, "layer") and self in self.layer:
            self.stop_draw()
        self.layer = layer
        self.start_draw()

    def start_draw(self):
        self.layer.append(self)

    def stop_draw(self):
        self.layer.remove(self)


# Entrance image dict
ted = {
    'Blacksmith': { 'x':112, 'y': 48, 'bank': 0, 'u': 0, 'v': 128, 'w':16, 'h':16, 'colkey': 0, 'name': 'Blacksmith', 'color': 8, "offset": 10},
    "Alchemist's Shop": {'x':80, 'y': 80, 'bank': 0, 'u': 16, 'v': 128, 'w':16, 'h':16, 'colkey': 0, 'name': 'Alchemist', 'color': 3, "offset": 10},
    "Inn": {'x':128, 'y': 80, 'bank': 0, 'u': 32, 'v': 128, 'w':16, 'h':16, 'colkey': 0, 'name': 'Inn', 'color': 10, "offset": -4},
    "shining_forest": {'x':176, 'y': 32, 'bank': 0, 'u': 48, 'v': 128, 'w':16, 'h':16, 'colkey': 0, 'name': 'Shining Forest', 'color': 7, "offset": 32},
    'underbelly': {'x':176, 'y': 96, 'bank': 0, 'u': 64, 'v': 128, 'w':16, 'h':16, 'colkey': 10, 'name': 'The Underbelly', 'color': 7, "offset": 32},
}

# Background location dict
background = {
    'town': {'u':256, 'v':0},
    'blacksmith': {'u':0, 'v':0},
    "alchemist": {'u':128, 'v':0},
    'inn': {'u': 0, 'v': 384 },
    'shining_forest': {'u': 256, 'v': 128},
    'underbelly':{'u': 384, 'v': 128},
    'combat': {'u': 128, 'v': 128}
}

sidebar = {
    'character_info': {'x':8, 'y': 8,  'u': 0, 'v': 256, 'name': 'Character Info', 'offset':4},
    'items': {'x':200, 'y': 8,  'u': 64, 'v': 256, 'name': 'Backpack', 'offset': 16}
}

item_location = [
     {'x': 88, 'y': 24, 'u':0, 'v':0, 'colkey': 7, 'name': 'Dagger', 'w': 16, 'h': 16},
     {'x': 120, 'y': 24, 'u': 16, 'v':0, 'colkey': 7, 'name': 'Sword', 'w': 16, 'h':16 },
     {'x': 152, 'y': 24, 'u': 32, 'v':0, 'colkey': 7, 'name': 'Axe', 'w':16 , 'h':16 },
     {'x': 104, 'y': 40, 'u':0, 'v':16, 'colkey': 7, 'name': 'Leather Armor', 'w':16 , 'h': 16},
     {'x': 136, 'y': 40, 'u': 16, 'v':16, 'colkey': 7, 'name': 'Chain Armor', 'w':16 , 'h':16 },
     {'x': 168, 'y': 40, 'u': 32, 'v':16, 'colkey': 7, 'name': "Brigandine", 'w':16 , 'h':16 },
     {'x': 1, 'y':3, 'u': 48, 'v':16, 'colkey': 7, 'name': 'Bone Mail' , 'w':16 , 'h': 16},
     {'x': 1, 'y':3, 'u': 48, 'v':0, 'colkey': 7, 'name': "Death's Scythe", 'w':16 , 'h':16 },
     {'x': 104, 'y': 40, 'u':0, 'v':32, 'colkey': 7, 'name': 'Small Health Potion', 'w':8 , 'h':8 },
     {'x': 160, 'y': 40, 'u':0, 'v':40, 'colkey': 7, 'name': 'Medium Health Potion', 'w':8 , 'h':8 },
     {'x': 132, 'y': 32, 'u':8, 'v':32, 'colkey': 7, 'name': 'Large Health Potion', 'w':8 , 'h':8 },
]

# abstract check mouse position in town into a dictionary so check mouse position can stay the same.