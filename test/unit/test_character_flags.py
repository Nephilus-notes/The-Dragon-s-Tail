import pytest

from old_code.npc_classes import GraithApple, GraithLizard

def test_permanent_flags():
    """
    GIVEN flags for poison, stun, burning, and hit by wind in Character class
    WHEN a new Character child is instantiated
    THEN check the functions apply the correct flag
    """
    apple = GraithApple()
    apple.poison()
    apple.burn_baby_burn()
    apple.stun()
    apple.in_the_wind()
    assert apple.poisoned == True
    assert apple.stunned == True
    assert apple.burning == True
    assert apple.wind_hit_by == True

@pytest.mark.skip
def test_temp_flags():
    """
    GIVEN flags for poison, stun, burning, and hit by wind in Character class
    WHEN a new Character child is instantiated
    THEN check the functions apply the correct flag
    """
    apple = GraithApple()
    lizard = GraithLizard()
    apple.defend()
    apple.stone_armor()
    apple.dodge()
    apple.flee(lizard)
    apple.slow()
    apple.vulnerability()
    apple.stone_armor_2()
    apple.stony_fists()
    
    # Need one for burning blades eventually
    assert apple.defended == True
    assert apple.dodging == True
    assert apple.fleeing == True 
    assert apple.stone_armored == True
    assert apple.slowed == True
    assert apple.vulnerable == True
    assert apple.double_armed == True
    assert apple.burning_blades == False
    assert apple.stone_fists == True

@pytest.mark.skip
def test_flag_counts():
    """
    GIVEN flags for poison, stun, burning, and hit by wind in Character class
    WHEN a new Character child is instantiated
    THEN check the functions apply the correct flag
    """
    lizard = GraithLizard()
    apple = GraithApple()
    lizard.flee(apple)
    lizard.dodge()
    lizard.defend()
    assert lizard.fleeing == False
    assert lizard.flee_count == 1 
    assert lizard.defended == True
    assert lizard.dodging == True
    assert lizard.defend_round == 0
    assert lizard.dodge_round == 0
