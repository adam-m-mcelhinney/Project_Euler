"""
Project Euler
Problem 20

Find the sum of the digits in the number 100!

"""

def fact(k):
    j = 1
    for i in range(1, k+1):
        print i
        j *= i

    return j

def digit_sum(k):
    k = str(k)
    j = 0
    for i in k:
        print i
        j += int(i)
    return j






if __name__ == '__main__':

    assert fact(10) == 3628800
    assert digit_sum(3628800) == 27
    k = fact(100)
    print digit_sum(k)


