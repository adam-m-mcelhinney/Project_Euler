# Integer right triangles
#
# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# This is a forbenius problem. There are polynomial time solutions to this.
# https://arxiv.org/pdf/1001.0961.pdf


def perimeter(a, b, c):
    return a+b+c

def findC(a, b):
    return (a**2 + b**2)**(1/2)

def findP(a, b):
    return a + b + (a**2 + b**2)**(1/2)

def isRightTri(a, b, c):
    return a**2 + b**2 == c**2

resultsDict = {}

from itertools import product
p = 120
allSolutions = product(range(1,p), range(1,p))

for sol in allSolutions:
    a = sol[0]
    b = sol[1]
    c = findC(a, b)
    perim = perimeter(a, b, c)
    if perim in resultsDict:
        old = resultsDict[perim]
        old.append([a, b, c])
        resultsDict[perim] = old
    else:
        resultsDict[perim] = [[a, b, c]]


resultsDict[120]