from random import randint as RI
import pyxel as px

from .character_builder import Character
from .dicts import items as itm, attributes as atb, lvl_dict, currency_tiers, encounter_dict
from pyxel_code.image_classes import Sprite

class NPC(Character):
    def __init__(self, name, strength, dexterity, intelligence, constitution, armor, resistance):
        super().__init__(name, strength, dexterity, intelligence, constitution, armor, resistance)        
        self.class_name = self.class_name
        self.set_currency()

    def set_currency(self):
        self.currency = currency_tiers[lvl_dict[self.class_name]] + RI(- lvl_dict[self.class_name], 2* lvl_dict[self.class_name])

    
    def draw(self):
        px.blt(x=self.x, y=self.y, img=self.bank, u=self.u, v=self.v, w=self.w, h=self.h, colkey= self.colkey)
        px.text(74, 10, f"HP:{self.current_hp}/{self.hp}", 7)

class GraithLizard(NPC, Sprite):
    def __init__ (self, u=32, v=48):
        self.name = "Graith'Gesh Lizard"
        self.class_name = 'graith_lizard'
        self.strength = atb['strength_range']['strong']
        self.dexterity = atb['dexterity_range']['weak']
        self.intelligence = atb['intelligence_range']['very_weak']
        self.constitution = atb['constitution_range']['average']
        self.armor = atb['armor_type']['brigandine']
        self.resistance = atb['resist_range']['weak']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = self.constitution * 4
        self.set_dependant_atts()


class GraithQueen(NPC, Sprite):
    def __init__ (self, u=48, v=48):
        self.class_name = 'graith_queen'
        self.name = "Graith'Gesh Queen"
        self.strength = atb['strength_range']['very_strong']
        self.dexterity = atb['dexterity_range']['strong']
        self.intelligence = atb['intelligence_range']['very_weak']
        self.constitution = atb['constitution_range']['strong']
        self.armor = atb['armor_type']['bone']
        self.resistance = atb['resist_range']['average']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = self.constitution * 4
        self.set_dependant_atts()

class GraithTree(NPC, Sprite):
    def __init__ (self, u=80, v=48):
        self.name = "Graith'Gesh Tree"
        self.class_name = 'graith_tree'
        self.strength = atb['strength_range']['strong']
        self.dexterity = atb['dexterity_range']['weak']
        self.intelligence = atb['intelligence_range']['very_weak']
        self.constitution = atb['constitution_range']['strong']
        self.armor = atb['armor_type']['brigandine']
        self.resistance = atb['resist_range']['weak']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = self.constitution * 4
        self.set_dependant_atts()

    def entrap(self, target):
        # uses its branches to attack adn try to trap the target
        # less chance of hitting, but if it does hit chance to stun and 
        # raise a stunned flag on the target, disabling them from taking action the next turn
        pass

class GraithApple(NPC, Sprite):
     def __init__ (self, u=96, v=48):
        self.class_name = 'graith_apple'
        self.name = "Graith'Gesh Apple Tree"
        self.strength = atb['strength_range']['strong']
        self.dexterity = atb['dexterity_range']['very_strong']
        self.intelligence = atb['intelligence_range']['average']
        self.constitution = atb['constitution_range']['very_strong']
        self.armor = atb['armor_type']['brigandine']
        self.resistance = atb['resist_range']['weak']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = self.constitution * 4
        self.set_dependant_atts()

class KraktRat(NPC, Sprite):
    def __init__(self, u=16, v=48):
        self.name = "Krakt Rat"
        self.class_name = 'krakt_rat'
        self.strength = atb['strength_range']['very_weak']
        self.dexterity = atb['dexterity_range']['average']
        self.intelligence = atb['intelligence_range']['very_weak']
        self.constitution = atb['constitution_range']['weak']
        self.armor = atb['armor_type']['none']
        self.resistance = atb['resist_range']['average']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        print(self.name)
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        print(f'dex = {self.dexterity}')

