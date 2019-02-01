class Board:
    def __init__(self):
        self.players = []
        self.pieces =[[0 for x in range(7)] for y in range(6)]

    def add_player(self, player, color):
        self.players.append(Player(player, color))

    def print_board(self):
        for x in range(6):
            print(self.pieces[x])

    def next_turn(self, turn):
        column = self.players[turn].make_move()
        self.check_move(column, turn)
        self.add_piece(column, turn)

    def add_piece(self, column, turn):
        for row in range(5,-1,-1):
            if self.pieces[row][column - 1] != 0:
                continue
            else:
                self.pieces[row][column - 1] = turn + 1
                self.print_board()
                break

    def check_move(self, column, turn):
        if self.pieces[0][column - 1] !=0:
            print("\nNot a valid move!")
            self.next_turn(turn)

    def check_winner(self):
        pass

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

        return column
