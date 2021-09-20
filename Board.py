class Board:
    """Class for creating components of active player and opponent game boards
    and changing or checking the characteristics of the boards and displaying them.
    """

    def __init__(self):
        """Constructor method
        """

        self.shipObjects = [] # this is a list of ship objects. They will be checked to determine which ship is hit, and update ship coord, sunk variables
        self.shiplengths=[]
        self.waterGrid = [['O' for col in range(10)] for row in range(9)] # initialize board to be all 'O'
        self.oppGrid = [['*' for col in range(10)] for row in range(9)] # initialize board to be all '*'
        self.spots=0
        self.points=0
        self.allsunk=False

    def printBoard(self):
        """Prints the active player's game board with a border to mark coordinates
        (A-J for columns and 1-9 for rows). The printed board shows all the ships
        because it uses the waterGrid 2D array for printing data.
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

    def printOpp(self):
        """Prints the opponent player's game board with a border to mark coordinates
        (A-J for columns and 1-9 for rows). The printed board hides all the ships
        because it uses the oppGrid 2D array for printing data.
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
                print(self.oppGrid[row][col], " ", end = "")
            print()

    def checkShipOverlap(self, x, y, len,orient):
        start = 0
        for i in self.waterGrid[x]:
            for j in self.waterGrid[y]:
                if j != 'O' and j != '*':
                #if Board[x][y] == '1' or Board[x][y] == '2' or Board[x][y] =='3' or Board[x][y] == '4' or Board[x][y] == '5':
                    print("There is already a ship here, please reenter coordinates. ")
                    return False
                else:
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

    def createShip(self, startx, starty, orient, length,shipnumber):
        """Creates a ship object to place on a game board.

        :param startx: the column index in 2D array for start position for placing a ship
        :type startx: int
        :param starty: the row index in a 2D array for start position for placing a ship
        :type starty: int
        :param orient: the orientation from the start position for building a ship
        :type orient: string
        :param length: the size of a ship
        :type length: int
        :param shipnumber: the number label used as a symbol to indicate a ship
        :type shipnumber: int
        """
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
        """Determines whether entered coordinates hit a ship, and gives
        feedback on whether ship is hit and if a ship is sunk.

        :param y: the row for the shot location
        :type y: int
        :param x: the column for the shot location
        :type x: int
        """
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
        """Keeps track of the ships remaining for each player, and
        determines when all ships are sunk for a player, and which player won

        :param opp: the opponent's Board object, so it can be compared to self
        :type opp: a Board object

        """
        print("Player 1 Ships Remaining: "+str(self.points))
        print("Player 2 Ships Remaining: "+str(opp.points))
        if self.points == 0:
            print("Player 2 Won!")
            self.allsunk=True
        elif opp.points == 0:
            print("Player 1 Won!")
            opp.allsunk=True