class BrabaBat(NPC, Sprite):
    def __init__(self, u=0, v=48):
        self.name = "Braba Bat"
        self.class_name = 'braba_bat'
        self.strength = atb['strength_range']['very_weak']
        self.dexterity = atb['dexterity_range']['average']
        self.intelligence = atb['intelligence_range']['very_weak']
        self.constitution = atb['constitution_range']['weak']
        self.armor = atb['armor_type']['none']
        self.resistance = atb['resist_range']['average']
        self.u=u 
        self.v=v
        # If I have implimented multiple enemies, this is a great candidate for swarms of 3 +
        # if that's the case their stats have to be super low, but they will also try to flee if there is only one of them in the battle.
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        print(self.name)

        print(f'dex = {self.dexterity}')


    def feed(self, target):
        # an attack that heals them for half the amount of damage dealt
        pass


class ShadeFireFox(NPC, Sprite):
    def __init__(self, u=112, v=48):
        self.name = "Shadefire Fox"
        self.class_name = 'shadefire_fox'
        self.strength = atb['strength_range']['average']
        self.dexterity = atb['dexterity_range']['very_strong']
        self.intelligence = atb['intelligence_range']['average']
        self.constitution = atb['constitution_range']['average']
        self.armor = atb['armor_type']['chain']
        self.resistance = atb['resist_range']['strong']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = self.constitution * 4
        self.set_dependant_atts()


    def immolate(self, target):
        # any non magic attacks hurt the attack for 3 turns 
        # needs a cooldown
        pass

# Gratka stats - low str, mid dex, low int,, low/mid, hp no plus
class GraktaWolf(NPC, Sprite):
    def __init__(self, u=64, v=48):
        self.name = "Gratka Wolf"
        self.class_name = 'gratka_wolf'
        self.strength = atb['strength_range']['weak']
        self.dexterity = atb['dexterity_range']['average']
        self.intelligence = atb['intelligence_range']['weak']
        self.constitution = atb['constitution_range']['average']
        self.armor = atb['armor_type']['leather']
        self.resistance = atb['resist_range']['weak']
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)

    def trip(self, target):
        # decreases targets dodge value for 2/3 turns
        # needs a cooldown
        pass




npc_class_choice = {
    1: 'graith_lizard',
    2: 'graith_tree',
    3: 'krakt_rat', 
    4: 'braba_bat',
    5: 'shadefire_fox',
    6: 'gratka_wolf',
    7: 'rogue_goblin',
    8: 'graith_queen',
    9: 'graith_apple'
}

npc_class_dct = {
   'graith_lizard': GraithLizard,
     'graith_tree': GraithTree,
    'krakt_rat': KraktRat, 
     'braba_bat': BrabaBat,
    'shadefire_fox': ShadeFireFox,
   'gratka_wolf': GraktaWolf,
    #  'rogue_goblin': RogueGoblin,
    'graith_queen': GraithQueen,
    'graith_apple': GraithApple
} 


def lvl1_encounter(location:str):
    percentile_roll = RI(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 50:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 50 and percentile_roll <= 95:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 95:
        enemy_class = npc_class_dct[encounter_dict[location][3]]
    return enemy_class()

def lvl2_encounter(location:str):
    percentile_roll = RI(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 30:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 30 and percentile_roll <= 60:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 60:
        enemy_class = npc_class_dct[encounter_dict[location][3]]

    return enemy_class()

def lvl3_encounter(location:str):
    percentile_roll = RI(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 10:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 10 and percentile_roll <= 25:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 25:
        enemy_class = npc_class_dct[encounter_dict[location][3]]

    return enemy_class()

def lvl4_encounter(location:str):
    percentile_roll = RI(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 1:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 1 and percentile_roll <= 80:
        enemy_class = npc_class_dct[encounter_dict[location][4]]
    elif percentile_roll > 80:
        enemy_class = npc_class_dct[encounter_dict[location][6]]

    return enemy_class()

encounter_function_list = [lvl1_encounter, lvl2_encounter, lvl3_encounter, lvl4_encounter]
