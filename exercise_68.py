# Problem 68
# 5-gon ring
# Leveraging this class implementation of a graph
# http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
from collections import defaultdict
from numpy import nan

class gonRing():

    def __init__(self):
        self.numNodes = None
        '''Paths are lists of node numbers that are connected to sum to the magic number
        By convention, the first elemnet of the list will be the external node. Also, paths
        must be entered clockwise.
        '''
        self.paths = []
        self.numPaths = 0
        '''Path values are integers that are stored in a given node'''
        self.pathVals = []
        '''Path totals are the sum of all the path vals ni a given path'''
        self.pathTotals = []
        self.values = {}
        self.isMagic = False
        self.magicTotal = nan
        self.externalNodes = []
        self.magicConcat = nan

    def add_path(self, pathList):

        self.paths.append(pathList)
        self.numPaths = len(self.paths)
        self.pathVals.append([nan for i in range(len(pathList))])
        self.pathTotals = [nan for i in range(self.numPaths)]
        self.externalNodes.append(pathList[0])

    def add_value(self, node, val):
        self.values[node] = val
        for i,path in enumerate(self.paths):
            for j, t in enumerate(path):
                if t == node:
                    self.pathVals[i][j] = val
            self.pathTotals[i] = sum(self.pathVals[i])
        self._setmagic()

    def _setmagic(self):
        pathTotalSet = set(self.pathTotals)
        # Not sure what happens if everytihn is nan here
        if len(pathTotalSet) == 1:
            self.isMagic = True
            self.magicTotal = self.pathTotals[0]
            self._concatenateMagicTotal()
        else:
            self.isMagic = False
            self.magicTotal = nan
            self.magicConcat = nan

    def _concatenateMagicTotal(self):
        startList = self.pathVals[0]
        startVal = 999
        startIndex = 0
        for i, path in enumerate(self.pathVals):
            if path[0] < startVal:
                startIndex = i
        concatenateOrder = [(startVal+i)%self.numPaths for i in range(self.numPaths)]
        concatStr = ''
        for i in concatenateOrder:
            for j in self.pathVals[i]:
                concatStr = concatStr + str(j)
        self.magicConcat = concatStr










ring = gonRing()
paths = [[0, 1, 2], [3, 2, 4], [5, 4, 1]]
for path in paths:
    ring.add_path(path)

pathVals = {0:4, 1:3, 2:2, 3:6, 4:1, 5:5}

for node in pathVals.keys():
    ring.add_value(node=node, val = pathVals[node])

print(ring.pathVals)
print(ring.paths)
print(ring.numPaths)
print(ring.pathVals)
print(ring.pathTotals)
print(ring.isMagic)
print(ring.magicTotal)
print(ring.externalNodes)
print(ring.magicConcat)


pathVals = {0:4, 1:3, 2:2, 3:6, 4:1, 5:999}
for node in pathVals.keys():
    ring.add_value(node=node, val = pathVals[node])


# TODO: Need to work on this part
from itertools import permutations
testVals = permutations(list(range(5)))
allPaths = []
for testVal in testVals:
    pathVals = {}
    for i, val in enumerate(testVal):
        pathVals[i] = val
        ring = gonRing()
        for node in pathVals.keys():
            ring.add_value(node=node, val = pathVals[node])
            if ring.isMagic:
                print(ring.magicTotal)
                print(ring.magicConcat)

    allPaths.append(pathVals)


