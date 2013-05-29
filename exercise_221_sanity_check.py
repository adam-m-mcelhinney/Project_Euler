"""
Project Euler
Problem 221
Answer Check

Getting weird answers that dont tie out in Excel. May be an issue with the
way Excel handles large numbers.
"""

import csv
from fractions import Fraction

def check_prod(values):
    for i in range(len(values)):

        if(float(values[i][0]) != float(values[i][1]) *
        float(values[i][2]) * float(values[i][3])):
            return i

def check_fraction(values):
    for i in range(len(values)):
        if(
        Fraction(1,int(values[i][0])) !=
        Fraction(1,int(values[i][1])) +
        Fraction(1,int(values[i][2])) +
        Fraction(1,int(values[i][3]))
        ):
            return i

def check_type(values):
        for i in range(len(values)):
            if(
            str(int(values[i][0])) != values[i][0]

            ):

                return i

def check_distinct(values):
    A = list(set([int(values[i][0]) for i in range(len(values))]))
    A.sort()
    for i in range(0, len(A)-1):
            if(
            A[i] >= A[i+1]
            ):
                return i



if __name__ == '__main__':
    values = []
    with open('C:/Local Files/alex_integers.csv', 'rb') as csvfile:
        spamreader  = csv.reader(csvfile, delimiter=',')
        for row in spamreader :
            values.append(row)


    d = check_prod(values)
    print d
    f = check_fraction(values)
    print f
    g = check_type(values)
    print g
    h = check_distinct(values)
    print h
    A = list(set([int(values[i][0]) for i in range(len(values))]))
    A.sort()
    print len(A)
    print A[149999]
    print A[149999+1]
    print A[149997:150001]
    B = list(set([float(values[i][0]) for i in range(len(values))]))
    B.sort(reverse= True)
    B.sort()
    print len(B)
    print B[149999]
    print B[149999+1]
    print B[149997:150001]








