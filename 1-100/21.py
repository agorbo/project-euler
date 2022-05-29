from sympy.ntheory import proper_divisors

amicable_sum = 0

for a in range(10000):
    b = sum(proper_divisors(a))

    if a == sum(proper_divisors(b)) and a < b:
        print(a, b)
        amicable_sum += a + b

print(amicable_sum)
