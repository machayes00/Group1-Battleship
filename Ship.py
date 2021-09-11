#assume creation of 10x10 array board filled up with 'o'
#That array will be the game board
class ship:
    def createbool(self,array,startx,starty,orient,length):
        check=True
        start=0
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
                    self.shipspots.append([(starty*10)+(startx-start)])
                    start=start+1
            if orient == "R":
                while start < length:
                    array[(starty*10)+(startx+start)]='X'
                    self.shipspots.append([(starty*10)+(startx+start)])
                    start=start+1
            if orient == "U":
                while start < length:
                    array[startx+((starty-start)*10)] = "X"
                    self.shipspots.append([startx+((starty-start)*10)])
                    start=start+1
            if orient == "D":
                while start < length:
                    array[startx+((starty+start)*10)] != "X"
                    self.shipspots.append([startx+((starty+start)*10)])
                    start=start+1        
    def hit(self,array,startx,starty):
        spot=0
        for x in self.shipspots:
            if x == array[startx+(starty*10)]:
                spot=x
            self.shipspots.remove(x)
            self.sunk=False
            if len(self.shipspots) == 0:
                self.sunk=True
    def sinkcheck(self):
        if self.sunk == True:
            print("Ship is sunk!")
#s=ship
#print("Hey")
#arr=["o" for i in range(100)]
#s.createship(s,arr,3,1,'R',2)
#s.hit(s,arr,3,1)
#s.sinkcheck(s)
#print(arr)

#Previous lines were used for testing
