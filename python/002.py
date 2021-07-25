def solve():
    a, b = 1, 2
    s = 0
    while a < 4000000:
        if a % 2 == 0:
            s += a
        a, b = b, a + b
    return s

print(solve())


