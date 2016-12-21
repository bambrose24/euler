import numpy as np
from itertools import chain

def factors(n):
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2],range(3,n+1,2)):
        s = 0
        while n%i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n==1:
            return result

def primesUpTo(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def isPrime(n):
  if n == 2 or n == 3 or n == 11 or n == 13: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  if n%7 == 0: return False
  if n%11 == 0: return False
  if n%13 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def multiplicativeOrder(b,m):
    r = b
    count = 1
    while r != 1:
        count+=1
        r = (r*b) % m
    return count

def firstNPrimes(n):
    if n < 1:
        return []
    if n == 1:
        return [2]
    i = 3
    res = [2]
    while len(res) < n:
        if isPrime(i):
            res.append(i)
        i+=2
    return res
