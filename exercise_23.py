# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called
# abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can
# be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be
# shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known
# that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def properDivisors(n):
    output = []
    for i in range(1, int(n/2 + 1)):
        if n%i == 0:
            output.append(i)
    return output


assert  properDivisors(28) == [1, 2, 4, 7, 14]

def isAbdundant(n):
    propDivisors = properDivisors(n)
    if sum(propDivisors) > n:
        return True
    else:
        return False

assert isAbdundant(12) == True
assert isAbdundant(28) == False

abundant = []
for i in range(12, 28123):
    if isAbdundant(i):
        abundant.append(i)


from itertools import combinations_with_replacement

t = combinations_with_replacement(abundant, 2)

# Find all numbers that CAN be written as a the sum of two abundant numbers
abundantSum = []
for i in t:
    # Don't next to call next when for looping
    s = sum(i)
    abundantSum.append(s)

# There are dupes in here, but I think that is okay
# Removing them for speed though
abundantSum[len(abundantSum)-10:len(abundantSum)]
len(abundantSum)
len(set(abundantSum))
abundantSum = list(set(abundantSum))
assert abundantSum[0] == 24
abundantSum[len(abundantSum)-10:len(abundantSum)]

# Also remove all entries ge than 28123
abundantSumShort = [i for i in abundantSum if i < 28123]
len(abundantSumShort)

notAbundSum = []
for i in range(1, 28123):
    if i%100 == True:
        print(i)
    if i not in abundantSumShort:
        notAbundSum.append(i)


assert(24 not in notAbundSum)

sum(notAbundSum)