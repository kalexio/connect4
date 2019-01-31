class Board:
    def __init__(self):
        self.players = []
        self.pieces =[[0 for x in range(6)] for y in range(7)]

    def add_player(self, player, color):
        self.players.append(Player(player, color))

    def print_board(self):
        for x in range(5):
            print(self.pieces[x])

    def next_turn(self, turn):
        self.players[turn].make_move()
        self.print_board()

class Piece:
    def __init__(self):
        pass

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_move(self):
        column = int(input("Player select a column (1 to 7): "))
        while column > 7 or column < 1:
            print("Invalid choice\n")
            column = int(input("Player select a column (1 to 7): "))

