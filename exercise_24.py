# Problem 24
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations
# of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#https://docs.python.org/2/library/itertools.html#itertools.permutations
# Not permutations are emitted in lexographic order, so just need to count the
# millionth.

from itertools import permutations

n = 10
maxI = 10**6
#maxI = 10
digitSet = permutations(range(0, n))
for i, val in enumerate(digitSet):
    #print(i, val)
    if i==maxI-1:
        print(''.join(str(val).replace('(', '').replace(')', '').replace(',','')))
        break
