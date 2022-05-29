biggest_palindrome = 0

for i in range(100, 1000):
    for j in range(i + 1, 1000):
        str_repr = str(i * j)
        if str_repr == str_repr[::-1] and i * j > biggest_palindrome:
            biggest_palindrome = i * j

print(biggest_palindrome)
