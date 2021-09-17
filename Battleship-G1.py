# Import class methods needed for the program
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
choice = 0 # variable that allows quitting the game

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
        
        # make this a try-catch block to check acceptable arguments
        startCol = input("\nWhat is the starting column of your ship?\n")
        startRow = input("\nWhat is the starting row of your ship?\n")
        print()

        # EDIT NEEDED: modify the startCol and starRow variables, after user
        # input, so that they are indices for 2D waterGrid array.
        # I like the idea from Alice & George planning file, to use a
        # dictionary to covert coordinates to index numbers for 
        # waterGrid 2D array. Until we have that, pass in 2D index.


        print('What is the orientation of this ship? Enter\n')
        print('"L" for left of start (horizontal ship)\n')
        print('"R" for right of start (horizontal ship)\n')
        print('"U" for up from start (vertical ship)\n')
        print('"D" for down from start (vertical ship)\n')

        # try catch block, using code from Alex's and Mac's original Ship.py
        # createBool. I fixed that to allow both upper case and lower case entry.

        orient = input()

        # Enters correct arguments, including conversion for start coordinates.
        # This will update waterGrid for the next iteration of the for loop.
        board.createShip(startCol, startRow, orient, numberShips) 
        
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
    # not sure these variables are needed; depends on how playGame is designed
    player1 = "Player 1 "
    player2 = "Player 2 "

    # Print menu (see next method) will print between each shoot
    printMenu()
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

# Maybe printMenu should first print the player's own board, then the menu options, and if 
# player selects to take s shot, pirnt the opponent's board.

# But the menu should be short since it is presented repeatedly for each player at ever single turn.

def printMenu():
    """!
    Print menu items for users, like option to print boards (or make
    that automatic as part of the setup?)  Also, option to quit, etc.
    """
    choice = 0 
    while (choice != 3):
        print("\nWelcome to Battleship! Select option 1 to start the game!\n1)Play Game\n2)Rules \n3)Quit")
        choice = int(input())
        if(choice == 1):
            playGame(boardPlayer1, boardPlayer2)
            print("Would you like to play again?")

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
        else:
            print("Sorry invalid choice please pick again.\n")


# Ths next part starts the program.
stopgame = 0 # variable for giving option to quit game or play again, once a game is over

while stopgame == 0:

    print('\n *** WELCOME TO BATTLESHIP!! ***\n')
    print()
    # Maybe add instructions from George's printMenu here. But our Project 1 instructions
    # stated that the game should be "obvious" and not need much instrucion. So maybe 
    # it is better if the short prompts for user input, plus feedback to user, will let 
    # the user understand the game, without printing lengthy instrucitons.

    choice = 0 # bool for marking acceptable choice for numberShips
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
    if input == "Y" or "y":
        stopgame = 1











