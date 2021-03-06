import sys
import random

class Board:
    def __init__(self):
        self.players = []
        self.pieces = [[Piece() for y in range(7)] for x in range(6)]

    def add_player(self):
        name = input("Enter player's name: ")
        self.players.append(Player(name))

    def select_color(self):
        colors = ["R", "Y"]
        random_player = random.choice([self.players[0].name, self.players[1].name])
        selected_color = input("\n" + random_player + " select your color between RED and YELLOW (R/Y): ")
        if selected_color in colors:
            j = colors.index(selected_color)
            for i in range(2):
                if self.players[i].name == random_player:
                    self.players[i].color = selected_color
                    self.players[1 - i].color = colors[1 - j]
        else:
            print("Please enter R or Y!")
            self.select_color()

    def print_board(self):
        for x in range(6):
            print(end = "|")
            for y in range(7):
                print(self.pieces[x][y].color, end = "|")
            print()

    def next_turn(self, turn):
        choice = False
        while not choice:
            column = self.players[turn].make_move(self.players[turn].name)
            choice = self.check_move(column, turn)

        row = self.add_piece(column, turn)
        if self.check_winner(row, column, turn):
            print("\nCongratulations {0}! You won the game!".format(self.players[turn].name))
            return True

    def add_piece(self, column, turn):
        for row in range(5,-1,-1):
            if self.pieces[row][column - 1].color != "0":
                continue
            else:
                self.pieces[row][column - 1].color = self.players[turn].color
                self.print_board()
                return row

    def check_move(self, column, turn):
        if self.pieces[0][column - 1].color != "0":
            print("\nNot a valid move! Please select again")
            return False

        return True

    def check_winner(self, row, col, turn):
        if self.horizontal_check(row, turn):
            return True
        if self.vertical_check(col, turn):
            return True
        if self.diagonal_check(turn):
            return True

        return False

    def horizontal_check(self, row, turn):
        for col in range(4):
            if self.pieces[row][col].color == self.players[turn].color and self.pieces[row][col+1].color == self.players[turn].color and self.pieces[row][col+2].color == self.players[turn].color and self.pieces[row][col+3].color == self.players[turn].color:
                return True

        return False

    def vertical_check(self, col, turn):
        for row in range(5,2,-1):
            if self.pieces[row][col-1].color == self.players[turn].color and self.pieces[row-1][col-1].color == self.players[turn].color and self.pieces[row-2][col-1].color == self.players[turn].color and self.pieces[row-3][col-1].color == self.players[turn].color:
                return True

        return False

    def diagonal_check(self, turn):
        for c in range(4):
            for r in range(5,2,-1):
                if self.pieces[r][c].color == self.players[turn].color and self.pieces[r-1][c+1].color == self.players[turn].color and self.pieces[r-2][c+2].color == self.players[turn].color and self.pieces[r-3][c+3].color == self.players[turn].color:
                    return True

        for c in range(4):
            for r in range(0,3):
                if self.pieces[r][c].color == self.players[turn].color and self.pieces[r+1][c+1].color == self.players[turn].color and self.pieces[r+2][c+2].color == self.players[turn].color and self.pieces[r+3][c+3].color == self.players[turn].color:
                    return True

        return False

class Piece:
    def __init__(self):
        self.color = "0"

class Player:
    def __init__(self, name):
        self.name = name
        self.color = None

    def make_move(self, name):
        while True:
            try:
                column = int(input("\n" + name + " select a column (1 to 7): "))
                if column > 7 or column < 1:
                    print("Invalid choice")
                else:
                    return column
            except ValueError:
                print("Please enter the number of the column!")

