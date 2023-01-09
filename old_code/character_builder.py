from random import randint
from time import time, sleep
import json
import pyxel as px


from pyxel_code.combat_classes import CombatText
from .dicts import items as itm # Application Imports
from .dicts import * # Application Imports
from .item_screen import EquippedItems, Backpack # Application Imports
from pyxel_code.image_classes import Sprite, DisplayText # Application Imports

# from ..pyxel_code.image_classes import Sprite # Test Import Path





rirs = randint(0,1) # randint small (0,1)
rirm = randint(-1,1) # randint medium (-1,1)
nrn = randint(0,2)



class Character():
    def __init__ (self, name, strength, dexterity, intelligence, constitution, armor=0, resistance=0):
        self.name = name
        # Items
        self.lifetime_currency = 0
        self.currency = 0
        self.bag = Backpack()
        self.items_worn = EquippedItems(self.bag)

    #    Stats and whatnot
        self.armor = armor # 0 if self.items_worn.placement['slot']['body'] == {'nothing':'nothing'} else itm[self.items_worn.placement['slot']['body']['armor_value']]
        self.resistance = resistance
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.constitution = constitution
        self.hp = self.constitution * 2
        self.max_mp = self.intelligence * 2
        self.weapon = {}  if self.items_worn.placement['slot']['hand'] == {'nothing':'nothing'} else itm[self.items_worn.placement['slot']['hand']]
        self.weapon_damage = self.weapon['damage'] if 'damage' in self.weapon else 0
        self.damage = strength // 2 + self.weapon_damage if strength > 2 else 1 + self.weapon_damage
        self.attribute_list = []
        # self.level = 1

        # Ability list
        self.abilities = []
        self.abilities.append(self.attack)
        self.abilities.append(self.dodge)
        self.abilities.append(self.defend)
        self.abilities.append(self.flee)
        
        # // Persistent changed stats //
        self.current_hp = self.hp
        self.current_mp = self.max_mp        

        

        #  //  Temp Stat changes //
        self.armor_val = armor
        self.att_val = self.dexterity // 2 if self.dexterity >= self.strength else self.strength // 2
        self.damage_val = self.damage
        self.dodge_val = dexterity // 2 if dexterity > 2 else 1
        self.resist_val = self.resistance

        

        
        # // STATUSES //
        # Status flags
        self.defended = False  #incrementer
        self.dodging = False    # Incrementor
        self.fleeing = False    # Incrementor
        self.stone_armored = False  # Incrementor
        self.slowed = False         # Incrementor
        self.vulnerable = False     # Incrementor
        self.double_armed = False  # Incrementor
        self.burning_blades = False # Incrementor = damage = magic
        self.stone_fists = False # Incrementor = Bonus damage

        # No incrementors/counters
        self.poisoned = False       
        self.burning = False
        self.wind_hit_by = False 
        self.stunned = False        

        #  Status Incrementors
        self.dodge_round = 0
        self.defend_round = 0
        self.flee_count = 0
        self.set_attribute_list()
        # self.set_currency()

        self.game = None
        self.combat_state = None
        print(self.att_val, self.damage_val)


    def attack(self, target):
        self.in_combat_text(f'{self.name.title()} lashes out at {target.name.title()}!')

        if self.dexterity > self.strength:
            if attack_randint['dex'] == 2:
                damage_num = (self.damage + 2)
                self.in_combat_text('**Critical hit!**')
                self.attack_damage(target, damage_num)
            elif self.att_val + attack_randint['dex'] <= target.dodge_val:
                self.in_combat_text(f"{self.name.title()}'s missed!")
            elif self.att_val + attack_randint['dex'] > target.dodge_val:
                damage_num = (self.damage + attack_randint['dex']) - target.armor_val
                self.attack_damage(target, damage_num)

        elif self.strength >= self.dexterity:
            if attack_randint['str'] == 4:
                damage_num = (self.damage + 4) - target.armor_val
                self.in_combat_text('**Critical hit!**')
                self.attack_damage(target, damage_num)
            elif self.att_val + attack_randint['str'] <= target.dodge_val:
                self.in_combat_text (f'{self.name.title()} missed!')
            elif self.att_val + attack_randint['str'] > target.dodge_val:
                damage_num = (self.damage + attack_randint['str']) - target.armor_val
                self.attack_damage(target, damage_num)


    def attack_damage(self, target, damage_num):
            if damage_num > 0:
                CombatText(self.combat_state, f'{self.name.title()} has hit {target.name.title()} for {str(damage_num)} damage!', time())
                target.current_hp -= damage_num
                if target.current_hp <= 0:
                    target.current_hp = 0
                #     self.in_combat_text(f"\n{target.name.title()} has been defeated.")
                #     # del target
            elif damage_num <= 0 and target.name[-1] != "s":
                self.in_combat_text(f"{target.name.title()} blocks {self.name.title()}' strike.")
            elif damage_num <= 0 and target.name[-1] == "s":
                self.in_combat_text(target.name.title(), 'blocks', self.name.title() + "'s strike.")
                

    def wear_armor(self):
        self.armor = 0 if self.items_worn.placement['slot']['body'] == 'nothing' else itm[self.items_worn.placement['slot']['body']['armor_value']]
        self.armor_val = self.armor

    def defend(self):
        self.armor_val = self.armor + 2
        self.defended = True
        if self.class_name == 'player':
            self.in_combat_text(f"""You focus on defending. Armor: {self.armor_val}""")
        else:
            self.in_combat_text(f'''The { self.combat_state.enemy} hunkers down to defend.''')
        # rnd_count = 2

    def undefend(self):
        self.armor_val = self.armor
        if self.class_name != 'player':
            self.in_combat_text(f'''The { self.combat_state.enemy} relaxes their guard.''')

    def dodge(self):
        self.dodging = True
        self.dodge_val = self.dexterity + 2
        if self.class_name == 'player':
            self.in_combat_text(f"""You focus on defending. dodging: {self.dodge_val}""")
        else:
            self.in_combat_text(f'''The { self.combat_state.enemy} hunkers down to defend.''')
        # rnd_count = 2

    def undodge(self):
        self.dodge_val = self.dexterity

    def flee(self, enemy):
        if self.dexterity > enemy.dexterity or self.flee_count > 0:            
            self.fleeing = True
        else:
            self.flee_count += 1
            self.in_combat_text(f'You try to run from {enemy}')
            return False

    def __repr__(self):
        return self.name.title()

    def stone_armor(self):
        self.armor_val = self.armor + 2
        self.stone_armored = True
        print(f"You cast a spell to boost your armor. Armor: {self.armor_val}")

    def slow(self):
        if self.slowed:
            print(f"{self.name} is already slowed")
        else:
            self.dodge_val -= 2
            self.slowed = True
            print(f"{self.name} is slowed")

    def vulnerability(self):
        if self.vulnerable:
            print(f"{self.name} is already vulnerable.")
        else:
            self.resist_val -= 2
            self.vulnerable = True
            print(f"{self.name} is now vulnerable to magic.")

    def stone_armor_2(self):
        self.armor_val = self.armor + 4
        self.double_armed = True
        print(f"You cast a spell to boost your armor. Armor: {self.armor_val}")

    def damage_to_magic(self):
        # alter the attack action to add default parameters that can be over written
        pass

    def stony_fists(self):
        self.stone_fists = True
        self.damage_val = self.damage + 4
        print(f"You cast a spell to boost your damage. Damage: {self.damage_val}")

    def poison(self):
        if self.poisoned:
            print(f"{self.name} is already poisoned!")
        else:
            self.poisoned = True
            print(f"{self.name} is poisoned")

    def burn_baby_burn(self):
        if self.burning:
            print(f"{self.name} is already on fire!")
        else:
            self.burning = True
            print(f"{self.name} caught on fire!")

    def in_the_wind(self):
        self.wind_hit_by = True

    def stun(self):
        self.stunned = True
    
    def level_attribute(self, stat_choice:str, new_stat:int = 1):
        if stat_choice == 'STR':
            self.strength = new_stat
        elif stat_choice == 'DEX':
            self.dexterity = new_stat
        elif stat_choice == 'INT':
            self.intelligence = new_stat
        elif stat_choice == 'CON':
            self.constitution = new_stat
            self.set_hp()
            
        self.set_attribute_list()
        self.set_dependant_atts()
    
    def set_hp(self):
        self.hp = self.constitution * 2
    

    def set_attribute_list(self):
        self.attribute_list= [
            {'name': "STR", "att":self.strength}, {'name': "DEX", "att": self.dexterity}, 
            {'name': "CON", "att": self.constitution}, {'name': "INT", "att": self.intelligence}
        ]

    def set_dependant_atts(self):
        self.current_hp = self.hp
        self.armor_val = self.armor
        self.att_val = self.dexterity if self.dexterity > self.strength else self.strength  
        self.damage = self.strength // 2 + self.weapon_damage if self.strength > 2 else 1 + self.weapon_damage
        self.damage_val = self.damage
        self.dodge_val = self.dexterity // 2 if self.dexterity > 2 else 1
        self.resist_val = self.resistance

    def change_outfit(self, outfit:tuple):
        self.u = outfit[0]
        self.v = outfit[1]

    def in_combat_text(self, combat_text, display_time:int = 1):
        CombatText(self.combat_state, combat_text, time(), display_time=display_time)
        if self.game.text_timer >= display_time:
            pass
    

