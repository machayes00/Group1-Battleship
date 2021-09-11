#assume creation of 8x8 array board filled up with 'o'
#That array will be the game board
class ship:
    def createbool(self,array,startx,starty,orient,length):
        start = 0
        if orient == 'L':
            while start < length:
                if array[starty][startx-start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == 'R':
            while start < length:
                if array[starty][startx+start] != ' ':
                    return(False)
                else:
                    start=start+1
        elif orient == 'U':
            while start < length:
                if array[starty-start][startx] != ' ':
                    return(False)
                else:
                    start=start+1
        if orient == 'D':
            while start < length:
                if array[starty+start][startx] != ' ':
                    return False
                else:
                    start=start+1
        return True

    def createship(self, array, startx, starty, orient, length):
        if self.createbool(array, startx, starty, orient, length):
            start=0
            if orient == 'L':
                while start < length:
                    array[starty][startx-start] = 'x'
                    start=start+1
            elif orient == 'R':
                while start < length:
                    array[starty][startx+start] = 'x'
                    start=start+1
            elif orient == 'U':
                while start < length:
                    array[starty-start][startx] = 'x'
                    start=start+1
            elif orient == 'D':
                while start < length:
                    array[starty+start][startx] = 'x'
                    start=start+1

