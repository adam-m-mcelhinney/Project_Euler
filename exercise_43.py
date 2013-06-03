"""
Project Euler
Problem 43

Pandigital number because it is made up of each of the digits 0 to 9 in
some order

1406357289
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
etc

Find the sum of all 0 to 9 pandigital numbers with this property.

"""
from itertools import permutations

def pandigital(k):
    """
    Generates all pandigital numbers of k digits
    """
    w = ''.join([str(i) for i in range(0,k)])
    p = []
    z = list(permutations(w, len(w)))
    for i in range(len(z)):
        p.append(''.join(z[i]))
    return p

def substring_divisble(k):
    denom = [2, 3, 5, 7, 11, 13, 17]
    k = str(k)
    c = 1 # Counter, starting at one but in problem example the first digit is
          # considered in the first position
    for i in denom:
        j = int(k[c:c+3])
        #print j, i
        if j % i != 0:
            return False
        c += 1
    return True

def pand_sum(k):
    s = 0 # accumulator for the sum
    p = pandigital(k)
    for i in p:
        print 'Testing ' + str(i)
        if substring_divisble(i) == True:
            print 'Substring Found ' + str(i)
            s += int(i)
    return s




if __name__ == '__main__':
    k = 1406357289
    assert substring_divisble(k) == True
    assert '1406357289' in pandigital(10)
    print pand_sum(10)



