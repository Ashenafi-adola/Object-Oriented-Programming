class Player:
    def __init__(self, name, location):
        self.name = name
        self.inventory = []
        self.location = location

    def move(self, direction):
        if direction == "south":
            print("want go to south")
        elif direction == "north":
            pass
        elif direction == "east":
            pass
        elif direction == "west":
            pass
        else:print("unknown direction!go")

    def take_item(self, item):
        if item in self.location.items:
            self.inventory.append(item)
            self.location.remove_item(item)
        else:
            print(f"This room does't have item {item}")

    def use_item(self, item):
        if item in self.inventory:
            if item == "keys":
                for i in self.location.exits:
                    if self.location.exits[i] == "locked":
                        print("unlocked")
            else:print("can't use this tool")
        else:print("don't have such tool!")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.location.put_item(item)
        else:
            print(f"player does't have item {item}")
    def show_inventory(self):
        for i in self.inventory:
            print(i)

class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.exits = dict
        self.items = []

    def describe(self):
        print(self.description)

    def put_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_items(self):
        for i in self.items:
            print(i)

class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.can_be_taken = bool

    def describe(self):
        print(self.description)

Lobby = Room(
    'Lobby',
    "You are in a dusty lobby. To the north is a locked door. To the east is a kitchen. A rusty key sits on a table."
)
Lobby.exits = {"north": 'locked', "east": "to kitchen"}
Lobby.items = ['keys']

Kitchen = Room(
    "Kitchen",
    "The kitchen is filled with cobwebs. A recipe book lies on the counter. The only exit is back west."
)
Kitchen.exits = {"west": "to lobby"}
Kitchen.items = ['books']

Library = Room(
    "Library",
    "A grand library filled with ancient texts. A strange lockbox sits on a desk."
)
Library.exits = {"south": "to hellway"}
Library.items = ["lockbox"]

Hellway = Room(
    "Hellway",
    "A long hallway with doors to the north and east."
)
Hellway.exits = {"north": "to library"}

player = Player(
    "ashe",
    Lobby
)
player.inventory = ["book", "Knife", "keys"]