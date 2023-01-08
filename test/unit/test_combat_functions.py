from old_code.npc_classes import GraithLizard, RogueGoblin
from test.conftest import early_game_character, end_game_character

def test_str_based_attack(end_game_character):
    lizard = GraithLizard()

    lizard.attack(end_game_character)
    lizard.attack(end_game_character)
    lizard.attack(end_game_character)
    lizard.attack(end_game_character)
    lizard.attack(end_game_character)
    assert end_game_character.currency == 500
    lizard.current_hp = -2

def test_rogue_goblin_attack(early_game_character):
    gob = RogueGoblin()

    gob.attack(early_game_character)
    gob.attack(early_game_character)
    gob.attack(early_game_character)
    gob.attack(early_game_character)


