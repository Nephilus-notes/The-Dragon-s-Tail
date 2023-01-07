# inventory is going to be best in a list (for now), so that it's easily modified, 
# And slots can be taken up by whichever items make sense.
# Now, the equipped inventory is going to be a dictionary
# so that particular body slots can be called by functions to
# define combat attributes, etc.
# I could even have a function that starts every combat that would 
# check equipped item slots, and adjust combat function accordingly

# Also, going from the inventory screen (Which will just have a list with numbers)
# will allow you to equip things. but... perhaps the full dictionary entry for the item
# will dictate which slot it can go into? more information about it!

from .dicts import items as itm
from .text import text as txt




class DragonItem:
    def __init__(self):
        pass

class Backpack(DragonItem):
    def __init__(self, size=5):
        self.size = size
        self.slots = {}

# add an item to your bag, or give you the chance to replace an item in your bag with something else.
    def add_item(self, item_name:str):
        if len(self.slots) <= self.size:
            self.slots[item_name] = itm[item_name]
        else:
            print(txt['full_pack'].format(item=itm[item_name]['name'].title()))
            switch_choice = input("(Y/N)").lower()
            if switch_choice == 'y':
                self.swap_items(item_name)
            elif switch_choice == 'n':
                drop_choice = input(txt['drop_prompt'].format(item=item_name))
                if drop_choice == 'y':
                    # add different verbiage
                    self.drop_item(item_name)
                elif drop_choice == 'n':
                    # self.add_item(item)
                    pass


    def show_items(self,):
        print(txt['item_show'].format(bar='~'*15))
        for slot in self.slots.keys():
            if True:
                print(itm[slot]['name'].title())

    def drop_item(self, item):
        if item in self.slots.keys():
            # print(item)
            del self.slots[item]
            print(txt["drop_success"].format(item=itm[item]['name'].title()))
            # print(itm[item]['name'].title())
        else:
            print(item)
            print(txt['drop_fail'])

    def examine_item(self, item):
        # allows the player to look at specific items, and equip or drop them from there.
        for key, value in itm[item].items():
            print("{key}: {value}".format(key=key.title(), value=value))
        exa_task = input("What would you like to do with this item? (Equip/Drop/Go back)").lower().strip()
        if exa_task == 'go' or exa_task == 'go back':
            pass
        elif exa_task == 'd' or exa_task == 'drop':
            self.slots.drop_item(item)
        elif exa_task == 'e' or exa_task == 'equip':
            # pack.equip_item will be an equip inventory function, similar to add_item
            pass

    def equip_call(self, item):
        pass

    def swap_items(self, new_item):
        print(txt['item_show'])
        swap_items = {}
        cnt = 1
        for item in self.slots.keys():
            print('({cnt}) {item}'.format(cnt=cnt, item =itm[item]['name'].title()))
            swap_items[cnt] = itm[item]
            cnt += 1
        swap_choice = input(txt['swap_prompt'])
        while True:
            try:
                swap_choice = int(swap_choice)
                if swap_choice > len(swap_items):
                    raise ValueError
                elif swap_choice <= len(swap_items):
                    break
        
            except (ValueError):
                    swap_choice = input(txt['swap_wrong'])
                    if swap_choice.lower() == 'q' or swap_choice.lower() == 'quit':
                        break
            
        for num, value in swap_items.items():
            if swap_choice == num:
                print(value['name'])
                self.drop_item(value['name'])
                swap_choice = 0
                self.add_item(new_item)

