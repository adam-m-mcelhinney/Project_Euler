# Problem 68
# 5-gon ring
# Leveraging this class implementation of a graph
# http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
from collections import defaultdict
from numpy import nan

class gonRing():

    def __init__(self):
        '''Paths are lists of node numbers that are connected to sum to the magic number
        By convention, the first element of the list will be the external node. Also, paths
        must be entered clockwise.
        '''
        self.paths = []
        self.numPaths = 0
        #self.numNodes = 0
        '''Path values are integers that are stored in a given node'''
        self.pathVals = []
        '''Path totals are the sum of all the path vals in a given path'''
        self.pathTotals = []
        self.values = {}
        self.isMagic = False
        self.magicTotal = nan
        # self.externalNodes = []
        self.magicConcat = nan


    def __repr__(self):
        return(f'paths: {self.paths}, pathVals: {self.pathVals}, pathTotals: {self.pathTotals}, magicTotal: {self.magicTotal}')


    def add_path(self, pathList):

        self.paths.append(pathList)
        self.numPaths = len(self.paths)
        self.pathVals.append([nan for i in range(len(pathList))])
        self.pathTotals = [nan for i in range(self.numPaths)]
        #self.externalNodes.append(pathList[0])

    def add_value(self, node, val):
        self.values[node] = val
        # Need to update the path totals
        for i, path in enumerate(self.paths):
            for j, pathVal in enumerate(path):
                if pathVal == node:
                    self.pathVals[i][j] = val
            self.pathTotals[i] = sum(self.pathVals[i])
        self._setmagic()

    def _setmagic(self):
        pathTotalSet = set(self.pathTotals)
        # Not sure what happens if everything is nan here
        if len(pathTotalSet) == 1:
            self.isMagic = True
            self.magicTotal = self.pathTotals[0]
            self._concatenateMagicTotal()
        else:
            self.isMagic = False
            self.magicTotal = nan
            self.magicConcat = nan
    # TODO: This is wrong somehow.
    def _concatenateMagicTotal(self):
        startList = self.pathVals[0]
        startVal = 999
        startIndex = 0
        for i, path in enumerate(self.pathVals):
            if path[0] < startVal:
                startVal = path[0]
                startIndex = i
        concatenateOrder = [(startIndex+i)%self.numPaths for i in range(self.numPaths)]
        concatStr = ''
        for i in concatenateOrder:
            for j in self.pathVals[i]:
                concatStr = concatStr + str(j)
        self.magicConcat = concatStr









# print(ring.pathVals)
# print(ring.paths)
# print(ring.numPaths)
# print(ring.pathVals)
# print(ring.pathTotals)
# print(ring.isMagic)
# print(ring.magicTotal)
# print(ring.magicConcat)


def createTestCase(testString, paths):
    '''The website lists things in teh form
    9	4,2,3; 5,3,1; 6,1,2
    magicTotal  pathvals (separated by ;)
    '''
    splt_str =  testString.split('\t')
    magicTotal = int(splt_str[0])
    testVal = splt_str[1].replace(' ', '').replace(';',',').split(',')
    testVal = [int(i) for i in testVal]
    pathVals = {}
    flatPath = [node for path in paths for node in path]
    for i, val in enumerate(testVal):
        node = flatPath[i]
        if node not in pathVals:
            pathVals[node] = val
    return pathVals, magicTotal, testVal


def createRing(pathVals, paths, magicTotal = None, testString = None):

    ring = gonRing()
    # Add paths
    for i, path in enumerate(paths):
        ring.add_path(path)
    # Add nodes
    for node in pathVals.keys():
        ring.add_value(node=node, val = pathVals[node])
    if magicTotal != None:
        assert magicTotal == ring.magicTotal
    if testString != None:
        assert ring.magicConcat == testString
    return ring








# Taken from the website
website_solutions =\
    ['9	4,2,3; 5,3,1; 6,1,2',
'9	4,3,2; 6,2,1; 5,1,3',
'10	2,3,5; 4,5,1; 6,1,3',
'10	2,5,3; 6,3,1; 4,1,5',
'11	1,4,6; 3,6,2; 5,2,4',
'11	1,6,4; 5,4,2; 3,2,6',
'12	1,5,6; 2,6,4; 3,4,5',
'12	1,6,5; 3,5,4; 2,4,6']


for case in website_solutions:
    pathVals, magicTotal, cleanSolution = createTestCase(case, paths)
    ring = createRing(pathVals, paths, magicTotal = magicTotal)



from itertools import permutations
valuesToTest = permutations(list(range(1,7)))
nodeList = list(range(6))
solutions = []
for i, val in enumerate(valuesToTest):
    pathVals = dict(zip(nodeList, val))
    ring = createRing(pathVals, paths)
    if ring.isMagic:
        solutions.append(ring)


solutionConcats = []
for solution in solutions:
    print(solution.magicConcat)
    solutionConcats.append(solution.magicConcat)
uniqueSolutions = set(solutionConcats)
assert len(uniqueSolutions) == len(website_solutions)


# Test real solution
paths = [[0, 1, 2], [3, 2, 4], [5, 4, 6], [7, 6, 8], [9, 8, 1]]
from itertools import permutations
maxVal = 10
valuesToTest = permutations(list(range(1,maxVal+1)))
nodeList = list(range(maxVal+1))
solutions = []
for i, val in enumerate(valuesToTest):
    pathVals = dict(zip(nodeList, val))
    ring = createRing(pathVals, paths)
    if ring.isMagic:
        solutions.append(ring)


solutionConcats = []
for solution in solutions:
    print(solution.magicConcat)
    solutionConcats.append(solution.magicConcat)
uniqueSolutions = set(solutionConcats)
len(uniqueSolutions)

# need only 16 digit solutions
sixteen_sol = []
for sol in uniqueSolutions:
    if len(sol) == 16:
        sixteen_sol.append(int(sol))

sorted(sixteen_sol)[::-1]



