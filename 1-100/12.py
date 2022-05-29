from sympy.ntheory import divisor_count

trig_number = 0
i = 1

while divisor_count(trig_number) <= 500:
    trig_number += i
    i += 1

print(trig_number)