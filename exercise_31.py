# In England the currency is made up of pound, £, and pence, p, and there are eight coins
# in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# Notes
# We know the number of coins to make one amount of 2 GBP is between 1 and 200, inclusive
import numpy as np
from itertools import permutations, product

coinVals = [1, 2, 5, 10, 20, 50, 100, 200]
maxCoins = [int(200/coin) for coin in coinVals]



# Problem is to find A, B, C, D, E, F, G, H, such that
# A*1 + 2*B + 5*C + 10*D + 20*E + 50*F + 100*G + 200*H == 200
def computeValue(A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0):
    return(np.dot([A, B, C, D, E, F, G, H], coinVals))


def computeA(B, C, D, E, F, G):
    '''Return how many of coefficient A we need'''
    return(200 - np.dot(coinVals[1:7], [B, C, D, E, F, G]))

# Choose values of A, B, C, D, E, F, G
# Note we know only one combo for H works
# Also, if we know k-1 of the values, we know the final value, so we can eliminate one loop
# Since A has the most possible values, let's eliminate that one from the loop
counts = 1 # Accounts for H=1
DEBUG = False
maxDebugRuns = 100
debugRuns = 0
# TODO: I think there is a more elegant way to do this using permutations of lists, but for now this is fine
for B in range(0, maxCoins[1] + 1):
    for C in range(0, maxCoins[2] + 1):
        for D in range(0, maxCoins[3] + 1):
            for E in range(0, maxCoins[4] + 1):
                for F in range(0, maxCoins[5] + 1):
                    for G in range(0, maxCoins[6] + 1):
                        A = computeA(B=B, C=C, D=D, E=E, F=F, G=G)
                        if A >=0:
                            counts +=1
                            if DEBUG == True:
                                val = computeValue(A, B, C, D, E, F, G)
                                print(A, B, C, D, E, F, G, val)
                        debugRuns +=1
                        if debugRuns > maxDebugRuns and DEBUG == True:
                            raise TypeError #Per research, this is Pythonic way to break multiple for loops









assert(computeValue()==0)
assert(computeValue(H=1)==200)

# Didnt konw you could nest functions as function arguments in Python, but appears you can.
assert(200 == computeValue(A=computeA(B=4, C=3, D = 2, E = 1, F=0, G=0), B=4, C=3, D = 2, E = 1, F=0, G=0))
