import pytest
from old_code.character_builder import Character
from old_code.item_screen import Backpack, EquippedItems
from old_code.dicts import items as itm



@pytest.fixture
def empty_bag():
    bag = Backpack()
    return bag

@pytest.fixture
def bag_with_items():
    bag = Backpack()
    bag.add_item('dagger')
    bag.add_item('axe')
    bag.add_item('sword')
    bag.add_item('leather_armor')

    return bag

def full_bag_not_implimented():
    bag = Backpack()

    return bag

@pytest.fixture
def worn_items_none(bag_with_items):
    c_equip = EquippedItems(bag_with_items)
    
    return c_equip

@pytest.fixture
def worn_items_two(bag_with_items):
    c_equip = EquippedItems(bag_with_items, hand_item=itm['dagger'], body_item=itm['leather_armor'])
    
    return c_equip

@pytest.fixture
def end_game_character(bag_with_items):
    craelios_strong = Character("Craelios",  20, 20, 20, 20, 20, 20)
    craelios_strong.currency = 500
    craelios_strong.bag = bag_with_items
    return craelios_strong

@pytest.fixture
def early_game_character(bag_with_items):
    craelios_weak = Character("Craelios",  10, 10, 10, 10, 10, 10)
    craelios_weak.bag = bag_with_items
    return craelios_weak