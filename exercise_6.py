"""
Project Euler
Problem 6


Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""

def sum_squares(mn, mx):
    i = 0 # Counter
    t = 0 # total sum of squares
    while True:
        if i>mx:
            break
        t += i**2
        i +=1
    return t

def square_sum(mn, mx):
    return (sum(range(mn, mx+1)))**2





if __name__ == '__main__':
    assert sum_squares(1,10) == 385, 'Error 1'
    assert square_sum(1,10) == 3025, 'Error 2'
    assert square_sum(1,10) - sum_squares(1,10)  == 2640, 'Error 3'
    print square_sum(1,100) - sum_squares(1,100)
