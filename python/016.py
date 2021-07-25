def solve_naive(exp):
    a = 2 ** exp
    s = 0
    while a:
        s += (a%10)
        a //= 10
    return s

print(solve_naive(1000))
