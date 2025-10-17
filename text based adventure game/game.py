import os
import time
from theModule import *

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
os.system('cls')
while True:
    command = input("Enter your command: ")
    if command == "go":
        direction = input("Enter tool: ")
        time.sleep(2)
    if command == "use":
        tool = input("Enter direction: ")
        player.use_item(tool)
        time.sleep(2)
    elif command == "describe":
        player.location.describe()
        time.sleep(3)
    elif command == "drop":
        item = input("Enter item name: ")
        player.drop_item(item)
        time.sleep(3)
    elif command == "pick":
        item = input("Enter item name: ")
        player.take_item(item)
        time.sleep(3)
    elif command == "my items":
        player.show_inventory()
        time.sleep(3)
    elif command == "show items":
        player.location.show_items()
        time.sleep(3)
    os.system('cls')