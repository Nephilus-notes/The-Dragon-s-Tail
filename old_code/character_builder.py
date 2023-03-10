from random import randint as RI
from time import time, sleep
import pyxel as px


from pyxel_code.message_classes import CombatText
from pyxel_code.utils import items as itm, Interactable # Application Imports 
from .dicts import * # Application Imports
from .item_screen import EquippedItems, Backpack # Application Imports
from pyxel_code.image_classes import Sprite, DisplayText # Application Imports

# from ..pyxel_code.image_classes import Sprite # Test Import Path


dex = [-1, 2]
strength = [-3, 4]
intelligence = [-1, 1]


rirs = randint(0,1) # randint small (0,1)
rirm = randint(-1,1) # randint medium (-1,1)
nrn = randint(0,2)



class Character():
    def __init__ (self, name, strength, dexterity, intelligence, constitution, armor=0, resistance=0):
        self.name = name
        # Items
        self.lifetime_currency = 0
        self.currency = 0
        self.bag = Backpack(self)
        self.items_worn = self.bag.equipped

    #    Stats and whatnot
        self.armor = armor # 0 if self.items_worn.placement['slot']['body'] == {'nothing':'nothing'} else itm[self.items_worn.placement['slot']['body']['armor_value']]
        self.resistance = resistance
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.constitution = constitution
        self.hp = self.constitution * 2
        self.max_mp = self.intelligence * 2
        self.weapon = {}  if self.items_worn.slot['hand'] == {'nothing':'nothing'} else itm[self.items_worn.slot['hand']]
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
        self.att_val = self.dexterity // 2 if self.dexterity > self.strength else self.strength // 2
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
        self.dodging_rounds = 0
        self.defended_rounds = 0
        self.flee_count = 0
        self.slowed_rounds = 0
        self.stone_armored_rounds = 0
        self.vulnerable_rounds = 0
        self.double_armed_rounds = 0
        self.burning_blades_rounds = 0
        self.burning_rounds = 0
        self.poisoned_rounds = 0
        self.set_attribute_list()
        # self.set_currency()

        self.game = None
        self.combat_state = None



    def attack(self, target):
        damage_num = 0
        stat_mod = 0

        # Setting which attack modifier to use based on high stat
        if self.dexterity > self.strength and self.dexterity > self.intelligence:
            stat_mod = dex

        elif self.strength > self.dexterity and self.strength > self.intelligence:
            stat_mod = strength

        elif self.intelligence > self.dexterity and self.intelligence > self.strength:
            stat_mod = intelligence

        # checking for hitting and critting, then assigning damage and calling damage function
        attack_mod = RI(*stat_mod)
        if attack_mod == max(stat_mod):
            damage_num = (self.damage + 2)
            self.in_combat_text(f'''{self.name.title()} attacks!
            
**Critical hit!**''')
            self.attack_damage(target, damage_num)

        elif self.att_val + RI(*stat_mod) <= target.dodge_val:
            self.in_combat_text(f'{self.name.title()} attacks!')
            self.in_combat_text(f"{self.name.title()} missed!")
            
        elif self.att_val + RI(*stat_mod) > target.dodge_val:
            self.in_combat_text(f'{self.name.title()} attacks!')
            damage_num = (self.damage + RI(*stat_mod)) - target.armor_val
            self.attack_damage(target, damage_num)

        return attack_mod, damage_num



    def attack_damage(self, target, damage_num):
            if damage_num > 0:
                self.in_combat_text(f'''{target.name.title()} was hit! 
{str(damage_num)} damage!''',)
                target.current_hp -= damage_num
                if target.current_hp <= 0:
                    target.current_hp = 0
                #     self.in_combat_text(f"\n{target.name.title()} has been defeated.")
                #     # del target
            elif damage_num <= 0 and target.name[-1] != "s":
                self.in_combat_text(f"""{target.name.title()} blocks 
{self.name.title()}' strike.""")
            elif damage_num <= 0 and target.name[-1] == "s":
                self.in_combat_text(f"""{target.name.title()} blocks
{self.name.title()}'s strike.""")
                

    def wear_armor(self):
        self.armor = 0 if self.items_worn.placement['slot']['body'] == 'nothing' else itm[self.items_worn.placement['slot']['body']['armor_value']]
        self.armor_val = self.armor

    def defend(self):
        if self.defended:
            self.defended_rounds = 0
            self.in_combat_text(f"""{self.name}
is defending""")
        else:
            self.armor_val += 2
            self.defended = True
            if self.class_name == 'player':
                print(f'You are defended: Armor val = {self.armor_val} ')
                self.in_combat_text(f"""You defend. 
Armor: {self.armor_val}""")
            else:
                self.in_combat_text(f'''{ self.combat_state.enemy} 
hunkers down to defend.''')
        # rnd_count = 2

    def undefend(self):
        self.armor_val -= 2
        self.defended = False
        self.defended_rounds = 0
        if self.class_name != 'player':
            self.in_combat_text(f'''{ self.combat_state.enemy} 
relaxes their guard.''')

    def dodge(self):
        if self.dodging == True:
            self.dodging_rounds = 0
            self.in_combat_text(f"{self.name} is dodging")
        else:
            self.dodging = True
            self.dodge_val += 2
            if self.class_name == 'player':
                self.in_combat_text(f"""You focus on dodging.""")
            else:
                self.in_combat_text(f'''{ self.combat_state.enemy} 
dances about nimbly.''')
            # rnd_count = 2

    def undodge(self):
        self.dodging = False
        self.dodging_rounds = 0
        self.dodge_val -= 2

    def flee(self, enemy):
        if self.dexterity > enemy.dexterity or self.flee_count > 0:            
            self.fleeing = True
        else:
            self.flee_count += 1
            self.in_combat_text(f'You try to run')
            return False

    def __repr__(self):
        return self.name.title()

    def stone_armor(self):
        if self.stone_armored == True:
            self.in_combat_text(F'''{self.name}
is already protected''')
        else:
            self.armor_val += 2
            self.stone_armored = True
            print(f"You cast a spell to boost your armor. Armor: {self.armor_val}")

    def slow(self):
        if self.slowed:
            self.slowed_rounds = 0
            print(f"{self.name} is already slowed")
        else:
            self.dodge_val -= 2
            self.slowed = True
            print(f"{self.name} is slowed")
    
    def unslow(self):
        self.dodge_val += 2
        self.slowed_rounds = 0
        self.slowed = False

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
            self.in_combat_text(f"""{self.name} 
is poisoned""")

    def unpoison(self):
        self.poisoned = False
        self.poisoned_rounds = 0
        self.in_combat_text("""You recover
from poison""")

    def burn_baby_burn(self):
        if self.burning:
            print(f"{self.name} is already on fire!")
        else:
            self.burning = True
            print(f"{self.name} caught on fire!")

    def in_the_wind(self):
        self.wind_hit_by = True

    def stun(self):
        if self.stunned == True:
            self.stunned_rounds = 0
        else:
            self.stunned = True

    def unstun(self):
        self.stunned = False
        self.stunned_rounds = 0
    
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
        self.armor_val = self.armor if self.armor >= 0 else 0
        self.att_val = self.dexterity // 2 if self.dexterity > self.strength else self.strength  // 2
        self.damage = self.strength // 2 + self.weapon_damage if self.strength > 2 else 1 + self.weapon_damage
        self.damage_val = self.damage
        self.dodge_val = self.dexterity // 2 if self.dexterity > 2 else 1
        self.resist_val = self.resistance

        self.current_mp = self.max_mp

    def change_outfit(self, outfit:tuple):
        self.u = outfit[0]
        self.v = outfit[1]

    def reset_flags(self):
        # print('reseting flags')
        self.defended = False  #incrementer
        self.dodging = False    # Incrementor
        self.fleeing = False    # Incrementor
        self.stone_armored = False  # Incrementor
        self.slowed = False         # Incrementor
        self.vulnerable = False     # Incrementor
        self.double_armed = False  # Incrementor
        self.burning_blades = False # Incrementor = damage = magic
        self.stone_fists = False # Incrementor = Bonus damage
        self.stunned = False
        self.dodging_rounds = 0
        self.defended_rounds = 0
        self.flee_count = 0
        self.slowed_rounds = 0
        self.stone_armored_rounds = 0
        self.vulnerable_rounds = 0
        self.double_armed_rounds = 0
        self.burning_blades_rounds = 0
        self.burning_rounds = 0
        self.poisoned_rounds = 0


    def in_combat_text(self, combat_text, display_time:float = 1.5):
        self.add_text(self.combat_state, combat_text, {'display_time':display_time})


    def add_text(self, combat_state:object, text:str, kwarg_dict:dict):
        # print(f'Game text length = {len(self.game.text)}')
        if len(self.game.text) < 1:
           self.game.text.append({'combat_state': combat_state, 'combat_text': text, **kwarg_dict})
        elif len(self.game.text) >= 1:
            if self.game.text[-1] == Interactable.unfreeze:
                print('pop and switch')
                popped = self.game.text.pop()
                self.game.text.append({'combat_state': combat_state, 'combat_text': text, **kwarg_dict})
                self.game.text.append(popped)
            else:
                self.game.text.append({'combat_state': combat_state, 'combat_text': text, **kwarg_dict})


    
    def equip(self):
        self.armor = 0 if self.items_worn.slot['body'] == {'nothing':'nothing'} else self.items_worn.slot['body'].item_stat
        self.weapon = {}  if self.items_worn.slot['hand'] == {'nothing':'nothing'} else self.items_worn.slot['hand']
        self.weapon_damage = self.weapon.item_stat if self.weapon else 0
        self.damage = self.strength // 2 + self.weapon_damage if self.strength > 2 else 1 + self.weapon_damage
        self.armor_val = self.armor


