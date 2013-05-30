"""
Project Euler
Problem 3
What is the largest prime factor of the number 600851475143 ?

The prime factors of 13195 are 5, 7, 13 and 29.

Got the code from here:
http://blog.dhananjaynene.com/2009/01/2009-is-not-a-prime-number-a-python-program-to-compute-factors/
"""
def factor(n):
  yield 1
  i = 2
  limit = n**0.5
  while i <= limit:
    if n % i == 0:
      yield i
      n = n / i
      limit = n**0.5
    else:
      i += 1
  if n > 1:
    yield n


if __name__ == "__main__":
    p = 13195
    r = [i for i in factor(p)]
    print r

    p =600851475143
    r = [i for i in factor(p)]
    print r