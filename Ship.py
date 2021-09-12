#assume creation of 10x10 array board filled up with 'o'
#That array will be the game board

##documentaion for a class
#ships on a game board for the game of battle ship
#includes methods to create ship register hits and tell if ship is "sunk"
class ship:
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

    ##documentation for a method
    # @brief creates a ship
    # @pre array is valid
    # @param array: in place of gameboard
    # @param startx: x position in array
    # @param starty: y position in array
    # @param orient: orientation of ship(left, right, up, down)
    # @param length: length of ship
    # @post ship is placed
    def createship(self, array, startx, starty, orient, length):
        if self.createbool(array, startx, starty, orient, length): # Edina: deleted self from () because otherwise duplicate
            start=0
            self.shipspots=[]
            if orient == ('L' or 'l'):
                while start < length:
                    array[starty][startx-start] = 'x'
                    self.shipspots.append([starty][startx-start])
                    start=start+1
            elif orient == 'R':
                while start < length:
                    array[starty][startx+start] = 'x'
                    self.shipspots.append([starty][startx+start])
                    start=start+1
            elif orient == 'U':
                while start < length:
                    array[starty-start][startx] = 'x'
                    self.shipspots.append([starty-start][startx])
                    start=start+1
            elif orient == 'D':
                while start < length:
                    array[starty+start][startx] = 'x'
                    self.shipspots.append([starty+start][startx])
                    start=start+1

    ##documentation for a method
    # @brief "hits" spot on ship
    # @pre array is valid
    # @param array: in place of gameboard
    # @param startx: x position in array
    # @param starty: y position in array
    # @post shipspot is removed as it has been hit   
    def hit(self,array,startx,starty):  # Edina: array parameter was not used in this method; I added to spot
        self.sunk=False
        spot=array[starty][startx]
        self.shipspots.remove(spot)
        print("HIT!")
        if len(self.shipspots) == 0:
            self.sunk=True

    ##documentation for a method
    # @brief checks if ship is sunk
    # @post returns true if true false if false
    def sinkcheck(self):
        if self.sunk == True:
            print("Ship is sunk!")

#Following lines are used for testing
#s=ship
#arr=["o" for i in range(100)]
#s.createship(s,arr,3,1,'R',2)
#s.hit(s,arr,4,1)
#s.hit(s,arr,3,1)
#s.sinkcheck(s)
#for x in range(9):
    #print(arr[(x*10)+0]+" "+arr[(x*10)+1]+" "+arr[(x*10)+2]+" "+arr[(x*10)+3]+" "+arr[(x*10)+4]+" "+arr[(x*10)+5]+" "+arr[(x*10)+6]+" "+arr[(x*10)+7]+" "+arr[(x*10)+8]+" "+arr[(x*10)+9])

