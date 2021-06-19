from functools import reduce

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return int((a * b) / gcd(a, b))

print(reduce(lcm, range(1, 20)))
