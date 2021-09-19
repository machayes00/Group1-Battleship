# Import class methods needed for the program
#Note: Comments starting with G made by George
from Board import *


'''
Battleship-G1.py interacts with players to obtain values for the parameters
for methods that set up the game boards, and then it interacts with players
to obtain shooting coordinates while playing the game. It modifies the game
boards according to payer inputs.
The program first obtains the number of ships (same for each player), then
sets up a board for each player, calling the setup() method for each player.
Once setup completes, the program calls the playGame() method, which interacts
with players while they are taking shots trying to hit ships on the opponent's
board.

The top part of this file lists all the methods, and this is followed by the
program that sets up and plays the game.
'''

##  Documentation for setup method
#   @brief Interacts with player to set up a board with ships for a player
#   @param board is a Board object for a player
#   @param numberShips is an int, same for 2 players
#   @pre board object must have correct properties; numberShips must be
#       in the proper range, 1 to 6
#   @post the input board object is modified according to user input

# def checkvalidinput(x):


def setup(board, numberShips):
    """!
    In addition to the code from createBool, need to add more checks using
    the waterGrid array from board, which this method should update
    with ship locations.
    """

    for len in range(1, numberShips+1):
        # tf = True
        while True:
            startx = (ord(input("\nWhat is the starting column of your ship? (A-J)\n")) % 32) - 1
            # a=97, b=98, ... A=65, B=66, ... so subtracting taking mod 32 should get the values we want
            if startx not in range(0, 10):
                print("\nInvalid column.\n")
            else:
                break

        while True:
            starty = int(input("\nWhat is the starting row of your ship? (1-9)\n")) - 1
            if starty not in range(0, 9):
                print("\nInvalid row.\n")
            else:
                break

        orientation = {'R', 'r', 'D', 'd'}

        while True:
            orient = input("Enter the orientation of ship" + str(len) + ". (R|r for horizontal, D|d for vertical)\n")
            # print("Please enter the starting row for you ship: ")
            # print('"L" for left of start (horizontal ship)\n')
            # print('"R" for right of start (horizontal ship)\n')
            # print('"U" for up from start (vertical ship)\n')
            # print('"D" for down from start (vertical ship)\n')
            if orient not in orientation:
                print("Please enter a valid input. (R|r for horizontal, D|d for vertical)")
            else:
                if(board.isShipValid(startx, starty, orient, len)):
                # board.createShip(startx, starty, orient, numberShips, symbol)
                    board.createShip(startx, starty, orient, len, len)
                # else:

                break



        # if 0 <= startx <= 9 and 0 <= starty <= 8: # Edina: changed since we converted to index
        #     break
        # else:
        #     print("\nInvalid column and/or row number\n")


'''

    symbol = numberShips # this will be updated in the for loop, so different for each ship
    for i in range(numberShips):
        start=0

        #This could be changed to handle excetions, but I don't really see the difference unless we catch type errors too
        #so that's a possible continuation
        while True:
            startx = (ord(input("\nWhat is the starting column of your ship?\n")) % 32) - 1
            # a=97, b=98, ... A=65, B=66, ... so subtracting taking mod 32 should get the values we want
            starty = int(input("\nWhat is the starting row of your ship?\n")) - 1
            if 0 <= startx <= 9 and 0 <= starty <= 8: # Edina: changed since we converted to index
                break
            else:
                print("\nInvalid column and/or row number\n")

        print()

        orientation = {'L', 'R', 'U', 'D', 'l', 'r', 'u', 'd'}
        ooo = {"H", 'h', 'V', 'v'}
        while True:
            print("Enter the orientation of ship (H|h for horizontal, V|v for vertical)", i, '\n')
            # print("Please enter the starting row for you ship: ")
            # print('"L" for left of start (horizontal ship)\n')
            # print('"R" for right of start (horizontal ship)\n')
            # print('"U" for up from start (vertical ship)\n')
            # print('"D" for down from start (vertical ship)\n')
            orientInput = input()
            orient = orientInput.upper()
            if orient == 'L' or orient == 'R' or orient == 'U' or orient == 'D':
                break
            else:
                print("Invalid direction for ship")

        # the bool method is probably fine but the above code also checks if valid
        # so for now I commented out temporarilty just to see if things work, to minimize fail points
        # if(board.isShipValid()):
        board.createShip(startx, starty, orient, numberShips, symbol)
        symbol = symbol - 1 # so symbol entered for next ship will be smaller number
'''


