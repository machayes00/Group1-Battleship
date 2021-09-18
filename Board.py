class Board:

    # Constructor
    def __init__(self):
        """
        This constructs the full board, initialized to be empty of ships. 
        It contains a 2D self.waterGrid, waterGrid. Locations marked as '0' are water, 
        and these will be changed to S wherever there is a ship, and to * to 
        mark locations of hits. The S and * locations are obtained from two lists,
        shipSpots and shots, both of which are initialized to be empty.
        """
        self.waterGrid = [['O' for col in range(10)] for row in range(9)] # initialize board to be all 'O'
        # Edina: I commented out Ship objects list since we no longer have Ship objects (for now at least)
        # self.shipOjects = [] this was a list of ship objects. They will be checked to determine which ship is hit, and update ship coord, sunk variables

        # Edina: I also do not think we need a list of shots anymore. Simply change the waterGrid when it is shot at.
        # I commented out since neither Alex nor Mac are using it.
        # self.shots = [] # initialize list of shot locations to be empty 

        # We can think of additinal useful properties to add to board.
        # for example, number of ships, which can be passed in from setup() menu
        # and adujsted by a hit method that checks number of ships remaining.

    def printBoard(self):
        """
        This method prints the waterGrid self.waterGrid with a border to mark coordinates
        (A-J for columns and 1-9 for rows). 

        I think we need TWO of these methods, printMyBoard, printOpponentBoard??
        Instruction #4 indicates that: players should be able to see their own board
        and all their ships, and also of course the opponent's board because that helsp determine
        where to fire (ships are hidden unless a spot is revealed via a hit). So 
        the difference is:

        printMyBoard shows all the ships, printOpponentBoard shows only locations shot at and
        whether or not they hit a shipSpot. We do not need to mark on the board if the
        ship is sunk or not (tho this is in the ship's bool variable) because the player knows.
        Each ship is the same size (depending on the number of ships each player gets).
        """
        topOfBoard = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        
        # print top of board
        for i in topOfBoard:
            print(" ", end="")
            print(i, "", end = "")
        print()

        # print the rest of the board
        for row in range(9):
            print(row+1, " ", end = " ")
            for col in range(10):
                print(self.waterGrid[row][col], " ", end = "")
            print()

 
        # waterGrid will be updated as the game progresses, by createShip() and hits()
        # so original "O" is replaced with a number for ship, * for hit, X for hit on a ship

    # Edina: Mac inocrporated the purpose of the following bool method in setup() so
    # probably it is no longer needed but it does not harm anything to keep here in 
    # case we can adopt it and modify for a different use.
    # Alex also has this method, extensively modified in Friday's pull request
    # So we have 2 versions of a bool that we are not yet using.

    ##documentation for isShipValid method
    # @brief checks if ship placement would be valid
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post returns true if ship placement works
    def isShipValid(self, orient, startx, starty, length):
        start = 0
        if orient == ('L' or 'l'):
            while start < length:
                if self.waterGrid[starty][startx-start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == ('R' or 'r'):
            while start < length:
                if self.waterGrid[starty][startx+start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == ('U' or 'u'):
            while start < length:
                if self.waterGrid[starty-start][startx] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == ('D' or 'd'):
            while start < length:
                if self.waterGrid[starty+start][startx] != ' ':
                    return False
                else:
                    start=start+1
        else:
            return True

    # Edina: added count parameter, and changed to add whatever
    # this number is, to waterGrid as the ship is being added.
    # Like all parameters, the number is passed in from setup()
    # and when this method runs, setup can refresh count for the
    ##documentation for createShip method
    # @brief places a ship on the waterGrid array.
    # @param startx: x position in self.waterGrid (column index)
    # @param starty: y position in self.waterGrid (row index)
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post none
    def createShip(self, startx, starty, orient, length, shipnumber): 
        start = 0
        if orient == ('L'):
            while start < length:
                self.waterGrid[starty][startx-start] = shipnumber
                start=start+1
        elif orient == 'R':
            while start < length:
                self.waterGrid[starty][startx+start] = shipnumber
                start=start+1
        elif orient == 'U':
            while start < length:
                self.waterGrid[starty-start][startx] = shipnumber
                start=start+1
        elif orient == 'D':
            while start < length:
                self.waterGrid[starty+start][startx] = shipnumber
                start=start+1

# Edina: commented out older version of hit method because Alex updated.
# I pasted in his update; I did not check either method yet but neither can do
# any harm to the rest of the program so they can be merged
'''
    def hit(self, x, y):
        for x in range(5):
            return(self.waterGrid[y][x] == x+1)
'''

def hit(self, y, x):
    row = len(self.shipObjects)
    temp = self.spots
    for z in range(row):
        for w in range(len(self.shipObjects[z])):
            if self.shipObjects[z][w] == (y, x):
                self.waterGrid[y][x] = "x"
                self.spots = self.spots-1
                self.shiplengths[z] = self.shiplengths[z]-1
                if self.shiplengths[z] == 0:
                    print("Ship is sunk!")
                    self.points = self.points-1
    if temp == self.spots:
        self.waterGrid[y][x] = "m"
def score(self, opp):
    print("Player Ships Remaining:"+str(self.points))
    print("Opponent Ships Remaining:"+str(opp.points))
    if self.points == 0:
        print("You Lost!")
        self.allsunk = True
    elif opp.points == 0:
        print("You Won!")
        opp.allsunk = False
