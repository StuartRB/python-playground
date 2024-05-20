from utils.print_utils import slow_print


def start():
    print()
    slow_print("Welcome to...")
    print("")
    print("     ****************")
    print("     ** HALE QUEST **")
    print("     ****************")


class Game:
    def __init__(self, playerName):
        # The constructor method to initialize the attributes
        self.playerName = playerName
        self.inventory = []
        start()
        self.playerName = input("Please enter your name, brave adventurer: ")

    def add_item(self, item):
        self.inventory.append(item)
        return len(self.inventory)
