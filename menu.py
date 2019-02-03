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
        self.board.add_player()

    def select_colors(self):
        self.board.select_color()

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
        self.select_colors()

        turn = 0
        game_over = False
        while not game_over:
            if turn == 2:
                turn = 0
            if self.board.next_turn(turn):
                game_over = True

            turn += 1

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

