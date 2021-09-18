class Board:

    def __init__(self):
        """
        This constructs the full board, initialized to be empty of ships. 
        It contains a 2D self.waterGrid, waterGrid. Locations marked as '0' are water, 
        and these will be changed to S wherever there is a ship, and to * to 
        mark locations of hits. The S and * locations are obtained from two lists,
        shipSpots and shots, both of which are initialized to be empty.
        """
        self.waterGrid = [['O' for col in range(9)] for row in range(8)] # initialize board to be all 'O'
        self.shipOjects = [] # this is a list of ship objects. They will be checked to determine which ship is hit, and update ship coord, sunk variables
        self.shots = [] # initialize list of shot locations to be empty 

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
        # so original "O" is replaced with S for ship, * for hit, X for hit on a ship
        
    ##documentation for a method
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

    ##documentation for a method
    # @brief creates a ship
    # @param startx: x position in self.waterGrid
    # @param starty: y position in self.waterGrid
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post none
    def createShip(self, startx, starty, orient, length): 
        start = 0
        if orient == ('L'):
            while start < length:
                self.waterGrid[starty][startx-start] = length
                start=start+1
        elif orient == 'R':
            while start < length:
                self.waterGrid[starty][startx+start] = length
                start=start+1
        elif orient == 'U':
            while start < length:
                self.waterGrid[starty-start][startx] = length
                start=start+1
        elif orient == 'D':
            while start < length:
                self.waterGrid[starty+start][startx] = length
                start=start+1

    def hit(self, x, y):
        for x in range(5):
            return(self.waterGrid[y][x] == x+1)


    def score(self):
        """
        Either here (probably) or in executive, call ship.sinkcheck on each ship for each
        player to keep track of how many sunk/unsunk ships each have. Execitive can call this method
        and update the players and also end the game when a player wins.
        """
