# How many reversible numbers are there below one-billion?
#
# Problem 145
# Some positive integers n have the property that the sum [ n + reverse(n) ]
# consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313.
# We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
# Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (10**9)?
import timeit


def increment():
    for i in range(10**9+1):
        i

# Let's just see how long it takes to increment to a billion
# t = timeit.timeit(increment, number =1)
# print(t)
# ~26 seconds


n = 145
def reverseInt(n):
    return int(str(n)[::-1])



# Slowest part of the code is here
def isOddDigits(n=13131113131313131313131313131579):
    nS = str(n)
    result = True
    for digit in nS:
        if int(digit)%2==0:
            result = False
            break
    return result




def isOddDigits2(n=13131113131313131313131313131579):
    evenDigits = ['0', '2', '4', '6', '8']
    result = True
    nS = str(n)
    for digit in nS:
        if digit in evenDigits:
            result = False
            break
    return result


def isOddDigits3(n=13131113131313131313131313131579):
    evenDigits = ['0','2', '4', '6', '8']
    result = True
    nS = set(str(n)) # Dont check duplicate digits
    for digit in nS:
        if digit in evenDigits:
            result = False
            break
    return result

assert(isOddDigits(1313))
assert(isOddDigits2(1313))
assert(isOddDigits3(1313))
assert(isOddDigits(2468) == False)
assert(isOddDigits2(2468) == False)
assert(isOddDigits3(2468) == False)

# print(timeit.timeit(isOddDigits, number = 10000))
# print(timeit.timeit(isOddDigits2, number = 10000))
# print(timeit.timeit(isOddDigits3, number = 10000))

# Strategy, for every integer 1-10**9, comppute the reverse
# and then sum it. If odd, then reversible. Store all the inteegers tested,
# and the the reverse in dictionaries (O(1) complexity) and then as the value,
# store True/False for is reversable or not.


def isReverse(n, reverse):
    testVal = n + reverse
    if isOddDigits3(testVal):
        return 1
    else:
        return 0
# TODO: Consider exploiting fact that sum of two even is even and sum
# of two odd is odd etc
# http://www.math.vt.edu/people/mcquain/answks5_06.pdf

# assert isReverse(n=409, reverse=reverseInt(409))
# assert isReverse(n=36, reverse=reverseInt(36))

# maxN = 1000
maxN = 10**9
#maxN = 10**8
from numpy import nan
# Try preallocating the memory to speed it up
testDict = {i:-1 for i in range(1, maxN)}
for i in testDict:
#for i in range(11, maxN):
    #if i in testDict or i%10==0:
    if i%10==0 or testDict[i]!=-1:
        continue
    else:
        reverse = reverseInt(i)
        if reverse%10==0:
            continue
        t = isReverse(i, reverse)
        testDict[i] = t
        testDict[reverse] = t

# assert(sum(testDict.values()) == 120)
# assert(list(testDict.values()).count(1) == 120)
assert(testDict[36] ==1)
assert(testDict[63] ==1)
assert(testDict[409] ==1)
assert(testDict[904] ==1)
print(list(testDict.values()).count(1))

# for i in testDict:
#     if testDict[i] == 1:
#         print(i)