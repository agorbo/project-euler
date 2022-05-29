from re import L
from sympy import ilcm
from sympy.ntheory import proper_divisors

all_abundant = set()
cannot_be_writtern = []

for i in range(12, 28123):
    if sum(proper_divisors(i)) > i:
        all_abundant.add(i)

for i in range(1, 28123):
    if all([(i - abundant) not in all_abundant for abundant in all_abundant]):
        cannot_be_writtern.append(i)
        print(i)

print(sum(cannot_be_writtern))
