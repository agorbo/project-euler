from sympy import N
from sympy.ntheory import isprime

n_max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while isprime(n ** 2 + a * n + b):
            n += 1
        if n > n_max:
            n_max = n
            print(a, b)
print(n_max)
