from itertools import product, combinations
from functools import reduce
import operator
def check(i, j):
    """
        fibonacci nos take form of m**2 + n**2, m**2 - n**2, 2*m*n
        where m, n > 0

        we check for different values of m, n and to generate pythagorean triplets/triads

        if sum of generated triplets == 1000 we return tuple else False
    """
    if i < j:
        i, j = j, i
    if i == 400 and j == 25:
        print(i, j)
    a, b, c = (i**2+j**2, i**2-j**2, 2*i*j)
    if a + b + c == 1000:
        return (a, b, c)
    else:
        return False

def is_prime(n):
    for i in range(n-1, n//2):
        if n % i == 0:
            return False
    return True

def factorize(n):
    res = []
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0 and is_prime(i):
                res.append(i)
                n = int(n/i)
                break
    return res


def faster_solve():
    """
        refer to check function's docstring for triad generation

        sum(triad) => 2*m**2 + 2*m*n = 1000 (given in question)
        m**2 + m * n => 500
        m*(m+n) => 500 {gen factors of 500 and sort them in ascending order}
    """
    pass

def solve():
    """
        generate numerical pairs here and check triplet sum
    """
    a = range(1, 1000)
    itr = product(a, a)
    for i, j in itr:
        val = check(i, j)
        if val:
            return reduce(operator.mul, val, 1)
    return 1

print(solve())
print(factorize(500))
