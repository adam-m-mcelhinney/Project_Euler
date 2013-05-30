"""
Project Euler
Problem 2

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms

"""

def is_even(k):
    if k % 2 == 0:
        return 1
    else:
        return 0


def fib_sum(end):
    p = 0 # first value
    q = 1 # second value
    r = 0 # next fib value
    s = 0 # total sum
    while True:
        # break loop when r exceeds end
        if r> end:
            return s

        r = p + q
        print 'Fib value: ' + str(r)
        if is_even(r) ==1:
            s += r
        p = q
        q = r








if __name__ == '__main__':
##    print is_even(2)
##    print is_even(3)
##    print is_even(4)
##    print is_even(5)
##    print is_even(6)
    a = fib_sum(4000000)
