from old_code.npc_classes import GraithLizard, GraithTree, GraktaWolf, KraktRat, npc_class_choice, npc_class_dct, ShadeFireFox, BrabaBat, GraithQueen, GraithApple
from old_code.dicts import lvl_dict, currency_tiers

# Testing Bounds

# attributes
very_weak_lower = 1
very_weak_upper = 3
weak_lower = 4
weak_upper = 7
average_lower = 8
average_upper = 13
strong_lower = 14
strong_upper = 17
very_strong_lower = 18
very_strong_upper = 21

# Loot bounds
lower_1 = 4
upper_1 = 7
lower_2 = 10
upper_2 = 16
lower_3 = 17
upper_3 = 26
lower_4 = 26
upper_4 = 38
lower_5 = 40
upper_5 = 55
lower_6 = 64
upper_6 = 82

#  Vals
very_weak_val = 1
weak_lower_val = 2
weak_upper_val = 3
average_lower_val = 4
average_upper_val = 6
strong_lower_val = 7
strong_upper_val =8
very_strong_lower_val = 9
very_strong_upper_val = 10

bone_lower = 5
bone_upper = 7
brigandine_lower = 3
brigandine_upper = 5
chain_lower = 2
chain_upper = 4
leather_lower = 0 
leather_upper = 2
none_lower = 0
none_upper = 1



def test_ShadeFireFox():
    """
    GIVEN an Shadefire Fox class
    WHEN a new shadefire fox is created
    THEN check that strength, dexterity, constitution are true
    """
    shade_fire = ShadeFireFox()
    assert shade_fire.strength >= 8 and shade_fire.strength <= 13
    assert shade_fire.dexterity >= 18 and shade_fire.dexterity <= 21
    assert shade_fire.intelligence >= 8 and shade_fire.intelligence <= 13
    assert shade_fire.constitution >= 8 and shade_fire.constitution <= 13
    assert shade_fire.armor_val >= chain_lower and shade_fire.armor_val <= chain_upper
    assert shade_fire.resist_val >= 14 and shade_fire.resist_val <= 17
    assert shade_fire.damage_val >= average_lower_val and shade_fire.damage_val <= average_upper_val
    assert shade_fire.hp == shade_fire.constitution * 4
    assert shade_fire.current_hp >=  average_lower * 4 and shade_fire.current_hp <= average_upper * 4
    assert shade_fire.current_mp == shade_fire.max_mp and shade_fire.max_mp == shade_fire.intelligence * 2
    assert shade_fire.currency >= lower_6 and shade_fire.currency <= upper_6
    assert shade_fire.dodge_val >= very_strong_lower_val and shade_fire.dodge_val <= very_strong_upper_val

def test_graith_lizard():
    """
    GIVEN an GraithLizard class
    WHEN a new GraithLizard is created
    THEN check that strength, dexterity, constitution, defend ability and defended flag responds correctly
    """
    graith_lizard = GraithLizard()
    assert graith_lizard.strength >= strong_lower and graith_lizard.strength <= strong_upper
    assert graith_lizard.dexterity >= weak_lower and graith_lizard.dexterity <= weak_upper
    assert graith_lizard.intelligence >= very_weak_lower and graith_lizard.intelligence <= very_weak_upper
    assert graith_lizard.constitution >= average_lower and graith_lizard.constitution <= average_upper
    assert graith_lizard.armor_val >= brigandine_lower and graith_lizard.armor_val <= brigandine_upper
    assert graith_lizard.resist_val >= weak_lower and graith_lizard.resist_val <= weak_upper
    assert graith_lizard.damage_val >= 7 and graith_lizard.damage_val <= 9
    assert graith_lizard.hp == graith_lizard.constitution * 4
    assert graith_lizard.current_hp >= average_lower * 4 and graith_lizard.current_hp <= average_upper *4
    assert graith_lizard.current_mp == graith_lizard.max_mp and graith_lizard.max_mp == graith_lizard.intelligence * 2
    assert graith_lizard.currency >= lower_4 and graith_lizard.currency <= upper_4
    assert graith_lizard.dodge_val >= weak_lower_val and graith_lizard.dodge_val <= weak_upper_val

