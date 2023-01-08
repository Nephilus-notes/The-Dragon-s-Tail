from random import randint
import pyxel as px

from .character_builder import Character
from .dicts import items as itm, attributes as atb, lvl_dict, currency_tiers
from pyxel_code.image_classes import Sprite

class NPC(Character):
    def __init__(self, name, strength, dexterity, intelligence, constitution, armor, resistance):
        super().__init__(name, strength, dexterity, intelligence, constitution, armor, resistance)        
        self.class_name = self.class_name
        self.set_currency()

    def set_currency(self):
        self.currency = currency_tiers[lvl_dict[self.class_name]] + randint(- lvl_dict[self.class_name], 2* lvl_dict[self.class_name])

    
    def draw(self):
        px.blt(x=self.x, y=self.y, img=self.bank, u=self.u, v=self.v, w=self.w, h=self.h, colkey= self.colkey)
        px.text(74, 10, f"HP:{self.current_hp}/{self.hp}", 7)



class RogueGoblin(NPC):
    def slink(self):
        self.dex += 4
    def __init__ (self):
        self.name = "Rogue Goblin"
        self.class_name = 'rogue_goblin'
        self.strength = atb['strength_range']['weak']
        self.dexterity = atb['dexterity_range']['average']
        self.intelligence = atb['intelligence_range']['weak']
        self.constitution = atb['constitution_range']['weak']
        self.armor = itm['leather_armor']['armor_value']
        self.resistance = atb['resist_range']['weak']
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        self.hp = (self.constitution * 3) 
        self.set_dependant_atts()


# Kratab = RogueGoblin()
# print(Kratab.dexterity)
# print(Kratab.strength)

# ideas of different npc/monster classes
# Graith'gesh lizard - high str, low dex, very low int, average con, hp based on con? con x 2
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

# Graith'gesh trees - high str, low dex, very low int, average to high con, hp x3?
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


# Krakt Rat Stats - low str, average dex, very low int, low con, hp base
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
         # Krakt Rat - a rat that survived and fled down into the tunnels with the Goblins
        # it actually merged with some of the native lizards and began to dominate it's size category
        # growing more aggressive and larger as it did so. They came from the rats that 
        # ate the Goblins' stores when they lived above ground, so had a much faster evolution because of their proximity to magic
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)

#  Braba stats - vw str, low/mid dex, vw int, vw con, no extra hp
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
        # Braba Bat - A vicious bat that lurks in the shadows, using its own brand of magic to avoid the light
        # cast by Goblin skin, and it savagely bites its prey to mark it.  Once the prey is marked, it will often 
        # return to its colony and bring them back to take down the marked prey as a group
        # If I have implimented multiple enemies, this is a great candidate for swarms of 3 +
        # if that's the case their stats have to be super low, but they will also try to flee if there is only one of them in the battle.
        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)

    def feed(self, target):
        # an attack that heals them for half the amount of damage dealt
        pass

# Shadefire Fox - low/mid str, high dex, mid int, mid con, +hp?
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
        # An incredibly rare creature of magic, this fox can utilize fire magic in addition
        # to its fangs and claws when taking down prey. it can also use magic to make itself
        # more stealthy, making it a terrifying foe

        self.x=96
        self.y=24
        self.bank=2
        self.w=16
        self.h=16
        self.colkey=7
        super().__init__(self.name, self.strength, self.dexterity, self.intelligence, self.constitution, self.armor, self.resistance)
        # super(NPC, self).__init__(u=self.u, v =self.v, name=self.name, strength=self.strength, 
        # dexterity=self.dexterity, intelligence=self.intelligence, 
        # constitution=self.constitution, armor=self.armor, resistance=self.resistance, )
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
        # Gratka wolves - wolves that adapted to the Graith'gesh trees, these wolves are seen as 
        # plants by the trees and so are allowed to live. They are characterized by a mound of leaves growing from their shoulders
        # falling like a mane around them. They are formidable foes, either alone or in groups
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
     'rogue_goblin': RogueGoblin,
    'graith_queen': GraithQueen,
    'graith_apple': GraithApple
} 

    # def attribute_gen(self):
    #     self.name = "The goblin"
    #     self.armor = armor_type['leather_armor']
    #     self.resistance = resist_range['weak']
    #     self.strength = strength_range['average']
    #     self.dexterity = dexterity_range['strong']
    #     self.intelligence = intelligence_range['weak']
    #     self.constitution = constitution_range['weak']
    #     self.hp = 4
    #     # self.dodge_val = dexterity_range['strong']
    #     # self.armor_val = armor_type['leather_armor']
    #     # self.dodge_round = 0
    #     # self.defend_round = 0
    #     # self.defended = False
    #     # self.dodging = False
    #     # self.fleeing = False
    #     # self.flee_count = 0

        # if Goblin_warrior not in mob_list:
        #     print("A goblin lunges out of the darkness!")
        # elif mob_list.count(Goblin_warrior) == 1:

        #     print("Another goblin leers from the shadows.")
        # elif mob_list.count(Goblin_warrior) == 2:
        #     print("Another goblin cackles as it draws near!")
        # mob_list.append(Goblin_warrior)