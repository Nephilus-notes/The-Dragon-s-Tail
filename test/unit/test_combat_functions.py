import pytest 

from old_code.npc_classes import GraithLizard
from test.conftest import combat_state


@pytest.mark.skip
def test_str_based_attack(combat_state):
    lizard = GraithLizard()

    lizard.attack(combat_state.player)
    lizard.attack(combat_state.player)
    lizard.attack(combat_state.player)
    lizard.attack(combat_state.player)
    lizard.attack(combat_state.player)
    assert combat_state.currency == 500
    lizard.current_hp = -2


