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




def factors(n):
    # Adapted from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    # May need to refactor to save the factors to a dictionary to avoid
    # mem overflow
    return reduce(list.__add__,
                ([i, n//i] for i in
                range(1, int(n**0.5) + 1) if n % i == 0))
                #range(1, sqrt(n) + 1) if n % i == 0))

def Alex_new(A, prev_max, verbose = False, test = False):
    """
    Steps:
        1. Calculate all the factors of the number
        2. Calc all combinations of all positive or two negative factors
        3. Test those values
    """
    f = factors(A)
    #g = [-1 * i for i in f if i>= prev_max]
    g = [-1 * i for i in f]
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
            if verbose == True: return True, p, q, r
            else: return True, max(p, q, r)
    return False, None


def ith_Alex_new(N, verbose = False):

    start = datetime.now()
    i = 0
    j = 2 # Only even numbers can be Alexandarian
    mx = 0
    values = []
    while i <= N:

        if verbose == True:
            print 'testing ' + str(j)
        #t, mx = Alex_new(j, mx)
        z = Alex_new(j, mx, verbose= True)
        t = z[0]

        if t == True:
            p = z[1]
            q = z[2]
            r = z[3]
            mx = max(p, q, r)
            values.append([j, p, q, r])
            i += 1
            if verbose == True:
                print str(i) +'th Number is ' + str(j)
        if i == N:
            end = datetime.now()
            t = end - start
            print 'Execution time: ' + str(t)
            return values
        else:
            j += 2


def unit():
    """
    Tests whether the first 39 euler numbers agree
    with
    http://oeis.org/A147811/b147811.txt
    """
    f = open('C:/Local Files/euler_check.csv', 'rb')
    reader = csv.reader(f)
    control_values = []
    for row in reader:
        #print row
        v = row[0].split(' ')
        #print v
        i = v[0]
        #print i
        c_val = v[1]
        control_values.append([i, c_val])
        print c_val
    print i
    values = ith_Alex_new(i, verbose = True)
    for i in range(len(values)):
        test_val = values[i][0]
        control_val = control_values[i][1]
        #print test_val
        print control_val, test_val
        if float(control_val) != test_val:
            print 'Error on ' + str(i) + 'th value'
    return values
























if __name__ == '__main__':
    values = unit()
    with open('C:/Local Files/alex_integers.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', dialect = 'excel')
        spamwriter.writerows(values)







