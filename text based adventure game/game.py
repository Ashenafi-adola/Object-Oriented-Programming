import os
import time
from theModule import *

os.system('cls')
while True:
    print(player.location.describe())
    command = input("Enter your command: ")
    match command:
        case "go":
            direction = input("Enter direction: ")
            player.move(direction)
            time.sleep(2)
        case "use":
            tool = input("Enter direction: ")
            player.use_item(tool)
            time.sleep(2)
        case "describe":
            player.location.describe()
            time.sleep(3)
        case "drop":
            item = input("Enter item name: ")
            player.drop_item(item)
            time.sleep(3)
        case "pick":
            item = input("Enter item name: ")
            player.take_item(item)
            time.sleep(3)
        case "my items":
            player.show_inventory()
            time.sleep(3)
        case "show items":
            player.location.show_items()
            time.sleep(3)
    
    os.system('cls')