def test_graith_tree():
    """
    GIVEN an GraithTree class
    WHEN a new GraithTree is created
    THEN check that strength, dexterity, constitution, defend ability and defended flag responds correctly
    """
    graith_tree = GraithTree()
    assert graith_tree.strength >= strong_lower and graith_tree.strength <= strong_upper
    assert graith_tree.dexterity >= weak_lower and graith_tree.dexterity <= weak_upper
    assert graith_tree.intelligence >= very_weak_lower and graith_tree.intelligence <= very_weak_upper
    assert graith_tree.constitution >= strong_lower and graith_tree.constitution <= strong_upper
    assert graith_tree.armor_val >= brigandine_lower and graith_tree.armor_val <= brigandine_upper
    assert graith_tree.resist_val >= weak_lower and graith_tree.resist_val <= weak_upper
    assert graith_tree.damage_val >= 7 and graith_tree.damage_val <= 9
    assert graith_tree.hp == graith_tree.constitution * 4
    assert graith_tree.current_hp >= strong_lower * 4 and graith_tree.current_hp <= strong_upper * 4
    assert graith_tree.current_mp == graith_tree.max_mp and graith_tree.max_mp == graith_tree.intelligence * 2
    assert graith_tree.currency >= lower_4 and graith_tree.currency <= upper_4
    assert graith_tree.dodge_val >= weak_lower_val and graith_tree.dodge_val <= weak_upper_val
    # graith_tree.defend()
    # assert graith_tree.defended == True
    # # change this , and defended, to only giving 2 armor
    # assert graith_tree.armor_val == graith_tree.armor + 2

def test_grakta_wolf():
    """
    GIVEN an GraktaWolf class
    WHEN a new GraktaWolf is created
    THEN check that strength, dexterity, flee ability and fleeing flag responds correctly
    """
    grakta_wolf = GraktaWolf()
    assert grakta_wolf.strength >= average_lower and grakta_wolf.strength <= average_upper
    assert grakta_wolf.dexterity >= average_lower and grakta_wolf.dexterity <= average_upper
    assert grakta_wolf.intelligence >= weak_lower and grakta_wolf.intelligence <= weak_upper
    assert grakta_wolf.constitution >= average_lower and grakta_wolf.constitution <= average_upper
    assert grakta_wolf.armor_val >= leather_lower and grakta_wolf.armor_val <= leather_upper
    assert grakta_wolf.resist_val >= average_lower and grakta_wolf.resist_val <= average_upper
    assert grakta_wolf.damage_val >= average_lower_val and grakta_wolf.damage_val <= average_upper_val
    assert grakta_wolf.hp == grakta_wolf.constitution * 2
    assert grakta_wolf.current_hp >= average_lower * 2 and grakta_wolf.current_hp <= average_upper * 2
    assert grakta_wolf.current_mp == grakta_wolf.max_mp and grakta_wolf.max_mp == grakta_wolf.intelligence * 2
    assert grakta_wolf.currency >= lower_3 and grakta_wolf.currency <= upper_3
    assert grakta_wolf.dodge_val >= average_lower_val and grakta_wolf.dodge_val <= average_upper_val    
    second_wolf = GraktaWolf()
    second_wolf.dexterity = 1

    grakta_wolf.flee(second_wolf)
    assert grakta_wolf.fleeing == True

def test_krakta_rat():
    """
    GIVEN an KraktRat class
    WHEN a new KraktRat is created
    THEN check that constitution, dexterity, and intelligence instantiate correctly
    """
    krakta_rat = KraktRat()
    assert krakta_rat.strength >= very_weak_lower and krakta_rat.strength <= very_weak_upper
    assert krakta_rat.dexterity >= average_lower and krakta_rat.dexterity <= average_upper
    assert krakta_rat.intelligence >= very_weak_lower and krakta_rat.intelligence <= very_weak_upper
    assert krakta_rat.constitution >= weak_lower and krakta_rat.constitution <= weak_upper
    assert krakta_rat.armor_val >= none_lower and krakta_rat.armor_val <= none_upper
    assert krakta_rat.resist_val >= average_lower and krakta_rat.resist_val <= average_upper
    assert krakta_rat.damage_val ==  very_weak_val
    assert krakta_rat.hp == krakta_rat.constitution * 2
    assert krakta_rat.current_hp >= weak_lower * 2 and krakta_rat.current_hp <= weak_upper * 2
    assert krakta_rat.current_mp == krakta_rat.max_mp and krakta_rat.max_mp == krakta_rat.intelligence * 2
    assert krakta_rat.currency >= lower_1 and krakta_rat.currency <= upper_1
    assert krakta_rat.dodge_val >= average_lower_val and krakta_rat.dodge_val <= average_upper_val 

