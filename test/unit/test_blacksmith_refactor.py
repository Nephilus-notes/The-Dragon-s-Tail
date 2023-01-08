# from test.conftest import end_game_character, early_game_character
# import blacksmith_refactor as bs 
# from dicts import items as itm
# import pytest



# def test_blacksmith_player_bag(end_game_character):
#     blacksmith = bs.ShopScreen(end_game_character)
#     blacksmith.menu_running == True

#     assert blacksmith.player.bag.slots['dagger']
#     assert blacksmith.player.bag.slots['axe']
#     assert blacksmith.player.bag.slots['sword']
#     assert blacksmith.player.bag.slots['leather_armor']

# def test_blacksmith_player_bag_add_item(end_game_character):
#     blacksmith = bs.ShopScreen(end_game_character)
#     blacksmith.menu_running == True
#     blacksmith.player.bag.add_item('chain_armor')
#     assert blacksmith.player.bag.slots['chain_armor']

# # @pytest.mark.skip
# def test_blacksmith_logic_add_item(end_game_character):
#     blacksmith = bs.ShopScreen(end_game_character)
#     blacksmith.menu_running == True
#     blacksmith.blacksmith_add_item(itm['chain_armor'])

# # @pytest.mark.skip
# def test_blacksmith_buy(end_game_character, monkeypatch):

# # builtins.input
# # sys.stdin
#     assert end_game_character.currency == 500

#     monkeypatch.setattr('builtins.input', lambda _: 'y')

#     blacksmith = bs.ShopScreen(end_game_character)
#     blacksmith.menu_running == True
#     result = blacksmith.blacksmith_buy(itm['dagger']) 
#     assert end_game_character.currency == 490
#     assert end_game_character.bag.slots['dagger']