##  Documentation for playGame method
#   @brief interacts with both players, and takes their inputs for shooting coordinates
#   @param boardPlayer1 is a Board object bodified by the setup() method
#   @param boardPlayer2 is a Board object bodified by the setup() method
#   @pre appropriate Board objects must be passed in, after setup() modification
#   @post


def playGame(board1, board2):

    choice = 0
    turn = 1
    while (choice != 3):
            #Alex: There should be an addition to this while loop here checking if all ships are sunk on either side
            #Edina: while loops including for printMenu should be outside, in playGame
        if turn % 2 == 1:
            print("OPPONENT BOARD:")
                    #method to print "hidden" version of boardPlayer2
            print("\nPLAYER BOARD:")
            board1.printBoard()
        elif turn % 2 == 0:
            print("OPPONENT BOARD:")
                    #method to print "hidden" version of boardPlayer1
            print("\nPLAYER BOARD:")
            board2.printBoard()
        # Added by Edina.
            # Edina note: probably need to add in option to hide boards,
            # to prepare for next player.I don't think we can make a call
            # to terminal to hide stuff, so maybe print a long vertical
            # line of stars, to hide boards.
            # Edina: Alex's mod of the printMenu had lines of code
            # asking for shooting coordinates, but those lines belong in
            # playGame, not in a print menu. printMenu is called by playGame,
            # takes in user choice and returns that choice to the playGame f'n.
            # So for now the rest of the print menu is from George's original version
            # which probably needs modifications still -- I did not disturb it
            # except for choice 1 (to fit Alex's mod) but I added some comments
        # return this choice to playGame and start shootin')
                # with this choice returned to playGame, it could call a shoot method
                # added by Edina; return this to playGame which called printMenu
    # Ths next part starts the program.
    '''
    stopgame = 0  # variable for giving option to quit game or play again, once a game is over
    while stopgame == 0:
        print('\n *** WELCOME TO BATTLESHIP!! ***')
        print()
        # Maybe add instructions from George's printMenu here. But our Project 1 instructions
        # stated that the game should be "obvious" and not need much instrucion. So maybe
        # it is better if the short prompts for user input, plus feedback to user, will let
        # the user understand the game.

        choice = 0  # bool for marking acceptable choice for numberShips
        while choice == 0:
            print('How many ships per player for this game?')
            print('Enter a number from 1 to 6:')
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
        # Once playGame method ends, give players the option to play again rather than exit program.

        print("\nWould you like to play another game?\n")
        print('Enter "Y" for yes, "N" for no:\n')
        choice = input()
        if input == "N" or "n":
            stopgame = 1
    '''

def play():
    stopgame = 0  # variable for giving option to quit game or play again, once a game is over
    while stopgame == 0:
        print('\n *** WELCOME TO BATTLESHIP!! ***')
        print()
        # Maybe add instructions from George's printMenu here. But our Project 1 instructions
        # stated that the game should be "obvious" and not need much instrucion. So maybe
        # it is better if the short prompts for user input, plus feedback to user, will let
        # the user understand the game.

        choice = 0  # bool for marking acceptable choice for numberShips
        while choice == 0:
            print('How many ships per player for this game?')
            print('Enter a number from 1 to 6:')
            numberShips = int(input())
            shipcount = {1, 2, 3, 4, 5, 6}
            if numberShips in shipcount:
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

        playGame(boardPlayer1, boardPlayer2)

        print("\nWould you like to play another game?\n")
        print('Enter "Y" for yes, "N" for no:\n')
        choice = input()
        if input == "N" or "n":
            stopgame = 1

play()
