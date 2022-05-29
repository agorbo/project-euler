from sympy.ntheory import sieve

limit = 2 * 10**6
sum = 0

for i in sieve:
    if i < limit:
        sum += i
    else:
        break

print(sum) 
