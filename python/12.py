import math
def gen_tri_nos():
    s = 0
    i = 1
    while True:
        s+=i
        i+=1
        yield s

def factors(n):
    if n == 1:
        return 1
    else:
        res = 2
        for i in range(2, (n//2+1)):
            if n % i == 0:
                res += 1 #.append(i)
        return res

#print(factors(76576500))

for i in gen_tri_nos():
    #if i > 100:
    #    break
    #else:
    #    print(i, factors(i))
    n = factors(i)
    
    print(i)
    if n >= 500:

        break
