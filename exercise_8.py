
"""
Project Euler
Problem 8
Find the greatest product of five consecutive digits in the 1000-digit number.

"""
import csv

def str_prod(s):
    """
    Returns the product of the string passed in
    """
    prod = 1
    for i in s:
        prod = prod * int(i)
    return prod


def bigges_prod(num, n_digit):
    """
    Iterates through each digit in number and finds the biggest product of
    n_digits
    """
    mx = 0
    for i in range(len(num)):
        digits = num[i:i+k]
        prod = str_prod(digits)
        if prod > mx:
            mx = prod
    return mx



if __name__ == '__main__':

    file = 'C:\Users\Adam\Documents\GitHub\Project_Euler\problem_8_num.txt'
    num = ''
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print row
            num = num + str(row)

    num = num.replace('[', '').replace('\'', '').replace(']', '')
    print num
    r = bigges_prod(num, 5)
    print r

