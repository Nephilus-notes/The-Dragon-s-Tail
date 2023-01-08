import pytest 
import old_code.item_screen as i_s
from ..conftest import empty_bag, bag_with_items as bwi, worn_items_none as win, worn_items_two as wi2
from old_code.dicts import items as itm
from old_code.item_screen import Backpack, DragonItem, EquippedItems

# testing item classes
def test_BackPack():
    """
    GIVEN a Backpack class
    WHEN a new Backpack is created
    THEN check that bag size and slots type are correct.
    """
    bag = Backpack()
    assert bag.size == 5
    assert bag.slots == {}

def test_Backpack_size():
    bag = Backpack()
    assert bag.size == 5
    assert bag.slots == {}
    bag.add_item('dagger')
    bag.add_item('axe')
    bag.add_item('sword')
    bag.add_item('leather_armor')
    bag.add_item('chain_armor')
    assert bag.slots['dagger']
    assert bag.slots['axe']
    assert bag.slots['sword']
    assert bag.slots['leather_armor']
    assert bag.slots['chain_armor']

def test_equippedItems(bwi):
    """
    GIVEN an EquippedItems class
    WHEN a new EquippedItems is created
    THEN check that the worn item kwargs are passed in correctly
    """
    worn = EquippedItems(bwi, hand_item=itm['dagger'], body_item=itm['leather_armor'])
    assert isinstance(worn.placement['slot']['hand'], dict)
    assert worn.placement['slot']['hand']['name'] == 'dagger'

@pytest.mark.xfail
def test_equippedItems_fail(bwi):
    """
    GIVEN an EquippedItems class
    WHEN a new EquippedItems is created
    THEN check that the worn item kwargs are passed in correctly
    """
    worn = EquippedItems(bwi, hand_item=itm['dagger'], body_item=itm['leather_armor'])
    assert isinstance(worn.placement['slot']['hand'], dict)
    assert worn.placement['slot']['hand']['name'] == 'sword'


# testing class methods
def test_add_item_success(empty_bag):
    empty_bag.add_item(itm['dagger']['name'])
    assert empty_bag.slots['dagger']

def test_add_item_fail():
    pass

def test_show_items(capsys, empty_bag):
    empty_bag.show_items()
    empty_bag.add_item(itm['dagger']['name'])

    captured = capsys.readouterr()
    assert captured.out.strip() == "Carried Items:\n~~~~~~~~~~~~~~~"

def test_drop_item_success(bwi):
    bwi.drop_item('dagger')
    bwi.drop_item('axe')
    bwi.drop_item('sword')
    bwi.drop_item('leather_armor')
    assert bwi.slots == {}

@pytest.mark.xfail
def test_drop_item_fail(bwi):
    bwi.drop_item('dagger')
    bwi.drop_item('axe')
    assert bwi.slots == {}

# input gatherer, test in integration
def test_examine_item():
    pass


# Test equip instantiation and methods
def test_equip_call(win):
    win.equip_item('dagger')
    assert win.placement['slot']['hand']['name'] == 'dagger'

def test_unequip_call(wi2, capsys):
    wi2.unequip(itm['dagger'])
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "da fuq\nsuccess"
    assert wi2.placement['slot']['hand'] == {'nothing':'nothing'}