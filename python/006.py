from functools import reduce
import operator
from itertools import combinations
from functools import reduce

def sum_of_sq(n):
    return int(reduce(operator.add, (i*i for i in range(1, n+1))))

def sq_of_sum(n):
    return int(((n * (n+1)) / 2) ** 2)

def solve(n):
    return sq_of_sum(n) - sum_of_sq(n)

def mathy(n):
    return int((((n * (n+1))/2)**2) - (n*(n+1)*(2*n+1))/6)

def folder(acc, pair):
    return acc + pair[0]*pair[1]

def slicky(n):
    collection = range(1, n+1)
    pairs = combinations(collection, 2)
    return 2 *  reduce(folder, pairs, 0)

print(solve(10))
print(mathy(10))
print(slicky(10))
