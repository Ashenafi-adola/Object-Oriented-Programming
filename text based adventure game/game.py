class Player:
    def __init__(self, name, inventory, location):
        self.name = name
        self.inventory = inventory
        self.location = location

    def move(self, direction):
        pass

    def take_item(self, item):
        pass

    def drop_item(self, item):
        pass

    def show_inventory(self):
        pass

class Room:
    def __init__(self, name, description, exits):
        self.name = name 
        self.description = description
        self.exits = exits
        self.items = []

    def describe(self):
        pass

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

class Item:
    def __init__(self, name, description, can_be_taken):
        self.name = name
        self.description = description
        self.can_be_taken = can_be_taken

    def describe(self):
        print(self.description)