import sys

class Board:
    def __init__(self):
        self.players = []
        self.pieces =[[0 for x in range(5)] for y in range(5)]

    def add_player(self, player, color):
        self.players.append(Player(player, color))

    def print_board(self):
        for x in range(5):
            print(self.pieces[x])

class Menu:
    def __init__(self):
        self.Board = None
        self.choices = {
            "1": self.start_game,
            "2": quit,
        }

    def create_board(self):
        self.board = Board()

    def create_players(self):
        self.create_player()
        self.create_player()

    def create_player(self):
        player = input("Enter player's name: ")
        color = input("Enter player's color: ")
        self.board.add_player(player, color)

    def display_menu(self):
        print(
            """
Connect4

1. Start Game
2. Quit
"""
        )

    def start_game(self):
        self.create_board()
        self.create_players()

        for i in range(2):
            self.board.players[i].make_move()

        self.quit()


    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("Exiting!")
        sys.exit(0)

class Piece:
    def __init__(self):
        pass

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_move(self):
        print(self.name, "made a move")

if __name__ == "__main__":
    menu = Menu()
    menu.run()

#how to name private functions with _?

