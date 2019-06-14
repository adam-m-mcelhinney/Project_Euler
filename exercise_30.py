# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 1**4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# SOLVED! GRRR
from itertools import product

# Maybe the "one is not a sum thing" means that I skip all entries that have a
# 1 and I need maxExp +1 entries?
# WTF I am not understanding why this is the case




def sumOfPowers(maxExp):
    com = product(range(0, 10), repeat=maxExp+1)
    z =0
    resultList = []
    for i in com:
        z += 1
        testDigits = int(''.join([str(w) for w in i]))
        testSum = sum([j**maxExp for j in i])
        # Debug
        # if z%100 == 0:
        #     print(i)
        # Throw out
        if testDigits == 0 or testDigits == 1:
            continue
        # Can never be larger than 9 repeated maxExp times.
        # Ie, 9999 for maxExp=4
        # if testDigits > 10**maxExp:
        #     break
        if testDigits == testSum:
            print(testDigits)
            resultList.append(testDigits)
    print('Z interations', str(z))
    return resultList

third = sumOfPowers(3)

fourth = sumOfPowers(4)

assert(sum(fourth) == 19316)

fifth = sumOfPowers(maxExp=5)
sum(fifth)

# Not giving the correct answer.
# Does a leading zero count? Ie 04150
i = (0, 4, 1, 5, 0)