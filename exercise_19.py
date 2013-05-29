"""
Project Euler
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
#from datetime import date, weekday, timedelta
from datetime import *

def first_sundays(start_date, end_date):
    # Find the first Sunday in the time range
    d = start_date
    while True:
        if d.weekday() == 6:
            print d
            break
        else:
            d += timedelta(days = 1)
    count = 0
    while True:
        if d >= end_date:
            return count
        else:
            if d.day==1:
                count +=1
                print d
        d +=timedelta(days=7)

def first(start_date, end_date):
    d = start_date
    counter = 0
    while True:
        if d >= end_date:
            return counter
        if d.weekday() == 6 and d.day==1:
            counter+=1
        d +=timedelta(days=1)









if __name__ == '__main__':
    start_date = date(1900,01,01)
    end_date = date(2000,12,31)
    t= first_sundays(start_date, end_date)
    g = first(start_date, end_date)



