# Import class methods needed for the program
from Board import *
import string


'''
a short sum of this file here.
'''

##  Documentation for setup method
#   @brief Interacts with player to set up a board with ships for a player
#   @param board is a Board object for a player
#   @param numberShips is an int, same for 2 players
#   @pre board object must have correct properties; numberShips must be
#       in the proper range, 1 to 6
#   @post the input board object is modified according to user input
def setup(board, numberShips):
    """!
    Still need a fix for variable ship size
    """
    # symbol = numberShips # this will be updated in the for loop, so different for each ship
    for i in range(numberShips):
        start=0

        # Edina: I liked how in Alice's version the checks were split for start x and start y
        # so user gets feedback for each input -- can fix this later
        while True:
            startx = input("\nWhat is the starting column of your ship? (A-J)\n")
            startx_num = (ord(startx) % 32) - 1
            if len(startx) == 1:
                if startx.isalpha() and startx_num in range(0,10):
                    break
                print("That's not a valid option! Please enter a letter between A through J.")
            else:
                print("Please enter only one character")

        while True:
            starty = input("\nWhat is the starting row of your ship? (1-9)\n")
            if starty.isnumeric():
                starty_num = int(starty) - 1
                if starty_num in range(0,9):
                    break
                else:
                    print("That's not a valid option! Please enter a num from 1 through 9.")
            else:
                print("That's not a valid option! Please enter a num from 1 through 9.")
'''
        # guessInLower = userInput.lower()
        while True:
            while True:
                try:
                    startx = (ord(input("\nWhat is the starting column of your ship? (A-J)\n")) % 32) - 1
                    break
                except TypeError:
                    print("That's not a valid option! Please enter a letter between A through J.")

            if startx not in range(0, 10):
                 print("\nInvalid column.\n")
            else:
                 break

            # a=97, b=98, ... A=65, B=66, ... so subtracting taking mod 32 should get the values we want
            # subtract 1 to convert input to array index.
            while True:
                try:
                    starty = int(input("\nWhat is the starting row of your ship?\n")) - 1
                except:
                    print("That's not a valid option! Please enter a letter between A through J.")

            if starty not in range(0, 9):
                 print("\nInvalid row.\n")
            else:
                 break

        print()

        while True:
            print('What is the orientation of this ship? Enter\n')
            print('"L" for left of start (horizontal ship)\n')
            print('"R" for right of start (horizontal ship)\n')
            print('"U" for up from start (vertical ship)\n')
            print('"D" for down from start (vertical ship)\n')
            orientInput = input()
            orient = orientInput.upper()
            if orient == "L" or "R" or "U" or "D":
                break
            else:
                print("Invalid direction for ship")

        # Bool method should check to make sure ship being created does
        # not overlap with a coordinate that is not an "O" letter
        if(board.isShipValid()):
            board.createShip(startx, starty, orient, i, i)
            # symbol = symbol - 1 # update variable so symbol entered for next ship will be smaller number

'''

##  Documentation for playGame method
#   @brief interacts with both players, and takes their inputs for shooting coordinates
#   @param boardPlayer1 is a Board object modified by the setup() method
#   @param boardPlayer2 is a Board object modified by the setup() method
#   @pre appropriate Board objects must be passed in, after setup() modification
#   @post none
def playGame(boardPlayer1, boardPlayer2):
    """
    Thismethod asks players to enter the coordinates for shooting at ships,
    and then calls the board.hits method to check hits and if sunk, and
    calls the the board.score method to keep track of remaining ships.
    """
    turn=1
    quit= False
    while boardPlayer1.allsunk == False and boardPlayer2.allsunk == False and quit == False:
        if printMenu(boardPlayer1,boardPlayer2,turn) == 3:
            quit=True
        else:
            xhit = (ord(input("\nWhat collumn?\n")) % 32) - 1
            yhit = int(input("\nWhat row?\n")) - 1
            if turn%2 == 1:
                boardPlayer2.hit(yhit,xhit)
                boardPlayer1.score(boardPlayer2)
            elif turn%2 == 0:
                boardPlayer1.hit(yhit,xhit)
                boardPlayer1.score(boardPlayer2)
            turn=turn+1

