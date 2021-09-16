# Import class methods needed for the program
#Note: Comments starting with G made by George
from Board import *
from Ship import *
player1 = "Player1"
player2 = "Player2"

def setupplayer1(board, numberShips): # parameter is a Board object
    """
    
    Need to transpot the createBool code lines from Alex & Mac's
    Ship class here. I was thinking of getting rid of the exceptions
    but actually they are fine in try-catch blocks, but I have to 
    figure out how to do that in Python.
    Also, in addition to the code from createBool, need more checks using
    the waterGrid Board property which this method should update
    with ship locations.
    """
    
    
       

        
    pass
        # meke this a try-catch block to check acceptable arguments
    print("Welcome player 1! Select the number of ships you would like to play with. You must pick 1 ship and can have no more than 6 ships:\n")
    numberShips = int(input())
    if(numberShips<1 or numberShips >6):
        print("Error: Can only have 1 to 6 ships")
    for i in range(numberShips):
        #G: conditional statement asking for starting column input from the user, if input is not valid it returns an error
        #G: used if statement instead of try-catch block, can use try-catch 
        print("\nWhat is the starting column of your ship?\n")
        startCol = int(input())
        if(startCol <1 or  startCol>10):
            print("Error:please enter valid starting column.\n")
            
        #G: Asks for row input, returns an error if invalid
        print("\nWhat is the starting row of your ship?\n")
        startRow = int(input())
        if(startRow <1 or startRow > 9):
            print("Error:please enter valid starting row.\n ")
            print(startRow, startCol)
        # I like the idea from Alice&George planning file, to use a
        # dictionary to covert coordidantes to index numbers for 
        # waterGrid 2D array.
        print('What is the orientation of this ship? Enter\n')
        print('"L" for left of start (horizontal ship)\n')
        print('"R" for right of start (horizontal ship)\n')
        print('"U" for up from start (vertical ship)\n')
        print('"D" for down from start (vertical ship)\n')

        #G: conditional statement asking for orientation input from the user, if input is not valid it returns an error, needs more work
        #G: used if statement instead of try-catch block, can use try-catch but only advantage of try-catch is slightly faster speed
        orient = input()
        if(orient != ('L' or 'l') and orient != ('R' or 'r') and orient != ('U' or 'u') and orient != 'D' or 'd'):
            return("Error: please enter a valid orientation")
        board.createShip(startCol, startRow, orient, numberShips)

        #G: prints out which ship was created
        print("Ship #" + str(i) + "created!") 

        # try catch block, using code from Alex's original Ship.py
        # createBool. But we don't need it to be a bool. Also, allow both
        # upper case and lower case entry.

        #G: conditional statement asking for orientation input from the user, if input is not valid it returns an error
        #G: used if statement instead of try-catch block, can use try-catch but only advantage of try-catch is slightly faster speed

        
        # enter correct arguments, icluding coversion for start coordinates.
        # This will update waterGrid for the next iteration of the for loop.
    pass

pass
def setupplayer2(board, numberShips): # parameter is a Board object
        """
    
    Need to transpot the createBool code lines from Alex & Mac's
    Ship class here. I was thinking of getting rid of the exceptions
    but actually they are fine in try-catch blocks, but I have to 
    figure out how to do that in Python.
    Also, in addition to the code from createBool, need more checks using
    the waterGrid Board property which this method should update
    with ship locations.
    """
        # meke this a try-catch block to check acceptable arguments
