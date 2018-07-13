puzzle = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def getPuzzle():
    return puzzle
def getVerticalListForCoordinate(y):
    verticalList = []

    for i in range(0,9):
        verticalList.append(puzzle[i][y])

    return verticalList
def getHorizontalListForCoordinate(x):
    horizontalList = []

    for i in range(0,9):
        horizontalList.append(puzzle[x][i])

    return horizontalList
def getThreeByThreeListForCoordinates(x,y):
    list = []

    xrange = [0,0]
    yrange = [0,0]

    if 0 <= x <= 2 and 0 <= y <= 2:
        xrange = [0,2]
        yrange = [0,2]
    elif 0 <= x <= 2 and 3 <= y <= 5:
        xrange = [0,2]
        yrange = [3,5]
    elif 0 <= x <= 2 and 6 <= y <= 8:
        xrange = [0,2]
        yrange = [6,8]
    elif 3 <= x <= 5 and 0 <= y <= 2:
        xrange = [3,5]
        yrange = [0,2]
    elif 3 <= x <= 5 and 3 <= y <= 5:
        xrange = [3,5]
        yrange = [3,5]
    elif 3 <= x <= 5 and 6 <= y <= 8:
        xrange = [3,5]
        yrange = [6,8]
    elif 6 <= x <= 8 and 0 <= y <= 2:
        xrange = [6,8]
        yrange = [0,2]
    elif 6 <= x <= 8 and 3 <= y <= 5:
        xrange = [6,8]
        yrange = [3,5]
    elif 6 <= x <= 8 and 6 <= y <= 8:
        xrange = [6,8]
        yrange = [6,8]
    else:
        print("Array out of bounds error")

    for xCordinate in range(xrange[0], xrange[1]+1):
        for yCordinate in range(yrange[0], yrange[1]+1):
            #print(str(xCordinate) + ", " + str(yCordinate))
            list.append(puzzle[xCordinate][yCordinate])

    return list
def getBlankSpacesList():
    global blankspaces
    blankspaces = list()
    for x in range(0,9):
        for y in range(0,9):
            if puzzle[x][y] is 0:
                blankspaces.append([x,y,0])
def setCoordinate(x,y,value):
    puzzle[x][y] = value
def checkCoordinatesForValue(x,y, value):
    if value in getThreeByThreeListForCoordinates(x,y):
        return False
    elif value in getHorizontalListForCoordinate(x):
        return False
    elif value in getVerticalListForCoordinate(y):
        return False
    else:
        return True
def setup():
    getBlankSpacesList()

def traverse(startPos, iValue):
    puzzleFinish = False
    for item, i in zip(blankspaces[startPos:], range(iValue,len(blankspaces)+1)):
        for testNumber in range(item[2]+1,10):
            if checkCoordinatesForValue(item[0],item[1],testNumber):
                setCoordinate(item[0],item[1],testNumber)
                for i in range(0,9):
                    print(puzzle[i])
                print()
                if testNumber is not 9:
                    item[2] = testNumber
                else:
                    item[2] = 0
                if item[0] is 8 and item[1] is 8:
                    puzzleFinish = True
                    exit()
                break
            else:
                if testNumber is 9:
                    item[2] = 0
                    setCoordinate(item[0],item[1],0)
                    if not(puzzleFinish):
                        traverse(i-1, i-1)
                    else:
                        break
        if puzzleFinish:
            print("break")
            break

for i in range(0,9):
    print(puzzle[i])
print()
setup()
traverse(0,0)
print("Finished Sudoku Puzzle")

#print(getVerticalListForCoordinate(5))
#print(getHorizontalListForCoordinate(2))
#print(getThreeByThreeListForCoordinates(2,5))
#print(getBlankSpacesList(puzzle))
