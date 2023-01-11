from random import randint

# DELETE ALL RANDINT IN THIS FILE, REPLACE WITH RANDINT WHERE RANDOM IS NEEDED

rirs = randint(0,1) # randint small (0,1)
rirm = randint(-1,1) # randint medium (-1,1)



def vwa():
    2 + randint(0,1)

def wa():
    2 + randint(0,1)

def aa():
    5 + randint(-1,1)

def sa():
    7 + randint(0,1)

def vsa():
    9 + randint(0,1)


rirs = randint(0,3) # randint small (0,1)
rirm = randint(-2,3) # randint medium (-2,2)
nrn = randint(1,3)

att_randint = randint(-2,2)
damage_randint = randint(-2,2)
dex_randint = randint(-1,2)

attack_randint = { 
    'dex': randint(-1,2),
    'str': randint(-3,4),
    'int': randint(-1,1)
}



# Attributes for NPCs
attributes = {
'armor_type' :{'bone': 6, 'brigandine': 4, 'chain': 3, 'leather': 1, 'none': 0},
"resist_range" : {'very_weak': (0 + nrn), 'weak': 4 + rirs, 'average': 10 + rirm, 'strong': 14 + rirs, 'very_strong': 18 + rirs},
'strength_range': {'very_weak': (0 + nrn), 'weak': 4 + rirs, 'average': 10 + rirm, 'strong': 14 + rirs, 'very_strong': 18 + rirs},
'dexterity_range':{'very_weak': (0 + nrn), 'weak': 4 + rirs, 'average': 10 + rirm, 'strong': 14 + rirs, 'very_strong': 18 + rirs},
'intelligence_range': {'very_weak': (0 + nrn), 'weak': 4 + rirs, 'average': 10 + rirm, 'strong': 14 + rirs, 'very_strong': 18 + rirs},
'constitution_range' : {'very_weak': (0 + nrn), 'weak': 4 + rirs, 'average': 10 + rirm, 'strong': 14 + rirs, 'very_strong': 18 + rirs},
}

gob_war_name =['kikta', 'graga', 'kratab',]



currency_tiers = {
    1: 3 ,
    2: 8 ,
    3: 16 ,
    4: 27 ,
    5: 41 ,
    6: 58
}

lvl_dict = {
    'graith_lizard': 4,
     'graith_tree': 4,
    'krakt_rat': 1, 
     'braba_bat' : 2,
     'shadefire_fox': 6,
     'gratka_wolf':3,
     'rogue_goblin': 2,
     'graith_queen':6,
     'graith_apple':6,
}

# loot_group = {
#     "graktaw": 3,
#     "shadeff": 6,
#     'rogueg': 2,
#     "graithgl": 4,
#     "graithgq": 6,
#     "graitht": 4,
#     "graithat": 6,
#     "kraktr": 1,
#     "brabab": 1,
# }

# npc_class_choice = {
#     1: 'graith_lizard',
#     2: 'graith_tree',
#     3: 'krakt_rat', 
#     4: 'braba_bat',
#     5: 'shadefire_fox',
#     6: 'gratka_wolf',
#     7: 'rogue_goblin',
#     8: 'graith_queen',
#     9: 'graith_apple',

# }

underbelly = {
    1: 'krakt_rat', 
    2: 'braba_bat',
    3: 'rogue_goblin',
    4: 'graith_lizard',
    5: 'shadefire_fox',
    6: 'graith_queen'
}

shining_forest = {
    1: 'krakt_rat', 
    2: 'gratka_wolf',
    3: 'rogue_goblin',
    4: 'graith_tree',
    5: 'shadefire_fox',
    6: 'graith_apple'
}


encounter_dict = {
    'The Underbelly': {
        1: 'krakt_rat', 
        2: 'braba_bat',
        3: 'gratka_wolf',
        4: 'graith_lizard',
        5: 'shadefire_fox',
        6: 'graith_queen'
    },
    'The Shining Forest': {
        1: 'krakt_rat', 
        2: 'gratka_wolf',
        3: 'braba_bat',
        4: 'graith_tree',
        5: 'shadefire_fox',
        6: 'graith_apple'
    }
}

input_options = {
'yes':['yes','y','ye','yeah','yup','sure','mhm', 'ya', 'yep', 'yas', 'yaz', 'yaas!'],
'no': ['no','nope','naw','nuh uh', 'na', 'negatory', 'negative', 'n']
}


# Character Builder dicts
background_stats = {
    'b' :{
        'stats': {
            'strength': 12, 'dexterity':  8, 'intelligence': 8, 'constitution': 10},
        'name': "Apprentice Blacksmith"
        },
    't': {
        'stats': {
            'strength': 8, 'dexterity':  12, 'intelligence': 8, 'constitution': 10},
        'name': "Tunnel Scavenger"},
    'e':{
        'stats' :{
            'strength': 8, 'dexterity': 10, 'intelligence': 8, 'constitution': 12},
        'name': 'Explorer'
    },
    'a': { 
        'stats':{
            'strength': 8, 'dexterity':  10, 'intelligence': 12, 'constitution': 8},
         'name': 'Apprentice Herbalist' }

}

background_options = """(B) Blacksmith's Apprentice
(T) Tunnel Forager
(E) Explorer
(A) Alchemist's Apprentice """



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

# npc_class_dct = {
#    'graith_lizard': GraithLizard,
#      'graith_tree': GraithTree,
#     'krakt_rat': KraktRat, 
#      'braba_bat': BrabaBat,
#     'shadefire_fox': ShadeFireFox,
#    'gratka_wolf': GraktaWolf,
#     #  'rogue_goblin': RogueGoblin,
#     'graith_queen': GraithQueen,
#     'graith_apple': GraithApple
# } 
