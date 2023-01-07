from random import randint
import json

from .dicts import items as itm
from .dicts import *
from .item_screen import EquippedItems, Backpack
rirs = randint(0,1) # randint small (0,1)
rirm = randint(-1,1) # randint medium (-1,1)
nrn = randint(0,2)
# starting combat would instantiate base classes and would include a method to determine how con affects hp
#method = roll stats
#character - class, race -
# self.armor = platemail or other item
# level ups = adding stats, figuring out 
# 
# add a level counter ( and xp)
# if level >= (5), add ability #part of the level up ability 



class Character:
    def __init__ (self, name, strength, dexterity, intelligence, constitution, armor=0, resistance=0, ):
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
        # self.level = 1

        # Ability list
        self.abilities = []
        
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

        # self.set_currency()


    def attack(self, target):
        print(f'{self.name.title()} lashes out at {target.name.title()}!')

        if self.dexterity > self.strength:
            if attack_randint['dex'] == 2:
                damage_num = (self.damage + 2)
                print('**Critical hit!**')
                self.attack_damage(target, damage_num)
            elif self.att_val + attack_randint['dex'] <= target.dodge_val:
                print(f"{self.name.title()}'s missed!")
            elif self.att_val + attack_randint['dex'] > target.dodge_val:
                damage_num = (self.damage + attack_randint['dex']) - target.armor_val
                self.attack_damage(target, damage_num)

        elif self.strength >= self.dexterity:
            if attack_randint['str'] == 4:
                damage_num = (self.damage + 4) - target.armor_val
                print('**Critical hit!**')
                self.attack_damage(target, damage_num)
            elif self.att_val + attack_randint['str'] <= target.dodge_val:
                print (f'{self.name.title()} missed!')
            elif self.att_val + attack_randint['str'] > target.dodge_val:
                damage_num = (self.damage + attack_randint['str']) - target.armor_val
                self.attack_damage(target, damage_num)


    def attack_damage(self, target, damage_num):
            if damage_num > 0:
                print(f'{self.name.title()} has hit {target.name.title()} for {str(damage_num)} damage!')
                target.current_hp -= damage_num
                if target.current_hp <= 0:
                    target.current_hp = 0
                    print(f"\n{target.name.title()} has been defeated.")
                    # del target
            elif damage_num <= 0 and target.name[-1] != "s":
                print(f"{target.name.title()} blocks {self.name.title()}' strike.")
            elif damage_num <= 0 and target.name[-1] == "s":
                print(target.name.title(), 'blocks', self.name.title() + "'s strike.")
                

    def wear_armor(self):
        self.armor = 0 if self.items_worn.placement['slot']['body'] == 'nothing' else itm[self.items_worn.placement['slot']['body']['armor_value']]
        self.armor_val = self.armor

    def defend(self):
        self.armor_val = self.armor + 2
        self.defended = True
        print(f"You focus on defending. Armor: {self.armor_val}")
        # rnd_count = 2

    def undefend(self):
        self.armor_val = self.armor

    def dodge(self):
        self.dodging = True
        self.dodge_val = self.dexterity + 2
        print(f'You focus on dodging. Dodge: {self.dodge_val}')
        # rnd_count = 2

    def undodge(self):
        self.dodge_val = self.dexterity

    def flee(self, enemy):
        if self.dexterity > enemy.dexterity or self.flee_count > 0:
            self.fleeing = True
            print(f"You run from {enemy}")
        else:
            self.flee_count += 1
            print(f'You try to run from {enemy}')

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
    
    def show_stats(self):
        print(f'\nAttributes\n{"~"*10}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nConstitution: {self.constitution}\nArmor: {self.armor_val}\nResistance: {self.resist_val}')
    
    def show_combat_stats(self):
        print(f"""\nCombat Attributes\n{"~"*10}\nHP: {self.current_hp}/{self.hp}\nMP:: {self.current_mp}/{self.max_mp}
Attack: {self.att_val}\nDamage: {self.damage_val}\nDodge: {self.dodge_val}\nArmor: {self.armor_val}\nResist: {self.resist_val}""")

    def level_attribute(self, stat_choice:str):
        if stat_choice == 'strength':
            self.strength += 1
        elif stat_choice == 'dexterity':
            self.dexterity += 1
        elif stat_choice == 'intelligence':
            self.intelligence += 1
        elif stat_choice == 'constitution':
            self.constitution += 1


