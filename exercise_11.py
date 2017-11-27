# Project Euler
# Problem 11
# Started Wednesday, November 22, 2017
# https://projecteuler.net/problem=11
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
# in the 20×20 grid?
import itertools
from matplotlib import pyplot
import numpy as np

'''Notes
1. Each cell has a max of 8 possible moves
    --> up
    --> up right
    --> right
    --> down right
    --> down
    --> down left
    --> left
    --> up left
2. Cells on the boundary will not have all moves
3. If there are mults operations, an upper bound on computation would be cells in grid * 8 * mults
    = 20* 20 * 8 * 4 = 12800, which seems feasible to brute force
4. Upper bound on the value would be min(grid)** 4 = 100**4 = 1 * 10**8
5. Move count
--> Corner: 3
--> 
'''


filePath = '/Users/amcelhinney/repos/Project_Euler/exercise_11_grid.txt'

with open(filePath) as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [i.split(' ') for i in content]

grid = [[int(val) for val in row] for row in content]
import pandas as pd
grid = pd.DataFrame(grid)

def appendMoves(moves, col):
    return moves + [list(col)]



def returnCells(row, col, mults=4, maxRow=19, maxCol=19):
    '''For a given row and column index, return a list of tuples containing the rows and cells that
    are acceptable multiples for this problem
    '''
    # Validate whether there are acceptable moves up, right, down and left
        # Dont forget to add 1 becase we index from 0.
    upValid = row+1 - mults >= 0
    rightValid = col + mults <= maxCol + 1
    downValid = row + mults <= maxRow + 1
    leftValid = col+1 - mults >= 0
    moves = []
    # Calculate up moves
    # EVERY set of moves should have the start row and column in it
    if upValid:
        upCol = range(row-mults+1, row+1)
        up = zip(upCol, [col] * mults)
        moves = appendMoves(moves, col=up)
    # Calculate right moves
    if rightValid:
        rightCol = range(col, col+mults)
        right = zip([row] * mults, rightCol)
        moves = appendMoves(moves, col=right)
    # Calculate down moves
    if downValid:
        downCol = range(row, row+mults)
        down = zip(downCol, [col] * mults)
        moves = appendMoves(moves, col=down)
    # Calculate left moves
    if leftValid:
        leftCol = range(col-mults+1, col+1)
        left = zip([row] * mults, leftCol)
        moves = appendMoves(moves, col=left)

    # Calculate diagonal moves to the up and right
    if upValid and rightValid:
        #upRight = zip(upCol, rightCol)
        upRight = zip(upCol, sorted(list(rightCol), reverse=True))
        moves = appendMoves(moves, col=upRight)

    # Calculate moves down and to the right
    if rightValid and downValid:
        downRight = zip(downCol, rightCol)
        moves = appendMoves(moves, col=downRight)

    # Calculate moves down and to the left
    if downValid and leftValid:
        downLeft = zip(downCol, sorted(list(leftCol), reverse=True))
        moves = appendMoves(moves, col=downLeft)

    # Calculate moves up and to the left
    if upValid and leftValid:
        upLeft = zip(upCol, leftCol)
        moves = appendMoves(moves, col=upLeft)
    return moves


def multOneMove(move, grid):
    '''
    For one list containing tuples, look up the values from the grid and perform the multiplication
    :param move:
    :return: integer
    '''
    mult = 1
    for cell in move:
        mult = mult * grid.iloc[cell]
    return mult

def calcAllMoves(mults=4, maxRow=19, maxCol=19):
    '''
    Returns list of all moves
    '''
    allMoves = []
    for i in range(maxRow+1):
        for j in range(maxCol+1):
            moves = returnCells(row=i, col=j, mults=mults, maxRow=maxRow, maxCol=maxCol)
            allMoves = allMoves + moves
    return allMoves






################################################################


allMoves = calcAllMoves()
len(allMoves)
#2516

counter = 0
maxMult = 0
for move in allMoves:
    testVal = multOneMove(move, grid)
    plotMoves(0, 0, grid)
    if testVal > maxMult:
        maxMult = testVal
        print(str(counter) + ' : ' + str(move) + ' = ' + str(testVal))
    counter+=1

assert(len(allMoves) == counter)

