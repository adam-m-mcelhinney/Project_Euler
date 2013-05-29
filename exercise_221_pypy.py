"""
Project Euler
Problem 221
We shall call a positive integer A an "Alexandrian integer",
if there exist integers p, q, r such that:

A = p ? q ? r    and
1/A = 1/p + 1/q + 1/r
For example, 630 is an Alexandrian integer (p = 5, q = -7, r = -18). In fact,
630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being:
6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.



Strategy:
    1. Find all factors of the number
    2. Find all negative factors of the number
    3. Chose all combinations of 3 of the factors
    4. Figure out which combinations of 3 factors multiplied equals A
    5. Check those items from 4

Notes:
    1. Can show mathematically that two of the values must be negative
    2. A is Alexandrian, then by combining and re-arranging the two
        equations, we find that q*r + p*r + p*q -1 = 0
    3. It appears that all Alexandarian numbers are even
    4. Based on number 1, we know that the min value must be positive
"""
from fractions import Fraction
from math import sqrt
from itertools import combinations
from datetime import datetime
import csv



def Alex_three(start_p, max_iter = 100000, max_alex = 3000000
,verbose = False):
    """
    Steps:
        1. Take a starting value of p
        2. Increment through q's, then calc r
        3. Check if r is integer, if not then next q
        4. Check if p * q * r is postive and integer, if not, next q


    Notes:
        1. For the maximum value of p, you are gaurenteed to have
        found all Alexander integers less than that value (bc q and r are
        negative)
        2. Make sure to set max_iter = max_alex.

    """
    alex = []
    start = datetime.now()
    p = start_p


    while True:
        q = -1
        if verbose == True:
            print 'Value of p: ' + str(p)
        if p > max_iter:
            end = datetime.now()
            t = end - start
            print 'Execution time: ' + str(t)
            return alex
        while True:

            if abs(q) > max_iter:
                break
            # NOTE: THIS MAY BE THROWING OUT VALID ALEX INTEGERS!
            elif q + p == 0:
                pass
            else:

                r = Fraction(1- p * q, q + p)
                if int(r) == r: # If r is a non-integer, then ignore it
                    prod = p * q * r
                    if int(prod) == prod and prod > 0:
                        alex.append([prod, p, q, r])
                        if len(alex) >= max_alex:
                            end = datetime.now()
                            t = end - start
                            print 'Execution time: ' + str(t)
                            return alex
##                        if verbose == True:
##                            print ' Alex number found: ' + str(prod)
            q += -1
        p += 1
























if __name__ == '__main__':


    # New method
    values = Alex_three(1, max_iter = 500000, max_alex =500000,
    verbose = True)
    A_vals = list(set([values[i][0] for i in range(len(values))]))
    A_vals.sort()
    print len(A_vals)
    with open('C:/Local Files/alex_integers.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', dialect = 'excel')
        spamwriter.writerows(values)




