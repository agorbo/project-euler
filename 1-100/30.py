from sympy.ntheory.digits import digits

power = 2
i_sum = 0

i = 10
while True:
    i_digits = digits(i)[1:]
    digits_squares_sum = sum([a ** power for a in i_digits])
    if digits_squares_sum == i:
        i_sum += i
        print(i, i_sum)
    print(i, end='\r')
    i += 1
