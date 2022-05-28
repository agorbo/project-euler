from pkg_resources import find_distributions


fibonacci_sequence = [1, 2]

while fibonacci_sequence[-1] <= 4 * 10**6:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print(sum([i for i in fibonacci_sequence if i % 2 == 0]))