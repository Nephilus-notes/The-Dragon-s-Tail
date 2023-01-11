from random import randint

attack_randint = { 
    'dex': randint(-1,2),
    'str': randint(-3,4),
    'int': randint(-1,1)
}

attributes = {
    'armor_type' : {'bone': 6, 'brigandine': 4, 'chain': 3, 'leather': 1, 'none': 0},
    'attribute': {'very_weak': 0, 'weak': 4, 'average': 10, 'strong': 14, 'very_strong': 18}
}

attribute_range = {'very_weak': [1,3], 'weak': [0, 3], 'average': [-2, 3], 'strong': [0, 3], 'very_strong': [0, 3]}

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

npc_classes_attributes = {
    'graith_lizard': {'strength': 'strong', 'dexterity': 'weak', 'constitution': 'average', 'intelligence': 'very_weak', 'armor': 'brigandine', 'resistance': 'weak'},
    'graith_tree': {'strength': 'strong', 'dexterity': 'weak', 'constitution': 'strong', 'intelligence': 'very_weak', 'armor':'brigandine', 'resistance': 'weak'},
    'krakt_rat': {'strength': 'very_weak', 'dexterity': 'average', 'constitution': 'weak', 'intelligence': 'very_weak', 'armor': 'none', 'resistance': 'average'},
    'braba_bat': {'strength': 'very_weak', 'dexterity': 'average', 'constitution': 'weak', 'intelligence': 'very_weak', 'armor': 'none', 'resistance': 'average'},
    'shadefire_fox': {'strength': 'average', 'dexterity': 'very_strong', 'constitution': 'average', 'intelligence': 'average', 'armor': 'chain', 'resistance': 'strong'},
    'gratka_wolf': {'strength': 'average', 'dexterity': 'average', 'constitution': 'average', 'intelligence': 'weak', 'armor':'leather', 'resistance': 'average'},
    'graith_queen': {'strength': 'very_strong', 'dexterity': 'strong', 'constitution': 'very_strong', 'intelligence': 'very_weak', 'armor':'bone', 'resistance': 'average'},
    'graith_apple': {'strength': 'very_strong', 'dexterity': 'strong', 'constitution': 'very_strong', 'intelligence': 'average', 'armor':'brigandine', 'resistance': 'weak'},
}


npc_class_choice = {
    1: 'graith_lizard',
    2: 'graith_tree',
    3: 'krakt_rat', 
    4: 'braba_bat',
    5: 'shadefire_fox',
    6: 'gratka_wolf',
    7: None,
    8: 'graith_queen',
    9: 'graith_apple'
}