class Player(Character, Sprite):
    def __init__(self, name, strength, dexterity, intelligence, constitution, v, job, x=164, y=64, game:object = None, armor=0, resistance=0):
        super().__init__(name, strength, dexterity, intelligence, constitution, armor, resistance)
        self.class_name = 'player'
        self.job = job
        self.u=8
        self.v=v
        self.x = x
        self.y= y
        self.w=8
        self.h=8
        self.bank = 2
        self.colkey = 7
        # self.draw_sidebar()
        self.running = False


    def combat_draw(self):
        self.draw()
        px.text(168, 34, f"HP:{self.current_hp}/{self.hp}", 7)

    def draw_sidebar(self):
        stat_list = []

        px.text(12, 24, f'NAME: {self.name}', 7)
        px.text(12, 32, f"HP: {self.current_hp}/{self.hp}", 7)
        px.text(12, 42, f"STR: {self.strength}", 7)
        px.text(12, 50, f"DEX: {self.dexterity}", 7)
        px.text(12, 58, f"CON: {self.constitution}", 7)
        px.text(12, 66, f"INT: {self.intelligence}", 7)
        px.text(12, 76, f"Attack: {self.att_val}", 7)
        px.text(12, 84, f"Damage: {self.damage}", 7)
        px.text(12, 92, f"Defense: {self.armor_val}", 7)
        px.text(12, 100, f"Resistance: {self.resistance}", 7)
        px.text(12, 108, f"Dodge: {self.dodge_val}", 7)
        px.text(12, 118, f"Trophies: {self.currency}", 7)

        # placeholder
        # px.text(32, 118, "Quit", 0)

    def intersects(self, mouse_location:tuple):
        is_intersected = False
        if (
            px.mouse_x > self.x and px.mouse_x < self.x + self.w
            and px.mouse_y > self.y and px.mouse_y < self.y + self.h + 2
        ):
            is_intersected = True
            return is_intersected

    def intersection(self):
        self.character_choice_text()
    
    def character_choice_text(self):
            px.text(116, 84, self.name, 7)
            px.text(84, 92, f"Job: {self.job} ", 7)
            px.text(86, 102, f'{background_stats[self.name]["description"]}', 7)

    def set_combat_atts(self):
        self.armor_val = self.armor if self.armor >= 0 else 0
        self.att_val = self.dexterity // 2 if self.dexterity > self.strength else self.strength  // 2
        self.damage = self.strength // 2 + self.weapon_damage if self.strength > 2 else 1 + self.weapon_damage
        self.damage_val = self.damage
        self.dodge_val = self.dexterity // 2 if self.dexterity > 2 else 1
        self.resist_val = self.resistance