from Ship import *

class Board:

    def __init__(self):
        """
        This constructs the full board, initialized to be empty of ships. 
        It contains a 2D array, waterGrid. Locations marked as '0' are water, 
        and these will be changed to S wherever there is a ship, and to * to 
        mark locations of hits. The S and * locations are obtained from two lists,
        ships and hits, both of which are initialized to be empty.
        """
        self.waterGrid = [['O' for y in range(10)] for x in range(9)] # initialize board to be all 'O'
        self.shipSpots = [] # initialize list of ships to be empty. The list is for placing ships
        self.ships = [] # this is a list of ship objects. They will be called to determine which ship is hit, and update ship coord, sunk variables
        self.shots = [] # initialize list of shot locations to be empty 

    def printBoard(self):
        """
        This method prints the waterGrid array with a border to mark coordinates
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
        gameBoard = [] # need to create by adding border to waterGrid.
        # But first:
        # waterGrid is updated as the game progresses, by createShip() and hits()
        # so original "O" is replaced with S for ship, * for hit, X for hit on a ship

        print(gameBoard)

    # Below method is copy pasted createShip from original Ship class.
    # Removed array param since it is waterGrid, part of self for Board class

    ##documentation for a method
    # @brief creates a ship
    # @param startx: x position in array
    # @param starty: y position in array
    # @param orient: orientation of ship orientation of ship:
    #       (L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post ship is placed
    def createShip(self, startx, starty, orient, length): 
        '''
        Executive will use current waterGrid to determine accepable ship 
        placement and if acceptable, pass in parameters (start, orient
        and length). This method will then determine the ship's coordinates and
        update the ships[] list that is a component of the Board object.
        The method probably still has to be edited (I changed almost nothing).

        like it has to call Ship constructor,
        for example 
        ship1 = Ship()
        and then change it to contain proper coordinates.
        '''
        start = 0
        if orient == ('L'):
            while start < length:
                self.waterGrid[starty][startx-start] = 'x'
                self.shipSpots.append([starty][startx-start])
                start=start+1
        elif orient == 'R':
            while start < length:
                self.waterGrid[starty][startx+start] = 'x'
                self.shipSpots.append([starty][startx+start])
                start=start+1
        elif orient == 'U':
            while start < length:
                self.waterGrid[starty-start][startx] = 'x'
                self.shipSpots.append([starty-start][startx])
                start=start+1
        elif orient == 'D':
            while start < length:
                self.waterGrid[starty+start][startx] = 'x'
                self.shipSpots.append([starty+start][startx])
                start=start+1

    def checkShots(self, coordinate): 
        pass
        '''
        This obtains hit coordinates from user through the executive class.
        The coordinates are passed in to this function as a tuple, (x,y).

        I think I can iterate thru a list of tuples and check for exact match, since tuples
        are immutable and therefore considered as the same object if have same content, like
        strings but unlike lists (I need to check on that tho)

        The method then uses the board.ships list, to iterate thru the list of ships,
        using a for loop; for each ship, the method will call ship.hit method from Ship class
        to determine if the ship is hit, and if so, update the ship's ship.shipSpots list and 
        if applicable, its ship.sunk bool.

        In addition to updating all the ship objects in the board.ships list, the
        method also updates the board.shots list. This if for the use of the printBoard
        method, so the user can see all the shots.
    
        In other words it calls ship.hit method on every ship in the board.ship list,
        to determine if any of the ships are hit. If so, it updates the ship's
        member variables (size, and possibly its sunk bool).

        
        '''

    def score(self):
        """
        Either here (probably) or in executive, call ship.sinkcheck on each ship for each
        player to keep track of how many sunk/unsunk ships each have. Execitive can call this method
        and update the players and also end the game when a player wins.
        """