class EquippedItems():
    def __init__(self, owner: Backpack, size=3, head_item:dict={'nothing':'nothing'}, body_item:dict={'nothing':'nothing'}, hand_item:dict={'nothing':'nothing'}):
        # I had empty slots as a dictionary nothing: empty. if  I want to return to that I can.
        self.placement = {'slot':{'head':head_item,'body':body_item,'hand':hand_item}}
        self.size = size
        self.owner = owner

    def equip_item(self, item:str):
        # refactor to use item['slot'] 
        for key, value in self.placement['slot'].items():
            if key == itm[item]['slot']:
                if value == {'nothing':'nothing'}:
                    self.placement['slot'][key] = itm[item]
                    print(txt['equip_sucess'].format(item=itm[item]['name']))
                else:
                    choice = input(txt['equip_replace'].format(value=value)).lower().strip()
                    if choice == 'y':
                        self.owner.add_item(value)
                        self.placement['slot'][key] = itm[item]
                        self.owner.drop_item(itm[item]['name'])
                        print(txt['equip_sucess'].format(item=itm[item]['name']))
                    elif choice == 'n':
                        print(choice)
                        
                        pass
                    else:
                        print(choice + "damn")

    def show_equipped_items(self):
        print(txt['item_show'])
        for key, value in self.placement['slot'].items():
            if key == 'nothing' and key == "hand":
                print(txt['wield_nothing'].format(value=value))
            elif key == 'nothing' and key != "hand":
                print(txt['wear'].format(value=value, key=key))
            elif key == "hand" and value['name'][0] == 'a':
                # line above breaks sometimes TypeError, string indeces must be integers
                print(txt['wield_a'].format(value=value['name']))
            elif key == "hand" and value['name'][0] != 'a':
                print(txt['wield_not_a'].format(value=value['name']))
            else:
                print(txt['wear'].format(value=value['name'].title(), key=key))

    def unequip(self, item: dict):
        # rework this 
        print('da fuq')
        if self.placement['slot'][item['slot']] == item:
            self.placement['slot'][item['slot']] = {'nothing':'nothing'}
            print('success')

        # while True:
        #     try:
        #         for key, value in self.placement['slot'].items():
        #             # print(value['name'])
        #             if value == itm[item]:
        #                 print(item)
        #                 self.owner.add_item(item)
        #                 print(item)
        #                 self.placement['slot'][key] = {'nothing':'nothing'}
        #                 break
        #     except (TypeError):
        #         continue



# c_pack = Backpack()
# c_equip = EquippedItems(c_pack, hand_item='dagger')

# c_equip.equip_item('axe')
# c_equip.equip_item('bone_mail')
# c_equip.show_equipped_items()

# c_equip.unequip('axe')
# c_equip.show_items()



# c_pack.add_item("bone_mail")
# c_pack.add_item("dagger")
# c_pack.add_item("axe")
# c_pack.add_item("leather_armor")
# c_pack.add_item("sword")
# c_pack.add_item("chain_armor")
# c_pack.add_item("small_health_potion")


# c_pack.show_items()
# pack.drop_item("axe")
# pack.show_items()

# pack.examine_item("bone_mail")


equipped_items = {"head":'', "body":'chain armor', "hand":''}

inventory = {1:'', 2:'', 3:'', 4:'', 5:'',
6:'', 7:'', 8:'', 9:''}
inventory_list = ['healing potion']

def inventory_details(item_numbers, items_worn):
    key_count= 0
    for key, item in items_worn.items():
        print("\nYou are wearing {item} in your {key} slot.".format(item=item,key=key))
        key_count += 1
    # arrange a connection between dialogue and other code
    # equipped_description= f'''You are currently wearing an {equipped_items["head"]}, 
# {equipped_items["body"]} and wielding a {equipped_items['hand']}'''

    inventory_items = "What has it got in its pocketses?? Let's see!"
    
    print(inventory_items)
    if inventory_list:
        for item in inventory_list:
            print(item)
    elif not inventory_list:
        print("It's got nothing in its pocketses!!")


def inventory_screen():
    for value in inventory:
        item = 0
        if value:
            item += 1
    item_numbers = item
    
    items_worn ={}
    for key, value in equipped_items.items():
        if value:
            items_worn[key] = [value]

    inventory_details(item_numbers, items_worn)

# inventory_screen()

# inventory_screen()