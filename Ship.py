#assume creation of 10x10 array board filled up with 'o'
#That array will be the game board
class ship:
    def createbool(self,array,startx,starty,orient,length):
        check=True
        start=0
        if(startx < 0 or startx > 9):
            raise Exception("X coordinate is not valid")
        if(starty < 0 or starty > 9):
            raise Exception("Y coordinate is not valid")
        if(length < 1 or length > 10):
            raise Exception("Length is not valid")
        if(orient != 'L' and orient != 'R' and orient != 'U' and orient != 'D'):
            raise Exception("Orientation is not valid")
        if orient == 'L':
            while start < length:
                if array[(starty*10)+(startx-start)] != "o":
                    check=False
                start=start+1
        if orient == 'R':
            while start < length:
                if array[(starty*10)+(startx+start)] != "o":
                    check=False
                start=start+1
        if orient == 'U':
            while start < length:
                if array[startx+((starty-start)*10)] != "o":
                    check=False
                start=start+1
        if orient == 'D':
            while start < length:
                if array[startx+((starty+start)*10)] != "o":
                    check=False
                start=start+1
        return(check)
    def createship(self,array,startx,starty,orient,length):
        if self.createbool(self,array,startx,starty,orient,length) == True:
            start=0
            self.shipspots=[]
            if orient == "L":
                while start < length:
                    array[(starty*10)+(startx-start)]='X'
                    self.shipspots.append((starty*10)+(startx-start))
                    start=start+1
            if orient == "R":
                while start < length:
                    array[(starty*10)+(startx+start)]='X'
                    self.shipspots.append((starty*10)+(startx+start))
                    start=start+1
            if orient == "U":
                while start < length:
                    array[startx+((starty-start)*10)] = "X"
                    self.shipspots.append(startx+((starty-start)*10))
                    start=start+1
            if orient == "D":
                while start < length:
                    array[startx+((starty+start)*10)] != "X"
                    self.shipspots.append(startx+((starty+start)*10))
                    start=start+1        
    def hit(self,array,startx,starty):
        self.sunk=False
        spot=startx+(starty*10)
        self.shipspots.remove(spot)
        print("HIT!")
        if len(self.shipspots) == 0:
            self.sunk=True
    def sinkcheck(self):
        if self.sunk == True:
            print("Ship is sunk!")
#s=ship
#arr=["o" for i in range(100)]
#s.createship(s,arr,3,1,'R',2)
#s.hit(s,arr,4,1)
#s.hit(s,arr,3,1)
#s.sinkcheck(s)
#for x in range(9):
    #print(arr[(x*10)+0]+" "+arr[(x*10)+1]+" "+arr[(x*10)+2]+" "+arr[(x*10)+3]+" "+arr[(x*10)+4]+" "+arr[(x*10)+5]+" "+arr[(x*10)+6]+" "+arr[(x*10)+7]+" "+arr[(x*10)+8]+" "+arr[(x*10)+9])
#Previous lines were used for testing
