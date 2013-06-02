"""
Project Euler
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.



"""
from math import floor

def is_palin(k):
    k = str(k)
    for i in range(len(k)/2):
        #print k[i], k[-1-i]
        if k[i] != k[-1-i]:
            return False
    return True

def largest_palin(d):
    """
    Largest palindrome product consisting of d-digits
    """
    n = 0 # max palindrome value

    # Define end value. Should be 9 + (d-1) 9's. For example, d=3, end at 999
    mx = int('9' + ''.join(['9' for i in range(d-1)]))
    j = mx
    while True:
        if j == 0:
            break
        e = xrange(1, j)
        for i in e:

            prod = e[-i] * j
            print 'Testing ' + str(j) + ' * ' + str(e[-i]) + ' = ' + str(prod)

            if is_palin(prod) == True:
                print 'Found palindrome: '  + str(prod)
                if prod > n:
                    n = prod

        j += (-1)
    return n





if __name__ == '__main__':
    assert is_palin(9009) == True
    assert is_palin(913319) == True
    assert is_palin(91334319) == False
    w = largest_palin(2)
    print w
    z = largest_palin(3)
    print z


