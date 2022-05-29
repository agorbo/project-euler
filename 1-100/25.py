from sympy import fibonacci

i = 1
fib = fibonacci(i)
while len(str(fib)) < 1000:
    i += 1
    fib = fibonacci(i)

print(i, fib)
