"""
Some guy online claims this runs in 7 seconds.
Why?
"""

from itertools import permutations

perms = permutations(['0','1','2','3','4','5','6','7','8','9'])
winners = [int(e[0]+e[1]+e[2]+e[3]+e[4]+e[5]+e[6]+e[7]+e[8]+e[9])
            for e in perms
            if int(e[0]) != 0 and
            int(e[7]+e[8]+e[9]) % 17 == 0 and
            int(e[6]+e[7]+e[8]) % 13 == 0 and
            int(e[5]+e[6]+e[7]) % 11 == 0 and
            int(e[4]+e[5]+e[6]) % 7 == 0 and
            int(e[3]+e[4]+e[5]) % 5 == 0 and
            int(e[2]+e[3]+e[4]) % 3 == 0 and
            int(e[1]+e[2]+e[3]) % 2 == 0]
print sum(winners)