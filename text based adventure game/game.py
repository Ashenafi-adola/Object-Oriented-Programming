import os

class Player:
    def __init__(self, name, inventory, location):
        self.name = name
        self.inventory = []
        self.location = location

    def move(self, direction):
        pass

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        for i in self.inventory:
            print(i.name)

class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.exits = dict
        self.items = []

    def describe(self):
        print(self.description)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

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
Kitchen.exits = {"west": "to kitchen"}
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