def test_braba_bat():
    """
    GIVEN an BrabaBat class
    WHEN a new BrabaBat is created
    THEN check that constitution, dexterity, dodge ability and active dodge responds correctly
    """
    braba_bat = BrabaBat()
    assert braba_bat.strength >= very_weak_lower and braba_bat.strength <= very_weak_upper
    assert braba_bat.dexterity >= average_lower and braba_bat.dexterity <= average_upper
    assert braba_bat.intelligence >= very_weak_lower and braba_bat.intelligence <= very_weak_upper
    assert braba_bat.constitution >= weak_lower and braba_bat.constitution <= weak_upper
    assert braba_bat.armor_val >= none_lower and braba_bat.armor_val <= none_upper
    assert braba_bat.resist_val >= average_lower and braba_bat.resist_val <= average_upper
    assert braba_bat.damage_val ==  very_weak_val
    assert braba_bat.hp == braba_bat.constitution * 2
    assert braba_bat.current_hp >= weak_lower * 2 and braba_bat.current_hp <= weak_upper * 2
    assert braba_bat.current_mp == braba_bat.max_mp and braba_bat.max_mp == braba_bat.intelligence * 2
    assert braba_bat.currency >= lower_2 and braba_bat.currency <= upper_2
    assert braba_bat.dodge_val >= average_lower_val and braba_bat.dodge_val <= average_upper_val 

    # braba_bat.dodge()
    # assert braba_bat.dodging == True

def test_graith_queen():
    """
    GIVEN an GraithQueen class
    WHEN a new GraithQueen is created
    THEN check that constitution, dexterity, dodge ability and active dodge responds correctly
    """
    queen = GraithQueen()
    assert queen.strength >= very_strong_lower and queen.strength <= very_strong_upper
    assert queen.dexterity >= strong_lower and queen.dexterity <= strong_upper
    assert queen.intelligence >= very_weak_lower and queen.intelligence <= very_weak_upper
    assert queen.constitution >= strong_lower and queen.constitution <= strong_upper
    assert queen.armor_val >= bone_lower and queen.armor_val <= bone_upper
    assert queen.resist_val >= average_lower and queen.resist_val <= average_upper
    assert queen.damage_val >=  very_strong_lower_val and queen.damage_val <=  very_strong_upper_val
    assert queen.hp == queen.constitution * 4
    assert queen.current_hp >= strong_lower * 4 and queen.current_hp <= strong_upper * 4
    assert queen.current_mp == queen.max_mp and queen.max_mp == queen.intelligence * 2
    assert queen.currency >= lower_6 and queen.currency <= upper_6
    assert queen.dodge_val >= strong_lower_val and queen.dodge_val <= strong_upper_val 
    assert queen.class_name == "graith_queen"

def test_graith_apple():
    """
    GIVEN an GraithApple class
    WHEN a new GraithApple is created
    THEN check that constitution, dexterity, dodge ability and active dodge responds correctly
    """
    apple = GraithApple()
    assert apple.strength >= very_strong_lower and apple.strength <= very_strong_upper
    assert apple.damage_val >=  very_strong_lower_val and apple.damage_val <=  very_strong_upper_val
    assert apple.dexterity >= very_strong_lower and apple.dexterity <= very_strong_upper
    assert apple.dodge_val >= very_strong_lower_val and apple.dodge_val <= very_strong_upper_val 
    assert apple.intelligence >= average_lower and apple.intelligence <= average_upper
    assert apple.current_mp == apple.max_mp and apple.max_mp == apple.intelligence * 2
    assert apple.constitution >= very_strong_lower and apple.constitution <= very_strong_upper
    assert apple.hp == apple.constitution * 4
    assert apple.current_hp >= very_strong_lower * 4 and apple.current_hp <= very_strong_upper * 4
    assert apple.armor_val >= brigandine_lower and apple.armor_val <= brigandine_upper
    assert apple.resist_val >= weak_lower and apple.resist_val <= weak_upper
    assert apple.currency >= lower_6 and apple.currency <= upper_6
    