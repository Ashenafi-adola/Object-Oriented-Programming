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
    def __init__(self, name, description, exits):
        self.name = name 
        self.description = description
        self.exits = exits
        self.items = []

    def describe(self):
        print(self.description)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self, name, description, can_be_taken):
        self.name = name
        self.description = description
        self.can_be_taken = can_be_taken

    def describe(self):
        print(self.description)