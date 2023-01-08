import pyxel as px 


class DisplayImage:
    """Parent class for all displayed objects"""
    def __init__(self, x, y, bank, u, v, w, h, colkey=7) -> None:
        self.x = x
        self.y = y
        self.bank = bank
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)

# class DisplayTopLayer(DisplayImage):
#     def __init__(self, x, y, bank, u, v, w, h, colkey=7) -> None:
#         super().__init__(x, y, bank, u, v, w, h, colkey)

class Sprite(DisplayImage): 
    """Parent class for all objects that can move"""
    def __init__(self, u, v, x=96, y=24, bank=2, w=16, h=16, colkey=7) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.running= False

    def run(self):
        if self.running == False:
            self.y -= 2
            # // Transforming logic //
            # self.u += 8
            self.running = True
        elif self.running == True:
            self.y += 2
            # // Transforming logic //
            # self.u -= 8
            self.running = False

class Background(DisplayImage):
    """Class for all background images"""
    def __init__(self,  u, v, bank=0, x=72, y=8, w=128, h=128):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.u = u
        self.v = v
        self.bank = bank

        super().__init__(self.x, self.y, self.bank, self.u, self.v, self.w, self.h)

    def draw(self):
        px.bltm(self.x, self.y, tm=self.bank, u=self.u, v=self.v, w=self.w, h=self.h)

class Clickable:
    """"parent class for all objects that use hover or on click effects"""
    def intersects(self, mouse_location:tuple):
        is_intersected = False
        if (
            px.mouse_x > self.x and px.mouse_x < self.x + self.w
            and px.mouse_y > self.y and px.mouse_y < self.y + self.h + 2
        ):
            is_intersected = True
            return is_intersected

    def intersection(self):
        pass

class Sidebar(DisplayImage):
    """Side bar images for character info and items."""
    def __init__(self, x, y, u, v, name, offset, w=64, h=128, bank=0) -> None:
        self.name =name
        self.offset = offset
        super().__init__(x, y,bank, u, v, w, h)

    def draw(self):
        px.bltm(self.x, self.y, tm=self.bank, u=self.u, v=self.v, w=self.w, h=self.h)
        px.text(self.x + self.offset, self.y+8, f'{self.name.title()}', 10)

class Entrance(DisplayImage, Clickable):
    """ Images that display and use hover/onflick to provide routing from the townscreen"""
    def __init__(self, entrance_dict:dict):
        self.name= entrance_dict['name']
        self.x = entrance_dict['x']
        self.y = entrance_dict['y']
        self.bank = entrance_dict['bank']
        self.u = entrance_dict['u']
        self.v = entrance_dict['v']
        self.w = entrance_dict['w']
        self.h = entrance_dict['h']
        self.colkey = entrance_dict['colkey']
        self.entrance_dict = entrance_dict
        self.color = entrance_dict['color']
        self.offset = entrance_dict['offset']

    
    def intersection(self):
        self.flag = Pointer(self.entrance_dict)
        self.flag.draw()
        px.text(self.x - self.offset, self.y - 24, self.name, self.color)

# class Button(Clickable, DisplayImage): 
#     def __init__(self, x, y, bank, u, v, w, h, owner) -> None:
#         super().__init__(x, y, bank, u, v, w, h)
#     def intersection(self):
#         owner._next_state = BlacksmithScreen(self.game)

class ShopItem(Clickable, DisplayImage):
    """Items to display in the shop that will (eventually) hook up to the items dictionary"""
    def __init__(self, x, y, u, v, w, h, name, item_stat, price, slot, id, description, bank=2, colkey=7) -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.item_stat = item_stat
        self.price = price
        self.name =name
        self.slot = slot
        self.description =description
        self.id = id


    def intersection(self):
        px.text(84, 84, self.name, 7)
        px.text(84, 92, f"Price: {self.price} ", 7)
        px.text(127, 92, f'Slot: {self.slot}', 7)
        px.text(84, 108, f'{self.description}', 7)
        if self.id in range(3):
            px.text(84, 100, f'DAM: {self.item_stat}', 7)
        elif self.id in range(3, 6):
            px.text(84, 100, f"DEF: {self.item_stat}", 7)
        elif self.id in range(8,11):
            px.text(84, 100, f'HEAL: {self.item_stat}', 7)



class Button(Clickable, DisplayImage): 
    def __init__(self, owner=None, x=152, y=127, bank=1, u=0, v=0, w=32, h=8, colkey=10, use:str = "Town") -> None:
        super().__init__(x, y, bank, u, v, w, h, colkey)
        self.owner = owner
        self.use= use

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 8, self.y +2, F'{self.use}', 7)


