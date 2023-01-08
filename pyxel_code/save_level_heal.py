import pyxel as px

from pyxel_code.image_classes import DisplayImage, Clickable, AddStat, LevelUpStat, Button
from pyxel_code.utils import Interactable, Layer



# Inn Functionality


class Save(DisplayImage, Clickable):

    def __init__(self, colkey=13) -> None:
        self.x=96
        self.y = 32
        self.bank = 0
        self.u = 0
        self.v = 144
        self.w = 16 
        self.h = 16
        self.colkey = colkey

    def intersection(self):
        px.text(84, 84, "save", 7)
        if px.btn(px.MOUSE_BUTTON_LEFT):
            # api call to save player state in the database
            # if successful px.text "saved" for 5 seconds (Integrate code to check the time)
            pass



class Level(DisplayImage, Clickable):
    def __init__(self, player:object, colkey=13) -> None:
        self.x=128
        self.y = 24
        self.bank = 0
        self.u = 32
        self.v = 64
        self.w = 16 
        self.h = 16
        self.colkey = colkey
        self.player = player
        self.stat_location = {
            1: {'x': 96, 'y':104},
            0: {'x': 152, 'y':104},
            2: {'x': 96, 'y':120},
            3: {'x': 152, 'y':120}
            }

    def intersection(self):
        px.text(84, 84, "level", 7)
        if px.btn(px.MOUSE_BUTTON_LEFT):
            for item in Interactable.main:
                Interactable.frozen.append(item)
            Interactable.main = []

            stats = []
            for index, val in enumerate(self.player.attribute_list):
                stat=LevelUpStat(self.stat_location[index]['x'], self.stat_location[index]['y'], stat_name=val['name'], stat=val['att'])
                Layer.fore.append(stat)
                stats.append(stat)

                plus= AddStat(self.player, stat = stat,
                stat_location_x=self.stat_location[index]['x'], stat_location_y=self.stat_location[index]['y'])
                minus= AddStat(self.player,stat = stat,
                stat_location_x=self.stat_location[index]['x'], stat_location_y=self.stat_location[index]['y'], use='-')
                Interactable.main.append(plus)
                Interactable.main.append(minus)
                Layer.fore.append(plus)
                Layer.fore.append(minus)

            self.save_stats = SaveStatsButton(self.player, *stats, self)
            self.cancel = CancelButton(self)
            Layer.fore.append(self.cancel)
            Layer.fore.append(self.save_stats)
            Interactable.main.append(self.cancel)
            Interactable.main.append(self.save_stats)

            
    def clear_save_values(self):
        del self.save_stats



class Rest(DisplayImage, Clickable):
    def __init__(self, colkey=13) -> None:
        self.x=160
        self.y = 32
        self.bank = 0
        self.u = 0
        self.v = 160
        self.w = 16 
        self.h = 16
        self.colkey = colkey

    def intersection(self):
        px.text(84, 84, "rest", 7)




class SaveStatsButton(Button):
    def __init__(self, player:object, stat_object:object, stat_object2:object, stat_object3:object, stat_object4:object, owner, x=112, y=74, bank=1, u=0, v=0, w=32, h=8, colkey=10, use: str = "Save Stats") -> None:
        super().__init__(x=x, y=y, bank=bank, u=u, v=v, w=w, h=h, colkey=colkey, use=use)
        self.player=player
        self.owner=owner
        object_list = [stat_object, stat_object2, stat_object3,stat_object4]
        self.strength = [stat for stat in object_list if stat.stat_name =='STR'][0]
        self.dexterity = [stat for stat in object_list if stat.stat_name == 'DEX'][0]
        self.intelligence = [stat for stat in object_list if stat.stat_name =='INT'][0]
        self.constitution = [stat for stat in object_list if stat.stat_name =='CON'][0]

    def intersection(self):
        if px.btn(px.MOUSE_BUTTON_LEFT):
            self.player.level_attribute(self.strength.stat_name, self.strength.stat)  
            self.player.dexterity = self.dexterity.stat
            self.player.constitution = self.constitution.stat
            self.player.intelligence = self.intelligence.stat
            for item in Interactable.main:
                if item != self:
                    del item
            Interactable.main = []
            Interactable.main += Interactable.frozen
            for item in Layer.fore:
                if item != self:
                    del item
            Layer.fore.clear()
            self.owner.clear_save_values()

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 2, self.y +2, F'{self.use}', 7)
        # px.text

class CancelButton(Button):
    def __init__(self, owner=None, x=96, y=127, bank=1, u=0, v=0, w=32, h=8, colkey=10, use: str = "Cancel") -> None:
        super().__init__(owner, x, y, bank, u, v, w, h, colkey, use)

    def intersection(self):
        if px.btn(px.MOUSE_BUTTON_LEFT):
            for item in Interactable.main:
                if item != self:
                    del item
            Interactable.main = []
            Interactable.main += Interactable.frozen
            for item in Layer.fore:
                if item != self:
                    del item
            Layer.fore.clear()
