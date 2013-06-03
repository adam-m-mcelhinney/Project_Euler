"""
Project Euler
Problem 9


A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.



"""
from itertools import combinations

from math import sqrt

def find_c(a, b):
    return sqrt(a**2 + b**2)

def check_trip(a, b, c):
    if a**2 + b**2 == c**2 and c == int(c):
        return True
    else:
        return False

def check_sum(a, b, c):
    if a + b + c == 1000:
        return True
    else:
        return False






if __name__ == '__main__':
    search_space = combinations(range(1, 1000),2)
    for i in search_space:
        a = i[0]
        b = i[1]
        c = find_c(a, b)
        if check_trip(a, b, c) == True:
            if check_sum(a, b, c)== True:
                break

    print 'Solution found ' + str(a) + ', ' + str(b) + ', ' + str(c)