def printMenu(board1, board2,turn):
    """
    Print menu items and boards for the players.
    """
    choice = 0
    if turn % 2 == 1:
        print("OPPONENT BOARD:")
        board2.printOpp()
        print("\nPLAYER BOARD:")
        board1.printBoard()
    elif turn % 2 == 0:
        print("OPPONENT BOARD:")
        board1.printOpp()
        print("\nPLAYER BOARD:")
        board2.printBoard()
    while choice != 3:
            print("Please select a menu option:\n")
            # Added by Edina.
            # Edina note: probably need to add in option to hide boards,
            # to prepare for next player.I don't think we can make a call
            # to terminal to hide stuff, so maybe print a long vertical
            # line of stars, to hide boards.
            print("\n1) Take a Shot!\n2) Read rules \n3) Quit game")
            choice=int(input())

            if choice == 1:
                return(1) # return this choice to playGame and start shootin'
            elif choice == 2:
                print("-----------------------------------------------------------------------------------------------------------------------------------------------Rules of Battleship-----------------------------------------------------------------------------------------------------------------------------------------------\n")
                print("Overview:\nBattleship is a two player game where both players secretly place 1 to 6 ships on a 9x10 grid. Taking turns each player announces where on the opponents grid they wish to fire. The opponent must announce whether or not one of the ships was hit. The first player to sink all of the oponents ships wins\n ")
                print("1)Ship size will be dependent on number of ships chosen. If one ship is chosen each player will be given a 1x1 ship . If two ships are chosen each player will be given a 1x1 and a 1x2 ship and so on.\n")
                print("2)After the ships have been chosen, players will be able to place and orient their ships, you may place your ship anywhere within the board and orient it up, down, left or right. You may not orient it diagonally or intersect another ship.\n")
                print("3)Taking turns, the users pick a space on the opponent's board to fire at,each shot must be updated to indicate a hit or miss.\n")
                print("4)Once a ship has been hit in every space it occupies, it is sunk.\n")
                print(
                    "5)As the great Colonel Sanders once said \"I'm too drunk to taste this fried chicken. \"\n ")
            elif choice == 3:
                print("\nGoodbye...")
                return(3)
            else:
                print("Sorry, invalid choice! Please pick again.\n")

# I like Alice's fix to put the starting part of the program below in its own method, because this
# facilitates documentation. But it should be called run() not play() because it is weird to have
# a play() method and a playGame() method. So I changed this back to Alice's format of new method.

def run():
    stopgame = 0  # variable for giving option to quit game or play again, once a game is over

    while stopgame == 0:

        print('\n *** WELCOME TO BATTLESHIP!! ***\n')
        print()
        # Maybe add instructions from George's printMenu here. But our Project 1 instructions
        # stated that the game should be "obvious" and not need much instrucion. So maybe
        # it is better if the short prompts for user input, plus feedback to user, will let
        # the user understand the game.

        choice = 0  # bool for marking acceptable choice for numberShips
        while choice == 0:
            print('How many ships per player for this game?\n')
            print('Enter a number from 1 to 6:\n')
            numberShips = int(input())
            if numberShips == 1 or 2 or 3 or 4 or 5 or 6:
                choice = 1
            else:
                print("Please enter a valid ship number.\n")

        # Create a board object for player 1
        boardPlayer1 = Board()

        print('\nReady to set up the board for Player 1!\n')

        # This step runs the setup method for Player 1. The method modifies
        # the waterGrid 2D array of boardPlayer1.
        setup(boardPlayer1, numberShips)

        # Create a board object for player 2
        boardPlayer2 = Board()

        print('\nReady to set up the board for Player 2!\n')

        # This step runs the setup method for Player 2. The method modifies
        # the waterGrid 2D array of boardPlayer2.
        setup(boardPlayer2, numberShips)

        # This now starts the shooting steps, printing printMenu() between each player's shot
        playGame(boardPlayer1, boardPlayer2)

        # Once playGame method ends, give players the option to play again rather than exit program.
        print("\nWould you like to play another game?\n")
        print('Enter "Y" for yes, "N" for no:\n')
        choice = input()
        if input == "N" or "n":
            stopgame = 1

run()
