import operator
from functools import reduce

def C(m, n):
    nume = reduce(operator.mul, range(1, m+1))
    deno = reduce(operator.mul, range(1, n+1)) * reduce(operator.mul, range(1, m-n+1))
    return nume//deno

def solve(n):
    print(C(2*n, n))

solve(20)
#print(C(4, 2))