class ExploreButton(Button):
    def __init__(self, owner, x=120, y=72, bank=1, u=0, v=0, w=32, h=8, colkey=10) -> None:
        super().__init__(owner, x, y, bank, u, v, w, h, colkey)
    
    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        px.text(self.x + 2, self.y +2, "Explore", 7)

class AddStat(Button):
    def __init__(self, player:object, stat:object, stat_location_x:int, stat_location_y:int, bank=1, colkey=10, use='+') -> None:
        self.stat_object = stat
        self.stat = stat.stat
        self.min = stat.stat
        # self.stat_index = stat_index
        self.player = player
        self.name = 'Plus' if use == '+' else "Reduce"
        self.stat_location_x = stat_location_x
        self.stat_location_y = stat_location_y
        self.x = stat_location_x + 24 if self.name == 'Plus' else self.stat_location_x - 10
        self.y = stat_location_y - 2
        self.bank = bank
        self.u = 32
        self.v = 152 if self.name == 'Plus' else 144
        self.w = 8
        self.h = 8
        self.colkey = colkey

    
    def intersection(self):
        if self.name == 'Plus':
            px.text(120, 86, f"Cost: {self.stat*4}", 7)
            px.text(120, 94, f"MON: {self.player.currency}", 7)
            if px.btn(px.MOUSE_BUTTON_LEFT):
                # if self.player.currency >= self.stat * 4:
                    # self.player.currency -= self.stat * 4
                self.stat_object.stat +=1
                self.stat = self.stat_object.stat

        if self.name == "Reduce":
            if self.stat_object.stat > self.min:
                px.text(120, 86, "Click to reduce", 7)
                px.text(120, 94, f"Refund: {(self.stat_object.stat -1) *4}", 7)
                if px.btn(px.MOUSE_BUTTON_LEFT):
                    self.stat_object.stat -=1
                    self.stat = self.stat_object.stat

    def draw(self):
        px.blt(self.x, self.y, self.bank, self.u, self.v, self.w, self.h, colkey= self.colkey)
        # px.text(self.stat_location_x, self.stat_location_y, F'{self.stat_name}:{self.stat}', 7)


class LevelUpStat(DisplayImage):
    def __init__(self, x:int, y:int, stat_name:str, stat:int) -> None:
        self.x = x
        self.y = y
        self.stat_name = stat_name
        self.stat = stat
        self.bank = 0

    def draw(self):
        px.text(self.x, self.y, F'{self.stat_name}:{self.stat}', 7)
            

# class SaveStatsButton(Button):
#     def __init__(self, player:object, stat_object:object, stat_object2:object, stat_object3:object, stat_object4:object, x=120, y=74, bank=1, u=0, v=0, w=32, h=8, colkey=10, use: str = "Save Stats") -> None:
#         super().__init__(x, y, bank, u, v, w, h, colkey, use)
#         self.player=player
#         object_list = [stat_object, stat_object2, stat_object3,stat_object4]
#         self.strength = [stat for stat in object_list if stat.stat_name =='STR'][0].stat
#         self.dexterity = [stat for stat in object_list if stat.stat_name == 'DEX'][0].stat
#         self.intelligence = [stat for stat in object_list if stat.stat_name =='INT'][0].stat
#         self.constitution = [stat for stat in object_list if stat.stat_name =='CON'][0].stat

#     def intersection(self):
#         if px.btn(px.MOUSE_BUTTON_LEFT):
#             self.player.strength = self.strength
#             self.player.dexterity = self.dexterity
#             self.player.constitution = self.constitution
#             self.player.intelligence = self.intelligence
#             Interactible.main = []
#             interactible.main += interactible.frozen

class Rat(Sprite): 
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.u = 32
        self.v = 0
        self.w = 16
        self.h = 16
        super().__init__(x=self.x, y=self.y, bank=0, u=self.u, v= self.v, w=self.w, h=self.h)

class Mouse(Sprite):
    def __init__(self, x, y,u=0) -> None:
        self.u = 8
        super().__init__(x, y, 0, 0, 16, 8, 8)

    
class Pointer(Sprite):
    """A companion for the houses on the town screen to give info on what the house is."""
    def __init__(self, entrance_dict:dict) -> None:
        self.x = entrance_dict['x']
        self.y = entrance_dict['y'] - 16
        self.u = entrance_dict['u']
        self.bank = entrance_dict['bank']
        self.v = entrance_dict['v']-16
        self.w = entrance_dict['w']
        self.h = entrance_dict['h']
        self.colkey = 0
        super().__init__(x=self.x, y=self.y, bank=self.bank, u=self.u, v= self.v, w=self.w, h=self.h, colkey=self.colkey)
