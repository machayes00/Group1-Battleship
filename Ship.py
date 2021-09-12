#assume creation of 9x10 array board filled up with 'o'
#That array will be the game board

##documentaion for a class
#ships on a game board for the game of battle ship
#includes methods to create ship register hits and tell if ship is "sunk"
class ship:

    def __init__(self):
        self.size = 1
        self.shipSpots = [] # this will be a list of tuples, initially empty
        self.sunk = False


    # The function of the code in the bool method below should be part of
    # the executive that interacts with user; prints out query for input, check if acceptible,
    # and if not, prints message to user to fix; once acceptable, executive passes start, orient and size to
    # Board class, which calls the Ship constructor and then sets its coordinates in shipSpots.

    ##documentation for a method
    # @brief checks whether a ship of a certain size, place and orientation fits on a gameboard
    # @pre array is valid
    # @param array: a 10 by 10 array representing a gameboard BUT EDINA thinks this param belongs in Board class
    # @param startx: x position of start of ship in array
    # @param starty: y position of start of ship in array
    # @param orient: orientation of ship(L=left of start, R=right of start, U=up from start, D=down from start)
    # @param length: length of ship
    # @post gives either true or false dependent on whether ship is placeable
    def createbool(self, array, startx, starty, orient, length):
        # check=True Edina: this variable was not used in the method, so it should be removed
        start=0
        if(startx < 0 or startx > 9):
            # raise Exception("X coordinate is not valid") #Edina: I think Exception is if you want program to quit
            return False # Edina: better to make createbool return False, instead of throw exception
        if(starty < 0 or starty > 9):
            # raise Exception("Y coordinate is not valid")
            return False
        if(length < 1 or length > 10):
            # raise Exception("Length is not valid")
            return False
        if(orient != ('L' or 'l') and orient != ('R' or 'r') and orient != ('U' or 'u') and orient != 'D' or 'd'):
            # raise Exception("Orientation is not valid")
            return False
        if orient == ('L' or 'l'):
            while start < length:
                if array[starty][startx-start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == ('R' or 'r'):
            while start < length:
                if array[starty][startx+start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == ('U' or 'u'):
            while start < length:
                if array[starty-start][startx] != ' ':
                    return(False)
                else:
                    start=start+1
        if orient == ('D' or 'd'):
            while start < length:
                if array[starty+start][startx] != ' ':
                    return False
                else:
                    start=start+1
        return True

    
    # It is good to leave other methods here; Board can call them
    # to check if ship is hit or not, and also if sunk or not

    ##documentation for a method
    # @brief "hits" spot on ship
    # @pre array is valid
    # @param array: in place of gameboard
    # @param startx: x position in array
    # @param starty: y position in array
    # @post shipspot is removed as it has been hit   
    def hit(self, coordinates):  # a tuple with two members is passed in
        '''
        I did not change this method but it needs fix. It just needs the coordinates
        from the Ship member list of coordinates. The x and y parameters and passed in
        from Board shot method.
        '''
        # self.sunk=False remove this since ship is initialized for sunk = False
        # need to check if passed in (x,y) is in the list of shipspots and if so:
        spot=coordinates # method needs fix still
        self.shipSpots.remove(spot)
        print("HIT!") # executive would print HIT. This method just updates Ship object members.
        if len(self.shipSpots) == 0:
            self.sunk=True

    ##documentation for a method
    # @brief checks if ship is sunk
    # @post returns true if true false if false
    def sinkcheck(self):
        if self.sunk == True:
            print("Ship is sunk!")

#Following lines were used for testing previous version
#s=ship
#arr=["o" for i in range(100)]
#s.createship(s,arr,3,1,'R',2)
#s.hit(s,arr,4,1)
#s.hit(s,arr,3,1)
#s.sinkcheck(s)
#for x in range(9):
    #print(arr[(x*10)+0]+" "+arr[(x*10)+1]+" "+arr[(x*10)+2]+" "+arr[(x*10)+3]+" "+arr[(x*10)+4]+" "+arr[(x*10)+5]+" "+arr[(x*10)+6]+" "+arr[(x*10)+7]+" "+arr[(x*10)+8]+" "+arr[(x*10)+9])

