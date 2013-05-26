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

def confirm_Alex(A, p, q, r):
    """
    Confirms whether a number is Alexandrian using the formal definition
    Slow performance
    """
    prod = p * q * r
    frac = Fraction(1, p) + Fraction(1, q) + Fraction(1, r)
    A_in = Fraction(1, A)
    #print prod, frac, A_in
    if prod == A and frac == A_in:
        return True
    else:
        return False

def confirm_Alex_fast(p, q, r):
    """
    Faster way to confirm if Alexandrian
    """
    if p*q*r < 0:
        return False
    if q*r + p*r + p*q -1 == 0:
        return True
    else:
        return False

def calc_p(q, r):
    """
    Returns the value of p, given q and r
    """
    return Fraction(1-q*r, r+q)

def prod(p, q, r):
    return p * q * r

def catch_zero(in_val, out_val):
    if in_val == 0:
        return out_val+1
    else:
        return out_val

##def is_Alex(A, verbose = False):
##    """
##    Checks whether a given number is Alexandrian
##    """
##    q = -A
##    # Using a for loop will result in overflow
##    # Loop through q- space
##    while True:
##        # If you've tried all values of q on the set -A:A and no solultion
##        # found, then none exists
##        print 'q: ' + str(q)
##        if q > A:
##            return False
##
##        # Skip q = zero
##        q= catch_zero(q, q)
##
##        max_r = A/float(q)
##        print 'max_r: ' + str(max_r)
##
##
##        r = int(abs(max_r) * -1)
##        # Loop through r - space
##        while True:
##
##            # Check to see if loop should continue
##            if r > max_r:
##                break
##            r = catch_zero(r+q, r)
##            p = calc_p(q, r)
##            print 'q =' + str(q) + ' r = ' + str(r) + ' p=' + str(p)
##
##            # Check if p is an integer
##            if p % p.denominator != 0:
##                r +=1
##
##
##            if confirm_Alex_fast(p, q, r) == True:
##                    if verbose == True:
##                        out = (A, p, q, r)
##                    else:
##                        out = True
##            r +=1
##        q += 1


def factors(n):
    # Adapted from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    # May need to refactor to save the factors to a dictionary to avoid
    # mem overflow
    return reduce(list.__add__,
                ([i, n//i] for i in
                range(1, int(n**0.5) + 1) if n % i == 0))


def Alex_simple(A, verbose = False):
    """
    Steps:
        1. Calculate all the factors of the number
        2. Calc all combinations of all positive or two negative factors
        3. Test those values
    """
    f = factors(A)
    g = [-1 * i for i in f]
    g.extend(f)
    g.sort()
    y = list((combinations(g,3)))
    for i in range(len(y)):
        p = y[i][0]
        q = y[i][1]
        r = y[i][2]
        if confirm_Alex_fast(p, q, r) == True and p * q * r == A:
            if verbose == True: return p, q, r
            else: return True
    return False

def Alex_new(A, prev_max, verbose = False, test = False):
    """
    Steps:
        1. Calculate all the factors of the number
        2. Calc all combinations of all positive or two negative factors
        3. Test those values
    """
    f = factors(A)
    g = [-1 * i for i in f if i>= prev_max]
    if test == True:
        print g
    g.extend(f)
    g.sort()
    y = list((combinations(g,3)))
    for i in range(len(y)):
        p = y[i][0]
        q = y[i][1]
        r = y[i][2]
        if confirm_Alex_fast(p, q, r) == True and p * q * r == A:
            if verbose == True: return p, q, r
            else: return True, max(p, q, r)
    return False, None


def ith_Alex(N, verbose = False):
    start = datetime.now()
    i = 0
    j = 2 # Only even numbers can be Alexandarian
    while i <= N:

        if verbose == True:
            print 'testing ' + str(j)
        if Alex_simple(j)== True:
            i += 1
            if verbose == True:
                print str(i) +'th Number is ' + str(j)
        if i == N:
            end = datetime.now()
            t = end - start
            print 'Execution time: ' + str(t)
            return j
        else:
            j += 2

def ith_Alex_new(N, verbose = False):
    start = datetime.now()
    i = 0
    j = 2 # Only even numbers can be Alexandarian
    mx = 0
    while i <= N:

        if verbose == True:
            print 'testing ' + str(j)
        t, mx = Alex_new(j, mx)
        if t == True:
            i += 1
            if verbose == True:
                print str(i) +'th Number is ' + str(j)
        if i == N:
            end = datetime.now()
            t = end - start
            print 'Execution time: ' + str(t)
            return j
        else:
            j += 2






















if __name__ == '__main__':
    p = 5
    q = -7
    r = -18
    A = 630

##    print Alex_new(630, prev_max = 4, verbose = True)
##    assert ith_Alex(1) == 6
##    assert ith_Alex(2) == 42
##    assert ith_Alex(3) == 120
##    assert ith_Alex(4) == 156
##    assert ith_Alex(5) == 420
##    assert ith_Alex(6) == 630
##    print ith_Alex(5, verbose = True)
##    a = [6, 42, 120, 156, 420, 630]
##    print [Alex_simple(i, verbose = True) for i in a]
    print ith_Alex(15, verbose = False)
    print ith_Alex_new(15, verbose = False)
##    Alex_new(420, 2, False, True)
##    Alex_simple(420, True)



