class Board:

    def __init__(self):
        """
        This constructs the full board, initialized to be empty of ships.
        It contains a 2D self.waterGrid, waterGrid. Locations marked as '0' are water,
        and these will be changed to S wherever there is a ship, and to * to
        mark locations of hits. The S and * locations are obtained from two lists,
        shipSpots and shots, both of which are initialized to be empty.
        """

        self.shipObjects = [] # this is a list of ship objects. They will be checked to determine which ship is hit, and update ship coord, sunk variables
        self.shiplengths=[]
        self.waterGrid = [['O' for col in range(10)] for row in range(9)] # initialize board to be all 'O'
        self.oppGrid = [['*' for col in range(10)] for row in range(9)] # initialize board to be all '*'
        self.spots=0
        self.points=0
        self.allsunk=False

    def printBoard(self):
        """
        This method prints the waterGrid self.waterGrid with a border to mark coordinates
        (A-J for columns and 1-9 for rows).
        This printed board shows all the ships.
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

    ##documentation for a method
    # @brief checks if ship placement would be valid
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post returns true if ship placement works
    def printOpp(self):
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
                print(self.oppGrid[row][col], " ", end = "")
            print()

    def checkShipOverlap(self, x, y, len):
        for i in self.waterGrid:
            for j in i:
                if j != 'O':
                    return False
        return True


    def isShipValid(self, orient, startx, starty, length):
        start = 0
        bool=True
        if orient == ('L' or 'l'):
            while start < length:
                if self.waterGrid[starty][startx-start] != 'O' and self.waterGrid[starty][startx-start] != "*":
                    bool=False
                start=start+1
        elif orient == ('R' or 'r'):
            while start < length:
                if self.waterGrid[starty][startx+start] != 'O' and self.waterGrid[starty][startx+start] != "*":
                    bool=False
                start=start+1
        elif orient == ('U' or 'u'):
            while start < length:
                if self.waterGrid[starty-start][startx] != 'O' and self.waterGrid[starty-start][startx] != "*":
                    bool=False
                start=start+1
        elif orient == ('D' or 'd'):
            while start < length:
                if self.waterGrid[starty+start][startx] != 'O' and self.waterGrid[starty+start][startx] != "*":
                    bool=False
                start=start+1
        return bool

    ##documentation for createShip method
    # @brief creates a ship
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post none
    def createShip(self, startx, starty, orient, length,shipnumber):
        start = 0
        shipcoords=[]
        self.shiplengths.append(length)
        if orient == ('L'):
            while start < length:
                self.waterGrid[starty][startx-start] = shipnumber
                shipcoords.append((starty,startx-start))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'R':
            while start < length:
                self.waterGrid[starty][startx+start] = shipnumber
                shipcoords.append((starty,startx+start))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'U':
            while start < length:
                self.waterGrid[starty-start][startx] = shipnumber
                shipcoords.append((starty-start,startx))
                start=start+1
                self.spots=self.spots+1
        elif orient == 'D':
            while start < length:
                self.waterGrid[starty+start][startx] = shipnumber
                shipcoords.append((starty+start,startx))
                start=start+1
                self.spots=self.spots+1
        self.shipObjects.append(shipcoords)
        self.points=self.points+1

    def hit(self, y, x):
        row = len(self.shipObjects)
        temp=self.spots
        for z in range(row):
            for w in range(len(self.shipObjects[z])):
                if self.shipObjects[z][w] == (y,x):
                    self.waterGrid[y][x] = "x"
                    self.oppGrid[y][x] = "x"
                    self.spots=self.spots-1
                    self.shiplengths[z]=self.shiplengths[z]-1
                    print("\nHIT!\n")
                    if self.shiplengths[z] == 0:
                        print("Ship is sunk!")
                        self.points=self.points-1
                else:
                    print("\nMISS!\n")
        if temp == self.spots:
            self.oppGrid[y][x] = "m"

    def score(self,opp):
        print("Player 1 Ships Remaining: "+str(self.points))
        print("Player 2 Ships Remaining: "+str(opp.points))
        if self.points == 0:
            print("Player 2 Won!")
            self.allsunk=True
        elif opp.points == 0:
            print("Player 1 Won!")
            opp.allsunk=True