print("Welcome player 2! Please enter your ship(s) for your board:\n")
numberShips = int(input())
for i in range(numberShips):
        #G: conditional statement asking for starting column input from the user, if input is not valid it returns an error
        #G: used if statement instead of try-catch block, can use try-catch but only advantage of try-catch is slightly faster speed
    print("\nWhat is the starting column of your ship?\n")
    startCol = int(input())
    if(startCol <1 or  startCol>10):
        print("Error:please enter valid starting column.\n")
            
        #G: Asks for row input, returns an error if invalid
        print("\nWhat is the starting row of your ship?\n")
    startRow = int(input())
    if(startRow <1 or startRow > 9):
        print("Error:please enter valid starting row.\n ")
        print(startRow, startCol)
        # I like the idea from Alice&George planning file, to use a
        # dictionary to covert coordidantes to index numbers for 
        # waterGrid 2D array.
        print('What is the orientation of this ship? Enter\n')
        print('"L" for left of start (horizontal ship)\n')
        print('"R" for right of start (horizontal ship)\n')
        print('"U" for up from start (vertical ship)\n')
        print('"D" for down from start (vertical ship)\n')
        #G: conditional statement asking for orientation input from the user, if input is not valid it returns an error, needs more work
        #G: used if statement instead of try-catch block, can use try-catch but only advantage of try-catch is slightly faster speed
        orient = input()
        if(orient != ('L' or 'l') and orient != ('R' or 'r') and orient != ('U' or 'u') and orient != 'D' or 'd'):
            print("Error: please enter a valid orientation")
        # try catch block, using code from Alex's original Ship.py
        # createBool. But we don't need it to be a bool. Also, allow both
        # upper case and lower case entry.
        #G: conditional statement asking for orientation input from the user, if input is not valid it returns an error
        #G: used if statement instead of try-catch block, can use try-catch but only advantage of try-catch is slightly faster speed
        board.createShip(startCol, startRow, orient, numberShips) 
        print("Ship #" + str(i) + "created!")
        # enter correct arguments, icluding coversion for start coordinates.
        # This will update waterGrid for the next iteration of the for loop
        pass

pass
def playGame(board, player1, player2, ):
    
    setupplayer1()

    setupplayer2()
    

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



#made a simple little menu, doesn't do anything right now. Used a while loop instead of a do-while because do-while loops don't exist in python
def printMenu():
    choice = 0
    while (choice !=3):
        print("\nWelcome to Battleship! Select option 1 to start the game!\n1)Play Game\n2)Rules \n3)Quit")
        choice = int(input())
        if(choice == 1):
            playGame()
            print("Would you like to play again?")
            
        elif(choice == 2):
            print("-----------------------------------------------------------------------------------------------------------------------------------------------Rules of Battleship-----------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("Overview:\nBattleship is a two player game where both players secretly place 1 to 6 ships on a 9x10 grid. Taking turns each player announces where on the opponents grid they wish to fire. The opponent must announce whether or not one of the ships was hit. The first player to sink all of the oponents ships wins\n ")
            print("1)Ship size will be dependent on number of ships chosen. If one ship is chosen each player will be given a 1x1 ship . If two ships are chosen each player will be given a 1x1 and a 1x2 ship and so on.\n")
            print("2)After the ships have been chosen, players will be able to place and orient their ships, you may place your ship anywhere within the board and orient it up, down, left or right. You may not orient it diagonally or intersect another ship.\n")
            print("3)Taking turns, the users pick a space on the opponent's board to fire at,each shot must be updated to indicate a hit or miss.\n")
            print("4)Once a ship has been hit in every space it occupies, it is sunk.\n")
            print("5)As the great Colonel Sanders once said \"I'm too drunk to taste this fried chicken. \"\n ")
        elif(choice == 3 ):
            print("\nGoodbye...")
        else:
            print("Sorry invalid choice please pick again.\n")
        
           
    
        """
        Print menu items for users, like option to print boards (or make
        that automatic as part of the setup?)  Also, option to quit, etc.
        """
   

# probably the code below should be in a while block, do while players
# don't want to quit

#print('\n *** WELCOME TO BATTLESHIP!! ***\n')
#print()

#print('How many ships per player for this game?\n')
#print('Ener a number from 1 to 6:\n')
# try-catch block or if-else to confirm good entry
#numberShips = int(input())

# Create a board object for player 1
#boardPlayer1 = Board()

#print('\nReady to set up the board for Player 1!\n')

#setup(boardPlayer1, numberShips)

# Create a board object for player 2
#boardPlayer2 = Board()

#print('\nReady to set up the board for Player 2!\n')

#setup(boardPlayer2, numberShips)

#playGame()

printMenu()







