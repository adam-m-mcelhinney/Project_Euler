# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.

import pdb



testGrid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]



# https://www.python.org/doc/essays/graphs/
# Let's try to implement the graph in a dictionary, like this article.

def acceptableMove(positionTuple, graph):
    row = positionTuple[0]
    position = positionTuple[1]
    graph[positionTuple] = [(row+1, position), (row+1, position+1)]
    return graph



def generateGraph(grid):
    '''Generate a dictionary that stores the graph of acceptable moves.
    Returns a position tuple, then a list of other position tuples that its linked to.
    (0, 0): [(1, 0), (1, 1)]
    '''
    graph= dict()
    maxRows = len(grid)
    row = 0
    # Do not need to determine acceptableMoves for the last row
    while row < maxRows-1:
        maxPositions = row+1
        for i in range(maxPositions):
            positionTuple = (row, i)
            graph = acceptableMove(positionTuple=positionTuple, graph=graph)
        row += 1
    return graph

graph = generateGraph(grid=testGrid)



def getMaxRowMaxPos(graph):
    maxRow = 0
    maxPos = 0
    for node in graph.keys():
        if node[0] > maxRow:
            maxRow = node[0]
        if node[1] > maxPos:
            maxPos = node[1]
    # Recall that this is the max key, so the final row is this plus 1
    return maxRow+1, maxPos+1

maxRow, maxPos = getMaxRowMaxPos(graph)



def findAllPaths(graph, maxRow, maxPos, start = (0,0), path =[]):
    path = path + [start]
    row = start[0]
    position = start[1]
    # Should this be an or?
    if row == maxRow or position == maxPos:
        return [path]
    paths = []
    for node in graph[start]:
        # I think I need to split the start nodes here and run this twice?
        newpaths = findAllPaths(graph, maxRow, maxPos, start= node, path=path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

#pdb.set_trace()
allPaths = findAllPaths(graph=graph, maxRow=maxRow, maxPos=maxPos)
# from the example given in the problem
testPathList = [(0,0), (1, 0), (2, 1), (3, 2)]
assert testPathList in allPaths

def getValue(positionTuple, grid):
    '''For a given input tuple (row, position)
    return the corresponding value from the grid
    getValue((0, 0), grid = testGrid)
    getValue((1, 1), grid = testGrid)
    '''
    return grid[positionTuple[0]][positionTuple[1]]

def getPathSum(pathList, grid):
    '''For a given path list, return the total sum
    :rtype: object
    '''
    totalVal = 0
    for positionTuple in pathList:
        totalVal += getValue(positionTuple, grid)
    return totalVal

getPathSum(allPaths[0], grid=testGrid)
assert getPathSum(testPathList, grid=testGrid) == 23


def getMaxSum(allPathList, grid):
    '''For a given list of all paths, find the maximal sum'''
    maxSum = 0
    for pathList in allPathList:
        testVal = getPathSum(pathList, grid)
        if testVal > maxSum:
            maxSum = testVal
    return maxSum

assert getMaxSum(allPaths, grid=testGrid) == 23



# final run for answer
filePath = '/Users/amcelhinney/repos/Project_Euler/exercise_18_grid.txt'

with open(filePath) as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [i.split(' ') for i in content]

grid = [[int(val) for val in row] for row in content]
graph = generateGraph(grid=grid)
maxRow, maxPos = getMaxRowMaxPos(graph)
allPaths = findAllPaths(graph=graph, maxRow=maxRow, maxPos=maxPos)
t = getMaxSum(allPaths, grid=grid)
print(t)
