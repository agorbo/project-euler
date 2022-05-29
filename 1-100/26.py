from calendar import c
from locale import currency
import sympy
import math

longest_cycle = 0
longest_cycle_number = 0

for i in range(2, 1000):
    cycle_len = 0
    factors = sympy.ntheory.factorint(i)
    if 2 in factors:
        factors.pop(2)
    if 5 in factors:
        factors.pop(5)
    new_i = math.prod([k ** v for k, v in factors.items()])
    
    if new_i != 1:
        cycle_len = 1
        while (10 ** cycle_len) % new_i != 1:
            cycle_len += 1
    
    if cycle_len > longest_cycle:
        longest_cycle = cycle_len
        longest_cycle_number = i
    
print(longest_cycle_number, longest_cycle)
