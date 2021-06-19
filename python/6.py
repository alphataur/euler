from functools import reduce
import operator

def sum_of_sq(n):
    return int(reduce(operator.add, (i*i for i in range(1, n+1))))

def sq_of_sum(n):
    return int(((n * (n+1)) / 2) ** 2)

def solve(n):
    return sq_of_sum(n) - sum_of_sq(n)

print(solve(100))
