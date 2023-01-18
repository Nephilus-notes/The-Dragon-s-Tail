from threading import Timer

from pyxel_code.utils import  Layer, Interactable




class DragonItem:
    def __init__(self):
        pass

class Backpack(DragonItem):
    def __init__(self, player:object, size=9):
        self.owner = player
        self.size = size
        self.slots = []
        self.slots_used = []
        self.potion_slots = {}
        self.potion_slots_used = []
        self.equipped = EquippedItems(self)

# add an item to your bag, or give you the chance to replace an item in your bag with something else.
    def add_item(self, item:object):
        try:
            item.freeze()
        except:
            pass
        if len(self.slots) < self.size:
            key = self.new_key(self.slots_used)

        if key <=2:
            item.y = 24
        elif key  >= 3 and key  <= 5:
            item.y = 40
        elif key  >= 6 and key  <= 8:
            item.y = 56

        if key == 0 or key == 3 or key == 6:
            item.x = 208
        elif key == 1 or key == 4 or key == 7:
            item.x = 224
        elif key == 2 or key == 5 or key == 8:
            item.x = 240

        item.bag_id = key
        self.slots.append(item)
        self.slots_used.append(key)
        try:
            melt = Timer(1, item.unfreeze)
            melt.start()
        except:
            pass

    def add_potion(self, item:object):
        if len(self.slots) < self.size:
            key = self.new_key(self.potion_slots_used)

        if key == 0:
            item.y = 88
        elif key == 1:
            item.y = 104
        elif key == 2:
            item.y = 120

        item.bag_id = key
        self.potion_slots[key] = item
        self.potion_slots_used.append(key)


    def use_potion(self, potion:object):
        self.owner.current_hp += potion.item_stat
        if self.owner.current_hp > self.owner.hp:
            self.owner.current_hp = self.owner.hp
        del self.potion_slots[potion.bag_id]


    def equip_item(self, item:object):
        self.equipped.slot[item.slot] = item
        self.owner.equip()

        item.x = 240
        if item.slot == "hand":
            item.y = 88
        elif item.slot == 'body':
            item.y = 112

        # remove item from backpack and slots used
        self.slots_used.remove(item.bag_id)
        if item in self.slots:
            self.slots.remove(item)

    def equip(self, item:object):
        if self.equipped.slot[item.slot] == {'nothing':'nothing'}:
            return self.equip_item(item)
        unequipped = self.equipped.slot[item.slot]
        self.equip_item(item)
        self.add_item(unequipped)

    def new_key(self, slots_used:list):
        min = 0
        if slots_used:
            for num in sorted(slots_used):
                if min == num:
                    min += 1
                elif min < num:
                    return min
        return min
                

    def draw(self):
        for item in self.slots:
            Layer.main.append(item)
            Interactable.main.append(item)

        for item in self.equipped.slot.values():
            if item != {'nothing':'nothing'}:
                Layer.main.append(item)
                Interactable.main.append(item)
        
        for item in self.potion_slots.values():
            Layer.main.append(item)
            Interactable.main.append(item)
        pass



class EquippedItems():
    def __init__(self, owner: Backpack, head_item:dict={'nothing':'nothing'}, body_item:dict={'nothing':'nothing'}, hand_item:dict={'nothing':'nothing'}):
        # I had empty slots as a dictionary nothing: empty. if  I want to return to that I can.
        self.slot = {'head':head_item,'body':body_item,'hand':hand_item}
        self.owner = owner

       
