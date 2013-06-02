"""
Project Euler
Problem 35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?


Notes:
    1. This is really frigging slow. Can't figure out why.
    Perhaps the lookups in the ordered dict arent as fast?
    Perhaps I should first do a pass in the dictionary and only save primes that
    are less than one million?
    2. Not seeing a huge speed-up with pypy. Why?

"""
import csv
from itertools import cycle, islice
import collections

# http://stackoverflow.com/questions/8451532/why-doesnt-this-return-the-rotations-of-the-given-number
# Important modification to the 'yield list...' line!
def rotate(L):
    ln = len(L)
    it = cycle(iter(L)) #create an overall iterator
    for _ in range(ln): #there are len(L) output lists
        yield list(islice(it,ln)) #slice next elements, for a list and yield the rusult
        it.next() #skip one element to start a new list shifted by one

def is_circular_prime(k, prime):
    rotations = list(rotate(str(k)))

    for i in rotations:
        t = ''.join(i)
        #print t
        if int(t) not in prime.keys():
            return False
    return True

def count_circle_primes(prime, mx):
    """
    Counts the number of circular primes in prime, less  mx
    """
    count = 0
    i = 0
    while True:
        num = prime[prime.keys()[i]]
        print 'Testing ' + str(num)
        if num > mx:
            break
        if is_circular_prime(num, prime) == True:
            print 'Found circular prime: ' + str(num)
            count += 1
        i += 1
    return count








if __name__ == '__main__':
    file = 'C:\Users\Adam\Documents\GitHub\Project_Euler\one_million_primes.txt'

    # Read in the primes
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ')
        prime = {}
        for row in spamreader:
            for i in row:
                try:
                    prime[int(i)] =int(i)
                except:
                    pass

    # Need to order the dictionary!
    prime = collections.OrderedDict(sorted(prime.items()))
    r = count_circle_primes(prime, mx = 1000000)
    print r

