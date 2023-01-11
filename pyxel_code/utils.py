from time import time
from abc import ABC, abstractmethod
from threading import Timer

import pyxel as px

class Runners:
    main = []


class Updatable(ABC):

    updatables = []

    @abstractmethod
    def update(self, dt, t):
        pass

    def start_update(self):
        self.updatables.append(self)

    def stop_update(self):
        self.updatables.remove(self)


class Interactable:
    main = []
    frozen = []

    def freeze():
        Interactable.frozen += Interactable.main
        Interactable.main.clear()

    def unfreeze():
        Interactable.main += Interactable.frozen
        Interactable.frozen.clear()


class Layer:
    back = []  # background
    main = []  # Buildings, Characters
    fore = []  # Projectiles, on hit animations

class SpriteRunners:
    Runners = []

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
    'Blacksmith': {'x': 112, 'y': 48, 'bank': 0, 'u': 0, 'v': 128, 'w': 16, 'h': 16, 'colkey': 0, 'name': 'Blacksmith', 'color': 8, "offset": 10},
    "Alchemist's Shop": {'x': 80, 'y': 80, 'bank': 0, 'u': 16, 'v': 128, 'w': 16, 'h': 16, 'colkey': 0, 'name': 'Alchemist', 'color': 3, "offset": 10},
    "Inn": {'x': 128, 'y': 80, 'bank': 0, 'u': 32, 'v': 128, 'w': 16, 'h': 16, 'colkey': 0, 'name': 'Inn', 'color': 10, "offset": -4},
    "shining_forest": {'x': 176, 'y': 32, 'bank': 0, 'u': 48, 'v': 128, 'w': 16, 'h': 16, 'colkey': 0, 'name': 'Shining Forest', 'color': 7, "offset": 32},
    'underbelly': {'x': 176, 'y': 96, 'bank': 0, 'u': 64, 'v': 128, 'w': 16, 'h': 16, 'colkey': 10, 'name': 'The Underbelly', 'color': 7, "offset": 32},
}

# Background location dict
background = {
    'town': {'u': 256, 'v': 0},
    'blacksmith': {'u': 0, 'v': 0},
    "alchemist": {'u': 128, 'v': 0},
    'inn': {'u': 0, 'v': 384},
    'shining_forest': {'u': 256, 'v': 128},
    'underbelly': {'u': 384, 'v': 128},
    'combat': {'u': 128, 'v': 128}
}

sidebar = {
    'character_info': {'x': 8, 'y': 8,  'u': 0, 'v': 256, 'name': 'Character Info', 'offset': 4},
    'items': {'x': 200, 'y': 8,  'u': 64, 'v': 256, 'name': 'Backpack', 'offset': 16}
}

items = {
    # // WEAPONS //
    0: {'x': 88, 'y': 24, 'u': 0, 'v': 0, 'colkey': 7, 'name': 'Dagger',
        'w': 16, 'h': 16, 'item_stat': 1, 'price': 10, "slot": "hand",
        'description': 
"""          Small dagger

Good for cutting things and 
taking on large rodents."""},

    1: {'x': 120, 'y': 24, 'u': 16, 'v': 0, 'colkey': 7,
        'name': 'Sword', 'w': 16, 'h': 16,
        'item_stat': 3, 'price': 30, "slot": "hand",
        'description': 
"""          Well-made sword 

Used to fight 
many foes."""},
    2: {'x': 152, 'y': 24, 'u': 32, 'v': 0, 'colkey': 7,
        'name': 'Axe', 'w': 16, 'h': 16,
        'item_stat': 4, 'price': 45, "slot": "hand",
        'description': 
"""          Polished axe 

Can easily take chunks 
out of full grown trees."""},
    7: {'x': 1, 'y': 3, 'u': 48, 'v': 0, 'colkey': 7,
        'name': "Death's Scythe", 'w': 16, 'h': 16,
        'item_stat': 15, 'price': 1000, "slot": "hand",
        'description': 
"""          Magical scythe 
Whenever you touch this weapon 
you can hear faint whispers 
all around you."""},

    # // ARMOR //
    3: {'x': 104, 'y': 40, 'u': 0, 'v': 16, 'colkey': 7,
        'name': 'Leather Armor', 'w': 16, 'h': 16,
        'item_stat': 1, 'price': 10, "slot": "body",
        'description': 
"""         Toughened leather 

Protects against
both elements and enemies."""},
    4: {'x': 136, 'y': 40, 'u': 16, 'v': 16, 'colkey': 7,
        'name': 'Chain Armor', 'w': 16, 'h': 16,
        'item_stat': 3, 'price': 50, "slot": "body",
        'description': 
"""           Long steel shirt  

Great protection 
without limiting movement."""},
    5: {'x': 168, 'y': 40, 'u': 32, 'v': 16, 'colkey': 7,
        'name': "Brigandine", 'w': 16, 'h': 16,
        'item_stat': 4, 'price': 75, "slot": "body",
        'description': 
"""           Steel leather 

Unparellelled protection.
Great mobility."""},
    6: {'x': 1, 'y': 3, 'u': 48, 'v': 16, 'colkey': 7,
        'name': 'Bone Mail', 'w': 16, 'h': 16,
        'item_stat': 6, 'price': 150, "slot": "body",
        'description':
"""     Someone's prized posession, 
Armor made from the the bones 
of their ancestors. Stronger than steel 
and very intimidating."""},

    # // POTIONS //
    8: {'x': 104, 'y': 40, 'u': 0, 'v': 32, 'colkey': 7,
        'name': 'Minor Health Potion', 'w': 8, 'h': 8,
        'item_stat': 2, 'price': 10, 'slot': 'consumable', 'description':
"""             Red potion 

Smells of cinnamon and 
nutmeg. Heals a little."""},
    9: {'x': 160, 'y': 40, 'u': 0, 'v': 40, 'colkey': 7,
        'name': 'Health Potion', 'w': 8, 'h': 8,
        'item_stat': 5,
        'price': 20, 'slot': 'consumable', 'description': 
"""             Orange potion 

Smells of mint and orange.  
Heals some health."""},
    10: {'x': 132, 'y': 32, 'u': 8, 'v': 32, 'colkey': 7,
         'name': 'Major Health Potion', 'w': 8, 'h': 8, 'item_stat': 8,
         'price': 50, 'slot': 'consumable', 'description': 
"""             Yellow potion 

Smells of lemon and fresh 
air. Heals a lot!"""},
}

location_names = {
    'The Underbelly': ["Thagrag's Hope", "Web of Depths", "Graith's Grotto", "Graith Queen's Lair"],
    'The Shining Forest': ["Kratab's Folly", "Dripping Death", "{player}'s Respite", 'Tail Of The Dragon']
}

player_sprite_locations = {
    'The Underbelly': [(96, 32), (152, 32), (152, 92), (88, 112)],
    'The Shining Forest': [(128, 88), (144, 48), (168, 16), (184, 16)]
}


# # abstract check mouse position in town into a dictionary so check mouse position can stay the same.
# class GameTimer(object):
#     def __init__(self, interval, function):
#         self._timer     = None
#         self.interval   = interval
#         self.function   = function
#         self.start()

#     def start(self):
#         self._timer = Timer(self.interval, self.function)
#         self._timer.start()

#     # def _run(self):
#     #     self.is_running = False
#     #     self.start()
#     #     self.function(*self.args, **self.kwargs)

#     # def Repeat_start(self):
#     #     if not self.is_running:
#     #         self._timer = Timer(self.interval, self._run)
#     #         self._timer.start()
#     #         self.is_running = True

#     def stop(self):
#         self._timer.cancel()
#         self.is_running = False