class Player(Character, Sprite):
    def __init__(self, name, strength, dexterity, intelligence, constitution, game:object, armor=0, resistance=0):
        super().__init__(name, strength, dexterity, intelligence, constitution, armor, resistance)
        self.class_name = 'player'
        self.u=0
        self.v=64
        self.x = 164
        self.y= 64
        self.w=8
        self.h=8
        self.bank = 2
        self.colkey = 7
        self.draw_sidebar()


    def combat_draw(self):
        self.draw()
        px.text(168, 34, f"HP:{self.current_hp}/{self.hp}", 7)

    def draw_sidebar(self):
        stat_list = []

        px.text(12, 24, f"HP:{self.current_hp}/{self.hp}", 7)
        px.text(12, 34, f"STR:{self.strength}", 7)
        px.text(12, 42, f"DEX:{self.dexterity}", 7)
        px.text(40, 34, f"CON:{self.constitution}", 7)
        px.text(40, 42, f"INT:{self.intelligence}", 7)
        px.text(12, 50, f"DEF:{self.armor}", 7)
        px.text(40, 50, f"RESIST:{self.resistance}", 7)
        px.text(40, 58, f"DODGE:{self.dodge_val}", 7)
        px.text(12, 58, f"ATT:{self.att_val}", 7)
        px.text(12, 66, f"DAM:{self.damage}", 7)
        px.text(40, 66, f"MON:{self.currency}", 7)

        # placeholder
        px.text(32, 122, "Quit", 0)