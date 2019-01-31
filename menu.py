import sys
from board import Board

class Menu:
    def __init__(self):
        self.board = None
        self.choices = {
            "1": self.start_game,
            "2": self.quit,
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

        turn = False
        game_over = False
        while not game_over:
            self.board.next_turn(turn)
            turn = not turn

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


if __name__ == "__main__":
    menu = Menu()
    menu.run()

