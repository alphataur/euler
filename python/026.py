def count_digits(n):
    return len(str(n))

def detect_cycle(arr):
    breakpoint()

def cycles(n):
    ndig = count_digits(n)
    numerator = 10 ** ndig
    cycles = ""
    for i in range(10):
        d = numerator // n
        numerator = (numerator % n) * (10 ** ndig)
        if numerator == 0:
            return cycles
        else:
            cycles += str(d)
    return detect_cycle(cycles)

print(cycles(7))
