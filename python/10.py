from functools import lru_cache
import math
from functools import reduce

@lru_cache(maxsize=None)
def is_prime(n):
    for i in range(n//2, 1, -1):
        if n % i == 0:
            return False
    return True

def prime_gen():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

def slow():
    res = 0
    for i in prime_gen():
        if i < 2000000:
            res += i
        else:
            break
    print(res)

def sieve_of_erat(n):
    sieve = [(i, True) for i in range(n+1)]
    sieve[0] = (0, False)
    sieve[1] = (1, False)
    for i in range(2, n+1):
        if sieve[i] == (i, False):
            continue
        for j in range(2*i, n+1, i):
            sieve[j] = (j, False)
    return sieve

def faster_solve(n):
    sieve = sieve_of_erat(n)
    #s = 0
    #for i in range(2, n+1):
    #    if arr[i][1]:
    #        s += arr[i][0]
    #return s
    return reduce(lambda a, e: a+e[0], filter(lambda e: e[1], sieve), 0)

arr = faster_solve(2000000)
print(arr)



