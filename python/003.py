def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return (False, i)
    return (True, 1)

def solve(n):
    while n != 1:
        res, first = is_prime(n)
        if res:
            return n
        else:
            n = int(n/first)
    return 1




print(solve(600851475143))
