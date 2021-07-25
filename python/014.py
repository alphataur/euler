def generate(n):
    res = 1
    while n != 1:
        res += 1
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
    return res
#print(generate(13))







best = 0
res = 1
for i in range(1, 1000001):
    n = generate(i)
    print(i)
    if n > best:
        best = n
        res = i
print(res)
