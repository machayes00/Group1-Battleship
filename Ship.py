#assume creation of 8x8 array board filled up with 'o'
#That array will be the game board
class ship:
    def createbool(array,startx,starty,orient,length):
        check=True
        start=0
        if orient == "L":
            while start <= length:
                array[startx-start,starty]='x'
                start=start+1
        if orient == "R":
            while start <= length:
                array[startx+start,starty]='x'
                start=start+1
        if orient == "U":
            while start <= length:
                array[startx,starty+start] = "x"
                start=start+1
        if orient == "D":
            while start <= length:
                if array[startx,starty-start] != "o":
                    check=False
                start=start+1
        return(check)
    def createship(array,startx,starty,orient,length):
        if createbool(array,startx,starty,orient,length) == True:
            start=0
        if orient == "L":
            while start <= length:
                if array[startx-start,starty] != "o":
                    check=False
                start=start+1
        if orient == "R":
            while start <= length:
                if array[startx+start,starty] != "o":
                    check=False
                start=start+1
        if orient == "U":
            while start <= length:
                if array[startx,starty+start] != "o":
                    check=False
                start=start+1
        if orient == "D":
            while start <= length:
                if array[startx,starty-start] != "o":
                    check=False
                start=start+1

