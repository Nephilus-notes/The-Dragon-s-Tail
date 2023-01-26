from random import randint as RI
import pyxel as px

from .character_builder import Character, dex, strength, intelligence
from .dicts import attributes as atb, lvl_dict, currency_tiers, encounter_dict, npc_classes_attributes as npca, attribute_range as AR
from pyxel_code.utils import items as itm
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

    def generate_stats(self):
        print("generating stats")
        self.strength = atb['attribute'][npca[self.class_name]['strength']] + RI(*AR[npca[self.class_name]['strength']])
        self.dexterity = atb['attribute'][npca[self.class_name]['dexterity']] + RI(*AR[npca[self.class_name]['dexterity']])
        self.intelligence = atb['attribute'][npca[self.class_name]['intelligence']] + RI(*AR[npca[self.class_name]['intelligence']])
        self.constitution = atb['attribute'][npca[self.class_name]['constitution']] + RI(*AR[npca[self.class_name]['constitution']])
        self.armor = atb['armor_type'][npca[self.class_name]['armor']] + RI(-1, 1) if atb['armor_type'][npca[self.class_name]['armor']] > 0 else 0
        self.resistance = atb['attribute'][npca[self.class_name]['resistance']] + RI(*AR[npca[self.class_name]['resistance']])

    def replace_4th_ability(self, ability):
        self.abilities[3] = ability

class GraithLizard(NPC, Sprite):
    def __init__ (self, u=32, v=48):
        self.name = "Graith'Gesh Lizard"
        self.class_name = 'graith_lizard'
        self.generate_stats()
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
        self.replace_4th_ability(self.attack)


class GraithQueen(GraithLizard, Sprite):
    def __init__ (self, u=48, v=48):
        self.u=u 
        self.v=v
        super().__init__(self.u, self.v)
        self.class_name = 'graith_queen'
        self.name = "Graith'Gesh Queen"
        self.generate_stats()
        self.hp = self.constitution * 4
        self.max_mp = self.intelligence * 2
        self.set_dependant_atts()
        self.set_currency()

class GraithTree(NPC, Sprite):
    def __init__ (self, u=80, v=48):
        self.name = "Graith'Gesh Tree"
        self.class_name = 'graith_tree'
        self.generate_stats()
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
        self.replace_4th_ability(self.entrap)


    def entrap(self, target):
        attack = self.attack(target)
        if attack[1]:
            perc = RI(0, 1)
            if perc == 1 and target.current_hp > 0:
                self.in_combat_text("You are stunned!")
                target.stun()


class GraithApple(GraithTree, Sprite):
     def __init__ (self, u=96, v=48):
        self.u=u 
        self.v=v
        super().__init__(self.u, self.v)
        self.class_name = 'graith_apple'
        self.name = "Graith'Gesh Apple"
        self.generate_stats()
        self.hp = self.constitution * 4
        self.max_mp = self.intelligence * 2
        self.set_dependant_atts()
        self.set_currency()


class KraktRat(NPC, Sprite):
    def __init__(self, u=16, v=48):
        self.name = "Krakt Rat"
        self.class_name = 'krakt_rat'
        self.generate_stats()
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.replace_4th_ability(self.attack)

class BrabaBat(NPC, Sprite):
    def __init__(self, u=0, v=48):
        self.name = "Braba Bat"
        self.class_name = 'braba_bat'
        self.generate_stats()
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.replace_4th_ability(self.feed)


    def feed(self, target):
        attack = self.attack(target)

        if attack[1]:
            if self.current_hp < self.hp:
                self.current_hp += attack[1]
                self.in_combat_text(f"""{self.name} fed
off you and regained {attack[1]} hp""")
            
            if self.current_hp > self.hp:
                self.current_hp = self.hp


class ShadeFireFox(NPC, Sprite):
    def __init__(self, u=112, v=48):
        self.name = "Shadefire Fox"
        self.class_name = 'shadefire_fox'
        self.generate_stats()
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
        self.replace_4th_ability(self.double_strike)

    def double_strike(self, target):
        self.attack(target)
        self.in_combat_text(f"""{self.name} 
strikes again!""")
        self.attack(target)

    def immolate(self, target):
        # any non magic attacks hurt the attacker for 3 turns 
        # needs a cooldown
        pass

# Gratka stats - low str, mid dex, low int,, low/mid, hp no plus
class GraktaWolf(NPC, Sprite):
    def __init__(self, u=64, v=48):
        self.name = "Gratka Wolf"
        self.class_name = 'gratka_wolf'
        self.generate_stats()
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.replace_4th_ability(self.trip)


    def trip(self, target):
        attack = self.attack(target)
        if attack[1]:
            perc = RI(0, 1)
            if perc == 1 and target.current_hp > 0:
                self.in_combat_text("You are slowed!")
                target.slow()


class VenktathSpider(NPC, Sprite):
    def __init__(self, u=128, v=48):
        self.name = "Ven'ktath Spider"
        self.class_name = 'ven_spider'
        self.generate_stats()
        self.u=u 
        self.v=v
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.replace_4th_ability(self.spider_bite)

    def spider_bite(self, target):
        self.attack(target)

        target.poison()


npc_class_dct = {
   'graith_lizard': GraithLizard,
     'graith_tree': GraithTree,
    'krakt_rat': KraktRat, 
     'braba_bat': BrabaBat,
    'shadefire_fox': ShadeFireFox,
   'gratka_wolf': GraktaWolf,
    'ven_spider': VenktathSpider,
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
