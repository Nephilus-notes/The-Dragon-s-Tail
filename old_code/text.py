text = {
    #  // Opening Text //
    'opening': """
Many years ago the Goblins lived peacefully above ground, in harmony with nature and the gods.

But then there was a Reckoning when the gods turned their backs on us, sending the Graith'Gesh,
unnaturals trees that could live in stone, walk, and even kill. They savaged our
people and forced them into the darkness of the tunnels. 

We did not despair, for we found a light in the darkness. A light within ourselves
that grew to encompass almost all of us.  That light we call the God's Glow, the 
surest sign that we will one day return to the land of the light.

And I think you may be the one to lead us.

Humble beginnings for someone who will do so much.  
What were they again?
""",
    'background_confirmation': """Aha! That's right.
I think that you will surprise us all.""",
    'ritual_start': """
Elder Bortorb's voice echoes in your mind as you walk the Path of Light towards the 
Town Shrine. The elders and much of the town are there when you arrive. Bortorb, the Eldest, Nakat'th
the Blacksmith, and Gragta'th, the Herbalist, ready to give their blessing to your 
Enlightening.

Nakat'th's clear voice rings out as you kneel.
"Rise and speak your name"
""",
    'ritual_end': """
{name}

"And the task you have chosen for your Enlightening?" Elder Gragta'th rumbles.

"To find our brothers and sisters to the north. To reunite us with our lost people."
Your words surprise you, but they feel right.

Whispers erupt from the gathered Goblins before Bortorb silences them and asks, 
"Are you sure? There are many other ways to prove your worth. Many shorter paths."
You see the worry in his eyes as you nod, not trusting yourself to speak.

"Very well then!" Nakat'th cuts in, "If that is your goal I will grant you access to me
and my forge as if you were a true Goblin.  Anyone with the guts enough to take on the 
Graith are going to need some help."

"You may also avail yourself of my knowledge and potions in your endeavors." Gragta'th
growls gently, his light swirling slightly.

"Then may the gods bless this quest that will bring us so much closer to them." 
Bortorb entoned, continuing with the ritual.

In the end you don't feel that different but you have a new goal:
To travel through the Shining Forest, in a world full of light and terrible bloodthirsty creatures,
to bring your people up from the Dragon's Tail.
""",


    #  // Character Builder Text //
    # Class background text
     'apprentice_blacksmith' : """Apprentice Blacksmith you say? Toughened by years of heating metal and bone to melting, you are strong 
and willing to put your body on the line for your people. [Increased Strength and Constitution] (Yes/No) """,
    'tunnel_rat': """Tunnel Scavenger eh?  Years of hiding from the predators in your home tunnels have made you quick and 
agile, faster than many of the creatures that roam the dark. [Increased Dexterity and Constitution] (Yes/No) """ ,
    'explorer': """Tunnel Explorer is it?  Few have gone as far into the darkness as you, and even fewer have ventured 
as far into the light. You are a hardy explorer, often using the rivers both 
above and belowground as highways. [Increased Constitution and Dexterity] (Yes/No) """,
    'apprentice_herbalist': """Oh? An Apprentice Herbalist? As an apprentice to Naer'shob, the town healer, you have learned much about herbs 
and magic. Practical applications are much harder but it will come in time. [Increased Intelligence and Dexterity] (Yes/No) """,

    # # // BLACKSMITH TEXT START //
    'welcome':"""\nYou step into a shop with black and silver shining at you from all around as arms and armor coat the walls.
The blacksmith's face shines at you from over the counter""",
    'arms_armor':'She says, "Are you looking to \n(1) protect yourself? \n\tOr \n(2) deal some damage?"\n(3) Leave\n:',
    'armor_menu':'''\n"We\'ve got all kinds of armor here:"\n(1) Leather Armor for 10 
(2) Chain Armor for 50 \n(3) Brigandine Armor for 75 \n(4) Bone Mail for 150 \n(5) Leave\n:''',
'weapon_menu':'''\n"A little bloodthirsty eh? Nothing wrong with that! Here's what we've got:
(1) Dagger for 10 \n(2) Sword for 30 \n(3) Axe for 45 \n(4) Leave\n:''',
'buy_prompt': "\n(Y) Would you like to buy {name} for {price}? \n(N) Or just keep browsing?\n:",
"bought": '''\nShe grunts cheerfully as she takes your money then says, "So... still looking to 
(1) protect yourself? \n\tOr \n(2) deal some damage?"\n(3) Leave\n:''',
'not_bought': '''\nShe sighs and says, "So... still looking to 
(1) protect yourself? \n\tOr \n(2) deal some damage?"\n(3) Leave\n:''',

    # // GEN TEXT START //
    "wrong_move":"invalid choice. Try again.",
    "shop_exit": "You exit the shop",
    'buy_item': "\nCongratulations on your new {name}!",

    # // TOWN TEXT START //
    "town_blurb": """You have arrived back home in Grik'tath.  You can hear the 
beating of iron coming from the blacksmith, smell grass and sky coming from the 
dark windows of the alchemist's shop, and see the calming glow of people 
in the inn.  There's also a path deeper underground into The Underbelly, 
or the tunnel outside to the Shining Forest. """,
    "town_query": """Where will your journey take you next? \n(1)The Blacksmith
(2)The Apothecary \n(3)The Inn \n(4)The Underbelly 
(5)The Shining Forest\n(c)Character info\n(Q)Quit: """,
    "town_try_again": """Hmm... I may be a little new here but I guess I've been 
    here longer than you. Do you want me to review that? (Yes/No) """, 
    "town_repeat": """Okay! \n(1)The Blacksmith
(2)The Apothecary \n(3)The Inn \n(4)The Underbelly \n(5)The Shining Forest\n(c)Character info """,
'town_decline': "Alright then.  Where do you want to go? ",
"inn_away":"Your feet turn away as you try to head to the inn. ",
'the_underbelly': "You think better of it. Monsters dwell there. ",
'the_shining_forest': """The tunnel to a land of light, air, and ravenous monsters
bent on goblin blood. Probably not worth it at this point. """,

    # // ITEM TEXT START //
    "full_pack": "Your pack is full. Would you like to drop something to pick up this {item}",
    'drop_prompt': 'Would you like to drop {item}?',
    'item_show': "\nCarried Items:\n{bar}",
    'drop_success': "You have dropped your {item}",
    'drop_fail': "You have dropped your {item}",
    'swap_prompt': "What would you like to drop? Enter corresponding number: ",
    'swap_wrong': "Enter the correct number or quit.",
    'equip_sucess': "You equip your {item}.",
    'equip_replace': 'There is {value} in that slot already. Would you like to replace it?(y/n) ',
    'wield_nothing': "You are wielding {value}",
    'wield_a': "You are wielding an {value}",
    'wield_not_a': "You are wielding a {value}",
    'wear': "You are wearing {value} on your {key}",

    # // ALCHEMY SHOP TEXT START // 
    'a_welcome': """\nYou duck your head as you step into the alchemists shop.  
Dried bundles of fungi, sticks, and even flowers festoon the walls and 
Garthak the Brewer is humming to himself as he grinds something with a pestle.
Looking up he flashes his sharp teeth in a smile. """,
'pots_pans_prompt': '''Well now. What can I get for you? 
    \n(1)Potions? \n(2)Amulets and medallions?" \n(3)Leave\n: ''',
'potion_menu': '''\n
"I thought you looked a bit peaky," Garthak says, 
squinting at you as he bustles around the counter 
to check you for injuries. "So. What'll it be?: 
\n(1)Small health potion 10 \n(2)Medium health potion 20 
(3)Large health potion 50"\n(4)Leave\n:''', 
"potion_anyway": '''\n"Hmm.... So you're looking for an accessory? Well I don't have any! 
 \n(1)Keep browsing\n(2)Leave with your head held high \n(3)Slink away in shame 
    \n(4) Leave\n:''',
'pots_pans2':'''
"Well now. That should help keep you in fine fighting form. 
Anything else I can get for you? 
\n(1)Potions? \n(2)Amulets and medallions?" \n(3)Leave\n: ''',
'pots_disappointed':'''
    \nOh very well. But don't blame me if you end up as plant food. 
    those Graithgresh trees aren't quite the pushovers I am. Anything else?
     \n(1)Potions? \n(2)Amulets and medallions?" \n(3)Leave\n:''',


    #  UNDERBELLY/COMBAT TEXT STARTS HERE
    'return_to_town': "You return to the town.",
    'continue_exploring': 'You continue exploring.',
    'enemy_attacks': "An enemy attacks!",
    'underbelly_defeat': 'You limp back to town, hiding in the deepest darkness to avoid any fights.',


    'explore_query': "The battle is finished. Would you like to continue on? ",


    'shining_forest_defeat':  'You limp back to town, staying as low to the ground as possible without entering any unknown caves.',
    'game_won':
"""\nThe Graith is a creature unlike anything you've ever fought but you feel it 
start to slow and fall as you keep up your attacks. It can no longer stop you 
from hewing directly at its trunk, cutting it down to size once and for all.
The top half of the Graith falls with a thunderous groan, and you can feel the 
magic drain from its now lifeless limbs.
\nYou hear echoing crashes coming from the valley as more trees fall behind you.
You stand for a moment, curious to see the source of the other crashes but you 
are so clsoe. The pass is clear and once you are through you see a vast plain unlike anything you've seen.
\nGentle, rolling hills dot the plain and you see smoke coming from the other side of a 
nearby hill. You hurry, excitement giving wings to your leaden body.  You crest the hill
and see a small circle of wooden wagons with strange people moving, dancing within.
They look nothing like Goblins! Yet their pink skin and tall frames remind you of something 
the elders spoke of."""
}