# 0 : [(0, 0), (0, 1), (0, 2), (0, 3)] = 34144
# 1 : [(0, 0), (1, 0), (2, 0), (3, 0)] = 1651104
# 7 : [(0, 2), (1, 2), (2, 2), (3, 2)] = 6414210
# 10 : [(0, 3), (1, 3), (2, 3), (3, 3)] = 6514520
# 32 : [(0, 7), (1, 8), (2, 9), (3, 10)] = 11587200
# 90 : [(1, 0), (2, 1), (3, 2), (4, 3)] = 16194745
# 108 : [(1, 5), (2, 5), (3, 5), (4, 5)] = 25723980
# 181 : [(2, 1), (3, 2), (4, 3), (5, 4)] = 32719995
# 803 : [(6, 15), (7, 15), (8, 15), (9, 15)] = 51267216

################################################################
## Debug stuff

def lookupVals(move, grid):
    printStr = str(move) + '\n'
    for i in move:
        printStr = printStr + ', '+ str(grid.iloc[i])
    print(printStr)

move = [(6, 15), (7, 15), (8, 15), (9, 15)]
lookupVals(move, grid)

move = [(0, 2), (1, 3), (2, 4), (3, 5)]
lookupVals(move, grid)

# Walk through first values manually
move = [(0, 0), (0, 1), (0, 2), (0, 3)]
lookupVals(move, grid) # 34144


move = allMoves[1]
move = [(0, 0), (1, 0), (2, 0), (3, 0)]
lookupVals(move, grid) #1651104



from collections import Counter
def validateCount(allMoves):
    '''
    Determines whether the min and max values from the list of move tuples is >0 and <100
    Also gives you a count
    :param moves:
    :return: True or False
    '''
    allList = []
    for move in allMoves:
        allList = allList + list(itertools.chain(*move))
    print('min:' + str(min(allList)))
    print('max:' + str(max(allList)))
    c = Counter(allList)
    print(str(c.keys()))
    print(str(c.values()))



validateCount(allMoves)



def plotMoves(row, col, grid):
    gridVals = [[0 for i in range(len(grid))] for j in range(len(grid))]
    gridVals = pd.DataFrame(gridVals)
    gridVals.iloc[row, col] = 1
    moves = returnCells(row, col)
    for move in moves:
        for i in move:
            gridVals.iloc[i] = .5
    img = pyplot.imshow(gridVals)
    pyplot.show()


plotMoves(0, 0, grid)
plotMoves(10, 10, grid)
plotMoves(19, 19, grid)
plotMoves(19, 0, grid)
plotMoves(2, 0, grid)
plotMoves(17, 17, grid)
plotMoves(15, 18, grid)




########################################
# Count moves
moveCount = []
for i in range(20):
    mo = []
    for j in range(20):
        mo = mo + [len(returnCells(i, j))]
    moveCount = moveCount + [mo]




# tell imshow about color map so that only set colors are used
img = pyplot.imshow(moveCount)

# make a color bar
pyplot.colorbar(img, ticks=range(3, 8+1, 1))
pyplot.show()


#### Tests
# All corners should return 3 entries
assert(len(returnCells(row=0, col=0)) == 3)
assert(len(returnCells(row=19, col=0)) == 3)
assert(len(returnCells(row=19, col=19)) == 3)
assert(len(returnCells(row=0, col=19)) == 3)

# Some middle value should return 8 entries
assert(len(returnCells(row=5, col=5)) == 8)

# Top, bottom, left and right NON-corner and middle values should return 5 entries
# Top
assert(len(returnCells(row=0, col=10)) == 5)
# left
assert(len(returnCells(row=10, col=0)) == 5)
# Right
assert(len(returnCells(row=10, col=19)) == 5)
# Botton
assert(len(returnCells(row=19, col=10)) == 5)

assert(len(returnCells(3, 0)) == 5)
assert(len(returnCells(16, 0)) == 5)
assert(len(returnCells(0, 16)) == 5)
assert(len(returnCells(0, 3)) == 5)



assert(len(returnCells(2, 0)) == 3)
assert(len(returnCells(17, 0)) == 3)
assert(len(returnCells(0, 17)) == 3)
assert(len(returnCells(0, 2)) == 3)

# Test top left corner
moves = returnCells(row=0, col=0)
move = moves[0]
assert(multOneMove(move, grid) == grid.iloc[0,0] * grid.iloc[0,1] * grid.iloc[0,2]* grid.iloc[0,3])

# Validate example given in text of problem
move = [(6, 8), (7, 9), (8, 10), (9, 11)]
lookupVals(move, grid) # matches, 26, 63, 78, 14
assert(multOneMove(move, grid)==1788696)

# TODO: Validate move counts alegraically. Make sure matches len(allMoves)
# Move Counts
# (0:mults-1, 0) = 3
# (mults: n-mults, 0) = 5
# (n - mults +1:n-1, 0) = 3
#
