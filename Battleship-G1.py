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
def setup(board, numberShips):
    """!
    In addition to the code from createBool, need to add more checks using
    the waterGrid array from board, which this method should update
    with ship locations.
    """

    for i in range(numberShips):
        start=0
        #This could be changed to handle errors, but I don't really see the difference unless we catch type errors too
        #so that's a possible continuation
        while True:
            startx = ord(input("\nWhat is the starting column of your ship?\n")) % 32
            # a=97, b=98, ... A=65, B=66, ... so subtracting taking mod 32 should get the values we want
            starty = int(input("\nWhat is the starting row of your ship?\n"))
            if 1 <= startx <= 10 and 1 <= starty <= 9:
                break
            else:
                print("\nInvalid column and/or row number\n")

        
        print()
        while True:
            print('What is the orientation of this ship? Enter\n')
            print('"L" for left of start (horizontal ship)\n')
            print('"R" for right of start (horizontal ship)\n')
            print('"U" for up from start (vertical ship)\n')
            print('"D" for down from start (vertical ship)\n')
            orient = input()
            if orient == ('L' or 'l' or 'R' or 'r' or 'U' or 'u' or 'D' or 'd'):
                break
            else:
                print("Invalid direction for ship")

        if(board.isShipValid()):
            board.createShip(startx, starty, orient, numberShips)
        

            # Enters correct arguments, including conversion for start coordinates.
            # This will update waterGrid for the next iteration of the for loop.
            

##  Documentation for playGame method
#   @brief interacts with both players, and takes their inputs for shooting coordinates
#   @param boardPlayer1 is a Board object bodified by the setup() method
#   @param boardPlayer2 is a Board object bodified by the setup() method
#   @pre appropriate Board objects must be passed in, after setup() modification
#   @post
def playGame(boardPlayer1, boardPlayer2):
    """
    This is the method for asking players to enter the coordinates
    for shooting at ships, and then calling the board.checkShots method and 
    the board.Score method.
    If this gets too complex, possibly make it a separate class,
    with propertyies that include Player objects(?) But my suggestion is
    to at least start it out in this file, in order to start simple and be able
    to test an early form of the game, the minimal things.
    """


    # Print menu (see next method) will print between each shoot
    printMenu(boardPlayer1, boardPlayer2)
    pass

#G: made a simple little menu, doesn't do anything right now. Used a while loop
# instead of a do-while because do-while loops don't exist in python
# Edina: did not change anything at all in George's print menu. I like how the instructions are not
# printed unless a player asks to see them. But what I was thinking is to have a menu that prints
# options repeatedly while the game is played. The idea is to have this method
# be called by the playGame() method between each turn. Something simple. We could also
# add a menu option to print boards but maybe a better idea is to have them print automatically
# each time a new turn is taken. So, something like this presented by playGame each time a new
# turn is taken:

# print("\nPlease select an option:\n(1) Take a shot\n (2) Read rules\n(3) Quit game\n ")

# Maybe printMenu should first print the player's own board by calling the appropriate printBoard
# method from Board class, then print the menu options, and if player selects to take s shot, 
# then pirnt the opponent's board.

# But the menu should be short since it is presented repeatedly for each player at ever single turn.

# Edina: I added in some of Alex's changes to printMenu
# His method made use of the Board objects as arguments but these were not included
# in the function signature so I added them -- it is the only change I made to his mod of the f'n
# The idea is, when this funcion is called, boardPlayer1 and boardPlayer2
# can be passed in, which allows calling printBoard methods on them, within
# the printMenu function
# So to call this function in playGame, you have to type:
# printMenu(boardPlayer1, boardPlayer2)
def printMenu(board1, board2): 
    """!
    Print menu items for users, like option to print boards (or make
    that automatic as part of the setup?)  Also, option to quit, etc.
    """
    
    choice = 0
    # The next lines were added by Alex
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

        print("Please select a menu option:\n") # Added by Edina.
        # Edina note: probably need to add in option to hide boards,
        # to prepare for next player.I don't think we can make a call
        # to terminal to hide stuff, so maybe print a long vertical
        # line of stars, to hide boards.
        print("\n1) Take a Shot!\n2) Read rules \n3) Quit game")

        # Edina: Alex's mod of the printMenu had lines of code
        # asking for shooting coordinates, but those lines belong in 
        # playGame, not in a print menu. printMenu is called by playGame,
        # takes in user choice and returns that choice to the playGame f'n.
        # So for now the rest of the print menu is from George's original version
        # which probably needs modifications still -- I did not disturb it
        # except for choice 1 (to fit Alex's mod) but I added some comments
        if(choice == 1):
            return (1) # return this choice to playGame and start shootin')
            # with this choice returned to playGame, it could call a shoot method

        elif(choice == 2):
            print("-----------------------------------------------------------------------------------------------------------------------------------------------Rules of Battleship-----------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("Overview:\nBattleship is a two player game where both players secretly place 1 to 6 ships on a 9x10 grid. Taking turns each player announces where on the opponents grid they wish to fire. The opponent must announce whether or not one of the ships was hit. The first player to sink all of the oponents ships wins\n ")
            print("1)Ship size will be dependent on number of ships chosen. If one ship is chosen each player will be given a 1x1 ship . If two ships are chosen each player will be given a 1x1 and a 1x2 ship and so on.\n")
            print("2)After the ships have been chosen, players will be able to place and orient their ships, you may place your ship anywhere within the board and orient it up, down, left or right. You may not orient it diagonally or intersect another ship.\n")
            print("3)Taking turns, the users pick a space on the opponent's board to fire at,each shot must be updated to indicate a hit or miss.\n")
            print("4)Once a ship has been hit in every space it occupies, it is sunk.\n")
            print(
                "5)As the great Colonel Sanders once said \"I'm too drunk to taste this fried chicken. \"\n ")
        elif(choice == 3):
            print("\nGoodbye...")
            return(3) # added by Edina; return this to playGame which called printMenu
        else:
            print("Sorry, invalid choice! Please pick again.\n")


# Ths next part starts the program.
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
