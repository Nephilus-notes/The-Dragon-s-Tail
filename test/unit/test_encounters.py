from old_code.npc_classes import GraithLizard, GraithTree, GraktaWolf, RogueGoblin, KraktRat, npc_class_choice, npc_class_dct
import pytest

def test_always_passes():
    assert True

@pytest.mark.xfail
def test_always_fails():
    assert False


def test_lvl_1_encounter():
    """
    GIVEN a lvl 1 encounter function
    WHEN it is accessed
    THEN an enemy is created for the player to fight

    """
    pass

