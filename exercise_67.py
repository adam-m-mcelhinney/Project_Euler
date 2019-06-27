# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve
# this problem, as there are 299 altogether! If you could check
# one trillion (1012) routes every second it would take over twenty billion years to
# check them all. There is an efficient algorithm to solve it. ;o)



# NOT WORKING!!
# Think I need to research alogrithms to find the shortest path between a weighted graph
# I think Djikstra's algorithm does this but Ill need to adjust so its the highest weighted path.
# Also, it appears this implementation assumes that edges are bidirectional, so I will need to
# update that.
# http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

# Update: Apparently for longest path problems, you cannot simply use the shortest path technique, for some
# reason that I do not understand. I think I need to do something called topological sorting.

from exercise_18 import *
from collections import defaultdict


def compute_weight(key, graphDict, grid, edges):
    '''For one entry in the graph, compute the weight of going to the other two edges.'''
    from_node = key
    res = graphDict[key]
    to_node1 = res[0]
    to_node2 = res[1]
    baseSum = getValue(positionTuple=from_node, grid=grid)
    weight1 = baseSum + getValue(positionTuple=to_node1, grid=grid)
    weight2 = baseSum + getValue(positionTuple=to_node2, grid=grid)
    return edges + [(from_node, to_node1, weight1)] + [(from_node, to_node2, weight2)]

def compute_all_weights(graphDict, grid):
    edges = []
    for key in graphDict.keys():
        edges = compute_weight(key, graphDict, grid, edges)
    return edges






class Graph():
    def __init__(self):
        # Default dict will automatically call whatever is passed to the argument if you specify a
        # key that does not exist in the dictionary. For in this example, it will call the list function
        # on whatever is passed to the dict. It will never return a key error.
        # https://www.accelebrate.com/blog/using-defaultdict-python/
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight





# I tihnk we need to
# 1. recode dijsktra to find the "longest" (highest weighted) sum and return that sum
# 2. Run dikistra for 100 possible end points (the nodes on the bottom of the graph)

def dijstrka(graph, initial, end):
    # longest_paths is a dict of nodes
    # whose value is a tuple of (previous_node, weight)
    longest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        # log the node that we have looked at
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = longest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in longest_paths:
                longest_paths[next_node] = (current_node, weight)
            else:
                current_longest_weight = longest_paths[next_node][1]
                if current_longest_weight < weight:
                    longest_paths[next_node] = (current_node, weight)

        next_destinations = {node: longest_paths[node] for node in longest_paths if node not in visited}

        # next node is the destination with the highest weight
        current_node = max(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = longest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path


def dijstrkaAllEnds(graph, initial, grid):
    maxLen = len(grid)-1
    endPoints =[(maxLen, i) for i in range(maxLen)]
    maxWeight = 0
    maxPath = []
    for end in endPoints:
        testPath = dijstrka(graph=graph, initial=initial, end=end)
        weight = getPathSum(testPath, grid = grid)
        if weight > maxWeight:
            maxWeight = weight
            maxPath = testPath
    return maxWeight, maxPath




# test run

testGrid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
grid = testGrid

graphDict = generateGraph(grid=grid)
edges = compute_all_weights(graphDict = graphDict, grid = grid)

graph = Graph()

for edge in edges:
    graph.add_edge(*edge)

end = (13, 5)
end = (3, 2)
initial = (0,0)

path = dijstrka(graph = graph, initial=(0,0), end = end)
weight = getPathSum(path, grid = grid)
assert path == [(0,0), (1, 0), (2, 1), (3, 2)]
assert weight == 23, weight

# final run


filePath = '/Users/amcelhinney/repos/Project_Euler/exercise_67_grid.txt'

with open(filePath) as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [i.split(' ') for i in content]


grid = [[int(val) for val in row] for row in content]

graphDict = generateGraph(grid=grid)
edges = compute_all_weights(graphDict = graphDict, grid = grid)

graph = Graph()

for edge in edges:
    graph.add_edge(*edge)

end = (99, 5)
initial = (0,0)

path = dijstrka(graph = graph, initial=(0,0), end = end)
weight = getPathSum(path, grid=grid)

# Not giving the right answer. Fuck
maxWeight, maxPath = dijstrkaAllEnds(graph, initial, grid)