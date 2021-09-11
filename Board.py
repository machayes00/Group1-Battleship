from Ship import *

class game:
    board = []
    def __init__(self):
        for x in range (0,9):
            self.board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def printBoard(self):
        for x in range (0,9):
            print(self.board[x])

g = game()
s = ship()
s.createship(g.board,0,0,'D',5)
g.printBoard()

