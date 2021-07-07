from itertools import product


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


def solve():
    """
        generate numerical pairs here and check triplet sum
    """
    a = range(1, 1000)
    itr = product(a, a)
    for i, j in itr:
        val = check(i, j)
        if val:
            return val
    return ()

print(solve())
