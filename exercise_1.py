"""
Project Euler
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

TODO: Make this find the sum for arbitrary strings of multiples
TODO: Use the summation hint provided in the problem

Notes:
    * This is a hack-ish way of doing it, but it works
"""

def calc_multiple(max_value):
    """
    Calculates the sum all of the multiples of number until you reach max_value

    """
    total = 0
    for i in range(1, max_value):
        if i % 3 == 0:
            total += i
            print i, total
        elif i % 5 == 0:
            total += i
            print i, total








if __name__ == '__main__':
    total = calc_multiple(1000)
