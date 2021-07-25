import time

def is_palindrome(n):
    #very stupid idea; idk but its faster
    return n == int(str(n)[::-1])

def is_palindrome_custom(n):
    #stupid steps
    res = 0
    i = n
    while i != 0:
        res = (10 * res)+(i % 10)
        i = int(i/10)
    return res == n


def solve():
    return sorted(([(i*j, i, j) for i in range(100, 999) for j in range(100, 999) if is_palindrome_custom(i*j)]), key=lambda e: e[0], reverse=True)[0][0]


print(solve())

#n = 99886111168899
#
#c = time.time()
#print(is_palindrome_custom(n))
#print("custom", time.time()-c)
#
#
#c = time.time()
#print(is_palindrome(n))
#print("stringy", time.time()-c)
