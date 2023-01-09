from random import randint

from character_builder import Character
from npc_classes import RogueGoblin, GraithLizard, GraithTree, GraktaWolf, KraktRat, BrabaBat, ShadeFireFox, npc_class_choice, npc_class_dct, GraithQueen, GraithApple
from dicts import underbelly, shining_forest,input_options as i_u, encounter_dict
from text import text as txt



# starting combat would instantiate base classes and would include a method to determine how con affects hp
#method = roll stats
#character - class, race -
# self.armor = platemail or other item
# level ups = adding stats, figuring out 

craelios_strong = Character("Craelios",  20, 20, 20, 20, 20, 20) # Strong
craelios_strong.currency = 100
craelios_weak = Character("Craelios",  8, 8, 8, 8, 0, 4) # weak
craelios_weak.currency = 25
kraktar = Character("Kraktar", 6, 3, 3, 7, 5, 5)

# def random_encounter():
#     enemy_chooser = randint(1,7)
#     enemy_choice = npc_class_choice[enemy_chooser]
#     enemy_class = npc_class_dct[enemy_choice]
#     combat_start(enemy_class)


# Abstract encounter builder into 1 with a list or dictionary of the encounter percentages
def lvl1_encounter(location:str):
    percentile_roll = randint(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 50:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 50 and percentile_roll <= 95:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 95:
        enemy_class = npc_class_dct[encounter_dict[location][3]]
    # if enemy_class[0] == 'a':
    #     print(f'An {enemy_class.title()} appears out of the darkness!')
    # else:
    # print(f'A {enemy_class.title()} appears out of the darkness!')
    combat_start(enemy_class)

def lvl2_encounter(location:str):
    percentile_roll = randint(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 30:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 30 and percentile_roll <= 60:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 60:
        enemy_class = npc_class_dct[encounter_dict[location][3]]
    # if enemy_class[0] == 'a':
    #     print(f'An {enemy_class.title()} appears out of the darkness!')
    # else:
    #     print(f'A {enemy_class.title()} appears out of the darkness!')
    combat_start(enemy_class)

def lvl3_encounter(location:str):
    percentile_roll = randint(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 10:
        enemy_class = npc_class_dct[encounter_dict[location][1]]
    elif percentile_roll > 10 and percentile_roll <= 25:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 25:
        enemy_class = npc_class_dct[encounter_dict[location][3]]
    # if enemy_class[0] == 'a':
    #     print(f'An {enemy_class.title()} appears out of the darkness!')
    # else:
    #     print(f'A {enemy_class.title()} appears out of the darkness!')
    combat_start(enemy_class)

def lvl4_encounter(location:str):
    percentile_roll = randint(1,100)
    if percentile_roll == 100:
        enemy_class = npc_class_dct['shadefire_fox']
    elif percentile_roll <= 1:
        enemy_class = npc_class_dct[encounter_dict[location][2]]
    elif percentile_roll > 1 and percentile_roll <= 80:
        enemy_class = npc_class_dct[encounter_dict[location][4]]
    elif percentile_roll > 80:
        enemy_class = npc_class_dct[encounter_dict[location][6]]
    # if enemy_class[0] == 'a':
    #     print(f'An {enemy_class.title()} appears out of the darkness!')
    # else:
    #     print(f'A {enemy_class.title()} appears out of the darkness!')
    combat_start(enemy_class)
    return enemy_class

def combat_start(enemy_class):
    combat = (craelios_strong, enemy_class())
    combat.check_init()


def underbelly_area_1():
    count = 0
    print("\nYou enter the Underbelly and wend your way through the crevasses and crags of Thagrag's Hope.")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl1_encounter(underbelly)
        count += 1
        print(count)
        if craelios_strong.current_hp <=0:
            print(txt['underbelly_defeat'])
            break
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            underbelly_area_2()
            continue
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 
        elif keep_going in i_u['yes']:
            print(txt['continue_exploring'])
            continue
            
def underbelly_area_2():
    count = 0
    print("\nA waterfall deafens you as you enter the Web of the Depths.")
    print("Every surface is slick with moisture in this series of interwoven tunnels created by underground rivers.")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl2_encounter(underbelly)
        if craelios_strong.current_hp <=0:
            print(txt['underbelly_defeat'])
            break
        count += 1
        print(count)
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            underbelly_area_3()
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 4
        elif keep_going in i_u['yes']:
            print(txt['continue_exploring'])
            continue

def underbelly_area_3():
    count = 0
    print("\nOut of range of any natural light you navigate purely by your own light as you enter the Graith's Grotto.")
    print("Home to the lizards your people have learned to domesticate, none you might find here will be friendly.")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl3_encounter(underbelly)
        if craelios_strong.current_hp <=0:
            print(txt['underbelly_defeat'])
            break
        count += 1
        print(count)
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            underbelly_final_area()
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 4
        elif keep_going in i_u['yes']:
            # print('You continue exploring.')
            continue

def underbelly_final_area():
    print('\nYou tread even more softly as you pass into the deepest reaches of the Underbelly.')
    print("Back at the inn you'd heard whispers of a monstrous creature, far larger than any normal Graith'gesh Lizard.")
    print("Your heart beats faster with equal parts excitement and fear as the walls close in around you and you enter the Graith Queen's Lair.")
    enemy_class = lvl4_encounter(underbelly)
    if craelios_strong.current_hp <= 0:
        print("You know when you've bitten off more than you can chew. Retreat now, and live to fight another day.")
    elif enemy_class == 'graith_queen':
        print("You've done it. Killed a Graith Queen. The elders were right to say you've chosen the harder path.  Most wouldn't think to kill a Queen for their coming of age but here you are, alive and victorious. And you still have work to do.")
    else:
        print("Disappointment wars with relief inside you as you turn back towards town without having seen the fabled Queen.")



def shining_forest_area_1():
    count = 0
    print("\nYou walk towards the surface, leaving behind the familiar tunnels as the crisp mountain air and afternoon sunlight hit your face.")
    print("Your eyes take a moment to adjust before you can see the mountains of Kratab's Folly.")
    print("Towering mountains feel almost familiar but their twisted peaks point upwards into the vastness of the brilliant blue sky.")
    print("It will take some time before you can appreciate the savage beauty of the mountaintops as you do the roots of the mountain.")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl1_encounter(shining_forest)
        count += 1
        print(count)
        if craelios_strong.current_hp <=0:
            print(txt['shining_forest_defeat'])
            break
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            shining_forest_area_2()
            continue
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 4
        elif keep_going in i_u['yes']:
            print(txt['continue_exploring'])
            continue
            
def shining_forest_area_2():
    count = 0
    print("\nThe mountains finally level out into a shining mirrorlike plain, broken only by the malformed trunks of the trees that managed to claw their way to survival.")
    print("Dripping Death the elders called it.  A marsh that that separates the Goblins from the rest of our brothers to the north. Where anything can hide and everything would be happy to make you a dead little Goblin.")
    print("The hanging moss swaying in the breeze almost causing you to bolt. How long til the Graith Trees come for you?")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl2_encounter(shining_forest)
        if craelios_strong.current_hp <=0:
            print(txt['shining_forest_defeat'])
            break
        count += 1
        print(count)
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            shining_forest_area_3()
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 4
        elif keep_going in i_u['yes']:
            print(txt['continue_exploring'])
            continue

def shining_forest_area_3():
    count = 0
    print("\nDry land! After fighting your way through the marsh it's hard to keep from kissing the solid earth. As you finish wringing out your clothes you mentally name the forest {player.name}'s Respite")
    print("A bold move considering the Graith Trees will have more camouflage when creeping up on you but after the dismal, glaring grey of the marsh the sunlight green of forest feels like a godsend, even if it holds demons.")
    for i in range(3):
        print(txt['enemy_attacks'])
        lvl3_encounter(shining_forest)
        if craelios_strong.current_hp <=0:
            print(txt['shining_forest_defeat'])
            break
        count += 1
        print(count)
        keep_going = input(txt['explore_query'])
        if keep_going in i_u['yes'] and count == 3:
            shining_forest_final_area()
        elif keep_going in i_u['no']:
            print(txt['return_to_town'])
            return 4
        elif keep_going in i_u['yes']:
            # print('You continue exploring.')
            continue

def shining_forest_final_area():
    print('Your steps quicken as the ground starts to slope upwards again.  These mountains are the final barrier between you and your brothers and sisters to the north.')
    print("Even as you pick up the pace, your eyes continue to scan your surroundings feverishly.  While the trees are growing more scarce, there are plenty of stands for the Graith to hide.")
    print("As wend your way to a pass you see a magnificent gnarled fruit tree spreading over the path.  Your steps slow as you realize you haven't seen any other fruit trees in miles. Unfortunately there is no way around where the tree sits, its branches laden with bright red fruits that wink out like malevolent eyes from under its leaves.")
    while True:
        boss_prep = input("Are you ready?")
        if boss_prep in i_u['yes']:
            print("""As you draw closer the branches seem to shiver slightly in anticipation.
It is immobile for a long time, long enough to make you doubt your guess. But then the branches snap out like a nest of snakes, all trying to get the first bite.""")
            combat = (craelios_strong, GraithApple())
            if craelios_strong.current_hp <= 0:
                print("You feel yourself getting overwhelmed by the trees attacks and flee into a stand of trees, hopeful that their tight spacing prevents the Graith from following you.  AFter a few minutes of wild flight you pause, listening.")
                print("No sound. No crashing of a murderous tree. Not until the tree your slumped against explodes in a hail of needles and the Graith claims you as its latest victim.")
            else:
                print(txt['game_won'])
                break
        elif boss_prep in i_u['no']:
            print("You head back to town. Now you know the path and you'll come back when you're ready.")
            break

        else:
            input("Try again.")

    

# gogo = CombatDriver(craelios, RogueGoblin())
# gogo.check_init()


# lvl1_encounter()
# random_encounter()

# Combat Simulator:
# Craelios vs 3 goblin warriors, Kraktar sidelined

# def combat_round(PC, participant_2, participant_3, participant_4,):# participant_5) why is this messing up?
#     participant_list = [PC, participant_2, participant_3, participant_4]
#     friend = [PC]
#     foe = [participant_2, participant_3, participant_4]
#     for participant in participant_list:
#             if participant == PC:
#                 PC.attack(participant_2)
#             else:
#                 participant.attack(participant,PC)
#                 if PC.hp <= 0:      #health interogator needs to be earlier, and between all attacks.
#                     print("You died")
#                     break
#                 elif participant.hp <= 0:
#                     print("You won!")
#                     break
#                 elif participant.hp > 0 and PC.hp > 0: 
#                     combat_round(PC, participant_2, participant_3, participant_4)
                
                

# print("Combat Starting")
# combat_round(craelios, gob_war_1, gob_war_2, gob_war_3)

#if participant.dexterity == participant_list[max(participant.dexterity)]:  #pop the fastest, give it a turn
           # participant.attack(participant, )                                      #then return it to the list? or add init