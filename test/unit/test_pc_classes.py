import pytest
import pyxel as px
from old_code.character_builder import Player
from old_code.dicts import background_stats
from test.conftest import game

# @pytest.mark.skip
def test_blacksmith(game):
    """
    GIVEN an ApprenticeBlacksmith class
    WHEN a new ApprenticeBlacksmith is created
    THEN check that strength, dexterity, intelligence, constitution, 
        combat stats (armor, resist, damage, and dodge values), hp, mp
        and currency instantiate correctly
    """
    blacksmith = Player( **background_stats["Nakat'th"]['stats'])
    assert blacksmith.strength == 12
    assert blacksmith.dexterity == 8
    assert blacksmith.intelligence == 8
    assert blacksmith.constitution == 10
    assert blacksmith.armor_val == 0
    assert blacksmith.resist_val == 0
    assert blacksmith.damage_val == 6
    assert blacksmith.hp == blacksmith.constitution * 2
    assert blacksmith.current_hp == 20
    assert blacksmith.current_mp == blacksmith.max_mp and blacksmith.max_mp == blacksmith.intelligence * 2
    assert blacksmith.currency == 0
    assert blacksmith.dodge_val == 4
    
# @pytest.mark.skip
def test_herbalist(game):
    """
    GIVEN an ApprenticeHerbalist class
    WHEN a new ApprenticeHerbalist is created
    THEN check that strength, dexterity, intelligence, constitution, 
        combat stats (armor, resist, damage, and dodge values), hp, mp
        and currency instantiate correctly
    """
    herbalist = Player(**background_stats["Gragta'th"]['stats'])
    assert herbalist.strength == 8
    assert herbalist.dexterity == 10
    assert herbalist.intelligence == 12
    assert herbalist.constitution == 8
    assert herbalist.armor_val == 0
    assert herbalist.resist_val == 0
    assert herbalist.damage_val == 4
    assert herbalist.hp == herbalist.constitution * 2
    assert herbalist.current_hp == 16
    assert herbalist.current_mp == herbalist.max_mp and herbalist.max_mp == herbalist.intelligence * 2
    assert herbalist.currency == 0
    assert herbalist.dodge_val == 5
    
# @pytest.mark.skip
def test_scavenger(game):
    """
    GIVEN an TunnelScavenger class
    WHEN a new TunnelScavenger is created
    THEN check that strength, dexterity, intelligence, constitution, 
        combat stats (armor, resist, damage, and dodge values), hp, mp
        and currency instantiate correctly
    """
    scavenger = Player(**background_stats["Clichtka"]['stats'])
    assert scavenger.strength == 8
    assert scavenger.dexterity == 12
    assert scavenger.intelligence == 8
    assert scavenger.constitution == 10
    assert scavenger.armor_val == 0
    assert scavenger.resist_val == 0
    assert scavenger.damage_val == 4
    assert scavenger.hp == scavenger.constitution * 2
    assert scavenger.current_hp == 20
    assert scavenger.current_mp == scavenger.max_mp and scavenger.max_mp == scavenger.intelligence * 2
    assert scavenger.currency == 0
    assert scavenger.dodge_val == 6
    
# @pytest.mark.skip
def test_explorer(game):
    """
    GIVEN an TunnelExplorer class
    WHEN a new TunnelExplorer is created
    THEN check that strength, dexterity, intelligence, constitution, 
        combat stats (armor, resist, damage, and dodge values), hp, mp
        and currency instantiate correctly
    """
    explorer = Player(**background_stats["Bortorb"]['stats'])
    assert explorer.strength == 8
    assert explorer.dexterity == 10
    assert explorer.intelligence == 8
    assert explorer.constitution == 12
    assert explorer.armor_val == 0
    assert explorer.resist_val == 0
    assert explorer.damage_val == 4
    assert explorer.hp == explorer.constitution * 2
    assert explorer.current_hp == 24
    assert explorer.current_mp == explorer.max_mp and explorer.max_mp == explorer.intelligence * 2
    assert explorer.currency == 0
    assert explorer.dodge_val == 5

