"""
Project Euler
Problem 10

Find the sum of all the primes below two million.

http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2073279#2073279

"""

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

if __name__ == '__main__':
    w = sundaram3(2000000)
    print sum(w)
