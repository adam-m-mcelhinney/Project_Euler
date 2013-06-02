"""
Project Euler
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

"""

def is_divisible(m, mn=1, mx=20):
    """
    Returns whether a number is divisible evenly by all nums 1-20
    """
    i = 1
    while True:
        if i>mx:
            break
        if m % i != 0:
            return False
        i +=1
    return True

def smallest_divisible(mn=1, mx=20, max_iter = 1000000):
    i = 1
    while True:
        #print i
        if i> max_iter:
            return "Max Iterations"
        if is_divisible(i, mn, mx) == True:
            return i
        i += 1




if __name__ == '__main__':
    assert is_divisible(2520,1,10) == True
    assert smallest_divisible(mn = 1, mx = 10, max_iter = 1000000)==2520
    print smallest_divisible(mn = 1, mx = 20, max_iter = 100000000000000000)

