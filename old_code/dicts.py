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
    1: 5 ,
    2: 12 ,
    3: 20 ,
    4: 30 ,
    5: 45 ,
    6: 70
}

lvl_dict = {
    'graith_lizard': 5,
     'graith_tree': 5,
    'krakt_rat': 1, 
     'braba_bat' : 3,
     'shadefire_fox': 6,
     'gratka_wolf':4,
     'ven_spider': 4,
     'graith_queen':6,
     'graith_apple':6,
}

encounter_dict = {
    'The Underbelly': {
        1: 'krakt_rat', 
        2: 'braba_bat',
        3: 'ven_spider',
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
    "Nakat'th" :{
        'stats': {
            'strength': 12, 'dexterity':  8, 'intelligence': 8, 'constitution': 10, 'x': 96, 'y': 24,
            'name': "Nakat'th", 'v': 64,  'job': 'Apprentice Blacksmith', },
         "description": '''Increased Strength 
         
and Constitution''', 
        },
    "Clichtka": {
        'stats': {
            'strength': 8, 'dexterity':  12, 'intelligence': 8, 'constitution': 10, 'x': 96, 'y': 42,
            'name': "Clichtka", 'v': 88, 'job': "Tunnel Scavenger"},
        'description': '''Increased Dexterity 
        
and Constitution''', 
        },
    "Bortorb":{
        'stats' :{
            'strength': 8, 'dexterity': 10, 'intelligence': 8, 'constitution': 12, 'x': 156, 'y': 24,
            'name': "Bortorb", 'v': 80,'job': 'Explorer'},
         'description': '''Increased Constitution 
         
and Dexterity '''
    },
    "Gragta'th": { 
        'stats':{
            'strength': 8, 'dexterity':  10, 'intelligence': 12, 'constitution': 8, 'x': 156, 'y': 42,
            'name': "Gragta'th",  'v': 72, 'job': 'Apprentice Herbalist'},
         "description": '''Increased Intelligence 
         
and Dexterity''', 
         }

}

npc_classes_attributes = {
    'graith_lizard': {'strength': 'strong', 'dexterity': 'weak', 'constitution': 'average', 'intelligence': 'very_weak', 'armor': 'brigandine', 'resistance': 'weak'},
    'graith_tree': {'strength': 'strong', 'dexterity': 'weak', 'constitution': 'strong', 'intelligence': 'very_weak', 'armor':'brigandine', 'resistance': 'weak'},
    'krakt_rat': {'strength': 'very_weak', 'dexterity': 'average', 'constitution': 'weak', 'intelligence': 'very_weak', 'armor': 'none', 'resistance': 'average'},
    'braba_bat': {'strength': 'very_weak', 'dexterity': 'average', 'constitution': 'weak', 'intelligence': 'very_weak', 'armor': 'none', 'resistance': 'average'},
    'shadefire_fox': {'strength': 'average', 'dexterity': 'very_strong', 'constitution': 'average', 'intelligence': 'average', 'armor': 'chain', 'resistance': 'strong'},
    'gratka_wolf': {'strength': 'average', 'dexterity': 'average', 'constitution': 'average', 'intelligence': 'weak', 'armor':'leather', 'resistance': 'average'},
    'graith_queen': {'strength': 'very_strong', 'dexterity': 'strong', 'constitution': 'strong', 'intelligence': 'very_weak', 'armor':'bone', 'resistance': 'average'},
    'graith_apple': {'strength': 'very_strong', 'dexterity': 'very_strong', 'constitution': 'very_strong', 'intelligence': 'average', 'armor':'brigandine', 'resistance': 'weak'},
    'ven_spider': {'strength': 'weak', 'dexterity':'strong', 'constitution': 'average', 'intelligence': 'weak', 'armor': 'chain', 'resistance': 'average'}
}

npc_class_choice = {
    1: 'graith_lizard',
    2: 'graith_tree',
    3: 'krakt_rat', 
    4: 'braba_bat',
    5: 'shadefire_fox',
    6: 'gratka_wolf',
    7: 'ven_spider',
    8: 'graith_queen',
    9: 'graith_apple'
}
