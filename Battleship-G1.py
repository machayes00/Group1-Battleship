# Import class methods needed for the program
from Board import *


def setup(board, numberShips): # parameter is a Board object
    """
    Need to transpot the createBool code lines from Alex & Mac's
    Ship class here. I was thinking of getting rid of the exceptions
    but actually they are fine in try-catch blocks, but I have to 
    figure out how to do that in Python.
    Also, in addition to the code from createBool, need more checks using
    the waterGrid Board property which this method should update
    with ship locations.
    """

    print('Please enter your ship(s) for your board:\n')

    for i in range(numberShips):

        # meke this a try-catch block to check acceptable arguments
        startCol = input("\nWhat is the starting column of your ship?\n")
        startRow = input("\nWhat is the starting row of your ship?\n")
        print()

        # I like the idea from Alice&George planning file, to use a
        # dictionary to covert coordidantes to index numbers for 
        # waterGrid 2D array.

        print('What is the orientation of this ship? Enter\n')
        print('"L" for left of start (horizontal ship)\n')
        print('"R" for right of start (horizontal ship)\n')
        print('"U" for up from start (vertical ship)\n')
        print('"D" for down from start (vertical ship)\n')

        # try catch block, using code from Alex's original Ship.py
        # createBool. But we don't need it to be a bool. Also, allow both
        # upper case and lower case entry.
        orient = input()

        board.createShip(startCol, startRow, orient, numberShips) 
        # enter correct arguments, icluding coversion for start coordinates.
        # This will update waterGrid for the next iteration of the for loop.

def playGame():
    """
    This is the method for asking players to enter the coordinates
    for shooting at ships, and then calling the board.chedkShots method and 
    the board.Score method.
    If this gets too complex, possibly make it a separate class,
    with propertyies that include Player objects(?) But my suggestion is
    to at least start it out in this file, in order to start simple and be able
    to test an early form of the game, the minimal things.
    """
    pass


def printMenu():

    """
    Print menu items for users, like option to print boards (or make
    that automatic as part of the setup?)  Also, option to quit, etc.
    """
    pass

# probably the code below should be in a while block, do while players
# don't want to quit

print('\n *** WELCOME TO BATTLESHIP!! ***\n')
print()

print('How many ships per player for this game?\n')
print('Ener a number from 1 to 6:\n')
# try-catch block or if-else to confirm good entry
numberShips = int(input())

# Create a board object for player 1
boardPlayer1 = Board()

print('\nReady to set up the board for Player 1!\n')

setup(boardPlayer1, numberShips)

# Create a board object for player 2
boardPlayer2 = Board()

print('\nReady to set up the board for Player 2!\n')

setup(boardPlayer2, numberShips)

playGame()

printMenu()







