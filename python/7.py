def memorize(func):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return inner

@memorize
def is_prime(n):
    for i in range(int(n/2), 1, -1):
        if n % i == 0:
            return False
    return True

def prime_gen():
    fp = 2
    while True:
        if is_prime(fp):
            yield fp
        fp += 1


a = prime_gen()
for i in range(10001):
    print(i)
    res = next(a)
print(res)
